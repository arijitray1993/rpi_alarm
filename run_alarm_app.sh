PYTHON=python3 uwsgi --enable-threads --socket 0.0.0.0:5000 --protocol=http -w smart_alarm_rpi:app
