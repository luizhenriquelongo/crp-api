from crp_validator.crp_validation import CRPValidation
from conf import Config

from pprint import pprint

if __name__ == "__main__":
    crp = CRPValidation(Config)
    crp_number =  ''
    cpf_number = ''
    status, user_data = crp.validate_crp_register(crp_number, cpf_number)

    pprint(status)
    pprint(user_data)
