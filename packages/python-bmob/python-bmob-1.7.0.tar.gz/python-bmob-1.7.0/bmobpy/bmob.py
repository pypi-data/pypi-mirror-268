import json
import time
import os
import mimetypes
import datetime
from websockets.sync.client import connect

try:
	from urllib import quote, urlpase
	import urllib2 as import_urllib
except ImportError:
	from urllib.parse import quote,urlparse
	import urllib.request as import_urllib

class BmobDict(dict):
	"""将dict转为object模式

	Args:
		dict (_type_): _description_
	"""
	def __getattr__(self, name):
		return self.get(name)
    
class BmobObject:
	"""Bmob的基础对象类
	"""	
	def __init__(self, type):
		"""初始化

		Args:
			type (_type_): Bmob数据的类型，包括指针类、文件类、日期类、地理位置类
		"""		
		self.__dict__["__type"] = type

class BmobPointer(BmobObject):
	"""Bmob的指针类

	Args:
		BmobObject (BmobObject): 
	"""	
	def __init__(self, className, objectId):
		"""初始化指针类

		Args:
			className (string): 数据表的名称
			objectId (string): 对应数据的objectId
		"""		
		BmobObject.__init__(self, "Pointer")
		self.__dict__["className"] = className
		self.__dict__["objectId"] = objectId

class BmobFile(BmobObject):
	"""Bmob的文件类

	Args:
		BmobObject (BmobObject): 
	"""	
	def __init__(self, url, filename = ""):
		"""初始化文件类

		Args:
			url (string): 文件路径
			filename (str, optional): 文件名. Defaults to "".
		"""		
		BmobObject.__init__(self, "File")
		self.__dict__["url"] = url
		self.__dict__["filename"] = filename
	
	def __getattr__(self, name):
		return self.__dict__[name]
  
class BmobDate(BmobObject):
	"""Bmob的日期类

	Args:
		BmobObject (BmobObject): 
	"""	
	def __init__(self, timestamp):
		"""初始化日期类

		Args:
			timestamp (int): 时间戳
		"""		
		BmobObject.__init__(self, "Date")
		if type(timestamp) == float or type(timestamp) == int:
			timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp / 1000))
		self.__dict__["iso"] = timestamp
		
class BmobGeoPoint(BmobObject):
	"""Bmob的地理位置类

	Args:
		BmobObject (BmobObject): 
	"""	
	def __init__(self, latitude, longitude):
		"""初始化

		Args:
			latitude (float): 纬度
			longitude (float): 经度
		"""		
		if latitude>90 or latitude <-90:
			raise('纬度（latitude）必须在-90到90之间')

		if longitude>180 or longitude <-180:
			raise('经度（longitude）必须在-180到180之间')
		BmobObject.__init__(self, "GeoPoint")
		self.__dict__["latitude"] = latitude
		self.__dict__["longitude"] = longitude

def def_marshal(obj):
	return obj.__dict__

def dealBmobResult(bmobResult,types):
	error = bmobResult.getError()
	if error['error'] is None:
		return True
	print(f'{types}失败，原因：{error["error"]} 错误码：{error["code"]}')
	return False

def dealBmobResultDict(bmobResult,types):
	error = bmobResult.getError()
	if error['error'] is None:
		return BmobDict(bmobResult.jsonData)
	print(f'{types}失败，原因：{error["error"]} 错误码：{error["code"]}')
	return None

class BmobUpdate:
	@staticmethod
	def add(key, value, data = None):
		"""_summary_

		Args:
			key (_type_): _description_
			value (_type_): _description_
			data (_type_, optional): _description_. Defaults to None.

		Returns:
			_type_: _description_
		"""		
		if data == None:
			data = {}
		data[key] = value
		return data
	
	@staticmethod
	def ensuerArray(self, value):
		if isinstance(value, BmobObject):
			value = [value.__dict__]
		elif isinstance(value, dict):
			value = [value]
		elif isinstance(value, list) or isinstance(value, tuple):
			objs = []
			for i in range(0, len(value)):
				obj = value[i]
				if isinstance(obj, BmobObject):
					obj = obj.__dict__
				objs.append(obj)
			value = objs
		else:
			value = [value]
		return value
	
	@staticmethod
	def increment(key, number, data = None):
		return BmobUpdate.add(key, {"__op": "Increment", "amount": number}, data)
	
	@staticmethod
	def arrayAdd(key, value, data = None):
		return BmobUpdate.add(key, {"__op": "Add", "objects": BmobUpdate.ensuerArray(value)}, data)
	
	@staticmethod
	def arrayAddUnique(key, value, data = None):
		return BmobUpdate.add(key, {"__op": "AddUnique", "objects": BmobUpdate.ensuerArray(value)}, data)
	
	@staticmethod
	def arrayRemove(key, value, data = None):
		return BmobUpdate.add(key, {"__op": "Remove", "objects": BmobUpdate.ensuerArray(value)}, data)
	
	@staticmethod
	def addRelations(key, value, data = None):
		return BmobUpdate.add(key, {"__op": "AddRelation", "objects": BmobUpdate.ensuerArray(value)}, data)
	
	@staticmethod
	def removeRelations(key, value, data = None):
		return BmobUpdate.add(key, {"__op": "RemoveRelation", "objects": BmobUpdate.ensuerArray(value)}, data)

