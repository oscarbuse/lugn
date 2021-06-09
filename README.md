[doel](https://github.com/oscarbuse/lugn#doel)

[virtualenv](https://github.com/oscarbuse/lugn#virtualenv)
[runnen van de code](https://github.com/oscarbuse/lugn#runnen-van-de-code)

# doel
We gaan een website maken met python/flask/mysql.
Ter lering ende vermaak

# virtualenv
Het is handig om een python virtual env te gebruiken:
- je pip installs komen in een aparte directory: je systeem wordt niet "vervuild"
- je kunt installen als gewone user, je hoeft geen root te zijn

## virtual env directory aanmaken
```
$ cd
$ mkdir lugn
$ pip3 install virtualenv
$ virtualenv "directory naam" (bv. venv)
$ source venv/bin/activate
(venv) $ mkdir website_maken
(venv) $ git clone https://github.com/oscarbuse/lugn.git
(venv) $ pip3 install -r requirements.txt
```
## virtualenv verlaten
```
(venv) $ deavtivate
```

# runnen van de code
Je moet de variabele FLASK_APP setten naar het file wat je wilt runnen, bv.:
```
(venv) $ export FLASK_APP=hello.py
```
(later kiezen we een vaste naam: run.py)

Voor development is wat meer debug output wel handig, doe daarvoor:
```
(venv) $ export FLASK_ENV=development
```
Dan je code runnen met:
```
(venv) $ flask run
 * Serving Flask app 'hello.py' (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 652-128-401
```
En dan je resultaat bekijken via de link (http://127.0.0.1:5000/)
Die "Debugger PIN" is een extra security maatregel wat voorkomt dat men debug output ziet als je per ongeluk debug aan hebt staan en op een live systeem werkt.

Met `--host=` en `--port=` kun je een ander IP-adres en port toewijzen mocht dat nodig zijn, bv.:
```
(venv) $ flask run --host=0.0.0.0 --port=5001
```

