from typing import Union

from django.db.models.query import QuerySet

def get_safe_slice(l: Union[list, QuerySet], slice:int) -> list:
    return list(l) if len(list(l)) < slice else list(l)[:slice]