class BmobQuery:
	def __init__(self):
		self.filter = {}
  
	# 基础
	def putWhereFilter(self, key, value = None, oper = None):
		if key == None or len(key) == 0 or value == None:
			return self
		if isinstance(value, BmobObject):
			value = value.__dict__
		if oper == None:
			self.filter[key] = value
		else:
			self.filter[key] = {oper: value}
		return self
	def addWhereEqualTo(self, key, value = None):
		"""等于

		Args:
			key (_type_): _description_
			value (_type_, optional): _description_. Defaults to None.

		Returns:
			_type_: _description_
		"""     
		if value == None:
			return self.addWhereNotExists(key)
		else:
			return self.putWhereFilter(key, value)
	def addWhereNotEqualTo(self, key, value = None):
		"""不等于

		Args:
			key (_type_): _description_
			value (_type_, optional): _description_. Defaults to None.

		Returns:
			_type_: _description_
		"""     
		if value == None:
			return self.addWhereExists(key)
		else:
			return self.putWhereFilter(key, value, "$ne")

	def addWhereGreaterThan(self, key, value):
		"""大于

		Args:
			key (_type_): _description_
			value (_type_): _description_

		Returns:
			_type_: _description_
		"""     
		return self.putWhereFilter(key, value, "$gt")

	def addWhereGreaterThanOrEqualTo(self, key, value):
		"""大于等于

		Args:
			key (_type_): _description_
			value (_type_): _description_

		Returns:
			_type_: _description_
		"""     
		return self.putWhereFilter(key, value, "$gte")

	def addWhereLessThan(self, key, value):
		"""小于

		Args:
			key (_type_): _description_
			value (_type_): _description_

		Returns:
			_type_: _description_
		"""     
		return self.putWhereFilter(key, value, "$lt")

	def addWhereLessThanOrEqualTo(self, key, value):
		"""小于等于

		Args:
			key (_type_): _description_
			value (_type_): _description_

		Returns:
			_type_: _description_
		"""     
		return self.putWhereFilter(key, value, "$lte")

	def addWhereRelatedTo(self, table, objectId, key):
		"""关联

		Args:
			table (_type_): _description_
			objectId (_type_): _description_
			key (_type_): _description_

		Returns:
			_type_: _description_
		"""     
		return self.putWhereFilter(key, {"key": key, "object": {"__type": "Pointer", "className": table, "objectId": objectId}}, "$relatedTo")

	def addWhereExists(self, key, exists = True):
		"""存在

		Args:
			key (_type_): _description_
			exists (bool, optional): _description_. Defaults to True.

		Returns:
			_type_: _description_
		"""     
		return self.putWhereFilter(key, exists, "$exists")

	def addWhereNotExists(self, key):
		"""不存在

		Args:
			key (_type_): _description_

		Returns:
			_type_: _description_
		"""     
		return self.addWhereExists(key, False)

	# 地理位置
	def addWhereNear(self, key, bmobGeoPointer, maxMiles = None, maxKM = None, maxRadians = None):
		near = {"$nearSphere": bmobGeoPointer.__dict__}
		if maxMiles != None:
			near["$maxDistanceInMiles"] = maxMiles
		if maxKM != None:
			near["$maxDistanceInKilometers"] = maxKM
		if maxRadians != None:
			near["$maxDistanceInRadians"] = maxRadians
		return self.putWhereFilter(key, near)

	def addWhereWithinGeoBox(self, key,southwest, northeast):
		return self.putWhereFilter(key, {"$box": [southwest.__dict__, northeast.__dict__]}, "$within")
	
	# 列表
	def addWhereContainedIn(self, key, value, isIn = True):
		if isIn:
			isIn = "$in"
		else:
			isIn = "$nin"
		return self.putWhereFilter(key, value, isIn)
	
	def addWhereNotContainedIn(self, key, value):
		return self.addWhereContainedIn(key, value, False)
	
	def addWhereContainsAll(self, key, value):
		return self.putWhereFilter(key, value, "$all")
	
	def addWhereStrContains(self, key, value):
		"""模糊查询（正则查询）

		Args:
			key (str): 列名
			value (str): 是否存在的字符串

		Returns:
			self: 自身
		"""		
		return self.putWhereFilter(key, value, "$regex")
	
	# 子查询
	def addWhereMatchesSelect(self, key, innerQuery, innerKey, innerTable = None, isMatch = True):
		if isMatch:
			isMatch = "$select"
		else:
			isMatch = "$dontSelect"
		if isinstance(innerQuery, BmobQuery):
			innerQuery = {"className": innerTable, "where": innerQuery.filter}
		return self.putWhereFilter(key, {"key": innerKey, "query": innerQuery}, isMatch)
	
	def addWhereInQuery(self, key, value, className = None, isIn = True):
		if isIn:
			isIn = "$inQuery"
		else:
			isIn = "$notInQuery"
		if isinstance(value, BmobQuery):
			innerQuery = {"className": className, "where": value.filter}
		return self.putWhereFilter(key, value, isIn)

