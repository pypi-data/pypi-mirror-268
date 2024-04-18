from typing import *

from pydantic import BaseModel, Field

from .MapSidesEnum import MapSidesEnum


class MatchConfig(BaseModel):
    """
    None model

    """

    matchid: str = Field(alias="matchid")

    team1: Dict[str, Any] = Field(alias="team1")

    team2: Dict[str, Any] = Field(alias="team2")

    num_maps: int = Field(alias="num_maps")

    maplist: List[str] = Field(alias="maplist")

    map_sides: List[MapSidesEnum] = Field(alias="map_sides")

    clinch_series: bool = Field(alias="clinch_series")

    players_per_team: int = Field(alias="players_per_team")

    cvars: Optional[Dict[str, Any]] = Field(alias="cvars", default=None)
