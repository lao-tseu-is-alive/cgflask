#!/bin/bash
su -c "createdb cgflask" postgres
su -c "psql -d cgflask -f create_user.sql" postgres
