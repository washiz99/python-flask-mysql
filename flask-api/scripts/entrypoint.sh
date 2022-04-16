#!/usr/bin/env bash
set -euxo pipefail

cd `dirname $0` && cd ..

uwsgi --ini uwsgi.ini