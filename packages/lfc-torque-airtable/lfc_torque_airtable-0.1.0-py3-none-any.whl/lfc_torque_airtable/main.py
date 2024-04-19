import getopt
import sys
import json
from lfc_torque_airtable import TorqueToAirtable
from torqueclient import Torque, MemoryCache


def main():
    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            "",
            [
                "airtable-api-key=",
                "torque-endpoint=",
                "torque-user=",
                "torque-password=",
                "info",
                "dry-run",
            ],
        )
    except getopt.GetoptError as err:
        sys.stderr.write("ERROR: '%s'\n" % err)
        sys.exit(2)

    airtable_api_key = None
    torque_endpoint = None
    torque_user = None
    torque_password = None
    dry_run = False
    info = False

    for o, a in opts:
        if o == "--airtable-api-key":
            airtable_api_key = a
        elif o == "--torque-endpoint":
            torque_endpoint = a
        elif o == "--torque-user":
            torque_user = a
        elif o == "--torque-password":
            torque_password = a
        elif o == "--info":
            info = True
        elif o == "--dry-run":
            dry_run = True
        else:
            sys.stderr.write("ERROR: unrecognized option '%s'\n" % o)
            sys.exit(2)

    if not airtable_api_key:
        sys.stderr.write("ERROR: need --airtable-api-key\n")
        sys.exit(2)

    if not torque_endpoint:
        sys.stderr.write("ERROR: need --torque-endpoint\n")
        sys.exit(2)

    if not torque_user:
        sys.stderr.write("ERROR: need --torque-user\n")
        sys.exit(2)

    if not torque_password:
        sys.stderr.write("ERROR: need --torque-password\n")
        sys.exit(2)

    pairs = [arg.split("|") for arg in args]

    torque = Torque(torque_endpoint, torque_user, torque_password, cache=MemoryCache())
    converter = TorqueToAirtable(airtable_api_key, torque)
    converter.dry_run = dry_run

    if info:
        for pair in pairs:
            converter.get_information(pair[0], pair[1])
    else:
        for pair in pairs:
            converter.convert_proposal(pair[0], pair[1])

    print(json.dumps({"errors": converter.errors, "results": converter.results}))
