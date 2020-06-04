# Flask minimal example

## Running with PyCharm
Run this project in Pycharm as Flask application. Then send a request with the browser, curl or Postman.

## Running on a remote server

If your virtual environment is already installed and you are just (re)starting the server (Flask application) use the below command:
```
sudo $(pipenv --venv)/bin/flask run --host=0.0.0.0 -p 80
```

Explanation (more explicit approach):
```
sudo /home/$USER/.local/share/virtualenvs/flask_minimal_example-$XYZ-$ABCDE/bin/flask run --host=0.0.0.0 -p 80
```
Where:
  * `$USER` is your username (where virtual environment was created)
  * `$XYZ` and `$ABCDE` are hash codes for the directory of the virtual environment
  
## Installation

First clone this repository to the remote server:
```
git clone https://github.com/mikbuch/flask_minimal_example
cd flask_minimal_example
```

You'll need `pipenv` to run this server in virtual environment.

But first, install pip3:
```
sudo apt-get install python3-pip
```

Then install pipenv:
```
sudo pip3 install pipenv
```

Now install virtual env:
```
pipenv install --python $(which python3)
```

In order to run the server at port 80 (HTTP) you have to use sudo.
```
sudo $(pipenv --venv)/bin/flask run --host=0.0.0.0 -p 80
```

Explanation (more explicit approach):
```
sudo /home/$USER/.local/share/virtualenvs/flask_minimal_example-$XYZ-$ABCDE/bin/flask run --host=0.0.0.0 -p 80
```
Where:
  * `$USER` is your username (where virtual environment was created)
  * `$XYZ` and `$ABCDE` are hash codes for the directory of the virtual environment

## Example request received

An empty request:
```
127.0.0.1 - - [20/Apr/2020 10:12:44] "GET /?some_param=3 HTTP/1.1" 200 -

--------------------
I just got request!
10:12:44
Request:
<Request 'http://127.0.0.1:5000/' [GET]>
Args:
ImmutableMultiDict([])
--------------------
```

With some parameters:
```
127.0.0.1 - - [20/Apr/2020 10:12:44] "GET /?some_param=3 HTTP/1.1" 200 -

--------------------
I just got request!
Request:
10:12:44
<Request 'http://127.0.0.1:5000/?some_param=3' [GET]>
Args:
ImmutableMultiDict([('some_param', '3')])
--------------------
```
