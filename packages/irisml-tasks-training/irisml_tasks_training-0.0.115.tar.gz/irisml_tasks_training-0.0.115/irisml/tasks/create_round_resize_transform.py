import dataclasses
import typing
import numpy
import PIL.Image
import torch
import irisml.core


class Task(irisml.core.TaskBase):
    """Create a transform that resizes an image to the nearest multiple of a resolution.

    Config:
        max_input_size (int): The maximum size of the input image.
        resolution (int): The resolution to round the image to.
    """
    VERSION = '0.1.0'

    @dataclasses.dataclass
    class Config:
        max_input_size: int
        resolution: int

    @dataclasses.dataclass
    class Outputs:
        transform: typing.Callable

    def execute(self, inputs):
        return self.Outputs(Transform(self.config.max_input_size, self.config.resolution))

    def dry_run(self, inputs):
        return self.execute(inputs)


class Transform:
    def __init__(self, max_input_size, resolution):
        self._max_input_size = max_input_size
        self._resolution = resolution

    def __call__(self, inputs: PIL.Image.Image, targets):
        assert isinstance(inputs, PIL.Image.Image)

        ratio = self._max_input_size / max(inputs.size)
        new_size = (int(inputs.size[0] * ratio), int(inputs.size[1] * ratio))

        # Round to the nearest multiple of resolution
        new_size = (round(new_size[0] / self._resolution) * self._resolution,
                    round(new_size[1] / self._resolution) * self._resolution)

        resized = inputs.resize(new_size, PIL.Image.BICUBIC)
        image = torch.from_numpy(numpy.array(resized)).to(torch.float32).permute(2, 0, 1) / 255.0
        return image, targets
