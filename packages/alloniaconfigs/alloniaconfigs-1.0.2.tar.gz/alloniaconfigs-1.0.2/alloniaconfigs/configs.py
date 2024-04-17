import os
from typing import ClassVar

from dotenv import dotenv_values
from pydantic import BaseModel


class _ConfigsInstance:
    """Descriptor to handle the Configs's current instance."""

    def __set_name__(self, _, name):
        self.private_name = f"_{name}"
        self.value = None

    def __get__(self, obj, klass):
        value = klass._instance  # noqa: SLF001
        if value is None:
            value = klass()
        return value

    def __set__(self, obj, value):
        raise ValueError("Can not set Configs().instance manually")


class Configs:
    """
    .. _pydantic: https://docs.pydantic.dev/latest/

    Class to handle configurations.

    One must set :obj:`~Configs.schema` before using this class. It must
    be a class deriving from :obj:`~pydantic.BaseModel`.

    Can be instanciated with values that will take precedence over the defined
    environment variables.

    One can also have a .env file in the working directory. The priority
    to choose which value to use is as follows:

      1. If the variable is explicitely given when creating the class, uses
         this value
      2. Else, look into the .env file
      3. Else, look into :obj:`os.environ`
      4. Finally, use the default value found in :obj:`~Configs.schema`

    The allowed configuration names are the attributes of the
    :obj:`~Configs.schema`, that must derive from :obj:`~pydantic.BaseModel`.

    All configurations have a default value.

    No extra configurations will be kept in the class.

    Examples:
        Suppose you have 'ID' defined in `os.environ`, and 'SOME_STRING' in a
        .env file. You can then do:

        .. code-block:: python

            from alloniaconfigs import Configs
            from pydantic import BaseModel, Field, UUID4

            class MySchema(BaseModel):
                ID: str | None = Field(None, min_length=16, max_length=16)
                ID_MANDATORY: UUID4 = Field()
                SOME_STRING: str | None = Field(None)

            Configs.schema = MySchema
            configs = Configs(ID_MANDATORY=mandatory_id)
            configs.ID  # will have been loaded from os.environ
            configs.ID_MANDATORY  # will have been taken from the input args
            configs.SOME_STRING  # will have been taken from the .envfile

            # You only have to instanciate the Configs class once in your code,
            # then in any file you can do
            configs = Configs.instance
            # to get the exact same instance of Configs, which will be unique
    """

    _instance: ClassVar = None
    instance: ClassVar[_ConfigsInstance] = _ConfigsInstance()

    schema: ClassVar[type]
    """Must derive from :obj:`~pydantic.BaseModel`. See the `pydantic`_
    documentation if you are not familiar with it, but basically it is used to
    type-check data structures.
    """

    @classmethod
    def reset(cls):
        cls._instance = None

    def __init__(self, **kwargs):
        # copy env vars, in order not to change them with the updates
        values = {**os.environ}
        values.update(**dotenv_values(".env"))
        values.update(**kwargs)
        if not issubclass(self.schema, BaseModel):
            raise TypeError(
                "The 'schema' argument must be a class deriving from "
                "pydantic's BaseModel class"
            )
        for key, value in self.schema(**values).model_dump().items():
            setattr(self, key, value)

        Configs._instance = self
