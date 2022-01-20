from flask import Flask
import socket
import json

app = Flask(__name__)

#Accessing mock data
with open('/app/src/books.json', 'r') as bookFile:
    jsonObject = json.load(bookFile)
    bookFile.close()

@app.route("/")
def index():
    books_string = json.dumps(jsonObject)
    return f"<p>{books_string}</p>"


# Access title of book by rank
@app.route("/books/title/<int:number>")
def book_by_index(number):

    if number < 1 or number > 5:
        return "Sorry only numbers 1-5 are available"
    res = jsonObject[number-1]["title"]
    return f"<p>Book at rank {number} is {res}</p>"

if __name__ == '__main__':
    app.config['SERVER_NAME'] = 'bookscraper.xyz'
    app.run(debug=True, host='0.0.0.0')
