from typing import *

from pydantic import BaseModel, Field

from .MapSidesEnum import MapSidesEnum
from .MatchTypeEnum import MatchTypeEnum


class CreateMatch(BaseModel):
    """
    None model

    """

    discord_users_ids: List[str] = Field(alias="discord_users_ids")

    author_id: str = Field(alias="author_id")

    server_id: Optional[str] = Field(alias="server_id", default=None)

    guild_id: str = Field(alias="guild_id")

    match_type: Optional[MatchTypeEnum] = Field(alias="match_type", default=None)

    clinch_series: Optional[bool] = Field(alias="clinch_series", default=None)

    map_sides: Optional[List[Optional[MapSidesEnum]]] = Field(alias="map_sides", default=None)

    cvars: Optional[Dict[str, Any]] = Field(alias="cvars", default=None)
