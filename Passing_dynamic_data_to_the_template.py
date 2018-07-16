import feedparser
from flask import Flask
from flask import render_template

app = Flask(__name__)
RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640'}

@app.route("/")
@app.route("/bbc")
def bbc():
 return get_news('bbc')

@app.route("/cnn")
def cnn():
 return get_news('cnn')

@app.route("/")
@app.route("/<publication>")
def get_news(publication="bbc"):
 feed = feedparser.parse(RSS_FEEDS[publication])
 first_article = feed['entries'][0]
 return render_template("passing_dynamic_data.html",
                        title=first_article.get('title'),
                        published=first_article.get('published'),
                        summary=first_article.get('summary'))

if __name__ == "__main__":
 app.run(port=5000, debug=True)



## Output as HTML:

Headlines
Justine Greening calls for second Brexit referendum
Mon, 16 Jul 2018 04:04:01 GMT
The former cabinet minister calls Theresa May's Brexit plan a "fudge" and "the worst of both worlds".
