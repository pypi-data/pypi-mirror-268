from typing import *

from pydantic import BaseModel, Field


class MatchPickMapResult(BaseModel):
    """
    None model

    """

    picked_map: str = Field(alias="picked_map")

    next_pick_team_leader: str = Field(alias="next_pick_team_leader")

    maps_left: List[str] = Field(alias="maps_left")

    map_picks_count: int = Field(alias="map_picks_count")
