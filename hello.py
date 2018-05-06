from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('index.html')

@app.route('/send', methods = ['GET', 'POST'])
def send():
	if request.method == 'POST':
		url = request.form['url']
		#return url
		return render_template('landing.html')

@app.route("/stat")
def stat():
		return render_template('analytics.html')

if __name__ == "__main__":
	#app.run()
	#app.run(host='0.0.0.0')
	app.run(host="0.0.0.0", port=5000, threaded=True)
	#app.run(host='172.24.18.62')