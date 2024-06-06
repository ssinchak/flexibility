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


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
