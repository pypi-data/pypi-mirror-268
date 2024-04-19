from humps import camelize
from pydantic import BaseModel


class ParamsBaseModel(BaseModel):
    class Config:
        arbitrary_types_allowed = True
    #     alias_generator = camelize
    #     populate_by_name = True
