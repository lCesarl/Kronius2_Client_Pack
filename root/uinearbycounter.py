import ui
import event

class NearbyCounterWindow(ui.ScriptWindow):
	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.titleBar = 0
		self.isLoaded = 0

		if self.isLoaded == 0:
			self.__LoadWindow()
		
	def __LoadWindow(self):
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "UIScript/nearbycounterwindow.py")
		except:
			import exception
			exception.Abort("NearbyCounterWindow.LoadWindow.PythonScriptLoader")
			
		try:
			GetObject = self.GetChild
			self.titleBar = GetObject("titlebar")
		except:
			import exception
			exception.Abort("NearbyCounterWindow.LoadWindow.GetChild")

		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))

	def Open(self):
		self.SetCenterPosition()
		self.SetTop()
		ui.ScriptWindow.Show(self)

	def Close(self):
		self.Hide()
		return TRUE

	def OnPressEscapeKey(self):
		chat.AppendChat(chat.CHAT_TYPE_INFO, "OnPressEscapeKey")
		self.Close()
		return TRUE
		
	def OnPressExitKey(self):
		chat.AppendChat(chat.CHAT_TYPE_INFO, "OnPressExitKey")
		self.Close()
		return TRUE
		
	def Destroy(self):
		self.Close()