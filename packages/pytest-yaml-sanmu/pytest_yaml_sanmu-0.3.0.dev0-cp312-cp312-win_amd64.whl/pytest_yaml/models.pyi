from pydantic import BaseModel
from typing import List

class Case(BaseModel):
    test_name: str
    steps: List[dict]
    mark: List[str | dict]
    @classmethod
    def from_case_dict(cls, case_dict: dict): ...
    @classmethod
    def to_yaml(cls, obj) -> str: ...
    @classmethod
    def from_yaml(cls, yaml_str: str): ...
