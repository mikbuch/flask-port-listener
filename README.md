# Flask minimal example

A simple tool for testing requests and ports locally, as well as on a remote server.

## Running on a remote server

There are two cases of running _flask minimal example_ covered here:
 1. Using docker-compose (via `Dockerfile`)
 2. Running it directly with `bash` command line on a given server (directly on the server's system)

### Running with docker-compose

Make sure that you have `docker` and `docker-compose` installed on your server.

Modify the contents of the `docker-compose.yml` file for defining the port you would like to use. __Note!__ For using port `80` you need `sudo` rights -- this option was not tested yet with `docker-compose` case.

```yaml
    ports:
      - '8080:5000'
```

where:

 * `8080` - is the port on which your application will be accessible outside of the `docker` container
 * `5000` - is the port that is used by the `Flask` application inside the `docker` container

Use the following commands to run the dockerized `Flask` application:

```bash
docker-compose up
```

### Running directly on the system

With this approach running the application on port `80` has already been tested.

#### One-line command (installing & running for the first time)

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
