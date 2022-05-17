import datetime
import pywhatkit as kit

currentTimeDate = datetime.datetime.now()
currentTime = str(currentTimeDate.strftime('%H:%M:%S')).split(":")
print(currentTime)
print(type(currentTime[0]))
kit.sendwhatmsg(f"+919772168346", "fhfhfhfhhf",int(currentTime[0]),int(currentTime[1]))