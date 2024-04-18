from typing import *

from pydantic import BaseModel, Field

from .CreateGuildMember import CreateGuildMember


class CreateGuild(BaseModel):
    """
    None model

    """

    name: str = Field(alias="name")

    guild_id: str = Field(alias="guild_id")

    owner_id: str = Field(alias="owner_id")

    owner_username: str = Field(alias="owner_username")

    members: List[CreateGuildMember] = Field(alias="members")
