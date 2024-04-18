import enum


class Component(str, enum.Enum):
    ACCOUNT_ID = "account_id"
    ACCOUNT_TYPE = "account_type"
    ACCOUNT_CODE = "account_code"
    ACCOUNT_HOLDER_ID = "account_holder_id"
    BANK_CODE = "bank_code"
    BRANCH_CODE = "branch_code"
    NATIONAL_CHECKSUM_DIGITS = "national_checksum_digits"
