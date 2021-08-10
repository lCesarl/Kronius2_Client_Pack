import ui
import net
import item
import skill
import localeInfo
import wndMgr
import player
import constInfo
import mouseModule
import uiScriptLocale
import app
import event

def unsigned32(n):
	return n & 0xFFFFFFFFL

class MainWindow(ui.ImageBox):
	class TextToolTip(ui.Window):
		def __init__(self):
			ui.Window.__init__(self, "TOP_MOST")

			textLine = ui.TextLine()
			textLine.SetParent(self)
			textLine.SetHorizontalAlignCenter()
			textLine.SetOutline()
			textLine.Show()
			self.textLine = textLine

		def __del__(self):
			ui.Window.__del__(self)

		def SetText(self, text):
			self.textLine.SetText(text)

		def OnRender(self):
			(mouseX, mouseY) = wndMgr.GetMousePosition()
			self.textLine.SetPosition(mouseX, mouseY - 15)
			
	def __init__(self):
		ui.ImageBox.__init__(self)
		self.LoadImage("characterview/userpanel_bg.png")
		self.SetPosition(0, 120)
		self.SetWindowHorizontalAlignLeft()
		self.SetWindowVerticalAlignBottom()
		self.hpGaugeBoard = 0
		self.spGaugeBoard = 0
		
		self.LoadElements()
		
		self.RefreshStatus()
		
	def RefreshStatus(self):
		curHP = player.GetStatus(player.HP)
		maxHP = player.GetStatus(player.MAX_HP)
		curSP = player.GetStatus(player.SP)
		maxSP = player.GetStatus(player.MAX_SP)
		curEXP = unsigned32(player.GetStatus(player.EXP))
		nextEXP = unsigned32(player.GetStatus(player.NEXT_EXP))
		recoveryHP = player.GetStatus(player.HP_RECOVERY)
		recoverySP = player.GetStatus(player.SP_RECOVERY)
		
		self.LevelText.SetText("Lv. " + str(player.GetStatus(player.LEVEL)) + " " + player.GetName())

		self.SetHP(curHP, maxHP)
		self.SetMP(curSP, maxSP)
		self.SetExperience(curEXP, nextEXP)
		
	def Destroy(self):
		# self.ClearDictionary()
		self.hpBar = None
		self.mpBar = None
		self.expGauge = None
		
		self.tooltipHP = 0
		self.tooltipSP = 0
		
		self.Hide()
		
	def LoadElements(self):
		self.hpGaugeBoard = ui.ImageBox()
		self.hpGaugeBoard.SetParent(self)
		self.hpGaugeBoard.SetPosition(95, 33)
		self.hpGaugeBoard.LoadImage("characterview/outline_image.png")
		self.hpGaugeBoard.Show()
		
		self.hpGaugeBoard.OnMouseOverIn = ui.__mem_func__(self.OverInHPImage)
		self.hpGaugeBoard.OnMouseOverOut = ui.__mem_func__(self.OverOutHPImage)
	
		self.hpBarBG = ui.ExpandedImageBox()
		self.hpBarBG.SetParent(self.hpGaugeBoard)
		self.hpBarBG.SetPosition(2, 2)
		self.hpBarBG.LoadImage("characterview/hp_bg.png")
		self.hpBarBG.Hide()
	
		HPBar = []
		HPBar.append(self.hpBarBG)

		for hp in HPBar:
			hp.SetSize(0, 0)
			
		self.hpBar = HPBar
		
		self.mpGaugeBoard = ui.ImageBox()
		self.mpGaugeBoard.SetParent(self)
		self.mpGaugeBoard.SetPosition(95, 54)
		self.mpGaugeBoard.LoadImage("characterview/outline_image.png")
		self.mpGaugeBoard.Show()
		
		self.mpGaugeBoard.OnMouseOverIn = ui.__mem_func__(self.OverInMPImage)
		self.mpGaugeBoard.OnMouseOverOut = ui.__mem_func__(self.OverOutMPImage)
		
		self.mpBarBG = ui.ExpandedImageBox()
		self.mpBarBG.SetParent(self.mpGaugeBoard)
		self.mpBarBG.SetPosition(2, 2)
		self.mpBarBG.LoadImage("characterview/mana_bg.png")
		self.mpBarBG.Hide()
	
		MPBar = []
		MPBar.append(self.mpBarBG)

		for mp in MPBar:
			mp.SetSize(0, 0)
			
		self.mpBar = MPBar
		
		self.expBarBG = ui.ExpandedImageBox()
		self.expBarBG.SetParent(self)
		self.expBarBG.SetPosition(101, 89)
		self.expBarBG.LoadImage("characterview/exp.png")
		self.expBarBG.Hide()
	
		EXPBar = []
		EXPBar.append(self.expBarBG)

		for exp in EXPBar:
			exp.SetSize(0, 0)
			
		self.expBar = EXPBar
		
		self.expPercentage = ui.TextLine()
		self.expPercentage.SetParent(self.expBar[0])
		self.expPercentage.SetHorizontalAlignCenter()
		self.expPercentage.SetPosition(147/2, 0)
		
		self.hpText = ui.TextLine()
		self.hpText.SetParent(self.hpBar[0])
		self.hpText.SetPosition(5, 0)
		
		self.hpPercentage = ui.TextLine()
		self.hpPercentage.SetParent(self.hpBar[0])
		self.hpPercentage.SetHorizontalAlignCenter()
		self.hpPercentage.SetPosition(160/2, 0)
		
		self.mpText = ui.TextLine()
		self.mpText.SetParent(self.mpBar[0])
		self.mpText.SetPosition(5, 0)
		
		self.mpPercentage = ui.TextLine()
		self.mpPercentage.SetParent(self.mpBar[0])
		self.mpPercentage.SetHorizontalAlignCenter()
		self.mpPercentage.SetPosition(160/2, 0)
		
		self.LevelText = ui.TextLine()
		self.LevelText.SetParent(self.hpText)
		self.LevelText.SetPosition(-5, -30)
		self.LevelText.SetOutline()
		self.LevelText.SetText("Lv. " + str(player.GetStatus(player.LEVEL)) + " " + player.GetName())
		self.LevelText.Show()
		
		self.tooltipHP = self.TextToolTip()
		self.tooltipHP.Hide()
		self.tooltipSP = self.TextToolTip()
		self.tooltipSP.Hide()
		
		self.LoadRace()
		
	def IsWarriorMale(self):
		return player.GetRace() == 0
		
	def IsWarriorFemale(self):
		return player.GetRace() == 4
		
	def IsAssassinFemale(self):
		return player.GetRace() == 1
		
	def IsAssassinMale(self):
		return player.GetRace() == 5
		
	def IsSuraMale(self):
		return player.GetRace() == 2
		
	def IsSuraFemale(self):
		return player.GetRace() == 6
		
	def IsShamanFemale(self):
		return player.GetRace() == 3
		
	def IsShamanMale(self):
		return player.GetRace() == 7
		
	def LoadRace(self):
		self.RaceImg = ui.ImageBox()
		self.RaceImg.SetParent(self)
		self.RaceImg.SetPosition(17, -1)
		if self.IsWarriorMale():
			self.RaceImg.LoadImage("characterview/f_shaman.png")
		elif self.IsWarriorFemale():
			self.RaceImg.LoadImage("characterview/f_shaman.png")
		elif self.IsAssassinFemale():
			self.RaceImg.LoadImage("characterview/f_shaman.png")
		elif self.IsAssassinMale():
			self.RaceImg.LoadImage("characterview/f_shaman.png")
		elif self.IsSuraMale():
			self.RaceImg.LoadImage("characterview/f_shaman.png")
		elif self.IsSuraFemale():
			self.RaceImg.LoadImage("characterview/f_shaman.png")
		elif self.IsShamanFemale():
			self.RaceImg.LoadImage("characterview/f_shaman.png")
		elif self.IsShamanMale():
			self.RaceImg.LoadImage("characterview/f_shaman.png")
		self.RaceImg.Show()
		
	def OverInHPImage(self):
		self.tooltipHP.Show()
		
	def OverOutHPImage(self):
		self.tooltipHP.Hide()
		
	def OverInMPImage(self):
		self.tooltipSP.Show()
		
	def OverOutMPImage(self):
		self.tooltipSP.Hide()
		
	def SetHP(self, curPoint, maxPoint):
		curPoint = min(curPoint, maxPoint)
		
		self.hpBar[0].Hide()
		realPct = (curPoint * 100) / maxPoint
		
		if maxPoint > 0:
			Percentage = float(curPoint % maxPoint) / maxPoint - 1.0
			
			if curPoint == maxPoint:
				Percentage = 0.0
				
			self.hpBar[0].SetRenderingRect(0.0, 0.0, Percentage, 0.0)
			self.hpBar[0].Show()
			self.hpPercentage.SetText("%d%%" % (realPct))
			self.hpPercentage.Show()
			self.hpText.SetText("HP:")
			self.hpText.Show()
			self.tooltipHP.SetText("%s : %d / %d" % (localeInfo.TASKBAR_HP, curPoint, maxPoint))
		
	def SetMP(self, curPoint, maxPoint):
		curPoint = min(curPoint, maxPoint)
		
		self.mpBar[0].Hide()
		realPct = (curPoint * 100) / maxPoint
		
		if maxPoint > 0:
			Percentage = float(curPoint % maxPoint) / maxPoint - 1.0
			
			if curPoint == maxPoint:
				Percentage = 0.0
				
			self.mpBar[0].SetRenderingRect(0.0, 0.0, Percentage, 0.0)
			self.mpBar[0].Show()
			self.mpPercentage.SetText("%d%%" % (realPct))
			self.mpPercentage.Show()
			self.mpText.SetText("MP:")
			self.mpText.Show()
			
			self.tooltipSP.SetText("%s : %d / %d" % (localeInfo.TASKBAR_SP, curPoint, maxPoint))
		
	def SetExperience(self, curPoint, maxPoint):
		curPoint = min(curPoint, maxPoint)
		
		self.expBar[0].Hide()
		realPct = (curPoint * 100) / maxPoint
		
		if maxPoint > 0:
			Percentage = float(curPoint % maxPoint) / maxPoint - 1.0
			
			if curPoint == maxPoint:
				Percentage = 0.0
				
			self.expBar[0].SetRenderingRect(0.0, 0.0, Percentage, 0.0)
			self.expBar[0].Show()
			self.expPercentage.SetText("%d%% EXP" % (realPct))
			self.expPercentage.Show()
		
	def __del__(self):
		ui.ImageBox.__del__(self)