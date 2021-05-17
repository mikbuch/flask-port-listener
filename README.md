# Flask minimal example

## Running on a remote server

### One-line command (new installation)

```bash
git clone https://github.com/mikbuch/flask_minimal_example && \
  cd flask_minimal_example && \
  sudo apt-get install python3-pip && \
  sudo pip3 install pipenv && \
  pipenv install --python $(which python3) && \
  sudo $(pipenv --venv)/bin/flask run --host=0.0.0.0 -p 80
```

After running the appliction on the server, open the browser and type the IP of your server. You should see the output such as:

![image](https://user-images.githubusercontent.com/10733514/118406493-8b0cbd80-b67c-11eb-9a90-7ce6c530bb65.png)

#### Cleanup

In order to remove the application:

```bash
pipenv --rm && \
cd .. && \
rm -rf flask_minimal_example
```

Note: sometimes there can be some `root` files created under venv dir (`/home/$USER/.local/share/virtualenvs/flask_minimal_example-$XYZ-$ABCDE/`). In such cases you have to remove this venv directory manually with `sudo` command.

## Re-running the application

On the server when the application was previously installed you can just run flask application.

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
  
## Installation (step-by-step)

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

## Development

### Running with PyCharm
Run this project in Pycharm as Flask application. Then, to send a request with the browser, use curl or Postman.
