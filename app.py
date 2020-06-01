from flask import Flask, request, render_template
import sys
app = Flask(__name__)

requests = []

@app.route('/')
def hello_world():

    # Get the content of the request
    template = '\n--------------------'
    template += '\nI just got a request!'
    template += '\nRequest:\n%s' % request
    template += '\nArgs:\n%s' % request.args
    template += '\n--------------------\n'

    requests.append(template)

    # Print to terminal
    print(template, file=sys.stderr)

    # Show in the browser
    return render_template('index.html', requests=requests)
