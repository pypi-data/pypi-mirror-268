"""
Generates a typed client for Oso Cloud

Usage:
    python -m oso_cloud.experimental.client_gen > client_types.py
    python -m oso_cloud.experimental.client_gen --generate-helper-methods > client_helpers.py
"""

from oso_cloud import Oso
from oso_cloud.api import PolicyMetadata, ResourceMetadata
from os import environ
import argparse

from logging import getLogger

logger = getLogger(__name__)


def proper_to_snake(name: str) -> str:
    return "".join(map(lambda c: f"_{c.lower()}" if c.isupper() else c, name))[1:]


def snake_to_proper(name: str) -> str:
    return "".join(map(str.title, name.split("_")))


class PolicyMetadataHelpers(PolicyMetadata):
    def __init__(self, metadata: PolicyMetadata):
        # skip global resource
        self.resources = {k: v for k, v in metadata.resources.items() if k != "global"}

    def frontmatter(self) -> str:
        return """
import typing
from typing import List, Literal, Tuple, Union
from oso_cloud import Oso, Value, Fact
from dataclasses import dataclass
"""

    def _relation_to_type(self, resource: str, relation: str, to: str) -> str:
        return f"{resource}{snake_to_proper(relation)}Relation = Tuple[{resource}, Literal['{relation}'], \"{to}\"]"

    def _print_resource_types(self, resource: str, metadata: ResourceMetadata) -> str:
        s = f"""
@dataclass
class {resource}:
    id: str
    type = \"{resource}\"

    def __init__(self, id: typing.Any):
        self.id = str(id)

    def as_value(self) -> Value:
        return {{"type": self.type, "id": self.id}}
    """
        if len(metadata.permissions) == 0:
            s += f"\n{resource}Actions = typing.NoReturn"
        else:
            permissions = ", ".join(map(lambda p: f"'{p}'", metadata.permissions))
            s += f"\n{resource}Actions = Literal[{permissions}]"
        if len(metadata.roles) == 0:
            s += f"\n{resource}Roles = typing.NoReturn"
        else:
            roles = ", ".join(map(lambda p: f"'{p}'", metadata.roles))
            s += f"\n{resource}Roles = Literal[{roles}]"
        if len(metadata.relations) == 0:
            s += f"\n{resource}Relations = typing.NoReturn"
        elif len(metadata.relations) == 1:
            relation, to = next(iter(metadata.relations.items()))
            s += f"\n{self._relation_to_type(resource, relation, to)}"
            s += (
                f"\n{resource}Relations = {resource}{snake_to_proper(relation)}Relation"
            )
        else:
            relation_list = "\n".join(
                map(
                    lambda relation: f"{self._relation_to_type(resource, relation[0], relation[1])}",
                    metadata.relations.items(),
                )
            )
            relations = ", ".join(
                map(
                    lambda relation: f"{resource}{snake_to_proper(relation)}Relation",
                    metadata.relations.keys(),
                )
            )
            s += f"\n{relation_list}\n{resource}Relations = Union[{relations}]"

        return s

    def print_types(self) -> str:
        s = "\n".join(
            map(
                lambda k: self._print_resource_types(k[0], k[1]), self.resources.items()
            )
        )
        if len(self.resources) == 0:
            s += "\nResources = typing.NoReturn"
            s += "\nRelations = typing.NoReturn"
        elif len(self.resources) == 1:
            s += f"\nResources = {next(iter(self.resources.keys()))}"
            s += f"\nRelations = {next(iter(self.resources))}Relations"
        else:
            resource_list = ", ".join(
                map(lambda resource: f'"{resource}"', self.resources.keys())
            )
            s += f"\nResources = Union[{resource_list}]"
            relation_list = ", ".join(
                map(
                    lambda resource: f'"{resource}Relations"',
                    self.resources.keys(),
                )
            )
            s += f"\nRelations = Union[{relation_list}]"
        resource_list = ", ".join(
            map(lambda resource: f'"{resource}"', self.resources.keys())
        )

        s += """
class TypedRelation:
    def __init__(self, fact: Relations):
        self.fact = fact

    def as_fact(self) -> Fact:
        return {"name": "has_relation", "args": [self.fact[0].as_value(), self.fact[1], self.fact[2].as_value()]}
        """

        return s

    def __print_helper_methods(self, resource: str, metadata: ResourceMetadata) -> str:
        resource_lower = proper_to_snake(resource)
        s = ""
        if len(metadata.roles) > 0:
            s += f"""
    def assign_{resource_lower}_role(self, actor: User, resource: {resource}, role: {resource}Roles):
            return self.tell({{"name":"has_role", "args":[actor.as_value(), role, resource.as_value()]}})
    """
        s += f"""
    def authorize_{resource_lower}(self, actor: User, action: {resource}Actions, resource: {resource}) -> bool:
            return self.authorize(actor.as_value(), action, resource.as_value())

    def list_{resource_lower}s(self, actor: User, action: {resource}Actions) -> List[str]:
            return self.list(actor.as_value(), action, "{resource}")
    """
        return s

    def print_helper_methods(self) -> str:
        authorize_helpers = "\n".join(
            map(
                lambda k: self.__print_helper_methods(k[0], k[1]),
                self.resources.items(),
            )
        )

        return f"""
class TypedOso(Oso):
    def actions(self, actor: User, resource: Resources) -> List[str]:
        return super().actions(actor.as_value(), resource.as_value())
{authorize_helpers}
        """


def from_env() -> Oso:
    api_key = environ.get("OSO_AUTH")
    if api_key is None:
        raise Exception("OSO_AUTH not set")
    oso_url = environ.get("OSO_URL", "https://api.osohq.com")
    return Oso(api_key=api_key, url=oso_url)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="oso_cloud.typed_client",
        description="Generates a typed client for Oso Cloud",
    )
    # parser.add_argument('--version', type=int, help='Version of the policy to generate a client for')
    parser.add_argument(
        "--generate-helper-methods",
        action="store_true",
        help="Generate helper methods for assigning roles and authorizing resources",
    )

    args = parser.parse_args()
    oso = from_env()
    policy_metadata = PolicyMetadataHelpers(oso.get_policy_metadata())
    logger.debug("got metadata: ", policy_metadata)

    print(policy_metadata.frontmatter())
    print(policy_metadata.print_types())
    if args.generate_helper_methods:
        print(policy_metadata.print_helper_methods())
