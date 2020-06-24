import plivo

client = plivo.RestClient("MAMWU1M2FKMZCXMWUZOG", "OGU1NmY4YzlmOWNiNDVhZDU1MGQzZDhjNmMyYWE0")
response = client.messages.create(
    src='+16026107131',
    dst='+17134716525',
    text='Hello, this is a sample text'
    #url='http://foo.com/sms_status/',
)
print(response)
# prints only the message_uuid
print(response.message_uuid)