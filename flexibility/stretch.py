"""canvas() enlongates string."""


def canvas(myString = ' '):
    """
    function to add spaces between letters in a string

    Parameters
    ----------
    myString : str
        user input of string to manipulate.

    Returns
    -------
    myStringStretch : str
        elongated string.
    """
    list = []
    for i in myString:
        list.append(i)

    separator = ' '
    myStringStretch = separator.join(list)


    return myStringStretch

