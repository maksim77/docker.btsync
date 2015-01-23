#!/bin/bash
if [ -f /FIRSTRUN ]
then
	if [ $KEY ]
	then
		sed -i "s/KEY/$KEY/" /opt/btsync/btsync.conifg
		rm /FIRSTRUN
	else
		echo "KEY not set" >&2
		echo "Did you forget to add -e KEY=..." >&2
		exit
	fi

	if [ $FOLDER ]
	then
		sed -i "s/FOLDER/$FOLDER/" /opt/btsync/btsync.conifg
	fi
fi

/opt/btsync/btsync --config /opt/btsync/btsync.conifg --nodaemon
