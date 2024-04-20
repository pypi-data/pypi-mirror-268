import json
from pathlib import Path
from typing import Any, Dict, List, Tuple, Union

from detectools import load_json, raw_cocodict
from detectools.dataset import DetectionDataset
from torch.utils.data import random_split


def merge_jsons(
    jsonfiles: List[str], output_json: str, categories: List[Dict[str, Any]]
):
    """Take a list of json files paths and merge them in one respecting
    the images/annotations correspondance id

    Args:
        jsonfiles (List[str]): List of paths of jsons to merge.
        output_json (str): Path to store merged json.
        categories (List[Dict[str, Any]]): List of categories as COCO format.
    """
    # initialize counter and output json
    image_id = 0
    annotation_id = 0
    cocodict = raw_cocodict()
    cocodict["categories"] = categories
    # for each json file, read the file
    for jsonfile in jsonfiles:
        file = load_json(jsonfile)
        assert (
            categories == file["categories"]
        ), f"given categories should match coco jsons categories, got {categories} and {file['categories']}"
        # for each image
        for image in file["images"]:
            # get the corresponding anns in json file
            image_annotations = [
                a for a in file["annotations"] if a["image_id"] == image["id"]
            ]
            # define the new image id forimage and annotations
            image_id += 1
            image["id"] = image_id
            cocodict["images"].append(image)
            # for each annotations
            for ann in image_annotations:
                # set new id
                annotation_id += 1
                ann["id"] = annotation_id
                ann["image_id"] = image_id
                cocodict["annotations"].append(ann)

    # write  merged json
    Path(output_json).write_text(json.dumps(cocodict))


def split_dataset(
    source_datasets: Union[str, List[str]],
    destination: str,
    proportions: Tuple[float] = (0.8, 0.2, 0.0),
) -> None:
    """Split one or multiple dataset folder according to split proportions and write a new dataset
    with the fusion same split for each datqset (train, valid, test).

    Args:
        source_datasets (Union[str, List[str]]): Path to ad dataset or list of dataset.
        destination (str): Path of Splitted datset.
        proportions (Tuple[float], optional): prportions for train, valid & test resptively. Defaults to (0.8, 0.2, 0.0).
        scaling_off (bool): To disable scaling during dataset get item.
    """
    # if source_datasets is a string wrap it in list
    if isinstance(source_datasets, str):
        source_datasets = [source_datasets]
    # for each source dataset do the split
    for dataset_path in source_datasets:
        print(f"Splitting dataset: {dataset_path}")
        # create DetectionDataset
        dataset = DetectionDataset(dataset_path, preprocessing=None)
        # split dataset in 3 subsets
        train, valid, test = random_split(dataset, list(proportions))
        subsets = list(zip([train, valid, test], ["train", "valid", "test"]))
        # for each subset
        for subset_dataset, subset_name in subsets:
            print(f"Export {subset_name} data:")
            subset_path = Path(destination) / subset_name
            dataset.export_dataset(
                f"{subset_path}",
                indices=subset_dataset.indices,
            )
