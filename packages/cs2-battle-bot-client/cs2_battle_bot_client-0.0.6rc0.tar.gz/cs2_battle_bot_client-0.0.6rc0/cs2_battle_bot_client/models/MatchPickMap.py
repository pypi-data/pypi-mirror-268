from typing import *

from pydantic import BaseModel, Field


class MatchPickMap(BaseModel):
    """
    None model

    """

    interaction_user_id: str = Field(alias="interaction_user_id")

    map_tag: str = Field(alias="map_tag")
