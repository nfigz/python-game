class OpeningMessage:
    """
    The OpeningMessage Class is imported by the main program
    norilyzf@bu.edu_final_project.py. When the main program runs
    a message is displayed. The methods in this class help that
    message be displayed.
    """
    def __init__(self, filename='files\TarotCardsIntroduction.txt'):
        """
        the init method defines the filename of the file
        that will be used.
        """
        self.__filename = filename

    def open_file(self):
        """
        The open_file method opens the file defined in the init method
        then returns the contents to variable msg
        """
        opening_message = open(self.__filename, "r")
        msg = opening_message.read()
        return msg

    def close_file(self):
        """
        The close_file method verifies that the file gets closed
        """
        open(self.__filename, "r").close()
        
