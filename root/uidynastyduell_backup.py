###################################################################
# title_name		: Dynasty Duell System
# date_created		: 19.03.2020
# filename			: uidynastyduell.py
# author			: Cesar
#
import ui, event, player, time, net, chat, chr, item, uiToolTip, localeInfo

# Configuration

#	Duration how long the status should be displayed (default: 5.0 sec)
duration = 5.0
item_vnum = 50204

FACE_IMAGE_DICT = {
	0	:	['d:/ymir work/ui/dynastyduellsys/line/warrior_m.tga',	'd:/ymir work/ui/dynastyduellsys/line/warrior_w.tga'],
	1	:	['d:/ymir work/ui/dynastyduellsys/line/assassin_m.tga',	'd:/ymir work/ui/dynastyduellsys/line/assassin_w.tga'],
	2	:	['d:/ymir work/ui/dynastyduellsys/line/sura_m.tga',		'd:/ymir work/ui/dynastyduellsys/line/sura_w.tga'],
	3	:	['d:/ymir work/ui/dynastyduellsys/line/shaman_m.tga',		'd:/ymir work/ui/dynastyduellsys/line/shaman_w.tga'],
	4	:	['d:/ymir work/ui/dynastyduellsys/line/lykaner.tga'],
}

#self.childFace.LoadImage(FACE_IMAGE_DICT[iJob][iSex])

## Sidebar Screen
class DynastyDuellText(ui.ScriptWindow):
	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def __init__(self, szName, szString, iDuration, iJob, iSex, iPosition):
		ui.ScriptWindow.__init__(self)
		self.__LoadWindow()
		self.configureChilds(szName, szString, iJob, iSex, iPosition)
		
		self.Show()
		self.SetTop()
		
		self.WarteSchleife = WaitingDialog()
		self.WarteSchleife.Open(iDuration)
		self.WarteSchleife.SAFE_SetTimeOverEvent(self.Close)
		
	def __LoadWindow(self):
		try:
			PythonScriptLoader01 = ui.PythonScriptLoader()
			PythonScriptLoader01.LoadScriptFile(self, "UIScript/dynastyduelltext.py")
		except:
			import exception
			exception.Abort("DynastyDuell.LoadWindow.PythonScriptLoader")
			
		try:
			self.childName = self.GetChild("Player_Name")
			self.childText = self.GetChild("Status_Text")
			self.childFace = self.GetChild("faceIMG")
		except:
			import exception
			exception.Abort("DynastyDuell.LoadWindow.GetChild")
			
	def configureChilds(self, szName, szString, iJob, iSex, iPosition):
		self.childName.SetText(szName + ":")
		self.childText.SetText(szString)
		self.childFace.LoadImage(FACE_IMAGE_DICT[iJob][iSex])

		if iPosition == 2:
			self.x, self.y = self.GetGlobalPosition()
			self.SetPosition(self.x, (self.y/ 2) + 175)
			
		if iJob == 1:
			self.childFace.SetPosition(35, 47)
		elif iJob == 2:
			self.childFace.SetPosition(30, 50)
		elif iJob == 3:
			self.childFace.SetPosition(18, 50) 
		elif iJob == 4:
			self.childFace.SetPosition(37, 50)
		elif iJob == 5:
			self.childFace.SetPosition(45, 40)
		elif iJob == 6:
			self.childFace.SetPosition(30, 33)
		elif iJob == 7:
			self.childFace.SetPosition(55, 65)

	def Close(self):
		DynastyDuellWindow.iNumber -= 1
		self.Hide()
		
	def Destroy(self):
		self.Hide()
		self.Close()
		
