![Joe Sandbox API v2](https://raw.githubusercontent.com/joesecurity/jbxapi/master/img/logo.png)

# API Wrapper

The Joe Sandbox API Wrapper enables you to fully integrate Joe Sandbox into your malware analysis framework. Joe Sandbox is a deep malware analysis platform for analyzing malicious files.

You can use this wrapper with

 * [Joe Sandbox Cloud](https://www.joesecurity.org/joe-sandbox-cloud) — our Cloud hosted instance
 * [On-premise installations of Joe Sandbox](https://www.joesecurity.org/joe-security-products#on-premise) — for even more power and privacy

It is at the same time a powerful implementation of the Joe Sandbox API and also a command line tool for interacting with Joe Sandbox.

# License

The code is written in Python and licensed under MIT.

# Requirements

* Python 2.7 or higher
* Python 3.5 or higher

# Installation

## With Pip

    pip install jbxapi

For upgrading `jbxapi` to a more recent version, use

    pip install --upgrade jbxapi

## Manually

1. Install the python library [`requests`](https://requests.readthedocs.io/en/latest/).

        pip install requests

2. Copy `jbxapi.py` to where you need it.

# Documentation

* [Command Line Interface](docs/cli.md)
* [Python API](docs/api.md)

# Credits

* Thanks to [Pedram Amini](https://github.com/pedramamini) for a first wrapper implementation!

# Links

* [Joe Securiy LLC](https://www.joesecurity.org)
* [Joe Security Blog](https://blog.joesecurity.org)
* [Twitter @joe4security](https://twitter.com/joe4security)

