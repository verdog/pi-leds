#!/bin/bash

echo "--- PUSHING"
rsync -ruv ./ pi:~/Code/pi-leds/ --delete
echo "--- DONE!"