from flask import Flask, render_template, request, url_for, redirect
from database import WorkDatabase
from logic import createHref,checkSrcInDatabaseAndCreate,returnHex

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        href = createHref()
        checkSrcInDatabaseAndCreate(href)
        hex_ = returnHex(href)
        return redirect(url_for('url', src=hex_))

    return render_template("index.html")

@app.route('/url/<path:src>', methods=['GET', 'POST'])
def url(src):
    if WorkDatabase.checkSrcInDatabase(src):
        return redirect(url_for('index'))

    if request.method == "POST":
        href = createHref()
        checkSrcInDatabaseAndCreate(href)
        hex_ = returnHex(href)
        return redirect(url_for('url', src=hex_))

    hex_, srcSite = WorkDatabase.getHexAndSrc(src)
    WorkDatabase.AddView(src)
    views = WorkDatabase.getViews(src)

    return render_template("url.html",url=srcSite,hex=hex_,views=views)

@app.route('/u/<path:src>')
def u(src):
    if WorkDatabase.checkSrcInDatabase(src):
        return redirect(url_for('index'))

    hex_, srcSite = WorkDatabase.getHexAndSrc(src)
    WorkDatabase.AddView(src)

    return redirect(srcSite,code=302)

@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
