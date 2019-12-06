#!/bin/bash

# check if required command line args were supplied
if [ "$#" -ne 2 ]
then
	echo "script to record IP camera feeds"
	echo "output files are stored ~/Videos/'YYYY-MM-DD_hh-mm-ss.mp4'"
	echo ""
	echo "Usage: camera_record.sh [ipaddr] [duration in seconds]"
	echo "	e.g. camera_record.sh 192.156.1.14 20"
else
	#echo "MY NAME IS $0"
	#echo "addr: $1"
	#echo "duration: $2"
	today=`date +%Y-%m-%d_%H-%M-%S`
	cvlc -vvv rtsp://$1:554/live/video/profile1  --sout=file/ts:~/Videos/$today.mp4 --run-time=$3 vlc://quit
fi
