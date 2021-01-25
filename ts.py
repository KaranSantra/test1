import context
import paho.mqtt.publish as publish
import psutil

channelID = "1246971"
apiKey = "CU4Q7M4SH2DTH4BS"
useUnsecuredTCP = False
useSSLWebsockets = True
mqttHost = "mqtt.thingspeak.com"

if useSSLWebsockets:
    import ssl
    tTransport = "websockets"
    tTLS = {'ca_certs':'/etc/ssl/certs/ca-certificates.crt','tls_version' : ssl.PROTOCOL_TLSv1}
    tPort = 443

topic = "channels/" + channelID + "/publish/" + apiKey
while(True):
    cpuPer = psutil.cpu_percent(interval=20)
    ramPer = psutil.virtual_memory().percent
    print("CPU= ",  cpuPer, " RAM: ", ramPer)
    tPayload = "field1=" + str(cpuPer) + "&field2=" + str(ramPer)
    try:
        publish.single(topic, payload=tPayload, hostname=mqttHost, port=tPort, tls=tTLS, transport=tTransport)
    except (KeyboardInterrupt):
        break
    except:
        print("There was an error while publishing the data")