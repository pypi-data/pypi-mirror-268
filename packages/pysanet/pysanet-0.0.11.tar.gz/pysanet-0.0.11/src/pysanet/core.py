import functools
from typing import Annotated
from uuid import UUID

from pydantic import UUID4
from pydantic.functional_validators import AfterValidator


def sanetapi(func=None, *, schema_out=None):
    if func is None:
        return functools.partial(sanetapi, schema_out=schema_out)

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if "params" not in kwargs:
            kwargs["params"] = self.auth_data
        else:
            kwargs["params"].update(self.auth_data)
        for sanet_param in ["tenant", "username"]:
            if sanet_param in kwargs:
                kwargs["params"].update({sanet_param: kwargs[sanet_param]})

        response = func(self, *args, **kwargs)

        if not schema_out:
            return response
        result = schema_out.model_validate_json(response.content)
        result._response = response
        return result

    return wrapper


def check_sanet_id(value: str | UUID4) -> str:
    sanet_id = value.hex if isinstance(value, UUID) else value
    return sanet_id


SanetId = Annotated[str | UUID4, AfterValidator(check_sanet_id)]
