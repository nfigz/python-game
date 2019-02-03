class EndingMessage:
    """
    The EndingMessage Class uses the str method
    """

    def __str__(self):
        """
        __str__ is used to display the ending message which
        appears after card reading
        """
        return "\033[1;30;48m" +\
               "With an automated system like this, it's very tempting" \
               + " to immediately\n" +\
               "repeat a reading if the answer you got was either not" \
               + " what you wanted\n" +\
               "to hear. The first reading will always be the most" \
               + " appropriate. If you\n" +\
               "would like clarification on something, use a different " \
               + " reading spread.\n" +\
               "\033[0;30;48m \n\n"
