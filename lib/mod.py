def mod(code):
    """
    Return modulo of big string number code with divisor.

    Paramaters:
    -----------
        code : str
            IBAN string.

    Returns:
    --------
        rem : int
            Remander of modulo calculation

    Raises:
    -------
        TypeError: Wrong type of input IBAN number

    """

    rem = 0

    # By default, divisor is 97 by ISO 7064.
    divisor = 97

    if not type(code) is str:
        raise TypeError("Only String is allowed! Check input IBAN number!")

    for i in range(0, len(code)):
        rem = (rem*10 + int(code[i]))%divisor

    return rem
