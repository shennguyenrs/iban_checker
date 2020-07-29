def checker(iban_code):
    """
    Check IBAN number.

    Parameters:
    -----------
        iban_code : str
            IBAN number inputted by user.

    Returns:
    --------
        c_result : int or array
            If c_result = 0, IBAN is invalid.
            if c_result = 1, IBAN is wrong length.
            Else it will print information of IBAN: Country, Bank and BIC.

    Raises:
    -------

    """

    # Import modules
    from iban_checker.lib.code_to_country import to_country
    from iban_checker.lib.code_to_number import to_number
    from iban_checker.lib.code_to_bank import to_bank
    from iban_checker.lib.mod import mod

    # Remove all spaces
    iban_code = iban_code.replace(" ", "")

    # Extract Country name and default length
    country_code = ""
    country_code = iban_code[0] + iban_code[1]

    c_name = to_country(country_code)[0]
    c_length = int(to_country(country_code)[1])

    # Check inputted IBAN length
    if c_length != len(iban_code):
        print("Your IBAN number is not correct in length! Please enter again!")
        c_result = 1

    else:
        # Re-arrage IBAN to new string
        # Index is the number of digits of
        # Country code and check digits
        new_iban = ""
        index = 4

        # Add old Iban to new one
        for i in range(index, c_length):
            new_iban += iban_code[i]

        # Add converted country code to new IBAN
        new_iban += to_number(country_code)

        # Add 2 check digits at index 2 and 3
        new_iban += iban_code[2]
        new_iban += iban_code[3]

        # Check IBAN Valid or not
        valid = mod(new_iban)

        if valid == 1:
            c_result = []
            c_result.append(c_name)

            # Get Bank name and BIC
            c_result.append(to_bank(new_iban)[0])
            c_result.append(to_bank(new_iban)[1])

        else:
            print("Your IBAN number is invalid")
            c_result = 0

    return c_result
