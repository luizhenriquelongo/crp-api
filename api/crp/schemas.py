from pydantic import (
    BaseModel,
    Field,
    validator,
)
from validate_docbr import CPF

import utils


cpf_validator = CPF()


class CRPRegisterValidationInput(BaseModel):
    cpf: str = Field(..., title='CPF', description='Cadastro de Pessoa Física')
    crp_register: str = Field(
        ..., title='Registro CRP', description='Número de inscrição junto ao Conselho Regional de Psicologia'
    )

    @validator('cpf')
    def must_be_a_valid_cpf(cls, value: str):
        cleaned_cpf = utils.clean_str(value)
        cpf_with_mask = cpf_validator.mask(cleaned_cpf)
        if not cpf_validator.validate(cpf_with_mask):
            raise ValueError(f'O CPF: "{cpf_with_mask}" não é um CPF válido.')

        return cleaned_cpf

    @validator('crp_register')
    def must_have_6_digits(cls, value: str):
        cleaned_crp = utils.clean_str(value)
        if len(cleaned_crp) != 6:
            raise ValueError(f'O CRP: "{cleaned_crp}" não é possui 6 dígitos.')

        return cleaned_crp
