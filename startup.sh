#!/bin/bash
if [ -z $KEY ]
then
	echo
else
	sed -i "s/KEY/$KEY/" /opt/btsync/btsync.conifg
fi

if [ -z $FOLDER ]
then
	echo
else
	sed -i "s/FOLDER/$FOLDER/" /opt/btsync/btsync.conifg
fi

#/opt/btsync/btsync --config /opt/btsync/btsync.conifg --nodaemon
