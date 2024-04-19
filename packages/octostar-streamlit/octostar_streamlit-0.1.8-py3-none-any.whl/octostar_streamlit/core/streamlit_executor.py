from typing import Callable
from uuid import uuid4

from pydantic import BaseModel
from octostar_streamlit.core.method_call import MethodCall


class StreamlitMethodExecutor:
    def __init__(self, method_call: MethodCall, fn: Callable, key=None) -> None:
        self._method_call = method_call
        self._fn = fn
        self._key = key

    def execute(self):
        key = self._key
        if key is None:
            key = str(uuid4())

        service = self._method_call.service
        method = self._method_call.method

        if isinstance(self._method_call.params, BaseModel):
            # params = self._method_call.params.model_dump(by_alias=True)
            params = self._method_call.params.model_dump()
        else:
            params = self._method_call.params

        return self._fn(service=service, method=method, params=params, key=key)
