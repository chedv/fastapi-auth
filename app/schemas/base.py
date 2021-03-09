import inspect
from typing import Type
from pydantic import BaseModel
from pydantic.fields import ModelField
from fastapi import Form


def as_form(cls: Type[BaseModel]):
    new_parameters = []

    for field_name, field_model in cls.__fields__.items():
        new_parameters.append(
            inspect.Parameter(
                field_model.alias,
                inspect.Parameter.POSITIONAL_ONLY,
                default=Form(...) if field_model.required else Form(field_model.default),
                annotation=field_model.outer_type_,
            )
        )

    async def as_form_func(**data):
        return cls(**data)

    signature = inspect.signature(as_form_func)
    signature = signature.replace(parameters=new_parameters)
    as_form_func.__signature__ = signature

    setattr(cls, 'as_form', as_form_func)
    return cls
