import shutil
from pathlib import Path
from typing import Callable, Dict, List, Sequence, Tuple, Union

import torch
from computervisiontools import load_image
from computervisiontools.preprocessing import build_preprocessing
from detectools import (ANNOTATION_FILE, IMAGE_FOLDER, HiddenPrints, Task,
                        load_json, raw_cocodict, write_json)
from detectools.augmentation import Augmentation
from detectools.formats import (BaseFormat, BatchedFormats, Format,
                                SegmentationFormat)
from pycocotools.coco import COCO
from torch import Tensor
from torch.utils.data import DataLoader, Dataset
from tqdm import tqdm


class DetectionDataset(Dataset):
    def __init__(
        self,
        dataset_path: str,
        preprocessing: Callable = build_preprocessing(),
        augmentation: Augmentation = None,
        convert_labels_dict: Dict[int, int] = None,
        min_border_size: float = 10,
        rescale_boxes_from_masks: bool = False,
    ):
        """Create Torch Dataset for Detectools.

        Args:
            dataset_path (str): Path to folder of the dataset.
            preprocessing (Callable, optional): Callable that preprocess image images (i.e. Scale values to 0-1 then normalize with image weights channels mean). Defaults to build_preprocessing().
            augmentation (Augmentation, optional): Augmentation class that apply augmentation to bot images and targets (Formats. Defaults to None.
            convert_labels_dict (Dict[int, int], optional): Dict of {old_labels : new_labels} to dynamically convert labels. Defaults to None.
            min_border_size (float, optional): Minimum size of box sides to be kept, if one side of box is below the object will be ignored. Defaults to 10.
            rescale_boxes_from_masks (bool, optional): If True boxes are re-computed from masks by using cv2.FindContours. This duplicates object if mask is discontinuous.
                                                        It's time consuming so do it's better to use it for data preparation only. Works only when lib mode is instance_segmentation
        """
        self.image_folder = Path(dataset_path) / IMAGE_FOLDER
        annotation_file_path = Path(dataset_path) / ANNOTATION_FILE
        with HiddenPrints():
            self.coco = COCO(annotation_file_path.as_posix())
        self.coco_indexes = list(self.coco.imgs.keys())
        self.name_id_dict = {v["file_name"]: k for k, v in self.coco.imgs.items()}
        self.preprocessing = preprocessing
        self.augmentation = augmentation
        self.convert_labels_dict = convert_labels_dict
        self.categories = load_json(annotation_file_path)["categories"]
        # convert categories if needed
        if self.convert_labels_dict:
            for category in self.categories:
                cat_id = category["id"]
                if cat_id in self.convert_labels_dict:
                    category["id"] = self.convert_labels_dict[category["id"]]

        self.classes = [c["name"] for c in self.categories]
        self.min_border_size = min_border_size
        self.rescale_boxes_from_masks = rescale_boxes_from_masks
        if rescale_boxes_from_masks:
            assert (
                Task.mode == "instance_segmentation"
            ), f"rescale boxes from masques is only possible when lib mode is instance_segmentation, got {Task.mode}"

    def __len__(self) -> int:
        return len(self.coco.imgs.keys())

    def __iter__(self):
        for x in range(len(self)):
            yield self[x]

    def __getitem__(self, index: int) -> Tuple[Tensor, Format]:
        """Return image and Format of corresponding index.
        Apply all transformation needed for model training.

        Args:
            index (int): _description_

        Returns:
            Tuple[Tensor, Format]: Prepared image tensors and targets.
        """
        image, target, image_name = self.load_from_coco(index)
        image, target = self.transform(image, target)
        # rescale boxes from masks if needed
        if self.rescale_boxes_from_masks:
            target: SegmentationFormat
            target.rescale_boxes_from_masks()

        return image, target, image_name

    def transform(self, image: Tensor, target: BaseFormat) -> Tuple[Tensor, BaseFormat]:
        """Apply transformation to image/target pair:
            - Augmentation
            - Preprocessing
            - Labels conversion (if convert_labels_dict)
            - Sanitize boxes

        Args:
            image (Tensor): Tensor image.
            target (BaseFormat): Target.

        Returns:
            Tuple[Tensor, BaseFormat]: Transformed Image & Target.
        """
        # apply_augmentation if needed
        if self.augmentation:
            image, target = self.augmentation(image, target)
        # apply image preprocessing
        if self.preprocessing:
            image = self.preprocessing(image)
        # convert labels if needed
        if self.convert_labels_dict:
            target.convert_labels(self.convert_labels_dict)
        # remove small objects with small boxes
        target = target.sanitize(self.min_border_size)

        return image, target

    def load_from_coco(self, index: int) -> Tuple[Tensor, Format, str]:
        """Gather image name, indices & corresponding annotations from coco.

        Args:
            index (int): index of data.
        Returns:
            Tuple[Tensor, Format, str]: Transformed Image, BaseFormat & image name
        """
        image_dict = self.coco.imgs[self.coco_indexes[index]]
        image_name, image_id = image_dict["file_name"], image_dict["id"]
        image_size = (image_dict["height"], image_dict["width"])
        image_path = self.image_folder / image_name
        # load image
        image = load_image(image_path)
        # get corresponding image annotations
        annotations_ids = self.coco.getAnnIds(imgIds=image_id)
        annotations = self.coco.loadAnns(annotations_ids)
        # create Format
        target = Format.from_coco(annotations, image_size)

        return image, target, image_name

    def get_image_data(
        self, image_name: str, transform: bool = False
    ) -> Tuple[Tensor, BaseFormat, str]:
        """Return image Tensor & Format for image_name. It's a __getitem__ with name as indice.

        Args:
            image_name (str): Name of image to gather.
            transform (bool): To apply transformations or not. default False.

        Returns:
            Tuple[Tensor, BaseFormat, str]: Image Tensor, BaseFormat
        """
        image, target, _ = self.load_from_coco(
            self.coco_indexes.index(self.name_id_dict[image_name])
        )

        if transform:
            image, target = self.transform(image, target)

        return image, target

    def export_dataset(self, dataset_path: Union[str, Path], indices: Sequence[int]):
        """Export all or a part of dataset annotations to a json file.

        Args:
            json_path (Union[str, Path]): Path to jeon to write.
            indices (Sequence[int]): Indices of images to export.
        """
        # create output_dict
        (Path(dataset_path) / IMAGE_FOLDER).mkdir(parents=True)
        # Disable augmentations & preprocessing
        augmentation = self.augmentation
        self.augmentation = None
        # get indices of images to export
        export_indices = indices if indices else range(self.__len__())
        # export
        coco_dict = raw_cocodict()
        coco_dict["categories"] = self.categories
        img_id = 1
        ann_id = 1

        for indice in tqdm(export_indices, desc="Exporting: "):
            # get image, target
            image, target, name = self.load_from_coco(indice)
            h, w = image.shape[-2:]
            # create image dict and annotations dict
            image_dict = {"id": img_id, "file_name": name, "height": h, "width": w}
            annotations = target.coco(image_id=img_id, annotation_id=ann_id)
            # fill new coco_dict
            coco_dict["images"] = coco_dict["images"] + [image_dict]
            coco_dict["annotations"] = coco_dict["annotations"] + annotations
            # update ids of images and annotations
            img_id += 1
            ann_id += target.size
            # copy image
            shutil.copy(
                self.image_folder / name, Path(dataset_path) / IMAGE_FOLDER / name
            )

        write_json(Path(dataset_path) / ANNOTATION_FILE, coco_dict)
        # set back augmentations
        self.augmentation = augmentation


