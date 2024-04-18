import requests,random
#r=requests.get("https://api16-normal-c-alisg.tiktokv.com/passport/email/send_code/").cookies.get_dict()
#print(r)
def p():
	r="ch1","ch2","ch3"
	cha=random.choice(r)
	if cha=="ch1":
		prox=open('socks4.txt','r').read().splitlines()
		pr=random.choice(prox)
		return {'http':'socks4://'+pr}
	elif cha=="ch2":
		prox=open('socks5.txt','r').read().splitlines()
		pr=random.choice(prox)
		return {'http':'socks5://'+pr}
	elif cha=="ch3":
		prox=open('http.txt','r').read().splitlines()
		pr=random.choice(prox)
		return {'http':'http://'+pr,'http':'https://'+pr}
def tiktok(email):
		#r=requests.get("https://api16-normal-c-alisg.tiktokv.com/passport/email/send_code/").cookies.get_dict()
#		pss=r["passport_csrf_token"]
#		defl=r["passport_csrf_token_default"]

		prox=open('devices.txt','r').read().splitlines()
		from random import randint
		dd=randint(500, 1200)
		import secrets
		ss="{}".format(str(secrets.token_hex(8) * 2))
		did1=random.choice(prox)
		iid=did1.split(":")[0]
		dev=did1.split(":")[1]
		proxy=p()
		import uuid
		u=uuid.uuid4
		url = f"https://api16-normal-c-alisg.tiktokv.com/passport/email/send_code/?residence=AE&device_id={dev}&os_version=14.3&app_id=1233&iid={iid}&app_name=musical_ly&pass-route=1&vendor_id={u}&locale=ar&pass-region=1&ac=WIFI&sys_region=US&ssmix=a&version_code=17.2.0&vid={u}&channel=App%20Store&op_region=AE&os_api=18&idfa=00000000-0000-0000-0000-000000000000&install_id={iid}&idfv={u}&device_platform=iphone&device_type=iPhone9%2C4&openudid=3ce553bec09070081e5a698d3a14a988f3642ac4&account_region=&tz_name=Asia%2FDubai&tz_offset=14400&app_language=ar&carrier_region=AE&current_region=AE&aid=1233&mcc_mnc=42402&screen_width={dd}&uoo=1&content_language=&language=ar&cdid={u}&build_number=172025&app_version=17.2.0&resolution=1242%2A2208"
		headers = {
       'Host':'api16-normal-c-alisg.tiktokv.com', 
	   'Connection':'close', 
	   'Content-Length':'76', 
	   'Cookie':f'sessionid={ss}', 
       'x-Tt-Token':'2c593820065f9a47b9bf51281eda9604-1.0.0', 
	   'Content-Type':'application/x-www-form-urlencoded', 
	   'x-tt-passport-csrf-token':'b0b2ed352b9394eefc29754dfe80926c', 
       'sdk-version':'2', 
	   'passport-sdk-version':'5.12.1'}
		data = {
        'account_sdk_source':'app', 
	    'email':str(email), 
	    'mix_mode':'1', 
	    'type':'31'}
		
		response = requests.post(url, data=data, headers=headers,proxies=proxy)
		print(response.text)
		
		if ('"message":"success"') in response.text:
			
			return True
		
		else:
			
			return False
print(tiktok(input("Your Email : ")))