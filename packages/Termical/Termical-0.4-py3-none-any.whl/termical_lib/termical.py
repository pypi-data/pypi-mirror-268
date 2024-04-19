#!/usr/bin/env python3

from googleapiclient.discovery import build
import os.path
import argparse
import json
from termical_lib import termicalFunctions as tl
from termical_lib import authentication as tlAu

def main():
    CREDS = tlAu.auth()
    service = build("calendar", "v3", credentials=CREDS)
    
    parser = argparse.ArgumentParser(description="Simple terminal-based calendar")
    parser.add_argument("-s", "--settings", help="Edit settings", action="store_true")
    parser.add_argument("-c", "--create", help="Creates new event", action="store_true")
    parser.add_argument("--account_remove", help="Removes google account", action="store_true" )
    parser.add_argument("-l", "--list", help="List number of upcoming events in primary calendar", action="store_true")
    parser.add_argument("-d", "--delete", help="Delete upcoming event", action="store_true")
    args = parser.parse_args()
    
    settings = tl.usr_settings(service) #TODO: do i even want to have a dictionary here?
    if args.settings:
        tl.usr_settings_edit(settings, service)
    elif args.create:
        tl.event_create(settings, service)
    elif args.account_remove:
        tl.account_remove(settings)
    elif args.list:
        tl.event_list(settings, service, 5)
    elif args.delete:
        tl.event_delete(settings, service)
    else:
        tl.event_list_print(tl.event_list(settings, service, 10))

if __name__ == "__main__":
    main()