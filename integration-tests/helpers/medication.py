from typing import Dict

from faker import Faker


def get_body() -> Dict:
    fake: Faker = Faker()
    return {
        "name": f"{fake.word()}{fake.random_int()}",
        "sct_code": str(fake.random_number(digits=18, fix_len=False)),
        "unit": "units",
        "tags": [fake.word(), fake.word()],
    }
