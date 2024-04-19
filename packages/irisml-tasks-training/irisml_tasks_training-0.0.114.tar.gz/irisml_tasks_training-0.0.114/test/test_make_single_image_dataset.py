import pathlib
import tempfile
import unittest
import PIL.Image
import torch
from irisml.tasks.make_single_image_dataset import Task


class TestMakeSingleImageDataset(unittest.TestCase):
    def test_simple(self):
        with tempfile.NamedTemporaryFile(suffix='.jpg') as temp_file:
            image = PIL.Image.new('RGB', (64, 64))
            image.save(temp_file.name)

            outputs = Task(Task.Config(path=pathlib.Path(temp_file.name), task_type='classification_multiclass')).execute(Task.Inputs())
            dataset = outputs.dataset

            self.assertEqual(len(dataset), 1)
            image, target = dataset[0]
            self.assertIsInstance(image, PIL.Image.Image)
            self.assertEqual(image.size, (64, 64))
            self.assertIsInstance(target, torch.Tensor)
            self.assertEqual(target.item(), 0)

            outputs = Task(Task.Config(path=pathlib.Path(temp_file.name), task_type='object_detection')).execute(Task.Inputs())
            dataset = outputs.dataset

            self.assertEqual(len(dataset), 1)
            image, target = dataset[0]
            self.assertIsInstance(image, PIL.Image.Image)
            self.assertEqual(image.size, (64, 64))
            self.assertIsInstance(target, torch.Tensor)
            self.assertEqual(target.size(), (0, 5))

    def test_no_image(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            outputs = Task(Task.Config(path=pathlib.Path(temp_dir) / 'no_image.jpg', task_type='classification_multiclass')).execute(Task.Inputs())
            dataset = outputs.dataset

            self.assertEqual(len(dataset), 1)
            image, target = dataset[0]
            self.assertIsInstance(image, PIL.Image.Image)
            self.assertEqual(image.size, (224, 224))
            self.assertIsInstance(target, torch.Tensor)
            self.assertEqual(target.item(), 0)
