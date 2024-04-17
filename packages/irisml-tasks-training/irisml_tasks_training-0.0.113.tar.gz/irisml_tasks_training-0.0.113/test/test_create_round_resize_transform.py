import unittest
import PIL.Image
import torch
from irisml.tasks.create_round_resize_transform import Task


class TestCreateRoundResizeTransform(unittest.TestCase):
    def test_simple(self):
        outputs = Task(Task.Config(max_input_size=416, resolution=32)).execute(Task.Inputs())
        transform = outputs.transform

        self._assert_transform_image_size(transform, (416, 416), (416, 416))
        self._assert_transform_image_size(transform, (416, 401), (416, 416))
        self._assert_transform_image_size(transform, (401, 416), (416, 416))
        self._assert_transform_image_size(transform, (832, 420), (416, 224))
        self._assert_transform_image_size(transform, (224, 224), (416, 416))

    def _assert_transform_image_size(self, transform, input_size, expected_size):
        """input_size, expected_size: (width, height)"""
        image = PIL.Image.new('RGB', input_size)
        transformed_image = transform(image, torch.tensor(0))[0]
        self.assertEqual(transformed_image.shape[1:], (expected_size[1], expected_size[0]))
