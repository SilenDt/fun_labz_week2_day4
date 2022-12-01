import unittest

from src.high_scores import latest, personal_best, personal_top_three, sort_highest_to_lowest

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    
    # Tests
    def setUp(self): 
        self.scores1 = [100, 0, 90, 30, 20, 15, 60, 30, 88, 75, 100, 11]
        self.scores2 = [50, 66]
    # Test latest score (the last thing in the list)
    def test_latest_score(self):
        latest_score = latest(self.scores1)
        self.assertEqual(11, latest_score)

    # Test personal best (the highest score in the list)
    def test_highest_score(self):
        highest_score = personal_best(self.scores1)
        self.assertEqual(100, highest_score)

    # Test top three from list of scores
    def test_get_top_3_scores(self):
        top_3_scores = personal_top_three(self.scores1)
        self.assertEqual([100, 100, 90], top_3_scores)
    # Test ordered from highest tp lowest
    def test_order_highest_to_lowest(self):
        highest_to_lowest = sort_highest_to_lowest(self.scores1)
        self.assertEqual([100, 100, 90, 88, 75, 60, 30, 30, 20, 15, 11, 0], highest_to_lowest)
    # Test top three when there is a tie
    def 
    # Test top three when there are less than three

    # Test top three when there is only one
    
