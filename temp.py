import os

def getCPUtemperature():
	res = os.popen('vcgencmd measure_temp').readline()
	return(res.replace("temp=","").replace("'C\n",""))

temp1=int(float(getCPUtemperature()))
temp2= 9.0/5.0*temp1+32
print temp1,"C", "\n",  temp2,"F"