import requests
import json
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('index.html')

@app.route('/send', methods = ['GET', 'POST'])
def send():
	if request.method == 'POST':
		url = request.form['url']
		allPoints = getPositions(url)
		return render_template('landing.html', allPoints=json.dumps(allPoints))


def getPositions(url):
	ipDetails = []
	#print url
	#get ip addresses by calling traceroute function
	''' for each ip 
			sample json response for an ip
			try this in a url http://ip-api.com/json/208.80.152.201
			wjdata = requests.get('url').json()
			get the gps cordinate
			append to a list
			return
	'''
	ips = ['130.245.126.1','38.104.66.205','154.54.47.218','66.198.70.34','202.88.241.72']
	for ip in ips:
		ipUrl = 'http://ip-api.com/json/' + ip 
		r = requests.get(ipUrl).json()
		ipDetails.append(r)
		
	for ip in ipDetails:
		print (ip[u'city'], ip[u'lat'], ip[u'lon']) 

	return ipDetails	

if __name__ == "__main__":
	#app.run(host='0.0.0.0')
	app.run(host="0.0.0.0", port=5000, threaded=True)