import app
import ui
import player
import net

class GameButtonWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__LoadWindow("UIScript/gamewindow.py")

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadWindow(self, filename):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, filename)
		except Exception, msg:
			import dbg
			dbg.TraceError("GameButtonWindow.LoadScript - %s" % (msg))
			app.Abort()
			return FALSE

		try:
			self.gameButtonDict={
				"STATUS" : self.GetChild("StatusPlusButton"),
				"SKILL" : self.GetChild("SkillPlusButton"),
				"QUEST" : self.GetChild("QuestButton"),
				"HELP" : self.GetChild("HelpButton"),
				"BUILD" : self.GetChild("BuildGuildBuilding"),
				"EXIT_OBSERVER" : self.GetChild("ExitObserver"),

				"BATTLEPASS" : self.GetChild("BattlePass"),

			}

			self.gameButtonDict["EXIT_OBSERVER"].SetEvent(ui.__mem_func__(self.__OnClickExitObserver))

			self.gameButtonDict["BATTLEPASS"].SetEvent(ui.__mem_func__(self.__OnClickBattlePass))

		except Exception, msg:
			import dbg
			dbg.TraceError("GameButtonWindow.LoadScript - %s" % (msg))
			app.Abort()
			return FALSE

		self.__HideAllGameButton()
		self.SetObserverMode(player.IsObserverMode())
		return TRUE

	def Destroy(self):
		for key in self.gameButtonDict:
			self.gameButtonDict[key].SetEvent(0)

		self.gameButtonDict={}

	def SetButtonEvent(self, name, event):
		try:
			self.gameButtonDict[name].SetEvent(event)
		except Exception, msg:
			print "GameButtonWindow.LoadScript - %s" % (msg)
			app.Abort()
			return

	def ShowBuildButton(self):
		self.gameButtonDict["BUILD"].Show()

	def HideBuildButton(self):
		self.gameButtonDict["BUILD"].Hide()

	def ShowPassButton(self):
		self.gameButtonDict["BATTLEPASS"].Show()
	
	def HidePassButton(self):
		self.gameButtonDict["BATTLEPASS"].Hide()

	def CheckGameButton(self):

		if not self.IsShow():
			return

		statusPlusButton=self.gameButtonDict["STATUS"]
		skillPlusButton=self.gameButtonDict["SKILL"]
		helpButton=self.gameButtonDict["HELP"]

		passButton=self.gameButtonDict["BATTLEPASS"]

		if player.GetStatus(player.STAT) > 0:
			statusPlusButton.Show()
		else:
			statusPlusButton.Hide()

		if self.__IsSkillStat():
			skillPlusButton.Show()
		else:
			skillPlusButton.Hide()

		if 0 == player.GetPlayTime():
			helpButton.Show()
		else:
			helpButton.Hide()

	def __IsSkillStat(self):
		if player.GetStatus(player.SKILL_ACTIVE) > 0:
			return TRUE

		return FALSE

	def __OnClickBattlePass(self):
		net.SendChatPacket("/open_battlepass")

	def __OnClickExitObserver(self):
		net.SendChatPacket("/observer_exit")

	def __HideAllGameButton(self):
		for btn in self.gameButtonDict.values():
			btn.Hide()

	def SetObserverMode(self, isEnable):
		if isEnable:
			self.gameButtonDict["EXIT_OBSERVER"].Show()
		else:
			self.gameButtonDict["EXIT_OBSERVER"].Hide()
