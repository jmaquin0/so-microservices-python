import flask
import requests

app = flask.Flask(__name__)

@app.route("/hello")
def hello():
  return "hello world"

@app.route("/hacker_news_encoding")
def hacker_news_encoding():
  url = "https://news.ycombinator.com"
  response = requests.get(url)
  return response.headers["Content-Encoding"]

if __name__ == "__main__":
  app.run()
