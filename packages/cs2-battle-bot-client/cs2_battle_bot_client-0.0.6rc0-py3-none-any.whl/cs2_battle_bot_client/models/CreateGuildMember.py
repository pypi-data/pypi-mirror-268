from typing import *

from pydantic import BaseModel, Field


class CreateGuildMember(BaseModel):
    """
    None model

    """

    user_id: str = Field(alias="user_id")

    username: str = Field(alias="username")
