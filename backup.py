#!/usr/bin/env python3

# Need requests and configparser.
import requests
import configparser
import time
import json


def main():
    # List of pushes:
    push_list = []

    # Import configuration with API token.
    c = configparser.ConfigParser()

    # Read config file and set token var.
    c.read("config.ini")
    token = c["MAIN"]["token"]

    # Setup headers for requests.
    headers = {"Access-Token": token}

    # Setup initial payload for requests.
    payload = {"active": "true"}

    # Initial request:
    r = requests.get("https://api.pushbullet.com/v2/pushes",
                     headers=headers,
                     params=payload)

    # Get cursor for next page:
    cursor = r.json().get("cursor")

    # Add initial pushes to push_list
    push_list.extend(r.json().get("pushes"))

    while True:
        payload.update({"cursor": cursor})

        r = requests.get("https://api.pushbullet.com/v2/pushes",
                         headers=headers,
                         params=payload)

        if isinstance(r.json().get("cursor"), str):
            cursor = r.json().get("cursor")
        else:
            break

        push_list.extend(r.json().get("pushes"))

    # Generate filename for backup json file.
    backup_file = "pushbullet-backup-{0}.json".format(time.strftime("%d/%m/%Y"))

    with open(backup_file, "w") as output:
        json.dump(push_list, output)

if __name__ == "__main__":
    main()
