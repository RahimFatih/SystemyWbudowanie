import socket

def web_page():
    if deviceStan == "ON":
        gpio_state = b"ON"
    else:
        gpio_state = b"OFF"

    html = b"""<html><head> <title>Serwer WWW Denis Firat 249031</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #4286f4;}</style></head><body> <h1>Serwer WWW Denis Firat 249031</h1> 
  <p>Stan urzadzenia: <strong>""" + gpio_state + b"""</strong></p><p><a href="/?led=on"><button class="button">ON</button></a></p>
  <p><a href="/?led=off"><button class="button button2">OFF</button></a></p></body></html>"""
    return html


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    led_on = request.find('/?led=on')
    led_off = request.find('/?led=off')
    deviceStan="OFF"
    if led_on == 6:
        print('LED ON')
        deviceStan = "ON"
    if led_off == 6:
        print('LED OFF')
        deviceStan = "OFF"
    response = web_page()
    conn.send(b'HTTP/1.1 200 OK\n')
    conn.send(b'Content-Type: text/html\n')
    conn.send(b'Connection: close\n\n')
    conn.sendall(response)
    f = open("stan.txt", "w")
    f.write(deviceStan)
    f.close()
    conn.close()