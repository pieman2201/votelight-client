#!/bin/bash

# ss 66131

raspivid -o - -t 0 \
    -vf -hf \
    -ISO 100 -ex off -awb off -awbg 1.0,2.0 -ss 66131 \
    -w 480 -h 480 -b 1000000 | ffmpeg -re -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -f h264 -i - -vcodec copy -acodec aac -ab 128k -g 50 -strict experimental -tune zerolatency -f flv rtmp://18.222.108.51:1935/app/stream
