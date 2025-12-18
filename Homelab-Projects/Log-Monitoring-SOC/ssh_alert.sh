#!/bin/bash

THRESHOLD=3

journalctl -u ssh --no-pager | grep "Failed password" | \
awk '{print $(NF-3)}' | sort | uniq -c | while read count ip
do
    if [ "$count" -ge "$THRESHOLD" ]; then
        echo "🚨 ALERT: Brute-force suspected from $ip ($count attempts)"
    fi
done
