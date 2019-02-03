import pandas as pd
# imports the pandas module


class PandasToList:
    """
    The PandasToList class creates a data frame from from
    two csv files and then turns the data frame into a list.
    One csv contains tarot cards and descriptions for when the
    cards are in the upright position. The second csv contains
    tarot cards and descriptions for when the cards are in
    the reverse position.
    """
    def upright_deck(self, upright_file):
        """
        upright_deck has a required parameter upright_file.
        The main program passes parameter info when the program
        is executed

        upright_deck first reads the csv file and store it as a
        data frame. Then a list is created from data in the CARD
        column and another list is created from the data in the
        DESCRIPTION column.

        Using zip one list is created from the two list. This list
        keeps the card names and card descriptions together.

        The final list is returned(list_upright_taro)
        """
        df_upright_taro = pd.read_csv(upright_file)
        list_upright_card = df_upright_taro["CARD"].values
        list_upright_desc = df_upright_taro["DESCRIPTION"].values
        list_upright_taro = [[card, desc] for card, desc in zip(
            list_upright_card, list_upright_desc)]
        return list_upright_taro

    def reverse_deck(self, reverse_file):
        """
        reverse_deck has a required parameter reverse_file.
        The main program passes parameter info when the program
        is executed

        reverse_deck first reads the csv file and store it as a
        data frame. Then a list is created from data in the CARD
        column and another list is created from the data in the
        DESCRIPTION column.

        Using zip one list is created from the two list. This list
        keeps the card names and card descriptions together.

        The final list is returned(list_reverse_taro)
        """
        df_reverse_taro = pd.read_csv(reverse_file)
        list_reverse_card = df_reverse_taro["CARD"].values
        list_reverse_desc = df_reverse_taro["DESCRIPTION"].values
        list_reverse_taro = [[card, desc] for card, desc in zip(
            list_reverse_card, list_reverse_desc)]
        return list_reverse_taro
