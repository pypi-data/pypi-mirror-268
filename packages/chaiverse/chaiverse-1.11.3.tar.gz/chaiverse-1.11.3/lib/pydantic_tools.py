from cachetools import cached
import inspect
from typing import List

from pydantic import BaseModel


@cached(cache={})
def get_fields_in_schema(cls: BaseModel) -> List[str]:
    fields = list(cls.__fields__.keys()) + _get_class_properties(cls)
    fields = _remove_protected_fields(fields)
    return fields


def _remove_protected_fields(fields):
    fields = [field for field in fields if not field.startswith('_')]
    return fields


def _get_class_properties(cls):
    properties = [
        member_name for member_name, member_object in inspect.getmembers(cls)
        if inspect.isdatadescriptor(member_object)
    ]
    return properties
