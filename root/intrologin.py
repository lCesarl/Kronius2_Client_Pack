######################################## AICI INCEPE TREABA ######################################## ORA: 21:36
import app, net, ui, snd, wndMgr, dbg, os
import musicInfo, systemSetting
import constinfo, uiScriptLocale, uicommon
import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()
import ime
import serverInfo
import serverCommandParser
import time
import ServerStateChecker
import serverlogindata

if app.ENABLE_LOGIN_PIN_SYSTEM:
	import uiCommon
from _weakref import proxy

class LoginWindow(ui.ScriptWindow):
	def __init__(self, stream):
		ui.ScriptWindow.__init__(self)
		
		self.lang = [
			["Deutsch", "uiScriptLocale.UI_CHANGER_BUTTON_YUMANO3"],
			["English", "uiScriptLocale.UI_CHANGER_BUTTON_CLASSIC"],
		]
		
		net.SetPhaseWindow(net.PHASE_WINDOW_LOGIN, self)
		net.SetAccountConnectorHandler(self)

		self.AccountManager = [
									[None, None, None, None],
									[None, None, None, None],
									[None, None, None, None],
									[None, None, None, None],
									[None, None, None, None],
									[None, None, None, None],
								]
		self.AccountManagerData	= [
								["", ""],
								["", ""],
								["", ""],
								["", ""],
								["", ""],
								["", ""],
							  	]

		if app.ENABLE_LOGIN_PIN_SYSTEM:
			self.user_id = None
			self.user_pwd = None
			self.bReady = 0

		self.stateCH = [None, None, None, None, None, None]
		self.SelectedChannel = [None, None, None, None, None, None]
		self.stream = stream
		self.isDown = False
		
	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
		net.ClearPhaseWindow(net.PHASE_WINDOW_LOGIN, self)
		net.SetAccountConnectorHandler(0)

	def LoadAccountData(self):
		with open('account.cfg', 'r') as content_file:
			encContent = content_file.read()
			content = app.DecryptByHWID(encContent)
			
			if ';' in content:
				accounts = content.split(';')
				for idx, account in enumerate(accounts):
					if ':#:' in account:
						data = account.split(':#:')
						self.AccountManagerData[idx][0] = data[0]
						self.AccountManagerData[idx][1] = data[1]

						self.AccountManager[idx][0].Show()
						self.AccountManager[idx][1].Show()
						self.AccountManager[idx][2].Hide()
		
		
		for idx, account in enumerate(self.AccountManagerData):
			if account[0] != "":
				self.AccountManager[idx][3].SetText(str(idx+1) + ". " + account[0])
			else:
				self.AccountManager[idx][0].Hide()
				self.AccountManager[idx][1].Hide()
				self.AccountManager[idx][2].Show()
				self.AccountManager[idx][3].SetText(str(idx+1) + ". " + uiScriptLocale.LOGIN_INTERFACE_FREE_SPACE)

	def SaveAccountData(self):
		with open('account.cfg', 'w+') as content_file:
			data = self.AccountManagerData[0][0] + ':#:' + self.AccountManagerData[0][1] + ';'
			data += self.AccountManagerData[1][0] + ':#:' + self.AccountManagerData[1][1] + ';'
			data += self.AccountManagerData[2][0] + ':#:' + self.AccountManagerData[2][1] + ';'
			data += self.AccountManagerData[3][0] + ':#:' + self.AccountManagerData[3][1] + ';'
			data += self.AccountManagerData[4][0] + ':#:' + self.AccountManagerData[3][1] + ';'
			data += self.AccountManagerData[5][0] + ':#:' + self.AccountManagerData[3][1] + ';'
			
			encData = app.EncryptByHWID(data)
			content_file.write(encData)

	def Open(self):
		#ServerStateChecker.Initialize()
		#ServerStateChecker.Create(self)
		#for proxy_key in serverlogindata.PROXIES:
		#	if "CH" not in proxy_key:
		#		continue
		#	index = int(proxy_key.split("CH")[1])-1
		#	channel_data = serverlogindata.PROXIES[proxy_key]
		#	ServerStateChecker.AddChannel(index, channel_data[0], channel_data[1])

		self.loginFailureMsgDict={

			"ALREADY"	: localeInfo.LOGIN_FAILURE_ALREAY,
			"NOID"		: localeInfo.LOGIN_FAILURE_NOT_EXIST_ID,
			"WRONGPWD"	: localeInfo.LOGIN_FAILURE_WRONG_PASSWORD,
			"FULL"		: localeInfo.LOGIN_FAILURE_TOO_MANY_USER,
			"SHUTDOWN"	: localeInfo.LOGIN_FAILURE_SHUTDOWN,
			"REPAIR"	: localeInfo.LOGIN_FAILURE_REPAIR_ID,
			"BLOCK"		: localeInfo.LOGIN_FAILURE_BLOCK_ID,
			"WRONGMAT"	: localeInfo.LOGIN_FAILURE_WRONG_MATRIX_CARD_NUMBER,
			"QUIT"		: localeInfo.LOGIN_FAILURE_WRONG_MATRIX_CARD_NUMBER_TRIPLE,
			"BESAMEKEY"	: localeInfo.LOGIN_FAILURE_BE_SAME_KEY,
			"NOTAVAIL"	: localeInfo.LOGIN_FAILURE_NOT_AVAIL,
			"NOBILL"	: localeInfo.LOGIN_FAILURE_NOBILL,
			"BLKLOGIN"	: localeInfo.LOGIN_FAILURE_BLOCK_LOGIN,
			"WEBBLK"	: localeInfo.LOGIN_FAILURE_WEB_BLOCK,
			"WRONGPIN"	: localeInfo.LOGIN_FAILURE_WRONGPIN, ## PINCODE
			"WRONGVER"	: localeInfo.LOGIN_FAILURE_WRONG_VERSION,
			"HWIDBAN"	: "HWID Banned",
			"WRONGHWID"	: "Your HWID does not match",
			"WARTUNG"	: localeInfo.LOGIN_FAILURE_MAINTANENCE,
			"SAFE"		: "Sicherheitsbann - Bitte melde dich im Discord!"
		}

		self.loginFailureFuncDict = {
			"WRONGPWD"	: localeInfo.LOGIN_FAILURE_WRONG_PASSWORD,
			"WRONGMAT"	: localeInfo.LOGIN_FAILURE_WRONG_MATRIX_CARD_NUMBER,
			"QUIT"		: app.Exit,
		}

		self.SetSize(wndMgr.GetScreenWidth(), wndMgr.GetScreenHeight())
		self.SetWindowName("LoginWindow")
		self.__BuildKeyDict()

		self.__LoadScript("UIScript/loginwindow.py")
		# if not self.__LoadScript(uiScriptLocale.LOCALE_UISCRIPT_PATH + "LoginWindow.py"):
			# dbg.TraceError("LoginWindow.Open - __LoadScript Error")
			# return
		
		if musicInfo.loginMusic != "":
			snd.SetMusicVolume(systemSetting.GetMusicVolume())
			snd.FadeInMusic("BGM/" + musicInfo.loginMusic)

		snd.SetSoundVolume(systemSetting.GetSoundVolume())

		ime.AddExceptKey(91)
		ime.AddExceptKey(93)
		self.SetChannel(0)

		if not os.path.exists('account.cfg'):
			self.SaveAccountData()
		
		self.LoadAccountData()
		
		self.Show()
		app.ShowCursor()	

		if app.ENABLE_MULTI_LANGUAGE_SYSTEM:
			localeName = app.GetLoca()
			for i, k in constinfo.LOCALE_LANG_DICT.items():
				if localeName in constinfo.LOCALE_LANG_DICT[i]["locale"]:
					net.SetLanguage(i)
					break

	def Close(self):
		self.serverList					= None
		self.channelList				= None
		self.onPressKeyDict 			= None

		self.AccountManager = [
									[None, None, None, None],
									[None, None, None, None],
									[None, None, None, None],
									[None, None, None, None],
									[None, None, None, None],
									[None, None, None, None],
								]
		self.AccountManagerData	= None
		self.stateCH = [None, None, None, None, None, None]
		self.SelectedChannel = [None, None, None, None, None, None]

		if app.ENABLE_LOGIN_PIN_SYSTEM:
			self.user_id = None
			self.user_pwd = None
			self.bReady = 0

		if musicInfo.loginMusic != "" and musicInfo.selectMusic != "":
			snd.FadeOutMusic("BGM/"+musicInfo.loginMusic)
	
		if self.stream.popupWindow:
			self.stream.popupWindow.Close()
	
		self.Hide()
		app.HideCursor()
		ime.ClearExceptKey()

	def __BuildKeyDict(self):
		onPressKeyDict = {}

		onPressKeyDict[app.DIK_F1]	= lambda : self.loginWithHotkey(1)
		onPressKeyDict[app.DIK_F2]	= lambda : self.loginWithHotkey(2)
		onPressKeyDict[app.DIK_F3]	= lambda : self.loginWithHotkey(3)
		onPressKeyDict[app.DIK_F4]	= lambda : self.loginWithHotkey(4)
		onPressKeyDict[app.DIK_F5]	= lambda : self.loginWithHotkey(5)
		onPressKeyDict[app.DIK_F6]	= lambda : self.loginWithHotkey(6)

		self.onPressKeyDict = onPressKeyDict

	def OnKeyDown(self, key):
		try:
			self.onPressKeyDict[key]()
		except KeyError:
			pass
		except:
			raise

		return TRUE

	def OnConnectFailure(self):
		snd.PlaySound("sound/ui/loginfail.wav")
		self.PopupNotifyMessage(localeInfo.LOGIN_CONNECT_FAILURE, self.EmptyFunc)

	def OnHandShake(self):
		snd.PlaySound("sound/ui/loginok.wav")
		self.PopupDisplayMessage(localeInfo.LOGIN_CONNECT_SUCCESS)

	def OnLoginStart(self):
		self.PopupDisplayMessage(localeInfo.LOGIN_PROCESSING)

	def OnLoginFailure(self, error):
		ServerStateChecker.Request()
		try:
			loginFailureMsg = self.loginFailureMsgDict[error]
		except KeyError:
		
			loginFailureMsg = localeInfo.LOGIN_FAILURE_UNKNOWN  + error

		loginFailureFunc = self.loginFailureFuncDict.get(error, self.EmptyFunc)

		self.PopupNotifyMessage(loginFailureMsg, loginFailureFunc)

		snd.PlaySound("sound/ui/loginfail.wav")

	def __LoadScript(self, fileName):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, fileName)
		except:
			import exception
			exception.Abort("LoginWindow.__LoadScript.LoadObject")

		try:
			self.idEditLine			= self.GetChild("id")
			self.pwdEditLine		= self.GetChild("pwd")

			self.stateCH[0]			= self.GetChild("channel1_status")
			self.stateCH[1]			= self.GetChild("channel2_status")
			self.stateCH[2]			= self.GetChild("channel3_status")
			self.stateCH[3]			= self.GetChild("channel4_status")
			self.stateCH[4]			= self.GetChild("channel5_status")
			self.stateCH[5]			= self.GetChild("channel6_status")
				
			self.stateCH[0].SetFontColor(106.0 / 255.0, 209.0 / 255.0, 65.0 / 255.0)
			self.stateCH[1].SetFontColor(106.0 / 255.0, 209.0 / 255.0, 65.0 / 255.0)
			self.stateCH[2].SetFontColor(106.0 / 255.0, 209.0 / 255.0, 65.0 / 255.0)
			self.stateCH[3].SetFontColor(106.0 / 255.0, 209.0 / 255.0, 65.0 / 255.0)

			self.loginButton		= self.GetChild("login_button")
			#self.exitButton			= self.GetChild("exit_button")

			"""self.homepageButton		= self.GetChild("homepage_button")
			self.registerButton		= self.GetChild("register_button")
			self.forumButton		= self.GetChild("forum_button")
			self.changelogButton	= self.GetChild("changelog_button")"""

			self.language_de		= self.GetChild("lang_de_button")
			self.language_en		= self.GetChild("lang_en_button")

			self.AccountManager[0][0]	= self.GetChild("saved_accs_acc1_use")
			self.AccountManager[0][1]	= self.GetChild("saved_accs_acc1_del")
			self.AccountManager[0][2]	= self.GetChild("save_acc1")
			self.AccountManager[0][3]	= self.GetChild("saved_accs_acc1")

			self.AccountManager[1][0]	= self.GetChild("saved_accs_acc2_use")
			self.AccountManager[1][1]	= self.GetChild("saved_accs_acc2_del")
			self.AccountManager[1][2]	= self.GetChild("save_acc2")
			self.AccountManager[1][3]	= self.GetChild("saved_accs_acc2")

			self.AccountManager[2][0]	= self.GetChild("saved_accs_acc3_use")
			self.AccountManager[2][1]	= self.GetChild("saved_accs_acc3_del")
			self.AccountManager[2][2]	= self.GetChild("save_acc3")
			self.AccountManager[2][3]	= self.GetChild("saved_accs_acc3")

			self.AccountManager[3][0]	= self.GetChild("saved_accs_acc4_use")
			self.AccountManager[3][1]	= self.GetChild("saved_accs_acc4_del")
			self.AccountManager[3][2]	= self.GetChild("save_acc4")
			self.AccountManager[3][3]	= self.GetChild("saved_accs_acc4")

			self.AccountManager[4][0]	= self.GetChild("saved_accs_acc5_use")
			self.AccountManager[4][1]	= self.GetChild("saved_accs_acc5_del")
			self.AccountManager[4][2]	= self.GetChild("save_acc5")
			self.AccountManager[4][3]	= self.GetChild("saved_accs_acc5")

			self.AccountManager[5][0]	= self.GetChild("saved_accs_acc6_use")
			self.AccountManager[5][1]	= self.GetChild("saved_accs_acc6_del")
			self.AccountManager[5][2]	= self.GetChild("save_acc6")
			self.AccountManager[5][3]	= self.GetChild("saved_accs_acc6")

			self.SelectedChannel[0]	= self.GetChild("selected_channel1")
			self.SelectedChannel[1]	= self.GetChild("selected_channel2")
			self.SelectedChannel[2]	= self.GetChild("selected_channel3")
			self.SelectedChannel[3]	= self.GetChild("selected_channel4")
			self.SelectedChannel[4]	= self.GetChild("selected_channel5")
			self.SelectedChannel[5]	= self.GetChild("selected_channel6")
			
			self.channelButton = {
				0 : self.GetChild("ch1"),
				1 :	self.GetChild("ch2"),
				2 : self.GetChild("ch3"),
				3 : self.GetChild("ch4")}

			self.selectLabel = self.GetChild("ServerSelectLabel")
			self.buttonLive = self.GetChild("SERVER_LIVE_BUTTON")
			self.buttonDEV = self.GetChild("SERVER_TEST_BUTTON")
			self.buttonLocal = self.GetChild("SERVER_LOCAL_BUTTON")
			self.buttonLive.Down()
		except:
			import exception
			exception.Abort("LoginWindow.__LoadScript.BindObject")
			
		if not (constinfo.bIsDEV):
			self.selectLabel.Hide()
			self.buttonLive.Hide()
			self.buttonDEV.Hide()
			self.buttonLocal.Hide()
				
		for (channelID, channelButtons) in self.channelButton.items():
				channelButtons.SetEvent(ui.__mem_func__(self.SetChannel), channelID)
		
		self.loginButton.SetEvent(ui.__mem_func__(self.__OnClickLoginButton))
		#self.exitButton.SetEvent(ui.__mem_func__(self.OnPressExitKey))

		"""self.homepageButton.SetEvent(ui.__mem_func__(self.GoHomepage))
		self.registerButton.SetEvent(ui.__mem_func__(self.GoRegister))
		self.forumButton.SetEvent(ui.__mem_func__(self.GoForum))
		self.changelogButton.SetEvent(ui.__mem_func__(self.GoChangelog))"""

		self.language_de.SetEvent(ui.__mem_func__(self.__AskChangeLangDE))
		self.language_en.SetEvent(ui.__mem_func__(self.__AskChangeLangEN))

		self.idEditLine.SetReturnEvent(ui.__mem_func__(self.pwdEditLine.SetFocus))
		self.idEditLine.SetTabEvent(ui.__mem_func__(self.pwdEditLine.SetFocus))
		self.pwdEditLine.SetReturnEvent(ui.__mem_func__(self.__OnClickLoginButton))
		self.pwdEditLine.SetTabEvent(ui.__mem_func__(self.idEditLine.SetFocus))
		self.idEditLine.SetFocus()

		self.AccountManager[0][0].SetEvent(lambda:ui.__mem_func__(self.loginWithHotkey)(0+1))
		self.AccountManager[1][0].SetEvent(lambda:ui.__mem_func__(self.loginWithHotkey)(1+1))
		self.AccountManager[2][0].SetEvent(lambda:ui.__mem_func__(self.loginWithHotkey)(2+1))
		self.AccountManager[3][0].SetEvent(lambda:ui.__mem_func__(self.loginWithHotkey)(3+1))
		self.AccountManager[4][0].SetEvent(lambda:ui.__mem_func__(self.loginWithHotkey)(4+1))
		self.AccountManager[5][0].SetEvent(lambda:ui.__mem_func__(self.loginWithHotkey)(5+1))

		self.AccountManager[0][1].SetEvent(lambda:ui.__mem_func__(self.__OnClickAccountErase)(0))
		self.AccountManager[1][1].SetEvent(lambda:ui.__mem_func__(self.__OnClickAccountErase)(1))
		self.AccountManager[2][1].SetEvent(lambda:ui.__mem_func__(self.__OnClickAccountErase)(2))
		self.AccountManager[3][1].SetEvent(lambda:ui.__mem_func__(self.__OnClickAccountErase)(3))
		self.AccountManager[4][1].SetEvent(lambda:ui.__mem_func__(self.__OnClickAccountErase)(4))
		self.AccountManager[5][1].SetEvent(lambda:ui.__mem_func__(self.__OnClickAccountErase)(5))

		self.AccountManager[0][2].SetEvent(lambda:ui.__mem_func__(self.__OnClickAccountSave)(0))
		self.AccountManager[1][2].SetEvent(lambda:ui.__mem_func__(self.__OnClickAccountSave)(1))
		self.AccountManager[2][2].SetEvent(lambda:ui.__mem_func__(self.__OnClickAccountSave)(2))
		self.AccountManager[3][2].SetEvent(lambda:ui.__mem_func__(self.__OnClickAccountSave)(3))
		self.AccountManager[4][2].SetEvent(lambda:ui.__mem_func__(self.__OnClickAccountSave)(4))
		self.AccountManager[5][2].SetEvent(lambda:ui.__mem_func__(self.__OnClickAccountSave)(5))

		if (constinfo.bIsDEV):
			self.buttonLive.SetEvent(lambda:ui.__mem_func__(self.__OnClickServerSelectButton)(0))
			self.buttonDEV.SetEvent(lambda:ui.__mem_func__(self.__OnClickServerSelectButton)(1))
			self.buttonLocal.SetEvent(lambda:ui.__mem_func__(self.__OnClickServerSelectButton)(2))

		for i in range(len(self.AccountManager)):
			self.AccountManager[i][0].Hide()
			self.AccountManager[i][1].Hide()

		"""for i in range(len(self.stateCH)):
			self.stateCH[i].SetFontColor(176.0 / 255.0, 21.0 / 255.0, 21.0 / 255.0)"""
		
	def OnUpdate(self):
		ServerStateChecker.Update()
		
	def SetChannel(self, ch):
		for key, button in self.channelButton.items():
			button.SetUp()

		for i in range(6):
			self.SelectedChannel[i].Hide()
		self.SelectedChannel[ch].Show()
			
		self.channelButton[ch].Down()
		ch += 1

		ip = self.GetData(ch)[0]
		login = self.GetData("LOGIN")[1]

		if (constinfo.bIsDEV):
			if (self.buttonLive.IsDown()):
				self.stream.SetConnectInfo(self.GetData(ch)[0], self.GetData(ch)[1], self.GetData(ch)[0], self.GetData("LOGIN")[1])
			elif (self.buttonDEV.IsDown()):
				self.stream.SetConnectInfo(serverlogindata.TEST_SRV, self.GetData(ch)[1], serverlogindata.TEST_SRV, self.GetData("LOGIN")[1])
			elif (self.buttonLocal.IsDown()):
				self.stream.SetConnectInfo(serverlogindata.LOCAL_SRV, self.GetData(ch)[1], serverlogindata.LOCAL_SRV, self.GetData("LOGIN")[1])
		else:
			self.stream.SetConnectInfo(self.GetData(ch)[0], self.GetData(ch)[1], self.GetData(ch)[0], self.GetData("LOGIN")[1])

		net.SetMarkServer(self.GetData(1)[0], self.GetData(1)[1])
		app.SetGuildMarkPath("10.tga")
		app.SetGuildSymbolPath("10")

		
		text = "Channel %d" % ch
		if (ch == 4):
			text + " PVM"
		net.SetServerInfo(text)

		file=open("channel.inf", "w")
		file.write("%d %d %d" % (self.__GetServerID(), ch, self.__GetRegionID()))
		file.close()
		
	def GetData(self, token):
		return serverlogindata.PROXIES["CH%s" % token if token != "LOGIN" else token]

	if app.ENABLE_LOGIN_PIN_SYSTEM:
		def Connect(self, id, pwd, pincode):

			if constinfo.SEQUENCE_PACKET_ENABLE:
				net.SetPacketSequenceMode()

			self.stream.popupWindow.Close()
			self.stream.popupWindow.Open(localeInfo.LOGIN_CONNETING, self.EmptyFunc, localeInfo.UI_CANCEL)

			self.stream.SetLoginInfo(id, pwd, pincode)
			self.stream.Connect()
	else:
		def Connect(self, id, pwd):
			if constinfo.SEQUENCE_PACKET_ENABLE:
				net.SetPacketSequenceMode()
				
			constinfo.LastAccount = id.lower()

			self.stream.popupWindow.Close()
			self.stream.popupWindow.Open(localeInfo.LOGIN_CONNETING, self.EmptyFunc, localeInfo.UI_CANCEL)

			self.stream.SetLoginInfo(id, pwd)
			self.stream.Connect()
		
	def PopupDisplayMessage(self, msg):
		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(msg)

	def PopupNotifyMessage(self, msg, func=0):
		if not func:
			func = self.EmptyFunc

		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(msg, func, localeInfo.UI_OK)

	def OnPressExitKey(self):
		if self.stream.popupWindow:
			self.stream.popupWindow.Close()
		self.stream.SetPhaseWindow(0)
		return TRUE

	def __GetRegionID(self):
		return 0

	def __GetServerID(self):
		return 0

	def __GetChannelID(self):
		return self.channelList.GetSelectedItem()

