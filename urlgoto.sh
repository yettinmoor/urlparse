#!/usr/bin/env sh
setsid urlparse $( dmenu -p $BROWSER ) | xargs -r -I {} $BROWSER "{}" &
