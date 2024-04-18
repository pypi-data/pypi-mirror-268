from typing import *

from pydantic import BaseModel, Field


class MatchPlayerJoin(BaseModel):
    """
    None model

    """

    discord_user_id: str = Field(alias="discord_user_id")