class BmobResult:
	def __init__(self, data):
		if data == None:
			data = '{}'
		
		if data is not None and type(data) is not dict:
			data = data.decode('utf-8')   
		self.stringData = data
		self.queryResults = None
		self._statCount = 0
		self.jsonData = {}
		self._error = None

		try:
			if type(data) is not dict:
				self.jsonData = json.loads(data)
			else:
				self.jsonData = data
			if 'error' in self.jsonData:
				self._error = self.jsonData['error']
				self._code = self.jsonData['code']
			elif 'results' in self.jsonData:
				self.queryResults = self.jsonData["results"]
			elif 'count' in self.jsonData:
				self._statCount = self.jsonData["count"]

		except:
			self.jsonData = {}
	
	def getError(self):
		return {'error':self._error,'code':self._code}
  
	def __iter__(self):
		if self.queryResults is None:
			self.queryResults = {}
		return iter(self.queryResults)
	
	def __len__(self):
		if self._error is None:
			if self.queryResults is not None:
				return len(self.queryResults)
			elif self._statCount!=0:
				return 0
			else:
				return 1 
		return 0

	def __getattr__(self, name):
		return self.jsonData[name] if name in self.jsonData else None

def BmobRequest(url, method = 'GET', headers = None, body = None, timeout = 10, encode = True):
	"""发起HTTP请求

	Args:
		url (string): 请求地址
		method (str, optional): 请求方法，默认为GET请求. 
		headers (dict, optional): 请求头，默认为None.
		body (dict, optional): 请求体，默认为None. 
		timeout (int, optional): 超时时间，默认10秒.

	Returns:
		BmobResult: Http请求返回结果
	"""	
	if headers == None:
		headers = {}
	if body != None and encode:
		body = body.encode("utf-8")
	req = import_urllib.Request(url=url, data=body, headers=headers)
	if method != None:
		
		req.get_method = lambda: method

		try:
			res = import_urllib.urlopen(req, timeout = timeout)
			return BmobResult(res.read())
		except import_urllib.URLError as e:
			try:
				return BmobResult(e.read())
			except Exception as e:
				return BmobResult({'error':f'Exception: {e}','code':-1})
	else:
		errMsg = "Unknown Error"
		return BmobResult({'error':errMsg,'code':-1})

