
from flask import *
app = Flask(__name__)

@app.route('/')
def index():
	return redirect(url_for('topology'))

@app.route('/topology')
def topology():
    return render_template('topology.html')

@app.route('/hosttracker')
def hosttracker():
    return render_template('hosttracker.html')

if __name__ == '__main__':
    app.run(debug=True)