#!/bin/bash

# Get total RAM in gigabytes and round it to the nearest integer

echo "Welcome to Alchemist ! Lets check your PC specs, we are looking at your RAM to ensure that it will support the program"
total_ram=$(awk '/MemTotal/ {print int($2/1024/1024 + 0.5)}' /proc/meminfo)

echo "total RAM detected: $total_ram GB"

# Check if total RAM is less than 16GB
if [ $total_ram -lt 16 ]; then
    echo "I don't recommend you use llama 2 chat because of your RAM"
else
    echo "You are free to choose from whatever model but tinyllama will take time generating (a lot)"
fi
