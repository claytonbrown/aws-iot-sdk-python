
client_id = 'SampleThing'
topic_subscribe = '$aws/things/%s/shadow/update/accepted'  % (client_id)
topic_publish = "$aws/things/%s/shadow/update/" % (client_id)
mqtthost = "A1YWW1UJGZMYMX.iot.us-east-1.amazonaws.com"
mqttport = 8883
rootca = "./examples/certs/VeriSign-Class 3-Public-Primary-Certification-Authority-G5.pem"
privatekey = "./examples/certs/4a6ddf7be8-private.pem.key"
publickey = "./examples/certs/4a6ddf7be8-public.pem.key"
cert = "./examples/certs/4a6ddf7be8-certificate.pem.crt"
