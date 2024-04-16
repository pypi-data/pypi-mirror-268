import json
from dataclasses import dataclass, asdict
from typing import List, Mapping, Optional
import pathlib
import typing
import requests
import backoff
import platform
from .version import __version__
import logging

logger = logging.getLogger(__name__)

HTTP_ERROR_MAX_RETRIES = 2
HTTP_ERROR_MAX_TIME = 30

NETWORK_ERROR_MAX_RETRIES = 2
NETWORK_ERROR_MAX_TIME = 30

TIMEOUT_INTERVALS = (1, 5)


@dataclass
class ApiResult:
    message: str


@dataclass
class ApiError:
    message: str


@dataclass
class Policy:
    filename: Optional[str]
    src: str


@dataclass
class GetPolicyResult:
    policy: Optional[Policy]


@dataclass
class VariableValue:
    type: Optional[str]
    id: Optional[str]


@dataclass
class ConcreteValue:
    type: str
    id: str


@dataclass
class ConcreteFact:
    predicate: str
    args: List[ConcreteValue]

    @classmethod
    def from_json(cls, json):
        return cls(
            predicate=json["predicate"], args=[ConcreteValue(**v) for v in json["args"]]
        )


@dataclass
class VariableFact:
    predicate: str
    args: List[VariableValue]

    @classmethod
    def from_json(cls, json):
        return cls(
            predicate=json["predicate"], args=[VariableValue(**v) for v in json["args"]]
        )


@dataclass
class Bulk:
    delete: List[VariableFact]
    tell: List[ConcreteFact]


@dataclass
class AuthorizeResult:
    allowed: bool


@dataclass
class AuthorizeQuery:
    actor_type: str
    actor_id: str
    action: str
    resource_type: str
    resource_id: str
    context_facts: List[ConcreteFact]


@dataclass
class AuthorizeResourcesResult:
    results: List[ConcreteValue]


@dataclass
class AuthorizeResourcesQuery:
    actor_type: str
    actor_id: str
    action: str
    resources: List[ConcreteValue]
    context_facts: List[ConcreteFact]


@dataclass
class ListResult:
    results: List[str]


@dataclass
class ListQuery:
    actor_type: str
    actor_id: str
    action: str
    resource_type: str
    context_facts: List[ConcreteFact]


@dataclass
class ActionsResult:
    results: List[str]


@dataclass
class ActionsQuery:
    actor_type: str
    actor_id: str
    resource_type: str
    resource_id: str
    context_facts: List[ConcreteFact]


@dataclass
class QueryResult:
    results: List[VariableFact]


@dataclass
class Query:
    fact: VariableFact
    context_facts: List[ConcreteFact]


@dataclass
class StatsResult:
    num_roles: int
    num_relations: int
    num_facts: int


@dataclass
class ResourceMetadata:
    roles: List[str]
    permissions: List[str]
    relations: Mapping[str, str]


@dataclass
class PolicyMetadata:
    resources: Mapping[str, ResourceMetadata]


@dataclass
class LocalQueryResult:
    sql: str


def _fatal_retry_code(exc: Exception) -> bool:
    if isinstance(exc, requests.exceptions.HTTPError):
        # Allow retries on 429 rate-limits and 5xx errors only
        if exc.response.status_code == 429:
            return False
        return 400 <= exc.response.status_code < 500
    else:
        return False


