from iban_checker.lib.handle_file import handle_file

def to_country(code):
    """
    Extract Country name and default length of IBAN Number to an array

    Parameters:
    -----------
        code : str
            String of country code with 2 digits.

    Return:
    -------
        ctoc : array
            Return array result with country name and length.

    Raises:
    -------
        IndexError: Database is empty
        IndexError: Result list is empty

    """

    database = handle_file("countries.csv")

    # Raise missing database
    try:
        database[0][0]

    except IndexError:
        print("The database of countries is empty")
        print("Check data in file countries.csv")

    else:
        ctoc = []

        # Search for the country code
        for i in range(0, len(database)):
            if code == database[i][1]:
                ctoc.append(database[i][0])
                ctoc.append(database[i][2])
                break

        # Raise result list is empty
        try:
            ctoc[0]

        except IndexError:
            print("Result list ctoc is empty! Check the process!")

        else:
            return ctoc
