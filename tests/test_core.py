from pathlib import Path
import unittest

from reviews_lab.core import summarize_reviews
from reviews_lab.fixture_check import check


class ReviewTests(unittest.TestCase):
    def test_groups_histograms_and_rounds_averages(self):
        result = summarize_reviews([{"business_id": 2, "rating": 5}] + [{"business_id": 1, "rating": value} for value in (1, 2, 2)])
        self.assertEqual([row["business_id"] for row in result], [1, 2])
        self.assertEqual((result[0]["count"], result[0]["average"]), (3, 1.67))
        self.assertEqual(result[0]["histogram"], {"1": 1, "2": 2, "3": 0, "4": 0, "5": 0})

    def test_empty_input(self):
        self.assertEqual(summarize_reviews([]), [])

    def test_invalid_and_boolean_ratings_are_rejected(self):
        for rating in (True, 0, 6, 2.5, "3"):
            with self.subTest(rating=rating), self.assertRaises(ValueError):
                summarize_reviews([{"business_id": 1, "rating": rating}])

    def test_complete_fixture_corpus(self):
        self.assertGreaterEqual(check(Path(__file__).resolve().parents[1] / "fixtures/cases.jsonl", summarize_reviews), 350)


if __name__ == "__main__":
    unittest.main()
