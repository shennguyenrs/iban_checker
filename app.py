def run():
    """
    IBAN Cheker and Generator

    Parameters:
    -----------

    Returns:
    --------

    Raises:
    -------

    """

    from iban_checker.checker import checker
    from iban_checker.generator import generator

    print("------------------------------------------------")
    print("-----Welcome to IBAN Checker and Generator------")
    print("------------------------------------------------")

    control = True

    # Choose tools
    while control:
        print("\nPlease choose your tool:")
        print("1. Check your IBAN number")
        print("2. Generate your own IBAN number")
        print("0. Exit")
        print("Choose your tool:")
        tool = int(input())

        if tool == 0:
            control = False

        elif tool == 1:
            print("------------------------------------------------")
            sub_control = True

            while sub_control:
                # Input IBAN Code to check
                print("Input your IBAN number: ")
                iban_code = str(input())
                checker_result = checker(iban_code)

                if checker_result == 0:
                    sub_control = False

                elif checker_result == 1:
                    print("\nDo you want to input again? (y/n)")
                    sub_control = bool(str(input()).lower() == "y")

                else:
                    print("\n"+iban_code + " is valid")
                    print("Country:\t{0}".format(checker_result[0]))
                    print("Bank:\t{0}".format(checker_result[1]))
                    print("BIC:\t{0}".format(checker_result[2]))
                    sub_control = False
                    print("------------------------------------------------")

        elif tool == 2:
            print("------------------------------------------------")
            print("Enter country code: ")
            c_code = str(input())
            print("Enter bank codde: ")
            b_code = str(input())
            print("Enter ban account number: ")
            b_account = str(input())

            generator_result = generator(c_code, b_code, b_account)

            print("\nYour IBAN is", generator_result)
            print("------------------------------------------------")

        else:
            print("You enter wrong number! Please enter the tool number again!")
            print("------------------------------------------------")
