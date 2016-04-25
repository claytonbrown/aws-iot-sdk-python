
client_id = 'SampleThing'
topic_subscribe = '$aws/things/%s/shadow/update/accepted'  % (client_id)
topic_publish = "$aws/things/%s/shadow/update/" % (client_id)
mqtthost = "A1YWW1UJGZMYMX.iot.us-east-1.amazonaws.com"
mqttport = 8883
rootca = "./examples/certs/VeriSign-Class 3-Public-Primary-Certification-Authority-G5.pem"
privatekey = "./examples/certs/4a6ddf7be8-private.pem.key"
publickey = "./examples/certs/4a6ddf7be8-public.pem.key"
cert = "./examples/certs/4a6ddf7be8-certificate.pem.crt"

"""
// Get from console
// =================================================
#define AWS_IOT_MQTT_HOST              "A1YWW1UJGZMYMX.iot.us-east-1.amazonaws.com"
#define AWS_IOT_MQTT_PORT              8883
#define AWS_IOT_MQTT_CLIENT_ID         "SampleThing"
#define AWS_IOT_MY_THING_NAME          "SampleThing"
#define AWS_IOT_ROOT_CA_FILENAME      "VeriSign-Class 3-Public-Primary-Certification-Authority-G5.pem"
#define AWS_IOT_CERTIFICATE_FILENAME   "4a6ddf7be8-certificate.pem.crt"
#define AWS_IOT_PRIVATE_KEY_FILENAME   "4a6ddf7be8-private.pem.key"
// =================================================
"""