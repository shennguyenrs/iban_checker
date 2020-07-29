from iban_checker.lib.handle_file import handle_file

def to_number(code):
    """
    Convert country code to number.

    Parameters:
    ----------
        code : str
            Country code with 2 letter.

    Returns:
    --------
        cton : str
            A string number of fnum and snum.

    Raises:
    -------
        IndexError: Database is empty
        ValueError: Result string is empty

    """

    database = handle_file("letter_to_number.csv")

    # Raise the database is empty
    try:
        database[0]

    except IndexError:
        print("The database of converting from letter to number is empty")
        print("Check data in file letter_to_number.csv")

    else:
        cton = ""

        # Convert country code to string of number
        # First letter
        for i in range(0, len(database)):
            if code[0] == database[i][0]:
                fnum = database[i][1]
                break

        # Second letter
        for i in range(0, len(database)):
            if code[1] == database[i][0]:
                snum = database[i][1]
                break

        cton = str(fnum) + str(snum)

        # Raise cton is emty
        if cton == "":
            raise ValueError("cton is empty! Check convert process")

        else:
            return cton
