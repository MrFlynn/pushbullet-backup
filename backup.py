#!/usr/bin/env python3

# Need requests and configparser.
import requests
import configparser
import time
import glob
import sys
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
            print("Pushes downloaded. Writing to file...")
            break

        push_list.extend(r.json().get("pushes"))

    # Generate filename for backup json file.
    backup_file = "pushbullet-backup-{0}.json".format(time.strftime("%d-%m-%Y"))

    if not glob.glob(backup_file):
        # Create file if it doesn't exist already.
        open(backup_file, "a").close()
    else:
        answer = input("Old backup file will be overwritten. Continue (y/n): ")

        if answer.lower() == 'y':
            # Empty the file if it does exist.
            open(backup_file, "w").close()
        else:
            print("Application terminating...")
            sys.exit()

    # Write contents to file.
    with open(backup_file, "w") as output:
        json.dump(push_list, output)

if __name__ == "__main__":
    main()
