from iban_checker.lib.handle_file import handle_file

def to_bank(code):
    """
    Extract bank name and BIC from the IBAN code.

    Parameters:
    -----------
        code : str
            IBAN code after moved country code and check digits to the end.

    Return:
    -------
        ctob : array
            Array contains bank name and BIC.

    Raises:
    -------
        IndexError: Database is empty

    """

    database = handle_file("banks.csv")

    # Raise the database is empty
    try:
        database[0][0]

    except IndexError:
        print("The database of banks is empty")
        print("Check data in file banks.csv")

    else:
        # Add bank name and BIC to ctob
        for i in range(0, len(database)):
            bank_code = ""

            # Split the bank code from IBAN by the length depend on the bank
            for j in range(0, len(database[i][1])):
                bank_code += code[j]

            # Add the bank name and BIC if the lengths are equal
            ctob = []

            if int(bank_code) == int(database[i][1]):
                ctob.append(database[i][0])
                ctob.append(database[i][2])
                break

        if ctob == []:
            ctob.append("Can not found Bank in database")
            ctob.append("Can not found BIC in database")

        return ctob
