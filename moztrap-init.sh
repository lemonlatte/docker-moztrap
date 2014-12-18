#!/bin/sh

mysql -h $MYSQL_PORT_3306_TCP_ADDR -uroot -p$MYSQL_ENV_MYSQL_PASS -e "CREATE DATABASE IF NOT EXISTS  moztrap CHARACTER SET utf8"
mysql -h $MYSQL_PORT_3306_TCP_ADDR -uroot -p$MYSQL_ENV_MYSQL_PASS -e "GRANT ALL PRIVILEGES ON moztrap.* TO 'moztrap'@'%' IDENTIFIED BY '000000';"

cd moztrap

./with_venv.sh ./manage.py syncdb --migrate --noinput
./with_venv.sh ./manage.py create_default_roles
./with_venv.sh ./add_user.py admin admin@localhost.local 000000
