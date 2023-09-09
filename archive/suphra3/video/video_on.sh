#raspistill -w 640 -h 480 -rot 90 -q 5 -o /tmp/stream/pic.jpg -tl 100 -t 9999999 -th 0:0:0 &
#raspivid -t 9999999 -w 960 -h 540 -fps 25 -b 500000 -vf -o - | ffmpeg -i - -vcodec copy -an -f flv -metadata streamName=myStream tcp://0.0.0.0:6666
#sudo raspistill -w 640 -h 480 -q 5 -o mjpg/tmp/stream/pic.jpg -tl 100 -t 9999999 -th 0:0:0 &
#sudo mjpg/mjpg_streamer -i "mjpg/input_file.so -f ../tmp/stream -n pic.jpg" -o "mjpg/output_http.so -w ./www -p 8090"
#!/bin/bash
#cd /mjpg/
#export LD_LIBRARY_PATH=.
#sudo mjpg/mjpg_streamer -o "mjpg/output_http.so -w mjpg/www -p 8093" -i "mjpg/input_file.so -f tmp/stream -n pic.jpg"
sudo mjpg/mjpg_streamer -o "mjpg/output_http.so -w mjpg/www -p 8093" -i "mjpg/input_raspicam.so -rot 180 -x 640 -y 480"
