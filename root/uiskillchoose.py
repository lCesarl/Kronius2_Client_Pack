import ui
import uiScriptLocale
import event
import chat
import net

SKILL_NAMES = {
	0	:	[uiScriptLocale.skillchoose_warrior1,	uiScriptLocale.skillchoose_warrior2],
	1	:	[uiScriptLocale.skillchoose_ninja1,		uiScriptLocale.skillchoose_ninja2],
	2	:	[uiScriptLocale.skillchoose_sura1,		uiScriptLocale.skillchoose_sura2],
	3	:	[uiScriptLocale.skillchoose_shaman1,	uiScriptLocale.skillchoose_shaman2],
	4	:	[uiScriptLocale.skillchoose_wolfman1,	''],
}

class SkillChoose(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isLoaded = FALSE
		self.raceNum = 0
		
	def __LoadWindow(self, raceNum):
		if (self.isLoaded == TRUE):
			return
			
		self.isLoaded = TRUE
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "UIScript/skillchoosewindow.py")
		except:
			import exception
			exception.Abort("SelectJob.LoadWindow.LoadObject")
			
		try:
			self.__BindObjects()
		except:
			import exception
			exception.Abort("SelectJob.LoadWindow.BindObject")
		
		self.__BindEvents(raceNum)

	def __BindObjects(self):
		self.selectbutton1 = self.GetChild("SelectButton1")
		self.selectbutton2 = self.GetChild("SelectButton2")
		self.closeButton = self.GetChild("CloseButton")
		
	def __BindEvents(self, raceNum):
		self.selectbutton1.SetEvent(lambda arg = 1 : self.clickButtons(arg))
		self.selectbutton2.SetEvent(lambda arg = 2 : self.clickButtons(arg))
		self.closeButton.SetEvent(ui.__mem_func__(self.Close))

		self.selectbutton1.SetText(SKILL_NAMES[raceNum][0])
		self.selectbutton2.SetText(SKILL_NAMES[raceNum][1])
		
	def clickButtons(self, arg):
		net.SendSkillChooseInfo(arg)
		self.Destroy()

	def Open(self, raceNum):
		self.__LoadWindow(raceNum)
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def Close(self):
		self.Hide()
		
	def Destroy(self):
		self.Hide()
		self.Close()
		
	def OnPressEscapeKey(self):
		self.Close()
		return TRUE
		
	def OnPressExitKey(self):
		self.Close()
		return TRUE
		
	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
skillchoose = SkillChoose()
