from . import api
from . import types
from typing import List, Optional, Any, Sequence


def convert_to_str(s: Any) -> str:
    if not isinstance(s, str):
        return str(s)
    return s


def to_api_variable_value(instance: types.VariableValue) -> api.VariableValue:
    if instance is None:
        return api.VariableValue(None, None)
    if isinstance(instance, str):
        if instance == "":
            raise TypeError(
                "Oso: Instance cannot be an empty string. "
                + "For wildcards, use the empty dict ({}) or None."
            )
        return api.VariableValue("String", instance)
    if "id" not in instance or instance["id"] is None:
        if "type" not in instance or instance["type"] is None:
            return api.VariableValue(None, None)
        return api.VariableValue(instance["type"], None)

    if "type" not in instance or instance["type"] is None:
        raise TypeError(f"Oso: Instances with an ID must also have a type: {instance}")
    return api.VariableValue(instance["type"], convert_to_str(instance["id"]))


def to_api_value(instance: types.Value) -> api.ConcreteValue:
    if instance is None:
        raise TypeError("Oso: Expected a concrete value with type and ID. Got None.")
    if isinstance(instance, str):
        if instance == "":
            raise TypeError("Oso: Value cannot be an empty string. ")
        return api.ConcreteValue("String", instance)
    if "id" not in instance or instance["id"] is None:
        raise TypeError("Oso: Expected a concrete value, but ID was None")

    if "type" not in instance or instance["type"] is None:
        raise TypeError("Oso: Expected a concrete value, but type was None")
    return api.ConcreteValue(instance["type"], convert_to_str(instance["id"]))


def to_api_variable_fact(fact: types.VariableFact) -> api.VariableFact:
    return api.VariableFact(
        fact["name"], [to_api_variable_value(a) for a in fact["args"]]
    )


def to_api_fact(fact: types.Fact) -> api.ConcreteFact:
    return api.ConcreteFact(fact["name"], [to_api_value(a) for a in fact["args"]])


def from_api_concrete_value(value: api.ConcreteValue) -> types.ValueDict:
    return {"id": value.id, "type": value.type}


def from_api_variable_value(value: api.VariableValue) -> types.OutputVariableValue:
    if value.type is None:
        return None
    elif value.id is None:
        return {"type": value.type}
    else:
        return {"id": value.id, "type": value.type}


def to_api_facts(params: Optional[Sequence[types.Fact]]) -> List[api.ConcreteFact]:
    if not params:
        return []
    return [to_api_fact(param) for param in params]


def from_api_fact(fact: api.ConcreteFact) -> types.OutputFact:
    if isinstance(fact, api.ConcreteFact):
        return {
            "name": fact.predicate,
            "args": [from_api_concrete_value(a) for a in fact.args],
        }
    assert False


def from_api_facts(
    facts: Optional[Sequence[api.ConcreteFact]],
) -> List[types.OutputFact]:
    if not facts:
        return []
    return [from_api_fact(fact) for fact in facts]


def from_variable_api_fact(fact: api.VariableFact) -> types.OutputVariableFact:
    if isinstance(fact, api.VariableFact):
        return {
            "name": fact.predicate,
            "args": [from_api_variable_value(a) for a in fact.args],
        }
    assert False


def from_variable_api_facts(
    facts: Optional[List[api.VariableFact]],
) -> List[types.OutputVariableFact]:
    if not facts:
        return []
    return [from_variable_api_fact(fact) for fact in facts]
