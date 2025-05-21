#installation librairie
from Flask import Flask,render_template


#debut app
app = Flask(__name__)


#index
@app.route("/")
def index():
    return render_template("index.html")