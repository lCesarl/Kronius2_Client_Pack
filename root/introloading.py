import ui
import uiScriptLocale
import net
import app
import dbg
import player
import background
import wndMgr
import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()
import chrmgr
import colorInfo
import constInfo
import playerSettingModule
import stringCommander
import emotion
import uiRefine
import uiToolTip
import uiAttachMetin
import uiPickMoney
import uiChat
import uiMessenger
import uiHelp
import uiWhisper
import uiPointReset
import uiShop
import uiExchange
import uiSystem
import uiOption
import uiRestart

class LoadingWindow(ui.ScriptWindow):
	def __init__(self, stream):
		print "NEW LOADING WINDOW -------------------------------------------------------------------------------"
		ui.Window.__init__(self)
		net.SetPhaseWindow(net.PHASE_WINDOW_LOAD, self)

		self.stream=stream
		self.loadingImage=0
		self.loadingGage=0
		self.errMsg=0
		self.update=0
		self.playerX=0
		self.playerY=0
		self.loadStepList=[]

	def __del__(self):
		print "---------------------------------------------------------------------------- DELETE LOADING WINDOW"
		net.SetPhaseWindow(net.PHASE_WINDOW_LOAD, 0)
		ui.Window.__del__(self)

	def Open(self):
		print "OPEN LOADING WINDOW -------------------------------------------------------------------------------"

		#app.HideCursor()

		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, uiScriptLocale.LOCALE_UISCRIPT_PATH + "LoadingWindow.py")
		except:
			import exception
			exception.Abort("LodingWindow.Open - LoadScriptFile Error")

		try:
			self.loadingImage=self.GetChild("BackGround")
			self.errMsg=self.GetChild("ErrorMessage")
			self.loadingGage=self.GetChild("FullGage")
		except:
			import exception
			exception.Abort("LodingWindow.Open - LoadScriptFile Error")

		self.errMsg.Hide()
		imgFileNameDict = {
			0 : uiScriptLocale.LOCALE_UISCRIPT_PATH + "loading/loading0.sub",
			1 : uiScriptLocale.LOCALE_UISCRIPT_PATH + "loading/loading1.sub",
			2 : uiScriptLocale.LOCALE_UISCRIPT_PATH + "loading/loading2.sub",
			3 : uiScriptLocale.LOCALE_UISCRIPT_PATH + "loading/loading3.sub",
			4 : uiScriptLocale.LOCALE_UISCRIPT_PATH + "loading/loading4.sub",
			5 : uiScriptLocale.LOCALE_UISCRIPT_PATH + "loading/loading5.sub",
			6 : uiScriptLocale.LOCALE_UISCRIPT_PATH + "loading/loading6.sub",
			7 : uiScriptLocale.LOCALE_UISCRIPT_PATH + "loading/loading7.sub",
			8 : uiScriptLocale.LOCALE_UISCRIPT_PATH + "loading/loading8.sub",
			9 : uiScriptLocale.LOCALE_UISCRIPT_PATH + "loading/loading9.sub",
		}

		try:
			imgFileName = imgFileNameDict[app.GetRandom(0, len(imgFileNameDict) - 1)]
			self.loadingImage.LoadImage(imgFileName)

		except:
			print "LoadingWindow.Open.LoadImage - %s File Load Error" % (imgFileName)
			self.loadingImage.Hide()


		width = float(wndMgr.GetScreenWidth()) / float(self.loadingImage.GetWidth())
		height = float(wndMgr.GetScreenHeight()) / float(self.loadingImage.GetHeight())

		self.loadingImage.SetScale(width, height)
		self.loadingGage.SetPercentage(2, 100)

		self.Show()

		chrSlot=self.stream.GetCharacterSlot()
		net.SendSelectCharacterPacket(chrSlot)

		app.SetFrameSkip(0)

	def Close(self):
		print "---------------------------------------------------------------------------- CLOSE LOADING WINDOW"

		app.SetFrameSkip(1)

		self.loadStepList=[]
		self.loadingImage=0
		self.loadingGage=0
		self.errMsg=0
		self.ClearDictionary()
		self.Hide()

	def OnPressEscapeKey(self):
		app.SetFrameSkip(1)
		self.stream.SetLoginPhase()
		return TRUE

	def __SetNext(self, next):
		if next:
			self.update=ui.__mem_func__(next)
		else:
			self.update=0

	def __SetProgress(self, p):
		if self.loadingGage:
			self.loadingGage.SetPercentage(2+98*p/100, 100)
		#	self.loadingGage.SetPercentage(p, 160)

	def LoadData(self, playerX, playerY):
		self.playerX=playerX
		self.playerY=playerY

		self.loadStepList=[
			(100, ui.__mem_func__(self.__StartGame)),
		]

		self.__SetProgress(0)

	#	tmpLoadStepList = tuple(zip(*self.loadStepList))[0]
	#	for progress in set(range(tmpLoadStepList[0], tmpLoadStepList[-1] + 1)).difference(tmpLoadStepList):
	#		self.loadStepList.append((progress, lambda: None))
	#	self.loadStepList.sort()

	def OnUpdate(self):
		if len(self.loadStepList)>0:
			(progress, runFunc)=self.loadStepList[0]

			try:
				runFunc()

			except:	
				self.errMsg.Show()
				self.loadStepList=[]

				dbg.TraceError(" !!! Failed to load game data : STEP [%d]" % (progress))
				app.Exit()

				return

			self.loadStepList.pop(0)
			self.__SetProgress(progress)

	def __StartGame(self):
		background.SetViewDistanceSet(background.DISTANCE0, 25600)
		background.SelectViewDistanceNum(background.DISTANCE0)
		app.SetGlobalCenterPosition(self.playerX, self.playerY)
		net.StartGame()
