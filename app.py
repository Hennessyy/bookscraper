from flask import Flask
import socket

app = Flask(__name__)

#Current issue: 
#Routes breaking because of subdomains since transition to gunicorn
#If we remove the subdomain parameter the routes work correctly.

@app.route("/test", subdomain="www")
def test():
    return f"<p> TEST {socket.gethostname()}</p>"

@app.route("/", subdomain="www")
def welcome_page():
    return "<p>Home page</p>"

@app.route("/", subdomain="api")
def api_page():
    return "<p>API subdomain</p>"

if __name__ == '__main__':
    app.config['SERVER_NAME'] = 'bookscraper.xyz'
    app.run(debug=True, host='0.0.0.0')
