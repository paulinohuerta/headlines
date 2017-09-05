from flask import Flask
import feedparser
from flask import render_template

app= Flask(__name__)

BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"
@app.route("/")
def get_news():
  feed = feedparser.parse(BBC_FEED)
  first_article = feed['entries'][0]
  return render_template("home.html", article=first_article)

if __name__ == '__main__':
  app.run(port=5300,debug=True)
