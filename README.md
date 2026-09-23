<img width="1778" height="404" alt="numperms" src="https://github.com/user-attachments/assets/cede1ee8-73f9-450c-8732-e0c1d7be1558" />


# NumPerms
A permission library using number or 2 digits of letters to indicate permission nodes, groups and users. Designed for TI Nspire CX II.

# How to install?
1. Download tns file from release tab, use https://nspireconnect.ti.com/nsc/ webapp to copy it in your calculator.

2. If you have PyLib folder, put the tns in it. If you don't have it, create one and put the tns there.

3. Refreash lib. Press 2>menu>B to refreash lib.

4. You are all setup! Just import it in your project.


# API Reference

## `version()`
Returns the current NumPerm version.

```python
import nperm
print(nperm.version())
```

Example result: `(1, 1, 0)`

## Group API

A `Group` contains users and permission nodes and has its own weight.

### `Group.exist(name)`
Checks whether a group exists. Returns `True` or `False`.

```python
from nperm import Group

if Group.exist("ad"):
    print("Group exists.")
```

### `Group.Create(name, weight)`
Creates a group. The name is limited to 2 characters and the weight must be greater than `0`. Returns `0` on success and `-1` on failure.

```python
Group.Create("ad", 100)
```

### `Group.SetWeight(name, weight)`
Changes a group's weight. Returns `0` on success and `-1` on failure.

```python
Group.SetWeight("ad", 200)
```

### `Group.Remove(name)`
Removes a group. Returns `0` on success and `-1` if the group does not exist.

```python
Group.Remove("ad")
```

### `Group.Compare(name1, name2)`
Compares two group weights. Returns `1` if the first is greater, `2` if the second is greater, `3` if equal, and `-1` if comparison fails.

```python
result = Group.Compare("ad", "md")
```

## Node API

A `Node` is a permission node belonging to a group. Each node has its own weight.

### `Node.exist(name, group)`
Checks whether a node exists under a group. Returns `True` or `False`.

```python
Node.exist("rd", "ad")
```

### `Node.Create(name, fatherGroup, weight)`
Creates a node under a group. The name is limited to 2 characters and the weight must be greater than `0`. Returns `0` on success and `-1` on failure.

```python
Node.Create("rd", "ad", 10)
Node.Create("wr", "ad", 20)
```

### `Node.Compare(name1, fatherGroup1, name2, fatherGroup2)`
Compares two node weights. Returns `1` if the first is greater, `2` if the second is greater, `3` if equal, and `-1` if comparison fails.

```python
result = Node.Compare("rd", "ad", "wr", "ad")
```

### `Node.GetWeight(name, fatherGroup)`
Returns the node's weight, or `-1` if the node does not exist.

```python
weight = Node.GetWeight("rd", "ad")
print(weight)
```

### `Node.SetWeight(name, fatherGroup, weight)`
Changes a node's weight. Returns `0` on success and `-1` on failure.

```python
Node.SetWeight("rd", "ad", 30)
```

### `Node.Remove(name, fatherGroup)`
Removes a node. Returns `0` on success and `-1` if it does not exist.

```python
Node.Remove("rd", "ad")
```

## User API

A `User` belongs to a group, has its own weight, and can be assigned permission nodes.

### `User.exist(name, group)`
Checks whether a user exists under a group. Returns `True` or `False`.

```python
User.exist("ax", "ad")
```

### `User.Create(name, fatherGroup, weight)`
Creates a user under a group. The name is limited to 2 characters and the weight must be greater than `0`. Returns `0` on success and `-1` on failure.

```python
User.Create("ax", "ad", 50)
```

### `User.SetWeight(name, fatherGroup, weight)`
Changes a user's weight. Returns `0` on success and `-1` on failure.

```python
User.SetWeight("ax", "ad", 80)
```

### `User.CompareUser(user1, fatherGroup1, user2, fatherGroup2)`
Compares two user weights. Returns `1` if the first is greater, `2` if the second is greater, `3` if equal, and `-1` if comparison fails.

```python
result = User.CompareUser("ax", "ad", "bo", "ad")
```

### `User.AllocateNode(user, fatherGroup, node)`
Allocates a node to a user. Returns `0` on success and `-1` on failure.

```python
User.AllocateNode("ax", "ad", "rd")
```

### `User.RemoveNode(name, fatherGroup, node)`
Removes an allocated node from a user. Returns `0` on success and `-1` on failure.

```python
User.RemoveNode("ax", "ad", "rd")
```

### `User.CheckNode(...)`
Currently commented out/discarded in the source and is not an active API.

### `User.CompareNode(...)`
Currently retained as a non-stable/reserved function in the source. It should not be treated as part of the stable API yet.

## Complete Example

```python
from nperm import Group, Node, User

# Create a group
Group.Create("ad", 100)

# Create permission nodes
Node.Create("rd", "ad", 10)
Node.Create("wr", "ad", 20)

# Create a user
User.Create("ax", "ad", 50)

# Allocate nodes to the user
User.AllocateNode("ax", "ad", "rd")
User.AllocateNode("ax", "ad", "wr")

# Get a node's weight
print(Node.GetWeight("rd", "ad"))

# Compare nodes
print(Node.Compare("rd", "ad", "wr", "ad"))

# Change weights
Node.SetWeight("rd", "ad", 30)
User.SetWeight("ax", "ad", 80)

# Compare users
print(User.CompareUser("ax", "ad", "ax", "ad"))

# Remove permissions first
User.RemoveNode("ax", "ad", "rd")
User.RemoveNode("ax", "ad", "wr")

# Remove the user
User.Remove("ax", "ad")

# Remove nodes
Node.Remove("rd", "ad")
Node.Remove("wr", "ad")

# Remove the group
Group.Remove("ad")
```

## Return Values

| Return value | Meaning |
| --- | --- |
| `0` | Operation succeeded |
| `-1` | Operation failed |

Comparison APIs use `1` for the first object having greater weight, `2` for the second, and `3` for equal weights. Existence checks return `True` or `False`.

## Naming and Weight Rules

- Group names: maximum 2 characters.
- Node names: maximum 2 characters.
- User names: maximum 2 characters.
- Weights must be greater than `0`.


# Warnings

The Allocated node from a user will remain their nodes after being removed. You should remove the nodes under a user first before you remove the Node, User and Group.