class API:
    def __init__(
        self,
        url="https://api.osohq.com",
        api_key=None,
        fallback_url=None,
        *,
        data_bindings=None,
    ):
        self.url = url
        if not self.url.endswith("/"):
            self.url += "/"
        self.api_base = "api"
        self.user_agent = (
            f"Oso Cloud (python {platform.python_version()}; rv:{__version__})"
        )
        if api_key:
            self.token = api_key
        else:
            raise ValueError("Must set an api_key")
        self.session = requests.Session()
        self.session.headers.update(self._default_headers())

        self.fallback_url = fallback_url
        if self.fallback_url:
            if not self.fallback_url.endswith("/"):
                self.fallback_url += "/"
            self.fallback_session = requests.Session()
            self.fallback_session.headers.update(self._default_headers())

        self.data_bindings = None
        if data_bindings:
            self.data_bindings = pathlib.Path(data_bindings).read_text()

    def _handle_result(self, result, is_mutation=False):
        if not result.ok:
            code, text = result.status_code, result.text
            msg = f"Got unexpected error from Oso Service: {code}\n{text}"
            raise Exception(msg)
        try:
            if is_mutation:
                self._set_last_offset(result)
            return result.json()
        except json.decoder.JSONDecodeError:
            raise Exception("failed to deserialize results: ", result.text)

    def _fallback_eligible(self, path: str):
        return self.fallback_url and path in [
            "/authorize",
            "/authorize_resources",
            "/list",
            "/actions",
            "/query",
        ]

    def _default_headers(self):
        return {
            "Authorization": f"Bearer {self.token}",
            "User-Agent": self.user_agent,
            "X-OsoApiVersion": "0",
        }

    def _set_last_offset(self, result):
        last_offset = result.headers.get("OsoOffset")
        if last_offset:
            self.session.headers.update({"OsoOffset": last_offset})

    def _do_post(self, path, params, json, fallback=False):
        @backoff.on_exception(
            backoff.expo,
            (requests.exceptions.ConnectionError, requests.exceptions.Timeout),
            max_time=NETWORK_ERROR_MAX_TIME,
            max_tries=NETWORK_ERROR_MAX_RETRIES,
        )
        @backoff.on_exception(
            backoff.expo,
            requests.exceptions.HTTPError,
            max_time=HTTP_ERROR_MAX_TIME,
            max_tries=HTTP_ERROR_MAX_RETRIES,
            giveup=_fatal_retry_code,
        )
        def _do_post_inner(session, url, path, params, json):
            return session.post(
                f"{url}{self.api_base}{path}",
                params=params,
                json=json,
                timeout=TIMEOUT_INTERVALS,
            )

        try:
            return _do_post_inner(self.session, self.url, path, params, json)
        except (
            requests.exceptions.ConnectionError,
            requests.exceptions.Timeout,
        ) as exc:
            logger.info(f"_do_post: falling back to {self.fallback_url}")
            if self._fallback_eligible(path):
                return _do_post_inner(
                    self.fallback_session, self.fallback_url, path, params, json
                )
            else:
                raise exc

    def _do_get(self, path, params, json):
        @backoff.on_exception(
            backoff.expo,
            (requests.exceptions.ConnectionError, requests.exceptions.Timeout),
            max_time=NETWORK_ERROR_MAX_TIME,
            max_tries=NETWORK_ERROR_MAX_RETRIES,
        )
        @backoff.on_exception(
            backoff.expo,
            requests.exceptions.HTTPError,
            max_time=HTTP_ERROR_MAX_TIME,
            max_tries=HTTP_ERROR_MAX_RETRIES,
            giveup=_fatal_retry_code,
        )
        def _do_get_inner(session, url, path, params, json):
            return session.get(
                f"{url}{self.api_base}{path}",
                params=params,
                json=json,
                timeout=TIMEOUT_INTERVALS,
            )

        try:
            return _do_get_inner(self.session, self.url, path, params, json)
        except (
            requests.exceptions.ConnectionError,
            requests.exceptions.Timeout,
        ) as exc:
            logger.info(f"_do_get: falling back to {self.fallback_url}")
            if self._fallback_eligible(path):
                return _do_get_inner(
                    self.fallback_session, self.fallback_url, path, params, json
                )
            else:
                raise exc

    def _do_delete(self, path, params, json):
        @backoff.on_exception(
            backoff.expo,
            (requests.exceptions.ConnectionError, requests.exceptions.Timeout),
            max_time=NETWORK_ERROR_MAX_TIME,
            max_tries=NETWORK_ERROR_MAX_RETRIES,
        )
        @backoff.on_exception(
            backoff.expo,
            requests.exceptions.HTTPError,
            max_time=HTTP_ERROR_MAX_TIME,
            max_tries=HTTP_ERROR_MAX_RETRIES,
            giveup=_fatal_retry_code,
        )
        def _do_delete_inner(session, url, path, params, json):
            return session.delete(
                f"{url}{self.api_base}{path}",
                params=params,
                json=json,
                timeout=TIMEOUT_INTERVALS,
            )

        try:
            return _do_delete_inner(self.session, self.url, path, params, json)
        except (
            requests.exceptions.ConnectionError,
            requests.exceptions.Timeout,
        ) as exc:
            logger.info(f"_do_delete: falling back to {self.fallback_url}")
            if self._fallback_eligible(path):
                return _do_delete_inner(
                    self.fallback_session, self.fallback_url, path, params, json
                )
            else:
                raise exc

    def get_policy(self):
        params = None
        json = None
        result = self._do_get("/policy", params=params, json=json)
        response = self._handle_result(result)
        return GetPolicyResult(**response)

    def post_policy(self, data):
        params = None
        json = asdict(data)
        result = self._do_post("/policy", params=params, json=json)
        response = self._handle_result(result, True)
        return ApiResult(**response)

    def post_facts(self, data):
        params = None
        json = asdict(data)
        result = self._do_post("/facts", params=params, json=json)
        response = self._handle_result(result, True)
        return ConcreteFact.from_json(response)

    def delete_facts(self, data):
        params = None
        json = asdict(data)
        result = self._do_delete("/facts", params=params, json=json)
        response = self._handle_result(result, True)
        return ApiResult(**response)

    def post_bulk_load(self, data):
        params = None
        json = list(map(asdict, data))
        result = self._do_post("/bulk_load", params=params, json=json)
        response = self._handle_result(result, True)
        return ApiResult(**response)

    def post_bulk_delete(self, data):
        params = None
        json = list(map(asdict, data))
        result = self._do_post("/bulk_delete", params=params, json=json)
        response = self._handle_result(result, True)
        return ApiResult(**response)

    def post_bulk(self, data):
        params = None
        json = asdict(data)
        result = self._do_post("/bulk", params=params, json=json)
        response = self._handle_result(result, True)
        return ApiResult(**response)

    def post_authorize(self, data):
        params = None
        json = asdict(data)
        result = self._do_post("/authorize", params=params, json=json)
        response = self._handle_result(result)
        return AuthorizeResult(**response)

    def post_authorize_resources(self, data):
        params = None
        json = asdict(data)
        result = self._do_post("/authorize_resources", params=params, json=json)
        response = self._handle_result(result)
        return AuthorizeResourcesResult(
            results=[ConcreteValue(**r) for r in response["results"]]
        )

    def post_list(self, data):
        params = None
        json = asdict(data)
        result = self._do_post("/list", params=params, json=json)
        response = self._handle_result(result)
        return ListResult(**response)

    def post_actions(self, data):
        params = None
        json = asdict(data)
        result = self._do_post("/actions", params=params, json=json)
        response = self._handle_result(result)
        return ActionsResult(**response)

    def get_stats(self):
        params = None
        json = None
        result = self._do_get("/stats", params=params, json=json)
        response = self._handle_result(result)
        return StatsResult(**response)

    def post_authorize_query(self, query):
        params = None
        json = {
            "query": asdict(query),
            "data_bindings": self.data_bindings,
        }
        result = self._do_post("/authorize_query", params=params, json=json)
        response = self._handle_result(result)
        return LocalQueryResult(**response)

    def post_list_query(self, query, column):
        params = None
        json = {
            "query": asdict(query),
            "column": column,
            "data_bindings": self.data_bindings,
        }
        result = self._do_post("/list_query", params=params, json=json)
        response = self._handle_result(result)
        return LocalQueryResult(**response)

    def clear_data(self):
        params = None
        json = None
        result = self._do_post("/clear_data", params=params, json=json)
        response = self._handle_result(result, True)
        return ApiResult(**response)

    def get_facts(self, predicate: str, args: List[VariableValue]):
        params = {}
        params["predicate"] = predicate
        for i, arg in enumerate(args):
            if arg.type is not None:
                params[f"args.{i}.type"] = arg.type
            if arg.id is not None:
                params[f"args.{i}.id"] = arg.id
        json = None
        result = self._do_get("/facts", params=params, json=json)
        response = self._handle_result(result)
        result = []
        for item in response:
            result.append(ConcreteFact.from_json(item))
        return result

    def post_query(self, data):
        params = None
        json = asdict(data)
        result = self._do_post("/query", params=params, json=json)
        response = self._handle_result(result)
        return QueryResult(
            list(
                map(
                    VariableFact.from_json,
                    response["results"],
                )
            )
        )

    def get_policy_metadata(self, version: Optional[int] = None) -> PolicyMetadata:
        params = {"version": version}
        result = self._do_get("/policy_metadata", params=params, json=None)
        response: typing.Any = self._handle_result(result)
        metadata = response["metadata"]
        return PolicyMetadata(
            resources={
                k: ResourceMetadata(**v) for k, v in metadata["resources"].items()
            }
        )
