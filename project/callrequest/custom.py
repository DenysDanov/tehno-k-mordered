import re
from typing import List

from django.http import HttpRequest


def validate_phone_number(phone_number: str) -> bool:
    return not re.search(r'[^+0-9\s\(\)|-]', phone_number)

def validate_request(request_dict : dict, *args : List[str]) -> bool:
    return all([request_dict.get(key) for key in args])
