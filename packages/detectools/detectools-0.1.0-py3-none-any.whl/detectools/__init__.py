# -*- coding: utf-8 -*-

"""Torch prebuild functions to train, evaluate and use models in production."""
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, Literal, Union

__version__ = "0.1.0" # change detectools version here

IMAGE_FOLDER = "images"
ANNOTATION_FILE = "coco_annotations.json"

COLORS = [
    (0, 102, 204),
    (51, 255, 51),
    (255, 0, 0),
    (51, 51, 255),
    (255, 51, 255),
    (255, 255, 0),
    (86, 255, 255),
    (100, 200, 100),
    (250, 50, 125),
    (125, 250, 0),
    (125, 50, 250),
    (125, 125, 125),
    (20, 20, 200),
]  # set of colors for visualisation (max 13 classes for now)


def load_json(json_path: Union[str, Path]) -> Dict[str, Any]:
    """Load JSON file into dict.

    Args:
        json_path (Union[str, Path]): JSON file path.

    Returns:
        Dict[str, Any]
    """
    if isinstance(json_path, str):
        json_path = Path(json_path)

    return json.load(json_path.open())


def write_json(filename: str, dic: dict):
    """
    Write a dictionnary in json format
    """
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    Path(filename).write_text(json.dumps(dic))


class HiddenPrints:
    """
    class to block and allow printing
    """

    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, "w")

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout


class Task:

    mode = "detection"

    def set_mode(cls, mode: Literal["detection", "instance_segmentation"]):
        cls.mode = mode


def set_lib_mode(mode: Literal["detection", "instance_segmentation"]):
    """Set global mode for library.

    Args:
        mode (Literal[&quot;detection&quot;, &quot;instance_segmentation&quot;]): Mode for library.
    """
    Task.set_mode(Task, mode)


def raw_cocodict() -> dict:
    """
    Return an empty dictionnary for COCO basic keys
    """
    return {"categories": [], "images": [], "annotations": []}
