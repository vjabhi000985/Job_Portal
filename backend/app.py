from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/')
def home():
  return f"<h1>Hello, world!</h1>"

if __name__ == '__main__':
  app.run(debug=True)