class DetectionLoader(DataLoader):
    """Dataloader with custom collate_fn."""

    def __init__(self, *args, **kwargs):
        super().__init__(collate_fn=self.collate_fn, *args, **kwargs)

    def collate_fn(
        self, batch: List[Tuple[Tensor, Format]]
    ) -> Tuple[Tensor, BatchedFormats]:
        """Collate pairs of images & tensors into batch.

        Args:
            batch (List[Tuple[Tensor, Format]]): List of pairs image/target

            Returns:
                (Tensor): Batched images.
                (BatchedFormats): Formats wrapped into BatchedFormats class.
        """
        images = [triplet[0] for triplet in batch]
        targets = [triplet[1] for triplet in batch]
        names = {i: triplet[2] for i, triplet in enumerate(batch)}
        images, targets = self.pad_to_larger(images, targets)
        batch_images = torch.stack(images)
        batch_targets = BatchedFormats(targets)

        return batch_images, batch_targets, names

    def pad_to_larger(
        self, images: List[Tensor], targets: List[BaseFormat]
    ) -> Tuple[List[Tensor], List[BaseFormat]]:
        """Pad images and targets to larger image size.

        Args:
            images (Tensor): Images.
            targets (List[BaseFormat]): Targets.
        Returns:
            images (Tensor): Images.
            targets (List[BaseFormat]): Targets.
        """
        # get max borders sizes
        larger_width = max([image.shape[-1] for image in images])
        larger_height = max([image.shape[-2] for image in images])
        padded_images, padded_targets = [], []
        # for each image pad image & target
        for i, image in enumerate(images):
            im_h, im_w = image.shape[-2:]
            pad_image = torch.zeros((3, larger_height, larger_width))
            pad_image[:, :im_h, :im_w] = image
            pad_h, pad_w = larger_height - im_h, larger_width - im_w
            target = targets[i]
            pad_target = target.clone()
            pad_target.pad(0, 0, pad_w, pad_h)
            padded_images.append(pad_image)
            padded_targets.append(pad_target)

        return padded_images, padded_targets
