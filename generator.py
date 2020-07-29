from iban_checker.lib.code_to_number import to_number
from iban_checker.lib.mod import mod

def generator(country_code, bank_code, bank_account):
    """
    IBAN Generator from country code, bank code and bank code

    Parameters:
    -----------
        country_code: str
            2 letters of country
        bank_code: str
            Digits of bank and branches
        bank_account: str
            Bank account number

    Returns:
    --------
        g_result: str

    Raises:
    -------

    """

    # Convert country code to number
    cc_number = to_number(country_code)

    # Make BBAN code and add "00" to the end
    zero_bban_code = bank_code + bank_account + cc_number + "00"

    # Calculate check digits
    check_digit = str(98 - mod(zero_bban_code))

    # Final result IBAN
    g_result = country_code + check_digit + bank_code + bank_account

    # Add space to string
    g_result = " ".join(g_result[i:i+4] for i in range(0, len(g_result), 4))

    return g_result
