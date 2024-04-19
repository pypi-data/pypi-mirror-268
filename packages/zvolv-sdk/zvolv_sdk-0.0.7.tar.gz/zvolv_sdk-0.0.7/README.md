# ZvolvClient SDK

<div>
📚 <a href="#documentation">Documentation</a> - 🚀 <a href="#getting-started">Getting started</a> - 💻 <a href="#api-reference">API reference</a> - 💬 <a href="#feedback">Feedback</a>
</div>


Learn how to automate with Zvolv using Python.
## Documentation
- [Docs site](https://python-zvolv-sdk.readthedocs.io/) - explore our docs site and learn more about Zvolv.
- [User Guide](https://github.com/zvolvapi/python-zvolv-sdk/blob/main/UserGuide.md) - explore our user guide docs and learn more about sdk.

## Getting started
### Installation
You can install the Zvolv Python SDK using the following command.
```
pip install zvolv-sdk
```

> Requires Python 3.0 or higher.

# Usage
## Initialize ZvolvClient

constructor(base_url: string)

Initializes the ZvolvClient with the base url of the Zvolv server.

Once the package is installed, you can import the library using import or require approach:

```bash
from zvolv_sdk import ZvolvClient

client = ZvolvClient('http://twig-me.com')

```

## Initialize Workspace

methods for interacting with workspaces.

```bash

try:
    workspace = client.workspace.init('kapilwf');
except Error:
    print(Error)

```
## Perform Authentication

methods for authentication.

```bash
try:
    login = client.auth.login('email', 'pass');
except Error:
    print(Error)
```


### Feedback

---

If you get stuck, we’re here to help. The following are the best ways to get assistance working through your issue:

Use our [Github Issue Tracker][gh-issues] for reporting bugs or requesting features.
Visit the [Zvolv Community][zvolv-community] for getting help using Slack Developer Kit for Python or just generally bond with your fellow Zvolv developers.

<!-- Markdown links -->


[pypi-url]: https://pypi.org/project/slack-sdk/
[python-version]: https://img.shields.io/pypi/pyversions/slack-sdk.svg
[build-image]: https://github.com/slackapi/python-slack-sdk/workflows/CI%20Build/badge.svg
[build-url]: https://github.com/slackapi/python-slack-sdk/actions?query=workflow%3A%22CI+Build%22
[codecov-image]: https://codecov.io/gh/slackapi/python-slack-sdk/branch/main/graph/badge.svg
[codecov-url]: https://codecov.io/gh/slackapi/python-slack-sdk
[contact-image]: https://img.shields.io/badge/contact-support-green.svg
[contact-url]: https://slack.com/support
[slackclientv1]: https://github.com/slackapi/python-slackclient/tree/v1
[api-methods]: https://api.slack.com/methods
[rtm-docs]: https://api.slack.com/rtm
[events-docs]: https://api.slack.com/events-api
[bolt-python]: https://github.com/slackapi/bolt-python
[pypi]: https://pypi.org/
[gh-issues]: https://github.com/zvolvapi/python-zvolv-sdk/issues
[zvolv-community]: https://zvolv.com/
[urllib]: https://docs.python.org/3/library/urllib.request.html
