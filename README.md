# doel
We gaan een website maken met python/flask/mysql
Ter lering ende vermaak

# virtualenv
Het is handig om een python virtual env te gebruiken:
- je pip installs komen in een aparte directory: je systeem wordt niet "vervuild"
- je kunt installen als gewone user, je hoeft geen root te zijn

## virtual env directory aanmaken
$ cd
$ mkdir lugn
$ pip3 install virtualenv
$ virtualenv "directory naam" (bv. venv)
$ source venv/bin/activate
(venv) $ mkdir website_maken
(venv) $ git clone https://github.com/oscarbuse/lugn.git
(venv) $ pip3 install -r requirements.txt

## virtualenv verlaten
(venv) $ deavtivate