class Bmob:
    
	error = {}
	chatList = {}
	reply = ''
    
	def __init__(self, application_id, rest_api_key):
		"""初始化Bmob

		Args:
			application_id (string): 进入Bmob控制台，具体应用 -> 设置 -> 应用密钥 -> Application ID
			rest_api_key (string): 进入Bmob控制台，具体应用 -> 设置 -> 应用密钥 -> REST API Key
		"""		
		self.domain = 'https://api.codenow.cn'
		self.headers = {"X-Bmob-Application-Id": application_id, "X-Bmob-REST-API-Key": rest_api_key, "Content-Type": "application/json"}
		self.appid = application_id
		self.restkey = rest_api_key

	def connectAI(self):
		"""初始化AI服务
		"""		
		url = 'wss://api.codenow.cn/1/ai'
		self.ws = connect(url,additional_headers=self.headers)
	
	def closeAI(self):
		"""关闭AI服务
		"""		
		try:
			self.ws.close()
		except Exception as e:
			pass

	def chat(self,chatmsg='你好',session='default'):
		"""开始对话

		Args:
			chatmsg (str, optional): 发送的对话内容. Defaults to '你好'.
			session (str, optional): 会话名称. Defaults to 'default'.

		Returns:
			str: AI服务器返回的文字
		"""		
		# 发送消息到AI服务器
		if session not in self.chatList:
			self.chatList[session] = []
				
		sessionchatlist = self.chatList[session]

		if len(sessionchatlist) >=1:
			last = sessionchatlist[-1]
			if last['role'] =='assistant':
				sessionchatlist.append({
					'role':'user',
					'content':chatmsg
				})
		else:
			sessionchatlist.append({
				'role':'user',
				'content':chatmsg
			})

		if len(sessionchatlist) > 5:
			realsend = sessionchatlist[-6:]
		else:
			realsend = sessionchatlist
		
		sendmsg = {
			'messages':realsend,
			'session':'python'
		}

		self.ws.send(json.dumps(sendmsg))
		self.reply = ''

		while True:
			try:
				message = self.ws.recv_messages.get()
				data = json.loads(message)

				if 'choices' in message:
					finish = data['choices'][0]['finish_reason']
					if finish!='':
						sessionchatlist.append({
							'role':'assistant',
							'content':self.reply
						})
						return self.reply
					self.reply += data['choices'][0]['delta']['content']		
				else:
					print('ai的数据格式错误')
					return self.reply
			except Exception as e:
				print(e)
				return self.reply

	def getError(self):
		"""获取错误信息

		Returns:
			dict: 错误码和错误信息
		"""     
		return self.error

	def resetDomain(self, domain):
		"""重置域名

		Args:
			domain (string): 正式上线之后，建议在初始化Bmob之后，调用这个方法，将你的备案域名替换为正式域名
		"""		
		self.domain = domain
	
	def setUserSession(self, sessionToken):
		"""设置用户的登录sessionToken信息

		Args:
			sessionToken (string): 用户登录的sessionToken

		Returns:
			Bmob: self
		"""		
		self.headers["X-Bmob-Session-Token"] = sessionToken
		return self
	
	def setMasterKey(self, masterKey):
		"""设置masterKey

		Args:
			masterKey (string): 在 控制台 -> 设置 -> 应用密钥 -> Master Key

		Returns:
			Bmob: self
		"""		
		self.headers["X-Bmob-Master-Key"] = masterKey
		return self

	def signUp(self,username,password,userInfo=None):
		"""用户注册
  
		示例代码：
		from bmob import *
		b = Bmob('application_id','rest_api_key')
		rs = b.signUp('13800138002','123456', userInfo={
			'sex':True,
			'age':100
		})
		
		其中，13800138002是注册的账号，123456是登录的密码，userInfo是其他的用户信息，可为空.

		Args:
			username (string): 账号
			password (string): 密码
			userInfo (dict, optional): 用户表的其他字段信息. Defaults to None.

		Returns:
			object: 注册成功之后的用户记录信息
		"""     
		userInfo = {}
		if userInfo is None:
			userInfo = {
				'username':username,
				'password':password
			}
		else:
			userInfo['username'] = username
			userInfo['password'] = password

		return self.__signUp(userInfo)

	def __signUp(self, userInfo):
		"""用户注册

		Args:
			userInfo (dict): 用户的注册数据信息，封装为dict类型

		Returns:
			object: 注册成功之后的用户记录信息
		"""		
		bmobResult =  BmobRequest(url = self.domain + '/1/users', method = 'POST', headers = self.headers, body = json.dumps(userInfo, default=def_marshal))
		self.error = bmobResult.getError()
		if self.error['error'] is None:
			return  BmobDict(bmobResult.jsonData)
		print(f'用户注册失败，原因：{self.error["error"]} 错误码：{self.error["code"]}')
		return None
	
	def login(self, username, password):
		"""用户登录（账号+密码）

		示例代码：
		from bmob import *
		b = Bmob('application_id','rest_api_key')
		rs = b.login('13800138000','123456')

		Args:
			username (string): 账号
			password (string): 密码

		Returns:
			object: 登录用户的信息，如果为None，表示登录失败
		"""		
		bmobResult =  BmobRequest(url = self.domain + '/1/login?username=' + quote(username) + '&password=' + quote(password), method = 'GET', headers = self.headers)
		self.error = bmobResult.getError()
		if 'sessionToken' in bmobResult.jsonData:
			self.setUserSession(bmobResult.jsonData['sessionToken'])
		return dealBmobResultDict(bmobResult,'登录')
	
	def loginBySMSCode(self, mobile, smsCode, userInfo):
		"""使用手机号码一键注册或登陆
  
		调用此方法前，首先需要调用requestSMSCode方法。

		Args:
			mobile (string): 手机号码
			smsCode (string): 短信验证码
			userInfo (dict): 用户的注册数据信息，封装为dict类型

		Returns:
			object: 注册成功之后的用户记录信息
		"""		
		userInfo["mobilePhoneNumber"] = mobile
		userInfo["smsCode"] = smsCode
		return self._signUp(userInfo)
	
	def resetPasswordByEmail(self, email):
		"""邮件重置密码

		示例代码：
		from bmob import *
		b = Bmob('application_id','rest_api_key')
		rs = b.resetPasswordByEmail('需要重置密码的邮箱地址')

		Args:
			email (string): 邮箱

		Returns:
			bool: 是否成功发送重置密码的邮件
		"""		
		bmobResult = BmobRequest(url = self.domain + '/1/requestPasswordReset', method = 'POST', headers = self.headers, body = json.dumps({"email": email}))
		self.error = bmobResult.getError()
		if self.error['error'] is None:
			data =  BmobDict(bmobResult.jsonData)
			if data.msg =='ok':
				return True
		print(f'发送重置密码的邮件失败，原因：{self.error["error"]} 错误码：{self.error["code"]}')
		return False
	
	def resetPasswordBySMSCode(self, smsCode, newpassword):
		"""重置密码（短信验证码的方式重置）

		示例代码：
		在调用这个方法前，你需要先调用发送短信验证码的方法，即如下：
		from bmob import *
		b = Bmob('application_id','rest_api_key')
		rs = b.requestSMSCode('13800138000')

		然后。再执行重置密码的方法：
		rs = b.resetPasswordBySMSCode('用户收到的短信验证码','要变更的新密码')

		Args:
			smsCode (string): 短信验证码
			password (string): 密码

		Returns:
			bool: 是否重置密码成功
		"""		
		bmobResult = BmobRequest(url = self.domain + '/1/resetPasswordBySmsCode/' + smsCode, method = 'PUT', headers = self.headers, body = json.dumps({"password": newpassword}))
		self.error = bmobResult.getError()
		if self.error['error'] is None:
			data =  BmobDict(bmobResult.jsonData)
			if data.msg =='ok':
				return True
		print(f'短信验证码重置密码失败，原因：{self.error["error"]} 错误码：{self.error["code"]}')
		return False
	
	def updatePassword(self, objectId, oldPassword, newPassword):
		"""重置密码（旧密码方式安全修改用户密码）

		示例代码：
		from bmob import *
		b = Bmob('application_id','rest_api_key')
		rs = b.updatePassword('这个用户记录的objectId', '原密码', '新密码')

		Args:
			objectId (string): 要修改密码的用户的objectId
			oldPassword (string): 旧密码
			newPassword (string): 新密码

		Returns:
			bool: 是否修改成功
		"""		
		bmobResult = BmobRequest(url = self.domain + '/1/updateUserPassword/' + objectId, method = 'PUT', headers = self.headers, body = json.dumps({"oldPassword": oldPassword, "newPassword": newPassword}))
	
		self.error = bmobResult.getError()
		if self.error['error'] is None:
			data =  BmobDict(bmobResult.jsonData)
			if data.msg =='ok':
				return True
		print(f'旧密码方式安全修改用户密码失败，原因：{self.error["error"]} 错误码：{self.error["code"]}')
		return False
	
	def requestSMSCode(self, mobile, template=''):
		"""请求发送短信验证码

		示例代码：

		from bmob import *
		b = Bmob('application_id','rest_api_key')
		rs = b.requestSMSCode('13800138000','mytemplates')

		其中，13800138000是要接收验证码的手机号码，mytemplates是你在Bmob控制台上申请并且审核通过的短信验证码模板，如果不填，用默认的短信验证码模板.

		Args:
			mobile (string): 要接收验证码的手机号码
			template (string): 验证码的模板（你要先在控制台 -> 短信 -> 自定义模板 中创建你的短信验证码模板，待审核通过之后使用）

		Returns:
			BmobResult: 数据的查询结果
		"""		
		bmobResult = BmobRequest(url = self.domain + '/1/requestSmsCode', method = 'POST', headers = self.headers, body = json.dumps({'mobilePhoneNumber': mobile, 'template': template}))
		self.error = bmobResult.getError()
		if self.error['error'] is None:
			return BmobDict(bmobResult.jsonData)
		print(f'请求短信验证码失败，原因：{self.error["error"]} 错误码：{self.error["code"]}')
		return None
	
	def verifySmsCode(self, mobile, smsCode):
		"""检验验证码是否正确

		Args:
			mobile (string): 手机号码
			smsCode (string): 待检验的验证码（6位）

		Returns:
			bool: 验证码是否正确
		"""		
		bmobResult = BmobRequest(url = self.domain + '/1/verifySmsCode/' + smsCode, method = 'POST', headers = self.headers, body = json.dumps({'mobilePhoneNumber': mobile}))
		self.error = bmobResult.getError()
		if self.error['error'] is None:
			rs = BmobDict(bmobResult.jsonData)
			if rs.msg == 'ok':
				return True
			return False
		print(f'请求短信验证码失败，原因：{self.error["error"]} 错误码：{self.error["code"]}')
		return False
	
	def functions(self, funcName, body = None):
		"""调用云函数代码

		示例代码：
		from bmob import *
		b = Bmob('application_id','rest_api_key')
		rs = b.functions('myfun', body = {'param1':'value1','param2':'value2'})
		其中，myfun是你在Bmob后端云云函数中创建的方法名，body是你要传递给云函数的参数字典，如果不需要传递参数，默认为None.

		Args:
			funcName (string): 云函数名称
			body (dict, optional): 请求体. Defaults to None.

		Returns:
			string: 云函数的返回结果
		"""		
		if body == None:
			body = {}

		bmobResult = BmobRequest(url = self.domain + '/1/functions/' + funcName, method = 'POST', headers = self.headers, body = json.dumps(body, default=def_marshal))
		self.error = bmobResult.getError()
		if self.error['error'] is None:
			return bmobResult.jsonData['result']
		print(f'请求云函数失败，原因：{self.error["error"]} 错误码：{self.error["code"]}')
		return None
	
	def getServerTime(self):
		"""获取服务器时间戳

		示例代码：

		rs = b.getServerTime()
		print(rs)

		其中，rs返回服务器的时间戳和日期字典信息

		Returns:
			object: 服务器的时间戳对象，如 {'timestamp': 1712902737, 'datetime': '2024-04-12 14:18:57'}
		"""		
		bmobResult =  BmobRequest(url = self.domain + '/1/timestamp/', method = 'GET', headers = self.headers)
		self.error = bmobResult.getError()
		if self.error['error'] is None:
			return BmobDict(bmobResult.jsonData)
		print(f'获取服务器时间失败，原因：{self.error["error"]} 错误码：{self.error["code"]}')
		return None
	
	def doBatch(self, requests):
		"""批量数据操作

		Args:
			requests (json): requests的数据格式参考文档：https://doc.bmobapp.com/data/restful/develop_doc/#_22

		Returns:
			BmobResult: 数据的查询结果
		"""		
		return BmobRequest(url = self.domain + '/1/batch', method = 'POST', headers = self.headers, body = json.dumps(requests, default=def_marshal))
	
	def save(self, className, data):
		"""新增一条记录

		示例代码：
		from bmob import *
		b = Bmob('application_id','rest_api_key')
		isOK = b.save('ai_log',data={
			'messages':'这是新的内容'
		})

		其中，ai_log是表名，data存放要新增的内容信息，返回isOK表示是否新增成功

		Args:
			className (string): 数据表的名称
			data (dict): 要新增的数据内容

		Returns:
			bool: 是否新增数据成功
		"""		
		if isinstance(data, dict):
			for k, v in data.items():
				if(isinstance(v, BmobObject)):
					data[k] = v.__dict__
		bmobResult = BmobRequest(url = self.domain + '/1/classes/' + className, method = 'POST', headers = self.headers, body = json.dumps(data, default=def_marshal))
		self.error = bmobResult.getError()
  
		if self.error['error'] is None:
			return BmobDict(bmobResult.jsonData)
		print(f'新增数据失败，原因：{self.error["error"]} 错误码：{self.error["code"]}')
		return None
		# return dealBmobResult(bmobResult,'新增数据')
	
	def update(self, className, objectId, data):
		"""更新数据

		示例代码：
		from bmob import *
		b = Bmob('application_id','rest_api_key')
		isOK = b.update('ai_log','93a9b6847f',data={
			'messages':'mytest'
		})

		其中，ai_log是表名，93a9b6847f是要更新的那条记录的objectId，data存放要更新的内容信息，返回isOK表示是否更新成功


		Args:
			className (string): 数据表的名称
			objectId (string): 要更新的数据的objectId
			data (dict): 要更新的数据内容

		Returns:
			bool: 是否更新成功
		"""		
		if isinstance(data, dict):
			for k, v in data.items():
				if(isinstance(v, BmobObject)):
					data[k] = v.__dict__
		bmobResult =  BmobRequest(url = self.domain + '/1/classes/' + className + '/' + objectId, method = 'PUT', headers = self.headers, body = json.dumps(data, default=def_marshal))
		self.error = bmobResult.getError()
		return dealBmobResult(bmobResult,'更新')
	
	def delete(self, className, objectId):
		"""删除单条数据

		示例代码：
		from bmob import *
		b = Bmob('application_id','rest_api_key')
		isOK = b.delete('ai_log','93a9b6847f')

		其中，ai_log是表名，93a9b6847f是要删除的那条记录的objectId，返回isOK表示是否删除成功

		Args:
			className (string): 数据表的名称
			objectId (string): 要删除的数据的objectId

		Returns:
			bool: 是否删除成功
		"""		
		bmobResult = BmobRequest(url = self.domain + '/1/classes/' + className + '/' + objectId, method = 'DELETE', headers = self.headers)
		self.error = bmobResult.getError()
		return dealBmobResult(bmobResult,'删除')

	def count(self,className,where = None):
		"""查询where条件的记录数有多少条
  
		示例代码：
  
		from bmob import *
		b = Bmob('application_id','rest_api_key')
		rs = b.count('ai_log', where=None)
		print('查询到的数据的总行数是',rs)
  
		其中，ai_log是表名，where参数可传递BmobQuery对象.


		Args:
			className (string): 数据表名称
			where (string or BmboQuery, optional): 查询条件. Defaults to None.

		Returns:
			int: 记录数。如果发生异常，返回None.
		"""     
		return self.__basefindObjects(className,where=where,limit=0,count=1)

	def sum(self,className, sumName ,where = None):
		"""查询where条件下，sumName的和
  
		示例代码：
  
		from bmob import *
		b = Bmob('application_id','rest_api_key')
		rs = b.sum('ai_log', ['count','isShow'], where=None)
		print('求和是',rs)
  
		其中，ai_log是表名，['count','isShow']是要求和的列名，where的参数可以为BmobQuery对象

		Args:
			className (string): 数据表名称
			sumName (string or list): 求和的列，多列求和用list
			where (string or BmboQuery, optional): 查询条件. Defaults to None.

		Returns:
			dict or int: 和的结果
		"""     
		return self.__basefindObjects(className,where=where, sum=sumName)

	def max(self,className, maxName ,where = None):
		"""查询where条件下，maxName列的最大值
  
		示例代码：
		from bmob import *
		b = Bmob('application_id','rest_api_key')
		rs = b.max('ai_log', ['count','isShow'], where=None)
		print('最大值是',rs)
  
		其中，ai_log是表名，['count','isShow']是要求最大值的列名，where的参数可以为BmobQuery对象

		Args:
			className (string): 数据表名称
			maxName (string or list): 求最大值的列，多列求最大值用list
			where (string or BmboQuery, optional): 查询条件. Defaults to None.

		Returns:
			dict or int: 最大值
		"""     
		return self.__basefindObjects(className,where=where, max=maxName)

	def min(self,className, minName ,where = None):
		"""查询where条件下，minName列的最小值
  
		示例代码：
  
		from bmob import *
		b = Bmob('application_id','rest_api_key')
		rs = b.min('ai_log', ['count','isShow'], where=None)
		print('最小值是',rs)
  
		其中，ai_log是表名，['count','isShow']是要求最小值的列名，where的参数可以为BmobQuery对象

		Args:
			className (string): 数据表名称
			minName (string or list): 求最小值的列，多列求最小值用list
			where (string or BmboQuery, optional): 查询条件. Defaults to None.

		Returns:
			dict or int: 最小值
		"""     
		return self.__basefindObjects(className,where=where, min=minName)

	def mean(self,className, meanName ,where = None):
		"""查询where条件下，meanName列的平均值
  
		from bmob import *
		b = Bmob('application_id','rest_api_key')
		rs = b.mean('ai_log', ['count','isShow'], where=None)
		print('平均值是',rs)
  
		其中，ai_log是表名，['count','isShow']是要求平均值的列名，where的参数可以为BmobQuery对象

		Args:
			className (string): 数据表名称
			meanName (string or list): 求平均值的列，多列求平均值用list
			where (string or BmboQuery, optional): 查询条件. Defaults to None.

		Returns:
			dict or int: 平均值
		"""     
		return self.__basefindObjects(className,where=where, average=meanName)

	def findObjects(self, className, where = None, limit = None, skip = None, order = None, include = None, keys = None,groupby = None, groupcount = None, having = None):
		return self.__basefindObjects(className,where=where,limit=limit,skip=skip,order=order,include=include,keys=keys,groupby=groupby,groupcount=groupcount,having=having)
	
	def __basefindObjects(self, className, where = None, limit = None, skip = None, order = None, include = None, keys = None, count = None, groupby = None, groupcount = None, min = None, max = None, sum = None, average = None, having = None):
		"""多条数据的条件查询

		示例代码：
		from bmob import *
		b = Bmob('application_id','rest_api_key')
		rs = b.findObjects('ai_log',limit=10,order='-createdAt')
		for r in rs:
			print(r.messages)
		
		其中，ai_log是表名，limit表示最多获取10条记录，-createdAt表示按createdAt字段降序排列

		Args:
			className (string): 数据表名称
			where (json, optional): 查询条件. Defaults to None.
			limit (int, optional): 获取的最大记录数. Defaults to None.
			skip (int, optional): 跳过前面的多少条记录. Defaults to None.
			order (_type_, optional): 按什么进行排序. Defaults to None.
			include (_type_, optional): _description_. Defaults to None.
			keys (_type_, optional): _description_. Defaults to None.
			count (_type_, optional): _description_. Defaults to None.
			groupby (_type_, optional): _description_. Defaults to None.
			groupcount (_type_, optional): _description_. Defaults to None.
			min (string, optional): 需要计算最小值的字段名称. Defaults to None.
			max (string, optional): 需要计算最大值的字段名称. Defaults to None.
			sum (string, optional): 需要求和的字段名称. Defaults to None.
			average (string, optional): 需要计算平均值的字段名称. Defaults to None.
			having (dict, optional): 分组中的过滤条件. Defaults to None.

		Returns:
			list: 数据的查询结果，列表结果
		"""		
		try:
			url = self.domain + '/1/classes/' + className

			params = ''
			if limit != None:
				params += '&limit=' + str(limit)
			if skip != None:
				params += '&skip=' + str(skip)
			if count != None:
				params += '&count=' + str(count)
			if groupby != None:
				params += '&groupby=' + quote(groupby)
			if groupcount != None and (groupcount == True or groupcount == 1):
				params += '&groupcount=true'
			if sum != None:
				if type(sum) is list:
					params += '&sum=' + quote(','.join(sum))
				else:
					params += '&sum=' + quote(sum)
			if average != None:
				if type(average) is list:
					params += '&average=' + quote(','.join(average))
				else:
					params += '&average=' + str(average)
			if max != None:
				if type(max) is list:
					params += '&max=' + quote(','.join(max))
				else:
					params += '&max=' + str(max)
			if min != None:
				if type(min) is list:
					params += '&min=' + quote(','.join(min))
				else:
					params += '&min=' + str(min)
			if having != None:
				params += '&having=' + str(having)
			if order != None:
				params += '&order=' + str(order)
			if keys != None:
				if type(keys) is list:
					params += '&keys=' + quote(','.join(keys))
				else:
					params += '&keys=' + str(keys)
			if include != None:
				if type(include) is list:
					params += '&include=' + quote(','.join(include))
				else:
					params += '&include=' + str(include)
			if where != None:
				if isinstance(where, BmobQuery):
					where = where.filter
				params += '&where=' + quote(json.dumps(where, default=def_marshal))
			if len(params) != 0:
				url += '?' + params[1:]
			bmobResult = BmobRequest(url = url, method = 'GET', headers = self.headers)
		
			self.error = bmobResult.getError()
			if self.error['error'] is None:
				if (sum!=None and sum!='') or (max!=None and max!='') or (min!=None and min!='') or (average!=None and average!=''):
					if bmobResult.jsonData['results'] == []:
						return None
					results = bmobResult.jsonData['results'][0]
					if len(results)>1:
						return results
					elif len(results)==1:
						for d in results:
							return results[d]
					else:
						return None

				if 'count' in bmobResult.jsonData:
					return bmobResult.jsonData['count']
				
				data = []
				for r in bmobResult.queryResults:
					data.append(BmobDict(r))
				return data
			
			print(f'获取数据失败，原因：{self.error["error"]} 错误码：-1')

			if sum!=None or count!=None or max!=None or min!=None or average!=None:
				return None

			return []
		
		except Exception as e:
			msg = '发生异常：' + str(e)
			print(f'获取数据失败，原因：{msg} 错误码：-1')
			return []

	def getObject(self, className, objectId):
		"""查询一条记录

		示例代码：
		from bmob import *
		b = Bmob('application_id','rest_api_key')
		r = b.getObject("ai_log", "5949973169")
		print(r.messages)

		其中，ai_log是表名，5949973169是这条记录的objectId，messages是记录的字段名.

		Args:
			className (string): 数据表名称.
			objectId (string): 这条记录的objectId.

		Returns:
			object: 数据的查询结果.
		"""	
		
		bmobResult =  BmobRequest(url = self.domain + '/1/classes/' + className + '/' + objectId, method = 'GET', headers = self.headers)
	
		self.error = bmobResult.getError()
		if self.error['error'] is None:
			data = BmobDict(bmobResult.jsonData)
			return data
		print(f'获取数据失败，原因：{self.error["error"]} 错误码：{self.error["code"]}')
		return None

	def upload(self,filepath):
		"""上传文件

		Args:
			filepath (string): 文件的路径地址

		Returns:
			BmobFile: BmobFile对象，包括文件名和上传成功之后的url
		"""     
		if os.path.exists(filepath):
			filename = os.path.basename(filepath).rsplit(".", 1)[0]
			file_extension = os.path.splitext(filepath)[1]
			file_extension = file_extension.lower()
			mimetype, _ = mimetypes.guess_type(filename)
			uploadfilename = str(datetime.datetime.now().timestamp()) + file_extension
			if not mimetype:
				mimetype = 'application/octet-stream'
			try:
				with open(filepath,'rb') as file:
					content = file.read()
				self.headers['Content-Type'] = mimetype
				bmobResult =  BmobRequest(url = self.domain + f'/2/files/{uploadfilename}', method = 'POST', headers = self.headers,body=content,encode=False)
				self.headers['Content-Type'] = 'application/json'
				self.error = bmobResult.getError()
				if self.error['error'] is None:
					cdn = BmobDict(bmobResult.jsonData)
					print(bmobResult.jsonData)
					return BmobFile(cdn.url,filename + file_extension)
				print(f'上传失败，原因：{self.error["error"]} 错误码：{self.error["code"]}')
				return None
			except Exception as e:
				self.headers['Content-Type'] = 'application/json'
				print(f'发生异常:{e}')
				return False
		else:
			print('找不到对应的文件')
			return None

	def delFile(self,url):
		"""删除文件

		Args:
			url (str): 要删除的文件的url

		Returns:
			bool: 是否删除成功.
		"""		
		path = urlparse(url).path
		bmobResult =  BmobRequest(url = self.domain + f'/2/files/upyun{path}', method = 'DELETE', headers = self.headers)
		self.error = bmobResult.getError()
		return dealBmobResult(bmobResult,'删除文件')