## SERVER STATE CHECKER

	# This is called by the native code state-checker
	def NotifyChannelState(self, key, state):
		serverlogindata.SERVER_STATE_TABLE[key] = state

		serverIndex = self.__GetServerID()
		if (key / 10) == serverIndex:
			try:
				stateName = serverlogindata.STATE_DICT[state]
				stateNameText = serverlogindata.STATE_TEXT_DICT[state]
			except:
				stateName = serverlogindata.STATE_NONE
				stateNameText = serverlogindata.STATE_TEXT_NONE

			channelIndex = key % 10
			channelName = "Test"
			print "LoginWindow::NotifyChannelState(key=%d, state=%d): serverIndex=%d, channelIndex=%d, channelName=%s, stateName=%s" % (key, state, serverIndex, channelIndex, channelName, stateName)

			"""self.stateCH[channelIndex].SetText(str(stateNameText))
			if state > 0:
				self.stateCH[channelIndex].SetFontColor(106.0 / 255.0, 209.0 / 255.0, 65.0 / 255.0)
			else:
				self.stateCH[channelIndex].SetFontColor(176.0 / 255.0, 21.0 / 255.0, 21.0 / 255.0)"""

## ACCSAVE System ##
	"""def __OnClickEditButton(self, arg):
		if arg == 0:
			for i in range(len(self.AccountManagerData)):
				if self.AccountManagerData[i][0] != "":
					self.AccountManager[i][1].Show()
		else:
			for i in range(len(self.AccountManager)):
				self.AccountManager[i][1].Hide()"""

	if (constinfo.bIsDEV):
		def __OnClickServerSelectButton(self, parameter):

			if (parameter == 0):
				self.buttonLive.Down()
				self.buttonDEV.SetUp()
				self.buttonLocal.SetUp()

				constinfo.SERVER_LIVE = True
				constinfo.SERVER_DEV = False
				constinfo.SERVER_LOCAL = False
			if (parameter == 1):
				self.buttonDEV.Down()
				self.buttonLocal.SetUp()
				self.buttonLive.SetUp()

				constinfo.SERVER_DEV = True
				constinfo.SERVER_LOCAL = False
				constinfo.SERVER_LIVE = False
			if (parameter == 2):
				self.buttonLocal.Down()
				self.buttonLive.SetUp()
				self.buttonDEV.SetUp()

				constinfo.SERVER_LOCAL = True
				constinfo.SERVER_LIVE = False
				constinfo.SERVER_DEV = False

			self.SetChannel(0)

	def __OnClickAccountSave(self, idx):

		if self.AccountManagerData[idx][0] == "":
			id = self.idEditLine.GetText()
			pwd = self.pwdEditLine.GetText()
			
			if id == "" or pwd == "":
				return

			self.AccountManagerData[idx][0] = id
			self.AccountManagerData[idx][1] = pwd
			self.SaveAccountData()

			self.AccountManager[idx][0].Show()
			self.AccountManager[idx][1].Show()
			self.AccountManager[idx][2].Hide()
			self.AccountManager[idx][3].SetText(str(idx+1) + ". " + id)

	def __OnClickAccountErase(self, idx):
		self.questionDialog = uiCommon.QuestionDialog()
		self.questionDialog.SetText(localeInfo.REALLY_WANNA_DELETE_ACCOUNT_DATA) #translateme
		self.questionDialog.SetAcceptEvent(lambda arg=idx: self.OnDelAccAcceptEvent(arg))
		self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnDelAccQuestionCancel))
		self.questionDialog.Open()
		constinfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)
		
	def OnDelAccAcceptEvent(self, idx):
		self.OnCloseQuestionDialog()
		self.AccountManagerData[idx][0] = ""
		self.AccountManagerData[idx][1] = ""
		
		self.AccountManager[idx][0].Hide()
		self.AccountManager[idx][1].Hide()
		self.AccountManager[idx][2].Show()
		self.AccountManager[idx][3].SetText(str(idx+1) + ". " + uiScriptLocale.LOGIN_INTERFACE_FREE_SPACE)

		self.SaveAccountData()
		
	def OnDelAccQuestionCancel(self):
		self.OnCloseQuestionDialog()
		
	def OnCloseQuestionDialog(self):
		if not self.questionDialog:
			return
		
		self.questionDialog.Close()
		self.questionDialog = None
		constinfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)
