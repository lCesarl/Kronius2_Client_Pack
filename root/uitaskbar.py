import ui
import net
import item
import skill
import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()
import wndMgr
import player
import constInfo
import mouseModule
import uiScriptLocale
import app
import uicharacterview

if app.ENABLE_POISON_GAUGE_EFFECT:
	import chr
	import chrmgr

MOUSE_SETTINGS = [0, 0]

def InitMouseButtonSettings(left, right):
	global MOUSE_SETTINGS
	MOUSE_SETTINGS = [left, right]

def SetMouseButtonSetting(dir, event):
	global MOUSE_SETTINGS
	MOUSE_SETTINGS[dir] = event
	
def GetMouseButtonSettings():
	global MOUSE_SETTINGS
	return MOUSE_SETTINGS

def SaveMouseButtonSettings():
	global MOUSE_SETTINGS
	open("mouse.cfg", "w").write("%s\t%s" % tuple(MOUSE_SETTINGS))

def LoadMouseButtonSettings():
	global MOUSE_SETTINGS
	tokens = open("mouse.cfg", "r").read().split()

	if len(tokens) != 2:
		raise RuntimeError, "MOUSE_SETTINGS_FILE_ERROR"

	MOUSE_SETTINGS[0] = int(tokens[0])
	MOUSE_SETTINGS[1] = int(tokens[1])

def unsigned32(n):
	return n & 0xFFFFFFFFL

#-------------------Giftbox Begin------------------------------

class GiftBox(ui.ScriptWindow):
	class TextToolTip(ui.Window):
		def __init__(self):
			ui.Window.__init__(self, "TOP_MOST")
			self.SetWindowName("GiftBox")
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
		#print "NEW TASKBAR  ----------------------------------------------------------------------------"
		ui.ScriptWindow.__init__(self)
		self.tooltipGift = self.TextToolTip()
		self.tooltipGift.Show()
		
	def __del__(self):
		#print "---------------------------------------------------------------------------- DELETE TASKBAR"
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, uiScriptLocale.LOCALE_UISCRIPT_PATH + "giftbox.py")
		except:
			import exception
			exception.Abort("GiftBox.LoadWindow.LoadObject")		

		self.giftBoxIcon = self.GetChild("GiftBox_Icon")
		self.giftBoxToolTip = self.GetChild("GiftBox_ToolTip")
	
	def Destroy(self):		
		self.giftBoxIcon = 0
		self.giftBoxToolTip = 0		
			
#-------------------Giftbox End------------------------------

class ExpandedTaskBar(ui.ScriptWindow):
	BUTTON_DRAGON_SOUL = 0
	def __init__(self):
		ui.Window.__init__(self)
		self.SetWindowName("ExpandedTaskBar")
	
	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, uiScriptLocale.LOCALE_UISCRIPT_PATH + "ExpandedTaskBar.py")
		except:
			import exception
			exception.Abort("ExpandedTaskBar.LoadWindow.LoadObject")

		self.expandedTaskBarBoard = self.GetChild("ExpanedTaskBar_Board")

		self.toggleButtonDict = {}
		self.toggleButtonDict[ExpandedTaskBar.BUTTON_DRAGON_SOUL] = self.GetChild("DragonSoulButton")
		self.toggleButtonDict[ExpandedTaskBar.BUTTON_DRAGON_SOUL].SetParent(self)
	
	def SetTop(self):
		super(ExpandedTaskBar, self).SetTop()	
		for button in self.toggleButtonDict.values():
			button.SetTop()
	
	def Show(self):
		ui.ScriptWindow.Show(self)
	
	def Close(self):
		self.Hide()
	
	def SetToolTipText(self, eButton, text):
		self.toggleButtonDict[eButton].SetToolTipText(text)
		
	def SetToggleButtonEvent(self, eButton, kEventFunc):
		self.toggleButtonDict[eButton].SetEvent(kEventFunc)

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE
	
