Scratch API wrapper with support for almost all site features. Created by [TimMcCool](https://scratch.mit.edu/users/TimMcCool/).

This library can set cloud variables, follow Scratchers, post comments and do so much more! It has special features that make it easy to transmit data through cloud variables.

<p align="left">
  <img width="160" height="133" src="https://github.com/TimMcCool/scratchattach/blob/main/logos/logo_dark_transparent_eyes.svg">
</p>

[![PyPI status](https://img.shields.io/pypi/status/scratchattach.svg)](https://pypi.python.org/pypi/scratchattach/)
[![PyPI download month](https://img.shields.io/pypi/dm/scratchattach.svg)](https://pypi.python.org/pypi/scratchattach/)
[![PyPI version shields.io](https://img.shields.io/pypi/v/scratchattach.svg)](https://pypi.python.org/pypi/scratchattach/)
[![GitHub license](https://badgen.net/github/license/TimMcCool/scratchattach)](https://github.com/TimMcCool/scratchattach/blob/master/LICENSE)
[![Documentation Status](https://readthedocs.org/projects/scratchattach/badge/?version=latest)](https://scratchattach.readthedocs.io/en/latest/?badge=latest)

# Links

- **[Documentation](https://github.com/TimMcCool/scratchattach/wiki)**
- [Extended documentation (WIP)](https://scratchattach.readthedocs.io/en/latest/)
- [Examples](https://github.com/TimMcCool/scratchattach/wiki/Examples)
- [Change log](https://github.com/TimMcCool/scratchattach/blob/main/CHANGELOG.md)

# Contributors

- Allmost all code by TimMcCool.
- See the GitHub repository for full list of contributors.
- Create a pull request to contribute code yourself.

# Support

If you need help with your code, leave a comment in the [official forum topic](https://scratch.mit.edu/discuss/topic/603418/
) on [TimMcCool's Scratch
profile](https://scratch.mit.edu/users/TimMcCool/) or open an issue on the github repo

# Installation

Run the following command in your command prompt
/ shell:
```
pip install -U scratchattach
```

**OR**

Add this to your Python code:
```python
import os

os.system("pip install -U scratchattach")
```

# Logging in  `scratch3.Session`

**Logging in with username / password:**

```python
import scratchattach as scratch3

session = scratch3.login("username", "password")
```

`login()` returns a `Session` object that saves your login

**Logging in with a sessionId:**
*You can get your session id from your browser's cookies. [More information](https://github.com/TimMcCool/scratchattach/wiki/Get-your-session-id)*

```python
import scratchattach as scratch3

session = scratch3.Session("sessionId", username="username") #The username field is case sensitive
```

**All scratchattach features are documented in the [documentation](https://github.com/TimMcCool/scratchattach/wiki#logging-in).**

# Cloud variables  `scratch3.CloudConnection`

**Connect to the Scratch cloud:**

```python
conn = session.connect_cloud("project_id")
```

**Get / Set a cloud var:**

```python
value = scratch3.get_var("project_id", "variable")
conn.set_var("variable", "value") #the variable name is specified without the cloud emoji
```

**All scratchattach features are documented in the [documentation](https://github.com/TimMcCool/scratchattach/wiki/#cloud-variables).**
