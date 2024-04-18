import json
from typing import *

import httpx

from ..api_config import APIConfig, HTTPException
from ..models import *


def matches_list(page: Optional[int] = None, api_config_override: Optional[APIConfig] = None) -> PaginatedMatchList:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/matches/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {"page": page}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    with httpx.Client(base_url=base_path, verify=api_config.verify) as client:
        response = client.request(
            "get",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return PaginatedMatchList(**response.json()) if response.json() is not None else PaginatedMatchList()


def matches_create(data: CreateMatch, api_config_override: Optional[APIConfig] = None) -> Match:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/matches/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    with httpx.Client(base_url=base_path, verify=api_config.verify) as client:
        response = client.request("post", httpx.URL(path), headers=headers, params=query_params, json=data.dict())

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return Match(**response.json()) if response.json() is not None else Match()


def matches_retrieve(id: int, api_config_override: Optional[APIConfig] = None) -> Match:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/matches/{id}/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    with httpx.Client(base_url=base_path, verify=api_config.verify) as client:
        response = client.request(
            "get",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return Match(**response.json()) if response.json() is not None else Match()


def matches_update(id: int, data: Match, api_config_override: Optional[APIConfig] = None) -> Match:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/matches/{id}/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    with httpx.Client(base_url=base_path, verify=api_config.verify) as client:
        response = client.request("put", httpx.URL(path), headers=headers, params=query_params, json=data.dict())

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return Match(**response.json()) if response.json() is not None else Match()


def matches_destroy(id: int, api_config_override: Optional[APIConfig] = None) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/matches/{id}/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    with httpx.Client(base_url=base_path, verify=api_config.verify) as client:
        response = client.request(
            "delete",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 204:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return None


def matches_partial_update(id: int, data: PatchedMatch, api_config_override: Optional[APIConfig] = None) -> Match:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/matches/{id}/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    with httpx.Client(base_url=base_path, verify=api_config.verify) as client:
        response = client.request("patch", httpx.URL(path), headers=headers, params=query_params, json=data.dict())

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return Match(**response.json()) if response.json() is not None else Match()


def matches_ban_create(
    id: int, data: MatchBanMap, api_config_override: Optional[APIConfig] = None
) -> MatchBanMapResult:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/matches/{id}/ban/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    with httpx.Client(base_url=base_path, verify=api_config.verify) as client:
        response = client.request("post", httpx.URL(path), headers=headers, params=query_params, json=data.dict())

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return MatchBanMapResult(**response.json()) if response.json() is not None else MatchBanMapResult()


def matches_bans_retrieve(id: int, api_config_override: Optional[APIConfig] = None) -> MapBan:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/matches/{id}/bans/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    with httpx.Client(base_url=base_path, verify=api_config.verify) as client:
        response = client.request(
            "get",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return MapBan(**response.json()) if response.json() is not None else MapBan()


def matches_config_retrieve(id: int, api_config_override: Optional[APIConfig] = None) -> MatchConfig:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/matches/{id}/config/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    with httpx.Client(base_url=base_path, verify=api_config.verify) as client:
        response = client.request(
            "get",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return MatchConfig(**response.json()) if response.json() is not None else MatchConfig()


def matches_join_create(id: int, data: MatchPlayerJoin, api_config_override: Optional[APIConfig] = None) -> Match:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/matches/{id}/join/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    with httpx.Client(base_url=base_path, verify=api_config.verify) as client:
        response = client.request("post", httpx.URL(path), headers=headers, params=query_params, json=data.dict())

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return Match(**response.json()) if response.json() is not None else Match()


def matches_load_create(id: int, data: Match, api_config_override: Optional[APIConfig] = None) -> Match:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/matches/{id}/load/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    with httpx.Client(base_url=base_path, verify=api_config.verify) as client:
        response = client.request("post", httpx.URL(path), headers=headers, params=query_params, json=data.dict())

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return Match(**response.json()) if response.json() is not None else Match()


def matches_pick_create(
    id: int, data: MatchPickMap, api_config_override: Optional[APIConfig] = None
) -> MatchPickMapResult:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/matches/{id}/pick/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    with httpx.Client(base_url=base_path, verify=api_config.verify) as client:
        response = client.request("post", httpx.URL(path), headers=headers, params=query_params, json=data.dict())

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return MatchPickMapResult(**response.json()) if response.json() is not None else MatchPickMapResult()


def matches_picks_retrieve(id: int, api_config_override: Optional[APIConfig] = None) -> MatchMapSelected:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/matches/{id}/picks/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    with httpx.Client(base_url=base_path, verify=api_config.verify) as client:
        response = client.request(
            "get",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return MatchMapSelected(**response.json()) if response.json() is not None else MatchMapSelected()


def matches_recreate_create(id: int, data: Match, api_config_override: Optional[APIConfig] = None) -> Match:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/matches/{id}/recreate/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    with httpx.Client(base_url=base_path, verify=api_config.verify) as client:
        response = client.request("post", httpx.URL(path), headers=headers, params=query_params, json=data.dict())

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return Match(**response.json()) if response.json() is not None else Match()


def matches_shuffle_create(id: int, data: Match, api_config_override: Optional[APIConfig] = None) -> Match:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/matches/{id}/shuffle/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    with httpx.Client(base_url=base_path, verify=api_config.verify) as client:
        response = client.request("post", httpx.URL(path), headers=headers, params=query_params, json=data.dict())

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return Match(**response.json()) if response.json() is not None else Match()


def matches_webhook_create(data: Match, api_config_override: Optional[APIConfig] = None) -> Match:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/matches/webhook/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    with httpx.Client(base_url=base_path, verify=api_config.verify) as client:
        response = client.request("post", httpx.URL(path), headers=headers, params=query_params, json=data.dict())

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return Match(**response.json()) if response.json() is not None else Match()
