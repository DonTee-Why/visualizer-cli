import unittest
from .context import visualizer, terminal


class TestVisualizer(unittest.TestCase):

    arguments = terminal.parse_arguments(
        ['-s', '01-01-2022', '-e', '05-01-2022'])
    data = visualizer.get_data(arguments)

    def test_get_data_returns_dictionary(self):
        self.assertIsInstance(self.data, dict)

    def test_get_data_x_axis_is_list(self):
        self.assertIsInstance(self.data.get("X-Axis"), list)

    def test_get_data_y_axis_is_list(self):
        self.assertIsInstance(self.data.get("X-Axis"), list)

    def test_get_data_x_axis_list_is_not_null(self):
        self.assertIsNot(self.data.get("X-Axis"), [])

    def test_get_data_y_axis_list_is_not_null(self):
        self.assertIsNot(self.data.get("Y-Axis"), [])

if __name__ == '__main__':
    unittest.main()
