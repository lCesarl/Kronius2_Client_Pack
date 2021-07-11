import ServerStateChecker
import serverlogindata
import constInfo

import net
import app
import ui
import uiOption
import networkModule
import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()

class SwitchChannelDialog(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.channelButtons = []

		self.serverID = None
		self.channel = 0
		self.regionID = None
		
		self.__LoadWindow()
##	self.Open()		

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		print " -------------------------------------- DELETE SWITCH CHANNEL DIALOG"

	def Destroy(self):
		self.Close()
		self.ClearDictionary()
		print " -------------------------------------- DESTROY SWITCH CHANNEL DIALOG"	

	def OnUpdate(self):
		ServerStateChecker.Update()

	def __LoadWindow(self):
		pyScrLoader = ui.PythonScriptLoader()
		try:
			pyScrLoader.LoadScriptFile(self, "uiscript/SwitchChannelDialog.py")
		except:
			import exception
			exception.Abort("SwitchChannelDialog.__LoadDialog.LoadObject")

		file = open("channel.inf", "r")
		lines = file.readlines()
		file.close()
		
		if len(lines):
			tokens = lines[0].split()
			self.serverID = int(tokens[0])
			self.channel = int(tokens[1])
			if len(tokens) == 3:
				self.regionID = int(tokens[2])
			else:
				self.regionID = 0

	def Open(self):
		self.channelButtons = []
		try:
			GetObject=self.GetChild
			self.switchChannelBoard = GetObject("SwitchChannelBoard")
			self.blackBoard = GetObject("BlackBoard")

			self.GetChild("SwitchChannelTitle").SetCloseEvent(ui.__mem_func__(self.Close))

			for ch in range(constInfo.CHANNELS):
				btn = ui.Button()
				btn.SetUpVisual("d:/ymir work/ui/public/select_btn_01.sub")
				btn.SetOverVisual("d:/ymir work/ui/public/select_btn_02.sub")
				btn.SetDownVisual("d:/ymir work/ui/public/select_btn_03.sub")

				if (int(ch)+1 == 4):
					btn.SetText("Channel %d (PVM)" % (int(ch)+1))
				else:
					btn.SetText("Channel %d" % (int(ch)+1))

				btn.SetParent(self.blackBoard) 
				btn.SetPosition(6, 6 + (28 * (ch)))
				btn.SetEvent(ui.__mem_func__(self.__SelectChannel), ch)

				self.channelButtons.append(btn)
				self.channelButtons[ch].Show()			

			self.closeButton = ui.Button()
			self.closeButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
			self.closeButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
			self.closeButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
			self.closeButton.SetParent(self.switchChannelBoard)
			self.closeButton.SetPosition(114/2-6, 22 + (28 * (len(self.channelButtons) + 1)))
			self.closeButton.SetText(localeInfo.SWITCHCHANNEL_CANCEL)
			self.closeButton.SAFE_SetEvent(self.Close)
			self.closeButton.Show()		

			self.SetSize(190, len(self.channelButtons)* 28 + 74 + 9)	
			self.switchChannelBoard.SetSize(190, len(self.channelButtons) * 28 + 74 + 9)	
			self.blackBoard.SetSize(161, len(self.channelButtons) * 28 + 8)				
		except:
			import exception
			exception.Abort("SwitchChannelDialog.Open.BindObject")

		ui.ScriptWindow.Show(self)
				
				
	def __SelectChannel(self, channel):
		ServerStateChecker.Update()
		new_ch = int(channel)+1

		try:
			state = serverlogindata.STATE_DICT[state]
		except:
			state = serverlogindata.STATE_NONE

		if state == serverlogindata.STATE_NONE2:
			self.Popup = ui.ChannelSwitcherUI().Popup(localeInfo.SWITCHCHANNEL_CLOSED)
			return
		elif state == serverlogindata.STATE_DICT[3]:
			self.Popup = ui.ChannelSwitcherUI().Popup(localeInfo.SWITCHCHANNEL_FULL)
			return
		elif self.channel == new_ch:
			self.Popup = ui.ChannelSwitcherUI().Popup(localeInfo.SWITCHCHANNEL_SAME)
			return
			
		file=open("channel.inf", "w")
		file.write("%d %d %d" % (self.serverID, new_ch, self.regionID))
		file.close()

		net.SetServerInfo("CH%s" % (new_ch))
		self.Close()
		net.SendChatPacket("/channel_switch %d" % new_ch)

	def Close(self):
		self.Hide()
		print "close"
		return True

	def Hide(self):
		ui.Window.Hide(self)
			
	def Show(self):
		ui.ScriptWindow.Show(self)

		self.SetCenterPosition()
			
	def OnPressEscapeKey(self):
		self.Close()
		return True
