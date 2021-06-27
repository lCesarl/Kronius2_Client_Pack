import ui, player, time, net, chat, chr, uiToolTip, localeInfo, exception, constInfo

config = {
	'duration': 5.0,
	'itemVnum': 50204,
	'faces': [
		[
			'd:/ymir work/ui/dynastyduellsys/line/warrior_m.tga',
			'd:/ymir work/ui/dynastyduellsys/line/warrior_w.tga',
		],
		[
			'd:/ymir work/ui/dynastyduellsys/line/assassin_m.tga',
			'd:/ymir work/ui/dynastyduellsys/line/assassin_w.tga',
		],
		[
			'd:/ymir work/ui/dynastyduellsys/line/sura_m.tga',
			'd:/ymir work/ui/dynastyduellsys/line/sura_w.tga',
		],
		[
			'd:/ymir work/ui/dynastyduellsys/line/shaman_m.tga',
			'd:/ymir work/ui/dynastyduellsys/line/shaman_w.tga',
		],
		[
			'd:/ymir work/ui/dynastyduellsys/line/lykaner.tga',
		],
	],
	'positions': [
		[0, 0],
		[35, 47],
		[30, 50],
		[18, 50],
		[37, 50],
		[45, 40],
		[30, 33],
		[55, 65],
	]
}

class DynastyDuellText(ui.ScriptWindow):
	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def __init__(self, szName, szString, iDuration, iJob, iSex, iPosition):
		ui.ScriptWindow.__init__(self)
		self.loadWindow()
		self.displayDynasty(szName, szString, iJob, iSex, iPosition)

		self.Show()
		self.SetTop()

		self.WarteSchleife = WaitingDialog()
		self.WarteSchleife.Open(iDuration)
		self.WarteSchleife.SAFE_SetTimeOverEvent(self.close)
	
	def close(self):
		constInfo.DYNASTY_COUNT -= 1
		self.__del__()

	def displayDynasty(self, szName, szString, iJob, iSex, iPosition):
		chat.AppendChat(8, str(iJob))
		chat.AppendChat(8, str(iSex))
		self.childName.SetText(szName + ":")
		self.childText.SetText(szString)
		self.childFace.LoadImage(config["faces"][iJob][iSex])

		self.x, self.y = self.GetGlobalPosition()
		self.SetPosition(self.x, self.y - (175 * (iPosition -1)))

		data = config["positions"][iJob]
		self.childFace.SetPosition(data[0], data[1])
	
	def loadWindow(self):
		try:
			ui.PythonScriptLoader().LoadScriptFile(self, "UIScript/dynastyduelltext.py")

			self.childName = self.GetChild("Player_Name")
			self.childText = self.GetChild("Status_Text")
			self.childFace = self.GetChild("faceIMG")
		except Exception as e:
			exception.Abort(constInfo.getLogText(e))

class DynastyDuellWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.windows = []
		self.loadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
	
	def toggle(self):
		if self.IsShow():
			self.Hide()
		else:
			self.SetCenterPosition()
			self.SetTop()
			self.Show()
	
	def toggleToolTip(self):
		if self.toolTip:
			if self.toolTip.IsShow():
				self.toolTip.HideToolTip()
			else:
				self.toolTip.ShowToolTip()
	
	def __OnOverInItem(self):
		if self.toolTip:
			self.toolTip.SetItemToolTip(item_vnum)
			self.toolTip.ShowToolTip()

	def __OnOverOutItem(self):
		if self.toolTip:
			self.toolTip.HideToolTip()
	
	def choose(self):
		inputText = self.inputValue.GetText()
		if len(inputText) > 0:
			if net.IsInsultIn(inputText):
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.CHAT_INSULT_STRING)
				return
			self.toggle()
			net.SendDynastyStatusString(inputText)
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "DynastyDuell: no input")
			
	def preview(self):
		inputText = self.inputValue.GetText()
		if len(inputText) > 0:
			if net.IsInsultIn(inputText):
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.CHAT_INSULT_STRING)
				return
			self.showPlayer(inputText, player.GetName(), self.getRealRace(), self.getSex(player.GetRace()))
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "DynastyDuell: no input")
	
	def loadWindow(self):
		try:
			ui.PythonScriptLoader().LoadScriptFile(self, "UIScript/dynastyduellwindow.py")

			self.GetChild("chooseButton").SetEvent(ui.__mem_func__(self.choose))
			self.GetChild("previewButton").SetEvent((ui.__mem_func__(self.preview)))
			self.GetChild("Titlebar_Close").SetEvent(ui.__mem_func__(self.toggle))

			self.slot = self.GetChild("ItemSlot")
			self.inputValue = self.GetChild("InputValue")
			self.board = self.GetChild("Board")
		
			self.toolTip = uiToolTip.ItemToolTip()
			self.toolTip.SetItemToolTip(config["itemVnum"])
			self.toolTip.Hide()

			self.slot.SetItemSlot(0, config["itemVnum"])

			self.slot.SetOverInItemEvent(ui.__mem_func__(self.__OnOverInItem))
			self.slot.SetOverOutItemEvent(ui.__mem_func__(self.__OnOverOutItem))
			self.board.OnPressEscapeKey = ui.__mem_func__(self.toggle)
		except Exception as e:
			exception.Abort(constInfo.getLogText(e))
	
	def showPlayer(self, szString, szName, iJob, iSex):
		constInfo.DYNASTY_COUNT += 1
		self.windows.append(DynastyDuellText(szName, szString, config["duration"], iJob, iSex, constInfo.DYNASTY_COUNT))
	
	def getRealRace(self):
		race = player.GetRace()
		return race if race < 5 else race - 4
			
	def getSex(self, race):
		return not chr.RaceToSex(race)

	def destroy(self):
		self.Hide()
		self.board = 0
		self.inputValue = 0
		self.toolTip = 0
		self.slot = 0
		self.__del__()
	
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