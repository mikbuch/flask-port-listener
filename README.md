# Flask minimal example

Run this with pycharm. Just run and send a request with the browser, curl or Postman.

### Running, environmental variable and port
`FLASK_APP` variable is defined in `.env` file. It will load automatically.

To run flask server on port 80 (default is 5000):
```
sudo pipenv run flask -p 80
```
`sudo` is required to run an application on port 80.

Alternatively:
```
sudo /home/$USER/.local/share/virtualenvs/flask_minimal_example-$XYZ-$ABCDE/bin/flask run --host=0.0.0.0 -p 80
```
Where:
  * `$USER` is your username (where virtual environment was created)
  * `$XYZ` and `$ABCDE` are hash codes for the directory of the virtual environment

## Example request received

Empty request:
```
127.0.0.1 - - [20/Apr/2020 16:38:56] "GET /?some_param=3 HTTP/1.1" 200 -

--------------------
I just got request!
Request:
<Request 'http://127.0.0.1:5000/' [GET]>
Args:
ImmutableMultiDict([])
--------------------
```

Parameters:
```
127.0.0.1 - - [20/Apr/2020 16:38:51] "GET /?some_param=3 HTTP/1.1" 200 -

--------------------
I just got request!
Request:
<Request 'http://127.0.0.1:5000/?some_param=3' [GET]>
Args:
ImmutableMultiDict([('some_param', '3')])
--------------------
```
