APP_SERVICE='gunicorn'

if ps ax | grep -v grep | grep $APP_SERVICE > /dev/null
then
    processId=$(ps ax | grep $APP_SERVICE | awk '{split($0,a," "); print a[1]}' | head -n 1)
    echo "HUP: $processId"
    kill -HUP $processId
else
    echo "$APP_SERVICE service is not running, starting now.."
    gunicorn -D --workers=3 --bind=127.0.0.1:5002 --log-file=MicroSemi.log --capture-output --pid=gunicorn.pid --log-level=debug wsgi:app
    echo "Done"
fi
