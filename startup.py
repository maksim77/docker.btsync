#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import json
from argparse import RawTextHelpFormatter, ArgumentParser


def folders(key, folder):
    FOLDERS = {}
    FOLDERS['secret'] = key
    FOLDERS['dir'] = "/data/"+folder
    FOLDERS['use_relay_server'] = 'true'
    FOLDERS['use_tracker'] = 'true'
    FOLDERS['use_sync_trash'] = 'true'
    FOLDERS['overwrite_changes'] = 'true'
    return FOLDERS


def FirstRun():
    CONFIG = {}
    CONFIG["device_name"] = "Docker BtSync"
    CONFIG["listening_port"] = 55555
    CONFIG["pid_file"] = "/opt/btsync/btsync.pid"
    CONFIG["use_upnp"] = "True"
    CONFIG["download_limit"] = 0
    CONFIG["upload_limit"] = 0
    shared_folders = []
    if os.environ.get('FOLDER'):
        shared_folders = [folders(os.environ["KEY"],
                                  os.environ["FOLDER"])
                          ]
    else:
        shared_folders = [folders(os.environ["KEY"],
                                  "/data/bt_folder/")
                          ]
    CONFIG["shared_folders"] = shared_folders
    res_str = (json.dumps(CONFIG, indent=5))

    fopen = open('btsync.config', 'w')
    for index in res_str:
        fopen.write(index)
    fopen.close()
    print(json.dumps(CONFIG, indent=5))
    os.remove('FLAG')
    print("Running daemon")
    sys.exit(0)


def CreateParser():
    parser_description = "Управляющий скрипт контейнера BtSync"
    parser = ArgumentParser(usage="startup.py add -k KEY",
                            description=parser_description,
                            formatter_class=RawTextHelpFormatter)

    list_commands = parser.add_argument_group('Список комманд')
    list_options = parser.add_argument_group('Опции')

    list_commands.add_argument('cmd', choices=['add', 'delete'])
    list_options.add_argument('-k', '--key', metavar="", help="Ключ")
    return parser


if os.path.exists('FLAG'):
    if os.environ.get('KEY'):
        FirstRun()
    else:
        print("KEY not found")
        sys.exit(1)

parser = CreateParser()
args = parser.parse_args()

if args.cmd == "add":
    print(args.cmd)
elif args.cmd == "delete":
    if args.key:
        key = args.key
    else:
        key = input("Введите ключ:")

    fopen = open('btsync.config', 'r')
    conf_dict = json.load(fopen)
    for k in conf_dict["shared_folders"]:
        if k["secret"] == key:
            conf_dict["shared_folders"].remove(k)
            break
    print(json.dumps(conf_dict, indent=4))
