"""
UnitTest class first imports unittest module
then imports PandasToList class
"""
import unittest
from PandasToList import PandasToList


class UnitTest(unittest.TestCase):
    """
    The UnitTest class runs two unit test on the
    PandasToList class
    """

    def test_upright_deck_list(self):
        """
        test_upright_deck_list verifies that the
        return of upright_deck() in PandasToList class
        returns a list

        expected is type(list())
        result should be type(list())
        """
        p = PandasToList()
        upright_result = type(p.upright_deck('files/TarotCardsUpright.csv'))
        upright_expected = type(list())
        self.assertEqual(upright_expected, upright_result)

    def test_reverse_deck_list(self):
        """
        test_reverse_deck_list verifies that the
        return of reverse_deck() in PandasToList class
        returns a list

        expected is type(list())
        result should be type(list())
        """
        p = PandasToList()
        reverse_result = type(p.reverse_deck('files/TarotCardsReversed.csv'))
        reverse_expected = type(list())
        self.assertEqual(reverse_expected, reverse_result)


if __name__ == "__main__":
    # runs the unittest to see results
    unittest.main()
