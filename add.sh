#!/bin/bash
head -n 9 /opt/btsync/btsync.conifg > /tmp/config
jq '.shared_folders + [{"secret":"KEY","dir":"/data/FOLDER","use_relay_server":true,"use_tracker":true,"use_sync_trash":true,"overwrite_changes":false}]' /opt/btsync/btsync.conifg >> /tmp/config
echo "}" >> /tmp/config

sed -i "s/KEY/$1/" /tmp/config
sed -i "s/FOLDER/$2/" /tmp/config

rm -f /opt/btsync/btsync.conifg
mv /tmp/config /opt/btsync/btsync.conifg
