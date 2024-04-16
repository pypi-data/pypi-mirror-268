from typing import List, Sequence, Set, Union

from . import api
from .types import (
    Fact,
    OutputFact,
    OutputVariableFact,
    Value,
    VariableFact,
)
from .helpers import (
    from_api_fact,
    from_variable_api_facts,
    to_api_fact,
    to_api_value,
    from_api_facts,
    to_api_facts,
    to_api_variable_fact,
)


class Oso:
    """Oso Cloud client

    For more detailed documentation, see
    https://www.osohq.com/docs/reference/client-apis/python
    """

    def __init__(
        self,
        url: str = "https://api.osohq.com",
        api_key=None,
        fallback_url=None,
        *,
        data_bindings=None,
    ):
        self.api = api.API(url, api_key, fallback_url, data_bindings=data_bindings)

    def authorize(
        self,
        actor: Value,
        action: str,
        resource: Value,
        context_facts: List[Fact] = [],
    ) -> bool:
        """Check a permission:

        :return: true if the actor can perform the action on the resource;
        otherwise false.
        """
        actor_typed_id = to_api_value(actor)
        resource_typed_id = to_api_value(resource)
        data = api.AuthorizeQuery(
            actor_typed_id.type,
            actor_typed_id.id,
            action,
            resource_typed_id.type,
            resource_typed_id.id,
            to_api_facts(context_facts),
        )
        result = self.api.post_authorize(data)
        return result.allowed

    def authorize_resources(
        self,
        actor: Value,
        action: str,
        resources: Union[List[Value], None],
        context_facts: List[Fact] = [],
    ) -> List[Value]:
        """Check authorized resources:

        Returns a subset of the resources on which an actor can perform
        a particular action. Ordering and duplicates, if any exist, are preserved.
        """

        def key(e: Union[Value, api.ConcreteValue]) -> str:
            if isinstance(e, api.ConcreteValue):
                return f"{e.type}:{e.id}"
            else:
                e = to_api_value(e)
                return f"{e.type}:{e.id}"

        if not resources or len(resources) == 0:
            return []

        resources_extracted = [to_api_value(r) for r in resources]
        actor_typed_id = to_api_value(actor)
        data = api.AuthorizeResourcesQuery(
            actor_typed_id.type,
            actor_typed_id.id,
            action,
            resources_extracted,
            to_api_facts(context_facts),
        )
        result = self.api.post_authorize_resources(data)
        if len(result.results) == 0:
            return []

        results_lookup: Set[str] = set(map(lambda r: key(r), result.results))

        return list(
            filter(
                lambda r: key(r) in results_lookup,
                resources,
            )
        )

    def list(
        self,
        actor: Value,
        action: str,
        resource_type: str,
        context_facts: List[Fact] = [],
    ) -> List[str]:
        """List authorized resources:

        Fetches a list of resource ids on which an actor can perform a
        particular action.
        """
        actor_typed_id = to_api_value(actor)
        data = api.ListQuery(
            actor_typed_id.type,
            actor_typed_id.id,
            action,
            resource_type,
            to_api_facts(context_facts),
        )
        result = self.api.post_list(data)
        return result.results

    def actions(
        self,
        actor: Value,
        resource: Value,
        context_facts: List[Fact] = [],
    ) -> List[str]:
        """List authorized actions:

        Fetches a list of actions which an actor can perform on a particular resource.
        """
        actor_typed_id = to_api_value(actor)
        resource_typed_id = to_api_value(resource)
        data = api.ActionsQuery(
            actor_typed_id.type,
            actor_typed_id.id,
            resource_typed_id.type,
            resource_typed_id.id,
            to_api_facts(context_facts),
        )
        result = self.api.post_actions(data)
        return result.results

    def tell(self, fact: Fact) -> OutputFact:
        """Add a fact:

        Adds a fact with the given name and arguments.
        """
        api_fact = to_api_fact(fact)
        result = self.api.post_facts(api_fact)
        return from_api_fact(result)

    def bulk_tell(self, facts: List[Fact]):
        """Add many facts:

        Adds many facts at once.
        """
        self.api.post_bulk_load(to_api_facts(facts))

    def delete(self, fact: Fact):
        """Delete fact:

        Deletes a fact. Does not throw an error if the fact is not found.
        """
        api_fact = to_api_fact(fact)
        self.api.delete_facts(api_fact)

    def bulk_delete(self, facts: List[Fact]):
        """Delete many facts:

        Deletes many facts at once. Does not throw an error when some of the
        facts are not found.
        """
        self.api.post_bulk_delete(to_api_facts(facts))

    def bulk(self, delete: Sequence[VariableFact] = [], tell: Sequence[Fact] = []):
        self.api.post_bulk(
            api.Bulk([to_api_variable_fact(d) for d in delete], to_api_facts(tell))
        )

    def get(self, fact: VariableFact) -> List[OutputFact]:
        """List facts:

        Lists facts that are stored in Oso Cloud. Can be used to check the existence
        of a particular fact, or used to fetch all facts that have a particular
        argument.
        """
        variable_fact = to_api_variable_fact(fact)
        result = self.api.get_facts(variable_fact.predicate, variable_fact.args)
        return from_api_facts(result)

    def policy(self, policy: str):
        """Update the active policy:

        Updates the policy in Oso Cloud. The string passed into this method should be
        written in Polar.
        """
        policyObj: api.Policy = api.Policy("", policy)
        self.api.post_policy(policyObj)

    def query(
        self, query: VariableFact, context_facts: List[Fact] = []
    ) -> List[OutputVariableFact]:
        """Query Oso Cloud for any predicate, and any combination of concrete and
        wildcard arguments.
        """
        result = self.api.post_query(
            api.Query(to_api_variable_fact(query), to_api_facts(context_facts))
        )
        return from_variable_api_facts(result.results)

    def get_policy_metadata(self) -> api.PolicyMetadata:
        """Get metadata about the currently active policy."""
        return self.api.get_policy_metadata()

    # Local Filtering Methods:
    def authorize_local(self, actor, action, resource) -> str:
        """Fetches a query that can be run against your database to determine whether
        an actor can perform an action on a resource."""
        actor_typed_id = to_api_value(actor)
        resource_typed_id = to_api_value(resource)
        data = api.AuthorizeQuery(
            actor_typed_id.type,
            actor_typed_id.id,
            action,
            resource_typed_id.type,
            resource_typed_id.id,
            [],
        )
        result = self.api.post_authorize_query(data)
        return result.sql

    def list_local(self, actor, action, resource_type, column) -> str:
        """Fetches a filter that can be applied to a database query to return just
        the resources on which an actor can perform an action."""
        actor_typed_id = to_api_value(actor)
        data = api.ListQuery(
            actor_typed_id.type,
            actor_typed_id.id,
            action,
            resource_type,
            [],
        )
        result = self.api.post_list_query(data, column)
        return result.sql
