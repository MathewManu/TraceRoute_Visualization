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
		return render_template('landing.html', allPoints=json.dumps(allPoints), mapType="satelite")


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
	ips = ['130.245.126.1','130.245.128.1','130.245.5.253','38.104.66.205','154.54.84.201','154.54.47.218','154.54.12.18','63.243.216.6','66.198.111.21','66.198.70.34','14.140.230.250','202.88.241.72']
	#ips = ["130.245.126.1","130.245.128.1","130.245.5.253","38.104.66.205","154.54.84.201","154.54.47.49","154.54.6.221","154.54.42.165","154.54.5.89","154.54.41.145","154.54.44.141","154.54.43.70","154.54.1.162","38.122.92.2","49.255.255.18","49.255.255.5","49.255.255.13","175.45.108.214","124.47.136.4","124.47.136.25","124.47.136.52","124.47.136.52","124.47.136.66"]
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