## Main GUI
class DynastyDuellWindow(ui.ScriptWindow):
	iNumber = 0

	def __del__(self):
		ui.ScriptWindow.__del__(self)
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isLoaded = FALSE
		
		if FALSE == self.isLoaded:
			self.__LoadWindow()
		
	def __OnOverInItem(self):
		if self.toolTip:
			self.toolTip.SetItemToolTip(item_vnum)
			self.toolTip.ShowToolTip()

	def __OnOverOutItem(self):
		if self.toolTip:
			self.toolTip.HideToolTip()
		
	def __LoadWindow(self):
	
		try:
			ui.PythonScriptLoader().LoadScriptFile(self, "UIScript/dynastyduellwindow.py")
		except:
			import exception
			exception.Abort("uidynastyduell.__LoadWindow.LoadScript")
			
		try:
			GetObject=self.GetChild
			GetObject("chooseButton").SetEvent(lambda arg=0: self.Button(arg))
			GetObject("previewButton").SetEvent(lambda arg=1: self.Button(arg))
			GetObject("cancelButton").SetEvent(ui.__mem_func__(self.Close))
			GetObject("Titlebar_Close").SetEvent(ui.__mem_func__(self.Close))
			
			self.slot = GetObject("ItemSlot")
			self.inputValue = GetObject("InputValue")
			self.board = GetObject("Board")
		except:
			import exception
			exception.Abort("uidynastyduell.__LoadWindow.BindObject")
		
		self.toolTip = uiToolTip.ItemToolTip()
		self.toolTip.Hide()
		
		self.slot.SetItemSlot(0, item_vnum)
		self.slot.SetOverInItemEvent(ui.__mem_func__(self.__OnOverInItem))
		self.slot.SetOverOutItemEvent(ui.__mem_func__(self.__OnOverOutItem))
		
		self.board.OnPressEscapeKey = ui.__mem_func__(self.OnPressEscapeKey)

		self.isLoaded = True
		
	def Open(self):
		if self.isLoaded == FALSE:
			self.__LoadWindow()
			
		self.SetCenterPosition()
		self.SetTop()

		self.inputValue.SetText(self.readFile())
		self.Show()
			
	def Button(self, arg):
	
		# Button Choose
		if arg == 0:
			inputText = self.inputValue.GetText()
			if len(inputText) > 0:
				# insult filter from locale
				if net.IsInsultIn(inputText):
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.CHAT_INSULT_STRING)
					return
			
				self.saveFile(inputText)
				self.Close()
				
				net.SendDynastyStatusString(inputText) # Send to Client -> Game
			else:
				chat.AppendChat(chat.CHAT_TYPE_INFO, "DynastyDuell: no input")
			
		# Button Preview
		elif arg == 1:
			inputText = self.inputValue.GetText()
			
			# If value in inputField then preview
			if len(inputText) > 0:
				# insult filter from locale
				if net.IsInsultIn(inputText):
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.CHAT_INSULT_STRING)
					return
					
				self.ShowPlayer(inputText, player.GetName(), self.GetRealRace(), self.getSex(player.GetRace()))
			else:
				chat.AppendChat(chat.CHAT_TYPE_INFO, "DynastyDuell: no input")
			
	## Show attacker->szString to Player
	def ShowPlayer(self, szString, szName, iJob, iSex):
		chat.AppendChat(chat.CHAT_TYPE_INFO, "iNumber = %d" % DynastyDuellWindow.iNumber)

		if not (DynastyDuellWindow.iNumber > 1):
			self.hwnd = DynastyDuellText(szName, szString, duration, iJob, iSex, 1)
			DynastyDuellWindow.iNumber = 2
		else:
			self.hwnd2 = DynastyDuellText(szName, szString, duration, iJob, iSex, 2)
			DynastyDuellWindow.iNumber = 1
			
	def saveFile(self, szString):
		f = open("dynasty.cfg", "w")
		f.write(szString)
		
	def readFile(self):
		try:
			f = open("dynasty.cfg")
			data = f.readline()
			return str(data)
		except:
			import exception
			exception.Abort("DynastyDuell.readFile")
			
	# Get Race
	def GetRealRace(self):
		race = player.GetRace()
		if race >= 4: # at raceNum 4 = warrior female
			return race-4
		else:
			return race
			
	# Get male or female
	def getSex(self, race):
		sex = chr.RaceToSex(race)
		if sex == 1:
			return 0 # male
		else:
			return 1 # female

	def Close(self):
		self.Hide()
		
	def Destroy(self):
		self.Close()
		self.isLoaded = FALSE
		self.board = 0
		self.inputValue = 0
		self.toolTip = 0
		self.slot = 0
		
	def OnPressExitKey(self):
		self.Close()
		return TRUE

	def OnPressEscapeKey(self):
		chat.AppendChat(chat.CHAT_TYPE_INFO, "DynastyDuell: ESC")
		self.Close()
		return TRUE
		
## Waiting loops
class WaitingDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.eventTimeOver = lambda *arg: None
		self.eventExit = lambda *arg: None

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Open(self, waitTime):
		curTime = time.clock()
		self.endTime = curTime + waitTime
		self.Show()

	def Close(self):
		self.Hide()

	def Destroy(self):
		self.Hide()

	def SAFE_SetTimeOverEvent(self, event):
		self.eventTimeOver = ui.__mem_func__(event)

	def SAFE_SetExitEvent(self, event):
		self.eventExit = ui.__mem_func__(event)
		
	def OnUpdate(self):
		lastTime = max(0, self.endTime - time.clock())
		if 0 == lastTime:
			self.Close()
			self.eventTimeOver()
		else:
			return
		
wnd = DynastyDuellWindow()
