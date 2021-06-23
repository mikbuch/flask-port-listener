from datetime import datetime
from flask import Flask, request, render_template
import sys

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def handle_request():
    # Time when the server got the request
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    # Get the content of the request
    request_info = '\n--------------------'
    request_info += '\nI just got a request!'
    request_info += '\n%s' % current_time
    request_info += '\nRequest:\n%s' % request
    request_info += '\nArgs:\n%s' % request.args
    request_info += '\nBody:\n%s' % request.data
    request_info += '\n--------------------\n'

    # Print to terminal
    print(request_info, file=sys.stderr)

    # Show in the browser
    return render_template("index.html", request_info=request_info.split('\n'))
