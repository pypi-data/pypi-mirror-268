from typing import *

from pydantic import BaseModel, Field


class MatchBanMapResult(BaseModel):
    """
    None model

    """

    banned_map: str = Field(alias="banned_map")

    next_ban_team_leader: str = Field(alias="next_ban_team_leader")

    maps_left: List[str] = Field(alias="maps_left")

    map_bans_count: int = Field(alias="map_bans_count")
