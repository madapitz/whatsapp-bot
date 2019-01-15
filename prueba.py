from whatsapp import Client

phone_to = '584242130027'

client = Client(login='584168161470', password='8DJ5dRbEvcKMdaz3iwANs/5B+GM=')
print(client)
client.send_message(phone_to, 'Hello Lola')

