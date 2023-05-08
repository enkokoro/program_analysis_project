import choice
from mock import patch
import random
from random import Random
import unittest


class ChoiceTest(unittest.TestCase):
    @patch.object(Random, 'choice')
    def test_choice(self, mock_choice):
        mock_choice.return_value = 5
        self.assertEqual(
            choice.choice(items=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            5
        )


if __name__ == "__main__":
    unittest.main()
