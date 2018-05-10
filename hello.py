import sys
import socket
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

def traceroute(dest_addr, max_hops=30, timeout=0.2):
    ips = []
    proto_icmp = socket.getprotobyname('icmp')
    proto_udp = socket.getprotobyname('udp')
    port = 33434

    for ttl in range(1, max_hops+1):
        rx = socket.socket(socket.AF_INET, socket.SOCK_RAW, proto_icmp)
        rx.settimeout(timeout)
        rx.bind(('', port))
        tx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto_udp)
        tx.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
        tx.sendto('', (dest_addr, port))

        try:
            data, curr_addr = rx.recvfrom(512)
            curr_addr = curr_addr[0]
        except socket.error:
            curr_addr = None
        finally:
            rx.close()
            tx.close()

        if curr_addr is not None:
        #if type(curr_addr) is not NoneType:
            print "-----"
            print curr_addr
            ips.append(curr_addr)
            #ips.extend(curr_addr)

        if curr_addr == dest_addr:
            return ips

    return ips

def getPositions(url):

    ipDetails = []


    try:
       url_ip = socket.gethostbyname(url)
    except socket.error:
        return ipDetails


    ips = traceroute(url_ip)
    for ip in ips or []:
        ipUrl = 'http://ip-api.com/json/' + ip 
        r = requests.get(ipUrl).json()
        if r[u'status'] == "success":
            ipDetails.append(r)
        
    '''
        for ip in ipDetails:
        print (ip[u'city'], ip[u'lat'], ip[u'lon']) 
    '''
    return ipDetails    

if __name__ == "__main__":
    #app.run(host='0.0.0.0')
    app.run(host="0.0.0.0", port=5000, threaded=True)

            
            
            