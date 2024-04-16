from typing import Sequence, Optional, Union, TypedDict


VariableValueDict = TypedDict(
    "VariableValueDict", {"type": str, "id": str}, total=False
)


# This lets values be a subtype of variable values
class ValueDict(VariableValueDict, total=True):
    pass


Value = Union[str, ValueDict]
"""
APIs expecting concrete values accept either a string or a dict with type and ID fields.

### Example

```python
user: Value = {"type": "User", "id": "1"}
role: Value = "admin
```
"""


VariableValue = Union[None, str, VariableValueDict]
"""
Variable values allow for wildcards -- expressed by ommitting ID and/or type arguments

### Example

```python
any_user: VariableValue = {"type": "User"}
anything: VariableValue = None
anything: VariableValue = {}
```
"""

Fact = TypedDict("Fact", {"name": str, "args": Sequence[Value]})
"""
Facts are the core data model of Oso Cloud: https://www.osohq.com/docs/concepts/oso-cloud-data-model

### Example

```python

user = {"type": "User", "id": "1"}
role = "admin"
org = {"type": "Organization", "id": "2"}

user_admin: Fact = {"name": "has_role", "args": [user, role, org]}
```
"""


OutputFact = TypedDict("OutputFact", {"name": str, "args": Sequence[ValueDict]})
"""
Facts returned from the `oso.get` API.
"""

OutputVariableValueDict = TypedDict(
    "OutputVariableValueDict", {"type": str, "id": str}, total=False
)
OutputVariableValue = Optional[OutputVariableValueDict]
OutputVariableFact = TypedDict(
    "OutputVariableFact", {"name": str, "args": Sequence[OutputVariableValue]}
)
"""
Facts returned from the `oso.query` API can include wildcard values represented by `None` or
having `arg["id"] = None`.
"""

VariableFactDict = TypedDict(
    "VariableFactDict", {"name": str, "args": Sequence[VariableValue]}
)

VariableFact = Union[OutputFact, VariableFactDict, Fact]
"""
Variable facts allow for wildcards -- expressed by omitting ID and/or type arguments

### Example

```python

user = {"type": "User", "id": "1"}
roles = {"type": "String"}
orgs = {"type": "Organization"}

user_org_roles: VariableFact = {"name": "has_role", "args": [user, role, org]}
```
"""