#####################

## BUTTONS ##

	"""def GoHomepage(self):
		import os
		os.system('@echo off && explorer "http://yumano3.net/"')
		return TRUE

	def GoRegister(self):
		import os
		os.system('@echo off && explorer "http://yumano3.net/register"')
		return TRUE

	def GoForum(self):
		import os
		os.system('@echo off && explorer "http://board.yumano3.net/"')
		return TRUE

	def GoChangelog(self):
		import os
		os.system('@echo off && explorer "http://board.yumano3.net/forum/index.php?thread/4-patchnotes-yumano3/"')
		return TRUE"""

	def __AskChangeLangDE(self):
		self.question = uicommon.QuestionDialog()
		self.question.SetText("M�chtest du die Sprache auf Deutsch umstellen?")
		self.question.SetAcceptEvent(lambda flag=TRUE: self.AnswerChangeLangDE(flag))
		self.question.SetCancelEvent(lambda flag=FALSE: self.AnswerChangeLangDE(flag))
		self.question.Open()

	def AnswerChangeLangDE(self, flag):
		if flag:
			self.popup = uicommon.PopupDialog()
			self.popup.SetText("Dein Client wird neugstarten.")
			self.popup.SetAcceptEvent(self.__makeLanguage("de"))
			self.popup.Open()

		self.question.Close()

	def __AskChangeLangEN(self):
		self.question = uicommon.QuestionDialog()
		self.question.SetText("Do you want to change the language to English?")
		self.question.SetAcceptEvent(lambda flag=TRUE: self.AnswerChangeLangEN(flag))
		self.question.SetCancelEvent(lambda flag=FALSE: self.AnswerChangeLangEN(flag))
		self.question.Open()

	def AnswerChangeLangEN(self, flag):
		if flag:
			self.popup = uicommon.PopupDialog()
			self.popup.SetText("Your client will be closed.")
			self.popup.SetAcceptEvent(self.__makeLanguage("en"))
			self.popup.Open()

		self.question.Close()

	def __makeLanguage(self, bLanguage):
		file = open("lib/lang.cfg", "w")
		file.write(bLanguage) 
		file.close()
		if bLanguage == "en":
			file = open("locale.cfg", "w")
			file.write("10022 1252 en") 
			file.close()
		elif bLanguage == "de":
			file = open("locale.cfg", "w")
			file.write("10022 1252 de") 
			file.close()
		elif bLanguage == "pt":
			file = open("locale.cfg", "w")
			file.write("10022 1252 pt") 
			file.close()
		elif bLanguage == "es":
			file = open("locale.cfg", "w")
			file.write("10022 1252 es") 
			file.close()
		elif bLanguage == "fr":
			file = open("locale.cfg", "w")
			file.write("10022 1252 fr") 
			file.close()
		elif bLanguage == "ro":
			file = open("locale.cfg", "w")
			file.write("10022 1250 ro") 
			file.close()
		elif bLanguage == "pl":
			file = open("locale.cfg", "w")
			file.write("10022 1250 pl") 
			file.close()
		elif bLanguage == "it":
			file = open("locale.cfg", "w")
			file.write("10022 1252 it") 
			file.close()
		elif bLanguage == "cz":
			file = open("locale.cfg", "w")
			file.write("10022 1250 cz") 
			file.close()
		elif bLanguage == "hu":
			file = open("locale.cfg", "w")
			file.write("10022 1250 hu") 
			file.close()
		elif bLanguage == "tr":
			file = open("locale.cfg", "w")
			file.write("10022 1254 tr") 
			file.close()
		os.system('start Kuba2.exe')
		app.Exit()

