#!/bin/bash
for bal in ballon{14,21,39,60}; do ssh $bal 'sudo shutdown -h +1' ; done

