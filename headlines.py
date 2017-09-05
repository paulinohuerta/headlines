from flask import Flask
import feedparser
from flask import render_template

app= Flask(__name__)

BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"
@app.route("/")
def get_news():
  feed = feedparser.parse(BBC_FEED)
  return render_template("home.html", articles=feed['entries'])

if __name__ == '__main__':
  app.run(port=5300,debug=True)