############################

	def EmptyFunc(self):
		pass

	def __OnClickLoginButton(self):
		id = self.idEditLine.GetText()
		pwd = self.pwdEditLine.GetText()

		if len(id)==0:
			self.PopupNotifyMessage(localeInfo.LOGIN_INPUT_ID, self.EmptyFunc)
			return

		if len(pwd)==0:
			self.PopupNotifyMessage(localeInfo.LOGIN_INPUT_PASSWORD, self.EmptyFunc)
			return

		if app.ENABLE_LOGIN_PIN_SYSTEM:
			self.bReady = 0
			self.Connect(id, pwd, "")
		else:
			self.Connect(id, pwd)

	def loginWithHotkey(self, arg):
		if app.ENABLE_LOGIN_PIN_SYSTEM:
			self.user_id = self.AccountManagerData[arg-1][0]
			self.user_pwd = self.AccountManagerData[arg-1][1]
			self.bReady = 1
			self.Connect(self.AccountManagerData[arg-1][0], self.AccountManagerData[arg-1][1], "")
		else:
			self.Connect(self.AccountManagerData[arg-1][0], self.AccountManagerData[arg-1][1])

######################################
	if app.ENABLE_LOGIN_PIN_SYSTEM:
		def __OnClickConfirmPinCodeDialog(self, args):
			if not self.pincode_inputdialog:
				self.pincode_inputdialog = None
				return
		
			## ARGS => TRUE 	== PinCodeLogin
			## ARGS => FALSE 	== PinCodeRegister
			
			if args:
				if not len(self.pincode_inputdialog.GetText()):
					self.pincode_inputdialog = None
					self.PopupNotifyMessage(uiScriptLocale.PINCODE_NOINPUT)
					return
					
				if self.bReady == 0:
					self.Connect(self.idEditLine.GetText(), self.pwdEditLine.GetText(), "x " + self.pincode_inputdialog.GetText())
				else:
					self.Connect(str(self.user_id), str(self.user_pwd), "x " + self.pincode_inputdialog.GetText())
					
				self.__OnClickCancelPinCodeDialog()
			else:
				pin_text01 = self.pincode_inputdialog.GetText01()
				pin_text02 = self.pincode_inputdialog.GetText02()
				
				if not (len(pin_text01) or len(pin_text02)):
					self.pincode_inputdialog = None
					self.PopupNotifyMessage(uiScriptLocale.PINCODE_NOINPUT_BOTH)
					return
					
				if not pin_text01 == pin_text02:
					self.pincode_inputdialog = None
					self.PopupNotifyMessage(uiScriptLocale.PINCODE_INPUT_NEQUAL)
					return
					
				if self.bReady == 0:
					self.Connect(self.idEditLine.GetText(), self.pwdEditLine.GetText(), "r " + pin_text02)
				else:
					self.Connect(self.user_id, self.user_pwd, "r " + pin_text02)
					
				self.__OnClickCancelPinCodeDialog()
			
		def __OnClickCancelPinCodeDialog(self):
			self.pincode_inputdialog = None
			return TRUE
			
		def OpenPinCodeDialog(self, args):
			if args == 0:
				self.stream.popupWindow.Close()
				pincode_inputdialog = uiCommon.PinCodeDialogCreate()
				pincode_inputdialog.SetNumberMode()
				
				pincode_inputdialog.SetAcceptEvent(lambda arg=FALSE : self.__OnClickConfirmPinCodeDialog(arg))
				pincode_inputdialog.SetCancelEvent(ui.__mem_func__(self.__OnClickCancelPinCodeDialog))
				pincode_inputdialog.SetTabEvent()
				
				pincode_inputdialog.Open()
				pincode_inputdialog.SetTop()
				pincode_inputdialog.SetFocus()
				self.pincode_inputdialog = pincode_inputdialog
			elif args == 1:
				self.stream.popupWindow.Close()
				pincode_inputdialog = uiCommon.PinCodeDialog()
				pincode_inputdialog.SetNumberMode()
				pincode_inputdialog.SetSecretMode()
				
				pincode_inputdialog.SetAcceptEvent(lambda arg=TRUE : self.__OnClickConfirmPinCodeDialog(arg))
				pincode_inputdialog.SetCancelEvent(ui.__mem_func__(self.__OnClickCancelPinCodeDialog))
				
				pincode_inputdialog.Open()
				pincode_inputdialog.SetTop()
				pincode_inputdialog.SetFocus()
				self.pincode_inputdialog = pincode_inputdialog
