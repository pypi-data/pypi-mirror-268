# lfc-torque-airtable python package

This is a standalone application that should be installed via:

```
$ pip install lfc-torque-airtable
```

## Usage from commandline

```
$ lfc-torque-airtable \
        --airtable-api-key <airtable_api_key> \
        --torque-endpoint <torque-endpoint> \
        --torque-user <torque-user> \
        --torque-password <torque-password \
        --dry-run \
        <competition_name> <application_number>
```

The options are:
* `airtable-api-key` - can be found opass at clients/lever-for-change/airtable
* `torque-endpoint` - usually https://torque.leverforchange.org/GlobalView
* `torque-user` - your username, or in the case of the extension, usually csv2wiki
* `torque-password` - the api key you use for torque
* `dry-run` - include when you want information about the push, rather than actuallypushing it
* `competition_name` - the competition shortname in torque
* `application_number` - the application number in torque

## Usage from inside python

```

from lfc_torque_airtable import torque_to_airtable
from torqueclient import Torque

torque = Torque(torque_endpoint, torque_user, torque_password)
converter = TorqueToAirtable(airtable_api_key, torque)
converter.dry_run = dry_run

converter.convert_proposal(competition, application_no)
```

Where the variables are the same as the options above
