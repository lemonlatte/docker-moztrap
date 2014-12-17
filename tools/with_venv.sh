#!/bin/bash

# This file should be placed next to the virtualenv folder
# since the path is hardcode.

BASE=`dirname $0`
VENV=$BASE/.venv
source $VENV/bin/activate && $@
