#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import json
from argparse import RawTextHelpFormatter, ArgumentParser


def folders(key, folder):
    FOLDERS = {}
    FOLDERS['secret'] = key
    FOLDERS['dir'] = folder
    FOLDERS['dir'] = '/data/bt_folder/'
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
        os.remove('FLAG')
    else:
        print("KEY not found")
        sys.exit(1)

parser = CreateParser()
args = parser.parse_args()

if args.cmd == "add":
    if args.key:
        key = args.key
    else:
        key = input("Введите ключ:")
    print(key)
elif args.cmd == "delete":
    print(args.cmd)
