# YAGo

YAGo is some tinkering with Django + AngularJS using the game of <a href="http://en.wikipedia.org/wiki/Go_(game)">Go</a> as a motivator.


## Requirements

See: http://askubuntu.com/a/244642

* Python 2.7
* Pip
* Virtualenv
* Virtualenvwrapper


## Building and Installation

```bash
git clone git@github.com:jamesandres/YAGo.git

mkvirtualenv YAGo

cd YAGo

# Setup the the Django app
pip install -r requirements.txt
./manage.py syncdb

# Install the front end
cd go/frontend
npm install
bower install

# Compile the static assets
grunt build

cd ../..

# Done!
./manage.py runserver
```