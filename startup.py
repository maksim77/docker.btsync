#!/usr/local/bin/python3
import os
import json
import argparse
desc = "Управляющий скрипт контейнера BtSync"

parser = argparse.ArgumentParser(description=desc,
                                 usage="startup.py add -k KEY",
                                 formatter_class=argparse.RawTextHelpFormatter)

list_commands = parser.add_argument_group('Список комманд')
list_options = parser.add_argument_group('Опции')

list_commands.add_argument('cmd', choices=['add', 'delete'],
                           metavar=" \nADD\tADD\nDEL\tDELETE")
list_options.add_argument('-k', '--key', metavar="", help="Ключ")
args = parser.parse_args()

if os.path.exists('FLAG'):
    if os.environ.get('KEY'):
        CONFIG = {}
        CONFIG["device_name"] = "Docker BtSync"
        CONFIG["listening_port"] = 55555
        CONFIG["pid_file"] = "/opt/btsync/btsync.pid"
        CONFIG["use_upnp"] = "True"
        CONFIG["download_limit"] = 0
        CONFIG["upload_limit"] = 0

        FOLDERS = {}
        FOLDERS['secret'] = os.environ["KEY"]
        if os.environ.get('FOLDER'):
            FOLDERS['dir'] = '/data/'+os.environ["FOLDER"]
        else:
            FOLDERS['dir'] = '/data/bt_folder/'
        FOLDERS['use_relay_server'] = 'true'
        FOLDERS['use_tracker'] = 'true'
        FOLDERS['use_sync_trash'] = 'true'
        FOLDERS['overwrite_changes'] = 'true'

        shared_folders = []
        shared_folders = [FOLDERS]

        CONFIG["shared_folders"] = shared_folders

        res_str = (json.dumps(CONFIG, indent=5))

        fopen = open('btsync.config', 'w')
        for index in res_str:
            fopen.write(index)
        fopen.close()
        print(json.dumps(CONFIG, indent=5))
    else:
        print("KEY not found")
else:
    print(args.cmd)
    print(args.key)
