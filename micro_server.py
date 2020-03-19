import picoweb
import network

application = picoweb.WebApp("app")

@app.route("/")
def index(request, response):
    yield from picoweb.start_response(response, content_type="text/html")

    file = open('index.html', 'r')

    for line in file:
        yield from response.awrite(line)

def get_ip():
    wifi = network.WLAN(network.STA_IF)
    if wifi.active():
        address = wifi.ifconfig()[0]
    else:
        wifi = network.WLAN(network.AP_IF)
        if wifi.active():
            address = wifi.ifconfig()[0]
        else:
            print("No active connection")
    return address

host = get_ip()
application.run(debug=True, host=host)
