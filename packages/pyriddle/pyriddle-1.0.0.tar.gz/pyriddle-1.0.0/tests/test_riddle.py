import unittest
from pyriddle.riddle import riddle_factory


class TestRiddleFactory(unittest.TestCase):
    def setUp(self):
        self.data = {
            "What gets wetter as it dries?": ["A towel"],
            "I’m tall when I’m young and short when I’m old. What am I?": ["A candle"],
            "What has keys but can't open locks?": ["A piano"]
        }
        self.get_riddle, self.get_riddles = riddle_factory(self.data)

    def test_get_riddle(self):
        # Testing that get_riddle returns a dictionary with a question and answer
        riddle = self.get_riddle()
        self.assertIsInstance(riddle, dict)
        self.assertIn('question', riddle)
        self.assertIn('answer', riddle)
        self.assertIn(riddle['question'], self.data)
        self.assertIn(riddle['answer'], self.data[riddle['question']])

    def test_get_riddles_single(self):
        # Test fetching a single riddle via get_riddles
        riddles = self.get_riddles(1)
        self.assertEqual(len(riddles), 1)
        self.assertIsInstance(riddles[0], dict)

    def test_get_riddles_multiple(self):
        # Test fetching multiple riddles
        count = 2
        riddles = self.get_riddles(count)
        self.assertEqual(len(riddles), count)
        for riddle in riddles:
            self.assertIsInstance(riddle, dict)
            self.assertIn('question', riddle)
            self.assertIn('answer', riddle)
            self.assertIn(riddle['question'], self.data)
            self.assertIn(riddle['answer'], self.data[riddle['question']])

    def test_get_riddles_exceeds(self):
        # Test that a ValueError is raised when requesting more riddles than are available
        with self.assertRaises(ValueError):
            self.get_riddles(len(self.data) + 1)

    def test_cache_functionality(self):
        # Test to ensure that the cache gets used correctly
        first_call_riddle = self.get_riddle()
        second_call_riddle = self.get_riddle()
        self.assertNotEqual(first_call_riddle, second_call_riddle, "Cache should provide different riddles on subsequent calls until reset")

        # Verify that after exhausting cache, we get a repeated riddle or new one without error
        self.get_riddles(len(self.data))  # should repopulate the cache
        no_error_occurred = True
        try:
            self.get_riddles(len(self.data))
        except ValueError:
            no_error_occurred = False
        self.assertTrue(no_error_occurred, "Should not raise an error even after cache is exhausted and repopulated")

if __name__ == '__main__':
    unittest.main()
