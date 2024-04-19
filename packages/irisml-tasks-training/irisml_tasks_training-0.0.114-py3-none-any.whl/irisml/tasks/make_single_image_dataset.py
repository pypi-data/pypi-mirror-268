import dataclasses
import logging
import pathlib
import typing
import PIL.Image
import torch
import torch.utils.data
import irisml.core

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """Create a dataset with a single image.

    Config:
        path (Path): Path to the image file.
        task_type: Type of the task. Supported values are 'classification_multiclass' and 'object_detection'.
    """
    VERSION = '0.1.0'
    CACHE_ENABLED = False

    @dataclasses.dataclass
    class Config:
        path: pathlib.Path
        task_type: typing.Literal['classification_multiclass', 'object_detection']

    @dataclasses.dataclass
    class Outputs:
        dataset: torch.utils.data.Dataset

    def execute(self, inputs):
        return self.Outputs(SingleImageDataset(self.config.path, self.config.task_type))


class SingleImageDataset(torch.utils.data.Dataset):
    def __init__(self, path, task_type):
        self._path = path
        self._task_type = task_type

    def __len__(self):
        return 1

    def __getitem__(self, index):
        if index != 0:
            raise IndexError('Index out of range')

        if self._path.exists():
            logger.info(f"Loading image: {self._path}")
            with PIL.Image.open(self._path) as image:
                image = image.convert('RGB')
        else:
            logger.error(f"File not found: {self._path}. Using a dummy image.")
            image = PIL.Image.new('RGB', (224, 224))

        if self._task_type == 'classification_multiclass':
            return image, torch.tensor(0, dtype=torch.long)
        elif self._task_type == 'object_detection':
            return image, torch.zeros((0, 5), dtype=torch.float32)
        else:
            raise ValueError(f'Unsupported task type: {self._task_type}')
