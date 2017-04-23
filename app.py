from flask import Flask, render_template, request, redirect
import subprocess
import sqlite3
import os.path
import time
import sys
import nltk
import ast
from nltk.stem.wordnet import WordNetLemmatizer # princeton
lmtzr = WordNetLemmatizer()


from sys import platform
if sys.version_info.major < 3:
    reload(sys)
    sys.setdefaultencoding('utf8')

#if platform == "darwin":
#    sys.path.append('/Users/liup/DL/translate-uisummary')
#elif platform == "linux" or platform == "linux2":
#    sys.path.append('/home/lpxz/deepLearning/translate-uisummary')
#else:
#    pass
#import translateWrapperUISummary
#print translateWrapperUISummary.translate("user name password")


app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

#posts = [("post1", "this is the first post HUrray fjawo;eij"), ("post2", "a;sodifjawo;eifja;woeifjaw;oeifjas;ldkfjha;skdjfhalskdjfhalskdjfhaskldjf")]



    
@app.route("/")
def index():
    #Insert code here to fetch the trending posts now. -genji
    return render_template("search.html")






@app.route("/search", methods= ['GET', 'POST'])
def search(post_id=None):
# matching is based on two criteria: (1 ) screen description matching (2) button description matching
    cur = []
    screenInput = ""
    buttonInput = ""
    topK = 5  # let us simplify the search logic by giving the default K=5
    results = []
    if request.method=='POST':
        cmd = str(request.form['command'])
        screenInput = str(request.form['button']).lower()

        if cmd == 'Search':
            results = [screenInput, "how", "are", "you"]

                

    return render_template("search.html", mytitle="Search" ,result=results)


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=12345)
