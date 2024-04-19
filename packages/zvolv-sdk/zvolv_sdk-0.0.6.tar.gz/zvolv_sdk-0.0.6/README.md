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

### Usage
The Zvolv Hyper automation platform offers several APIs to build apps. Each Zvolv API delivers part of the capabilities from the platform, so that you can pick just those that fit for your needs. This SDK offers a corresponding package for each of Zvolv’s APIs.

#### Sending an email from Zvolv

One of the most simple use-cases is sending an email from Zvolv. In our examples, we specify the channel name, however it is recommended to use the `channel_id` where possible. Also, if your app's bot user is not in a channel yet, invite the bot user before running the code snippet (or add `chat:write.public` to Bot Token Scopes for posting in any public channels).

```python
import os
from zvolv_sdk import WebClient
from zvolv_sdk.errors import ZvolvApiError

client = WebClient(token=os.environ['ZVOLV_BOT_TOKEN'])

try:
    response = client.chat_postMessage(channel='#random', text="Hello world!")
    assert response["message"]["text"] == "Hello world!"
except SlackApiError as e:
    # You will get a ZvolvApiError if "ok" is False
    assert e.response["ok"] is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    print(f"Got an error: {e.response['error']}")
```

Here we also ensure that the response back from Zvolv is a successful one and that the message is the one we sent by using the `assert` statement.

### API References

- Database ( `authentication.Database` )
- Delegated ( `authentication.Delegated` )
- Enterprise ( `authentication.Enterprise` )
- API Authorization - Get Token ( `authentication.GetToken`)
- Passwordless ( `authentication.Passwordless` )
- RevokeToken ( `authentication.RevokeToken` )
- Social ( `authentication.Social` )
- Users ( `authentication.Users` )



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
