# import datetime
import requests
# import pywhatkit as kit
# hour=input("mention hours as per (24) ")
# minutes=input("mention hours as per (24) ")
# # currentTimeDate = datetime.datetime.now()
# # currentTime = str(currentTimeDate.strftime('%H:%M:%S')).split(":")
# # print(currentTime)
# # print(type(currentTime[0]))
# kit.sendwhatmsg(f"+919772168346", "fhfhfhfhhf",int(hour),int(minutes))
ip_address = requests.get('https://api64.ipify.org?format=json').json()
print(ip_address)
print( ip_address["ip"])


