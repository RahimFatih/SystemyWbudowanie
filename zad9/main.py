import socket
import smtplib, ssl

def web_page():
    if deviceStan == "ON":
        gpio_state = b"ON"
    else:
        gpio_state = b"OFF"

    html = b"""<html><head> <title>Serwer WWW Denis Firat 249031</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #4286f4;}</style></head><body> <h1>Kochasz mnie Olu?</h1> 
  <p><a href="/?led=on"><button class="button">TAK!</button></a></p>
  <p><a href="/?led=off"><button class="button button2">Jeszcze raz!</button></a></p></body></html>"""
    return html


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)


smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "testowydenisa@gmail.com"
password = "@Dnamama1google@"

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    # TODO: Send email here
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit() 

message = """\
Subject: Wiadomosc dla Oli

Ja Ciebie tez kocham."""
receiver_email = "aleksandra.wygnaniec@gmail.com"
#receiver_email = "dfirat998@gmail.com"
sended=0
deviceStan = "OFF"
while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    led_on = request.find('/?led=on')
    led_off = request.find('/?led=off')
    if led_on == 6 and sended==0:
        print('LED ON')
        deviceStan = "ON"
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        sended=1
    if led_off == 6:
        print('LED OFF')
        deviceStan = "OFF"
        sended=0
    response = web_page()
    conn.send(b'HTTP/1.1 200 OK\n')
    conn.send(b'Content-Type: text/html\n')
    conn.send(b'Connection: close\n\n')
    conn.sendall(response)
    f = open("stan.txt", "w")
    f.write(deviceStan)
    f.close()
    conn.close()
