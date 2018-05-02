#!/bin/sh
grep 'rawdog' /etc/crontab || echo "0 */8 * * * cd $(pwd) && git pull origin gh-pages && rm $(pwd)/state* && /usr/local/bin/rawdog -d $(pwd)/ -uw && ./upload.sh" >> /etc/crontab
