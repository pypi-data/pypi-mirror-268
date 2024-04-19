from collections import namedtuple
from dataclasses import dataclass
from typing import Any, Literal, Union

from pydantic import BaseModel

# @dataclass
class MethodCall(BaseModel):
    service: str
    method: str
    # params: BaseModel
    params: Any

# MethodCall(method="")