class TaskBar(ui.ScriptWindow):
	BUTTON_CHARACTER = 0
	BUTTON_INVENTORY = 1
	BUTTON_MESSENGER = 2
	BUTTON_SYSTEM = 3
	BUTTON_CHAT = 4
	BUTTON_EXPAND = 4
	IS_EXPANDED = FALSE
	
	QUICKPAGE_NUMBER_FILENAME = [
		"d:/ymir work/ui/game/taskbar/1.sub",
		"d:/ymir work/ui/game/taskbar/2.sub",
		"d:/ymir work/ui/game/taskbar/3.sub",
		"d:/ymir work/ui/game/taskbar/4.sub",
	]

	MOUSE_BUTTON_LEFT = 0
	MOUSE_BUTTON_RIGHT = 1
	NONE = 255

	EVENT_MOVE = 0
	EVENT_ATTACK = 1
	EVENT_MOVE_AND_ATTACK = 2
	EVENT_CAMERA = 3
	EVENT_SKILL = 4
	EVENT_AUTO = 5

	GAUGE_WIDTH = 133
	GAUGE_HEIGHT = 17

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

	class SkillButton(ui.SlotWindow):

		def __init__(self):
			ui.SlotWindow.__init__(self)

			self.event = 0
			self.arg = 0

			self.slotIndex = 0
			self.skillIndex = 0

			slotIndex = 0
			wndMgr.SetSlotBaseImage(self.hWnd, "d:/ymir work/ui/public/slot_base.sub", 1.0, 1.0, 1.0, 1.0)
			wndMgr.AppendSlot(self.hWnd, slotIndex, 0, 0, 32, 32)
			self.SetCoverButton(slotIndex,	"d:/ymir work/ui/public/slot_cover_button_01.sub",\
											"d:/ymir work/ui/public/slot_cover_button_02.sub",\
											"d:/ymir work/ui/public/slot_cover_button_03.sub",\
											"d:/ymir work/ui/public/slot_cover_button_04.sub", TRUE, FALSE)
			self.SetSize(32, 32)

		def __del__(self):
			ui.SlotWindow.__del__(self)

		def Destroy(self):
			if 0 != self.tooltipSkill:
				self.tooltipSkill.HideToolTip()

		def RefreshSkill(self):
			if 0 != self.slotIndex:
				self.SetSkill(self.slotIndex)

		def SetSkillToolTip(self, tooltip):
			self.tooltipSkill = tooltip

		def SetSkill(self, skillSlotNumber):
			slotNumber = 0
			skillIndex = player.GetSkillIndex(skillSlotNumber)
			skillGrade = player.GetSkillGrade(skillSlotNumber)
			skillLevel = player.GetSkillLevel(skillSlotNumber)
			skillType = skill.GetSkillType(skillIndex)

			self.skillIndex = skillIndex
			if 0 == self.skillIndex:
				self.ClearSlot(slotNumber)
				return

			self.slotIndex = skillSlotNumber

			self.SetSkillSlotNew(slotNumber, skillIndex, skillGrade, skillLevel)
			self.SetSlotCountNew(slotNumber, skillGrade, skillLevel)

			if player.IsSkillCoolTime(skillSlotNumber):
				(coolTime, elapsedTime) = player.GetSkillCoolTime(skillSlotNumber)
				self.SetSlotCoolTime(slotNumber, coolTime, elapsedTime)

			if player.IsSkillActive(skillSlotNumber):
				self.ActivateSlot(slotNumber)

		def SetSkillEvent(self, event, arg=0):
			self.event = event
			self.arg = arg

		def GetSkillIndex(self):
			return self.skillIndex

		def GetSlotIndex(self):
			return self.slotIndex

		def Activate(self, coolTime):
			self.SetSlotCoolTime(0, coolTime)

			if skill.IsToggleSkill(self.skillIndex):
				self.ActivateSlot(0)

		def Deactivate(self):
			if skill.IsToggleSkill(self.skillIndex):
				self.DeactivateSlot(0)

		def OnOverInItem(self, dummy):
			self.tooltipSkill.SetSkill(self.skillIndex)

		def OnOverOutItem(self):
			self.tooltipSkill.HideToolTip()

		def OnSelectItemSlot(self, dummy):
			if 0 != self.event:
				if 0 != self.arg:
					self.event(self.arg)
				else:
					self.event()

	
	def __init__(self):
		#print "NEW TASKBAR  ----------------------------------------------------------------------------"

		ui.ScriptWindow.__init__(self, "TOP_MOST")
		
		self.quickPageNumImageBox = None
		self.tooltipItem = 0
		self.tooltipSkill = 0
		self.selectSkillButtonList = []
		
		self.LoadWindow()
		
	def Destroy(self):		
		self.ClearDictionary()
		self.tooltipItem = 0
		self.tooltipSkill = 0
		self.toggleButtonDict = 0
		self.selectSkillButtonList = 0
		self.curSkillButton = 0
		self.CharacterView.Destroy()

	def SetItemToolTip(self, tooltipItem):
		self.tooltipItem = tooltipItem

	def SetSkillToolTip(self, tooltipSkill):
		self.tooltipSkill = tooltipSkill
		# self.curSkillButton.SetSkillToolTip(self.tooltipSkill)

	def SetToggleButtonEvent(self, eButton, kEventFunc):
		self.toggleButtonDict[eButton].SetEvent(kEventFunc)
		
	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()

			pyScrLoader.LoadScriptFile(self, "newtaskbar.py")
		except:
			import exception
			exception.Abort("TaskBar.LoadWindow.LoadObject")
			
		self.CharacterView = uicharacterview.MainWindow()
		self.CharacterView.Show()
		
		self.LoadObject()
		self.LoadSkills()
		self.LoadAll()
		
	def LoadAll(self):
		self.curSkillButton = self.SkillButton()
		self.curSkillButton.SetParent(self)
		self.curSkillButton.SetPosition(3, 3)
		self.curSkillButton.SetSkillEvent(ui.__mem_func__(self.ToggleRightMouseButtonModeWindow))
		self.curSkillButton.Hide()
		
		self.quickPageNumberBox = ui.ImageBox()
		self.quickPageNumberBox.SetParent(self)
		self.quickPageNumberBox.SetPosition(425, 60)
		self.quickPageNumberBox.LoadImage("taskbar/quickpage_slot.png")
		self.quickPageNumberBox.Show()
		
		self.quickPageNumImageBox = ui.ImageBox()
		self.quickPageNumImageBox.SetParent(self)
		self.quickPageNumImageBox.SetPosition(425+2, 60)
		self.quickPageNumImageBox.LoadImage("d:/ymir work/ui/game/taskbar/1.sub")
		self.quickPageNumImageBox.Show()
		
		self.QuickPageUpButton = ui.Button()
		self.QuickPageUpButton.SetParent(self)
		self.QuickPageUpButton.SetToolTipText(uiScriptLocale.TASKBAR_PREV_QUICKSLOT)
		self.QuickPageUpButton.SetPosition(425, 52)
		self.QuickPageUpButton.SetUpVisual("taskbar/quickslot_up.png")
		self.QuickPageUpButton.SetOverVisual("taskbar/quickslot_up.png")
		self.QuickPageUpButton.SetDownVisual("taskbar/quickslot_up.png")
		self.QuickPageUpButton.SetEvent(ui.__mem_func__(self.__OnClickQuickPageUpButton))
		self.QuickPageUpButton.Show()
		
		self.QuickPageDownButton = ui.Button()
		self.QuickPageDownButton.SetParent(self)
		self.QuickPageDownButton.SetToolTipText(uiScriptLocale.TASKBAR_NEXT_QUICKSLOT)
		self.QuickPageDownButton.SetPosition(425, 76)
		self.QuickPageDownButton.SetUpVisual("taskbar/quickslot_down.png")
		self.QuickPageDownButton.SetOverVisual("taskbar/quickslot_down.png")
		self.QuickPageDownButton.SetDownVisual("taskbar/quickslot_down.png")
		self.QuickPageDownButton.SetEvent(ui.__mem_func__(self.__OnClickQuickPageDownButton))
		self.QuickPageDownButton.Show()
		

		# self.GetChild("QuickPageUpButton").SetEvent(ui.__mem_func__(self.__OnClickQuickPageUpButton))
		# self.GetChild("QuickPageDownButton").SetEvent(ui.__mem_func__(self.__OnClickQuickPageDownButton))
		
	def RefreshStatus(self):
		self.CharacterView.RefreshStatus()
		
	def LoadSkills(self):
		self.GridTable = ui.GridSlotWindow()
		self.GridTable.SetParent(self)
		self.GridTable.SetPosition(75, 53)
		self.GridTable.SetSize(32*8, 32*1)
		self.GridTable.ArrangeSlot(0, 8, 1, 32, 32, 11, 0)
		self.GridTable.Show()
		self.GridTable.SetSlotBaseImage("taskbar/taskbar_slot.png", 1.0, 1.0, 1.0, 1.0)
		self.GridTable.SetUsableItem(True)
		
		self.GridTable.SetSlotStyle(wndMgr.SLOT_STYLE_NONE)
		self.GridTable.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptyQuickSlot))
		self.GridTable.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemQuickSlot))
		self.GridTable.SetUnselectItemSlotEvent(ui.__mem_func__(self.UnselectItemQuickSlot))
		self.GridTable.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		self.GridTable.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
		
		self.slotImages = []
		
		for i in range(8):
			slotImage = ui.ImageBox()
			slotImage.SetParent(self.GridTable)
			slotImage.SetPosition(3 + 43*i, 0)
			new_i = i+1
			if new_i < 5:
				slotImage.LoadImage("d:/ymir work/ui/game/taskbar/%d.sub" % (new_i))
			else:
				slotImage.LoadImage("d:/ymir work/ui/game/taskbar/f%d.sub" % (new_i-4))
			slotImage.Show()
			
			self.slotImages.append(slotImage)
			
	def LoadObject(self):
		self.CharacterBtn = ui.Button()
		self.CharacterBtn.SetParent(self)
		self.CharacterBtn.SetPosition(483, 52)
		self.CharacterBtn.SetUpVisual("taskbar/btn_character.png")
		self.CharacterBtn.SetOverVisual("taskbar/btn_character1.png")
		self.CharacterBtn.SetDownVisual("taskbar/btn_character2.png")
		self.CharacterBtn.Show()
		
		self.InventoryBtn = ui.Button()
		self.InventoryBtn.SetParent(self)
		self.InventoryBtn.SetPosition(524, 52)
		self.InventoryBtn.SetUpVisual("taskbar/btn_inventory.png")
		self.InventoryBtn.SetOverVisual("taskbar/btn_inventory1.png")
		self.InventoryBtn.SetDownVisual("taskbar/btn_inventory2.png")
		self.InventoryBtn.Show()
		
		self.FriendsBtn = ui.Button()
		self.FriendsBtn.SetParent(self)
		self.FriendsBtn.SetPosition(565, 52)
		self.FriendsBtn.SetUpVisual("taskbar/btn_friends.png")
		self.FriendsBtn.SetOverVisual("taskbar/btn_friends1.png")
		self.FriendsBtn.SetDownVisual("taskbar/btn_friends2.png")
		self.FriendsBtn.Show()
		
		self.SettingsBtn = ui.Button()
		self.SettingsBtn.SetParent(self)
		self.SettingsBtn.SetPosition(606, 52)
		self.SettingsBtn.SetUpVisual("taskbar/btn_settings.png")
		self.SettingsBtn.SetOverVisual("taskbar/btn_settings1.png")
		self.SettingsBtn.SetDownVisual("taskbar/btn_settings2.png")
		self.SettingsBtn.Show()
		
		toggleButtonDict = {}
		toggleButtonDict[TaskBar.BUTTON_CHARACTER]=self.CharacterBtn
		toggleButtonDict[TaskBar.BUTTON_INVENTORY]=self.InventoryBtn
		toggleButtonDict[TaskBar.BUTTON_MESSENGER]=self.FriendsBtn
		toggleButtonDict[TaskBar.BUTTON_SYSTEM]=self.SettingsBtn
		
		self.toggleButtonDict = toggleButtonDict
		
	def ToggleLeftMouseButtonModeWindow(self):

		wndMouseButtonMode = self.mouseModeButtonList[self.MOUSE_BUTTON_LEFT]

		if TRUE == wndMouseButtonMode.IsShow():

			wndMouseButtonMode.Hide()

		else:
			wndMouseButtonMode.Show()

	def ToggleRightMouseButtonModeWindow(self):

		wndMouseButtonMode = self.mouseModeButtonList[self.MOUSE_BUTTON_RIGHT]

		if TRUE == wndMouseButtonMode.IsShow():

			wndMouseButtonMode.Hide()
			self.CloseSelectSkill()

		else:
			wndMouseButtonMode.Show()
			self.OpenSelectSkill()

	def OpenSelectSkill(self):

		PAGE_SLOT_COUNT = 6

		(xSkillButton, y) = self.curSkillButton.GetGlobalPosition()
		y -= (37 + 32 + 1)

		for key in self.skillCategoryNameList:

			appendCount = 0
			startNumber = self.skillPageStartSlotIndexDict[key]
			x = xSkillButton

			getSkillIndex=player.GetSkillIndex
			getSkillLevel=player.GetSkillLevel
			for i in xrange(PAGE_SLOT_COUNT):

				skillIndex = getSkillIndex(startNumber+i)
				skillLevel = getSkillLevel(startNumber+i)

				if 0 == skillIndex:
					continue
				if 0 == skillLevel:
					continue
				if skill.IsStandingSkill(skillIndex):
					continue

				skillButton = self.SkillButton()
				skillButton.SetSkill(startNumber+i)
				skillButton.SetPosition(x, y)
				skillButton.SetSkillEvent(ui.__mem_func__(self.CloseSelectSkill), startNumber+i+1)
				skillButton.SetSkillToolTip(self.tooltipSkill)
				skillButton.SetTop()
				skillButton.Show()
				self.selectSkillButtonList.append(skillButton)

				appendCount += 1
				x -= 32

			if appendCount > 0:
				y -= 32

	def CloseSelectSkill(self, slotIndex=-1):

		self.mouseModeButtonList[self.MOUSE_BUTTON_RIGHT].Hide()
		for button in self.selectSkillButtonList:
			button.Destroy()

		self.selectSkillButtonList = []

		if -1 != slotIndex:
			self.curSkillButton.Show()
			self.curMouseModeButton[self.MOUSE_BUTTON_RIGHT].Hide()
			player.SetMouseFunc(player.MBT_RIGHT, player.MBF_SKILL)
			player.ChangeCurrentSkillNumberOnly(slotIndex-1)
		else:
			self.curSkillButton.Hide()
			self.curMouseModeButton[self.MOUSE_BUTTON_RIGHT].Show()

	def SelectMouseButtonEvent(self, dir, event):
		SetMouseButtonSetting(dir, event)

		self.CloseSelectSkill()
		self.mouseModeButtonList[dir].Hide()

		btn = 0
		type = self.NONE
		func = self.NONE
		tooltip_text = ""		
		
		if self.MOUSE_BUTTON_LEFT == dir:
			type = player.MBT_LEFT

		elif self.MOUSE_BUTTON_RIGHT == dir:
			type = player.MBT_RIGHT

		if self.EVENT_MOVE == event:
			btn = self.mouseModeButtonList[dir].GetChild("button_move")
			func = player.MBF_MOVE
			tooltip_text = localeInfo.TASKBAR_MOVE
		elif self.EVENT_ATTACK == event:
			btn = self.mouseModeButtonList[dir].GetChild("button_attack")
			func = player.MBF_ATTACK
			tooltip_text = localeInfo.TASKBAR_ATTACK
		elif self.EVENT_AUTO == event:
			btn = self.mouseModeButtonList[dir].GetChild("button_auto_attack")
			func = player.MBF_AUTO
			tooltip_text = localeInfo.TASKBAR_AUTO
		elif self.EVENT_MOVE_AND_ATTACK == event:
			btn = self.mouseModeButtonList[dir].GetChild("button_move_and_attack")
			func = player.MBF_SMART
			tooltip_text = localeInfo.TASKBAR_ATTACK
		elif self.EVENT_CAMERA == event:
			btn = self.mouseModeButtonList[dir].GetChild("button_camera")
			func = player.MBF_CAMERA
			tooltip_text = localeInfo.TASKBAR_CAMERA
		elif self.EVENT_SKILL == event:
			btn = self.mouseModeButtonList[dir].GetChild("button_skill")
			func = player.MBF_SKILL
			tooltip_text = localeInfo.TASKBAR_SKILL

		if 0 != btn:
			self.curMouseModeButton[dir].SetToolTipText(tooltip_text, 0, -18)
			self.curMouseModeButton[dir].SetUpVisual(btn.GetUpVisualFileName())
			self.curMouseModeButton[dir].SetOverVisual(btn.GetOverVisualFileName())
			self.curMouseModeButton[dir].SetDownVisual(btn.GetDownVisualFileName())
			self.curMouseModeButton[dir].Show()

		player.SetMouseFunc(type, func)

	def OnChangeCurrentSkill(self, skillSlotNumber):
		self.curSkillButton.SetSkill(skillSlotNumber)
		self.curSkillButton.Show()
		self.curMouseModeButton[self.MOUSE_BUTTON_RIGHT].Hide()
		
	def RefreshQuickSlot(self):

		pageNum = player.GetQuickPage()

		try:
			self.quickPageNumImageBox.LoadImage(TaskBar.QUICKPAGE_NUMBER_FILENAME[pageNum])
		except:
			pass

		startNumber = 0
		# for slot in self.quickslot:

		for i in xrange(8):

			slotNumber = i+startNumber

			(Type, Position) = player.GetLocalQuickSlot(slotNumber)

			if player.SLOT_TYPE_NONE == Type:
				self.GridTable.ClearSlot(slotNumber)
				continue

			if player.SLOT_TYPE_INVENTORY == Type:

				itemIndex = player.GetItemIndex(Position)
				itemCount = player.GetItemCount(Position)
				if itemCount <= 1:
					itemCount = 0
				
				if constInfo.IS_AUTO_POTION(itemIndex):
					metinSocket = [player.GetItemMetinSocket(Position, j) for j in xrange(player.METIN_SOCKET_MAX_NUM)]
					
					if 0 != int(metinSocket[0]):
						self.GridTable.ActivateSlot(slotNumber)
					else:
						self.GridTable.DeactivateSlot(slotNumber)

				if False:#app.ENABLE_NEW_BLEND:#TODO TODO TODO TODO IMPORTANT IMPORTANT WICHTIG WICHTIG
					if item.ITEM_TYPE_BLEND == item.GetItemType() and item.GetItemSubType() == item.INFINITY_BLEND:
						metinSocket = player.GetItemMetinSocket(slotNumber, 2)
						if metinSocket == 1:
							self.GridTable.ActivateSlot(slotNumber)
						else:
							self.GridTable.DeactivateSlot(slotNumber)
				
				self.GridTable.SetItemSlot(slotNumber, itemIndex, itemCount)

			elif player.SLOT_TYPE_SKILL == Type:

				skillIndex = player.GetSkillIndex(Position)
				if 0 == skillIndex:
					self.GridTable.ClearSlot(slotNumber)
					continue

				skillType = skill.GetSkillType(skillIndex)
				if skill.SKILL_TYPE_GUILD == skillType:
					import guild
					skillGrade = 0
					skillLevel = guild.GetSkillLevel(Position)

				else:
					skillGrade = player.GetSkillGrade(Position)
					skillLevel = player.GetSkillLevel(Position)

				self.GridTable.SetSkillSlotNew(slotNumber, skillIndex, skillGrade, skillLevel)
				self.GridTable.SetSlotCountNew(slotNumber, skillGrade, skillLevel)
				self.GridTable.SetCoverButton(slotNumber)

				if player.IsSkillCoolTime(Position):
					(coolTime, elapsedTime) = player.GetSkillCoolTime(Position)
					self.GridTable.SetSlotCoolTime(slotNumber, coolTime, elapsedTime)

				if player.IsSkillActive(Position):
					self.GridTable.ActivateSlot(slotNumber)

			elif player.SLOT_TYPE_EMOTION == Type:

				emotionIndex = Position
				self.GridTable.SetEmotionSlot(slotNumber, emotionIndex)
				self.GridTable.SetCoverButton(slotNumber)
				self.GridTable.SetSlotCount(slotNumber, 0)

		self.GridTable.RefreshSlot()
		startNumber += 4

	def canAddQuickSlot(self, Type, slotNumber):

		if player.SLOT_TYPE_INVENTORY == Type:

			itemIndex = player.GetItemIndex(slotNumber)
			return item.CanAddToQuickSlotItem(itemIndex)

		return TRUE

	def AddQuickSlot(self, localSlotIndex):
		AttachedSlotType = mouseModule.mouseController.GetAttachedType()
		AttachedSlotNumber = mouseModule.mouseController.GetAttachedSlotNumber()
		AttachedItemIndex = mouseModule.mouseController.GetAttachedItemIndex()

		if player.SLOT_TYPE_QUICK_SLOT == AttachedSlotType:
			player.RequestMoveGlobalQuickSlotToLocalQuickSlot(AttachedSlotNumber, localSlotIndex)

		elif player.SLOT_TYPE_EMOTION == AttachedSlotType:

			player.RequestAddLocalQuickSlot(localSlotIndex, AttachedSlotType, AttachedItemIndex)

		elif TRUE == self.canAddQuickSlot(AttachedSlotType, AttachedSlotNumber):

			## Online Code
			player.RequestAddLocalQuickSlot(localSlotIndex, AttachedSlotType, AttachedSlotNumber)
		
		mouseModule.mouseController.DeattachObject()
		self.RefreshQuickSlot()

	def SelectEmptyQuickSlot(self, slotIndex):

		if TRUE == mouseModule.mouseController.isAttached():
			self.AddQuickSlot(slotIndex)

	def SelectItemQuickSlot(self, localQuickSlotIndex):

		if TRUE == mouseModule.mouseController.isAttached():
			self.AddQuickSlot(localQuickSlotIndex)

		else:
			globalQuickSlotIndex=player.LocalQuickSlotIndexToGlobalQuickSlotIndex(localQuickSlotIndex)
			mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_QUICK_SLOT, globalQuickSlotIndex, globalQuickSlotIndex)

	def UnselectItemQuickSlot(self, localSlotIndex):

		if FALSE == mouseModule.mouseController.isAttached():
			player.RequestUseLocalQuickSlot(localSlotIndex)
			return

		elif mouseModule.mouseController.isAttached():
			mouseModule.mouseController.DeattachObject()
			return


	def OnUseSkill(self, usedSlotIndex, coolTime):

		QUICK_SLOT_SLOT_COUNT = 8
		slotIndex = 0

		## Current Skill Button
		if usedSlotIndex == self.curSkillButton.GetSlotIndex():
			self.curSkillButton.Activate(coolTime)

		## Quick Slot
		# for slotWindow in self.quickslot:

		for i in xrange(QUICK_SLOT_SLOT_COUNT):

			(Type, Position) = player.GetLocalQuickSlot(slotIndex)

			if Type == player.SLOT_TYPE_SKILL:
				if usedSlotIndex == Position:
					self.GridTable.SetSlotCoolTime(slotIndex, coolTime)
					return

			slotIndex += 1

	def OnActivateSkill(self, usedSlotIndex):
		slotIndex = 0

		## Current Skill Button
		if usedSlotIndex == self.curSkillButton.GetSlotIndex():
			self.curSkillButton.Deactivate()

		## Quick Slot
		# for slotWindow in self.quickslot:

		for i in xrange(8):

			(Type, Position) = player.GetLocalQuickSlot(slotIndex)

			if Type == player.SLOT_TYPE_SKILL:
				if usedSlotIndex == Position:
					self.GridTable.ActivateSlot(slotIndex)
					return

			slotIndex += 1

	def OnDeactivateSkill(self, usedSlotIndex):
		slotIndex = 0

		## Current Skill Button
		if usedSlotIndex == self.curSkillButton.GetSlotIndex():
			self.curSkillButton.Deactivate()

		## Quick Slot
		# for slotWindow in self.quickslot:

		for i in xrange(8):

			(Type, Position) = player.GetLocalQuickSlot(slotIndex)

			if Type == player.SLOT_TYPE_SKILL:
				if usedSlotIndex == Position:
					self.GridTable.DeactivateSlot(slotIndex)
					return

			slotIndex += 1

	def OverInItem(self, slotNumber):
		if mouseModule.mouseController.isAttached():
			return

		(Type, Position) = player.GetLocalQuickSlot(slotNumber)

		if player.SLOT_TYPE_INVENTORY == Type:
			self.tooltipItem.SetInventoryItem(Position)
			self.tooltipSkill.HideToolTip()

		elif player.SLOT_TYPE_SKILL == Type:

			skillIndex = player.GetSkillIndex(Position)
			skillType = skill.GetSkillType(skillIndex)

			if skill.SKILL_TYPE_GUILD == skillType:
				import guild
				skillGrade = 0
				skillLevel = guild.GetSkillLevel(Position)

			else:
				skillGrade = player.GetSkillGrade(Position)
				skillLevel = player.GetSkillLevel(Position)

			self.tooltipSkill.SetSkillNew(Position, skillIndex, skillGrade, skillLevel)
			self.tooltipItem.HideToolTip()

	def OverOutItem(self):
		if 0 != self.tooltipItem:
			self.tooltipItem.HideToolTip()
		if 0 != self.tooltipSkill:
			self.tooltipSkill.HideToolTip()
		
	def RefreshSkill(self):
		self.curSkillButton.RefreshSkill()
		for button in self.selectSkillButtonList:
			button.RefreshSkill()
			
	def __OnClickQuickPageUpButton(self):
		player.SetQuickPage(player.GetQuickPage()-1)

	def __OnClickQuickPageDownButton(self):
		player.SetQuickPage(player.GetQuickPage()+1)
