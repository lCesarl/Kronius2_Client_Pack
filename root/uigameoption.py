import ui
import snd
import systemSetting
import net
import chat
import app
import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()
import constInfo
import chrmgr
import player
import uiPrivateShopBuilder # ±Ë¡ÿ»£
import interfaceModule # ±Ë¡ÿ»£
import os
import skill

blockMode = 0
viewChatMode = 0

MOBILE = FALSE

class OptionDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__Initialize()
		self.__Load()
		self.RefreshViewChat()
		self.RefreshAlwaysShowName()
		self.RefreshShowDamage()
		self.RefreshShowSalesText()
		self.RefreshShowYangText()
		self.RefreshMobEffects()
		self.RefreshSkillEffects()
		self.RefreshBuffEffects()
		self.RefreshRenderTarget()
		self.RefreshPets()
		self.RefreshMounts()
		self.RefreshShops()
		"""if app.ENABLE_HIDE_COSTUMES_CLIENTSIDE:
			self.RefreshCostumes()
		if app.ENABLE_HIDE_SHINING_EFFECTS:
			self.RefreshShinings()"""
		if app.ENABLE_DYNASTY_DUELLSTYLE:
			self.RefreshDynastyText()
		"""if app.ENABLE_RELOAD_SKILLS:	
			self.RefreshShowModdedSkills()"""

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		print " -------------------------------------- DELETE GAME OPTION DIALOG"

	def __Initialize(self):
		self.titleBar = 0
		self.nameColorModeButtonList = []
		self.viewTargetBoardButtonList = []
		self.pvpModeButtonDict = {}
		self.blockButtonList = []
		self.viewChatButtonList = []
		self.alwaysShowNameButtonList = []
		self.showDamageButtonList = []
		self.showsalesTextButtonList = []
		self.showyangTextButtonList = []
		self.showMobEffectsButtonList = []
		self.showSkillEffectsButtonList = []
		self.showBuffEffectsButtonList = []
		self.renderTarget = []
		self.showPets = []
		self.showMounts = []
		self.showShops = []
		"""if app.ENABLE_HIDE_COSTUMES_CLIENTSIDE:
			self.showCostumes = []
		if app.ENABLE_HIDE_SHINING_EFFECTS:
			self.showShinings = []"""
		if app.ENABLE_DYNASTY_DUELLSTYLE:
			self.showDynastyButtonList = []
		"""if app.ENABLE_RELOAD_SKILLS:
			self.showModdedSkillsButtonList = []"""	

	def Destroy(self):
		self.ClearDictionary()

		self.__Initialize()
		print " -------------------------------------- DESTROY GAME OPTION DIALOG"
	
	def __Load_LoadScript(self, fileName):
		try:
			pyScriptLoader = ui.PythonScriptLoader()
			pyScriptLoader.LoadScriptFile(self, fileName)
		except:
			import exception
			exception.Abort("OptionDialog.__Load_LoadScript")

	def __Load_BindObject(self):
		try:
			GetObject = self.GetChild
			self.titleBar = GetObject("titlebar")
			self.nameColorModeButtonList.append(GetObject("name_color_normal"))
			self.nameColorModeButtonList.append(GetObject("name_color_empire"))
			self.viewTargetBoardButtonList.append(GetObject("target_board_no_view"))
			self.viewTargetBoardButtonList.append(GetObject("target_board_view"))
			self.pvpModeButtonDict[player.PK_MODE_PEACE] = GetObject("pvp_peace")
			self.pvpModeButtonDict[player.PK_MODE_REVENGE] = GetObject("pvp_revenge")
			self.pvpModeButtonDict[player.PK_MODE_GUILD] = GetObject("pvp_guild")
			self.pvpModeButtonDict[player.PK_MODE_FREE] = GetObject("pvp_free")
			self.blockButtonList.append(GetObject("block_exchange_button"))
			self.blockButtonList.append(GetObject("block_party_button"))
			self.blockButtonList.append(GetObject("block_guild_button"))
			self.blockButtonList.append(GetObject("block_whisper_button"))
			self.blockButtonList.append(GetObject("block_friend_button"))
			self.blockButtonList.append(GetObject("block_party_request_button"))
			self.viewChatButtonList.append(GetObject("view_chat_on_button"))
			self.viewChatButtonList.append(GetObject("view_chat_off_button"))
			self.alwaysShowNameButtonList.append(GetObject("always_show_name_on_button"))
			self.alwaysShowNameButtonList.append(GetObject("always_show_name_off_button"))
			self.showDamageButtonList.append(GetObject("show_damage_on_button"))
			self.showDamageButtonList.append(GetObject("show_damage_off_button"))
			self.showsalesTextButtonList.append(GetObject("salestext_on_button"))
			self.showsalesTextButtonList.append(GetObject("salestext_off_button"))
			self.showyangTextButtonList.append(GetObject("yangtext_on_button"))
			self.showyangTextButtonList.append(GetObject("yangtext_off_button"))
			self.showMobEffectsButtonList.append(GetObject("mobeffects_on_button"))
			self.showMobEffectsButtonList.append(GetObject("mobeffects_off_button"))
			self.showSkillEffectsButtonList.append(GetObject("skilleffects_on_button"))
			self.showSkillEffectsButtonList.append(GetObject("skilleffects_off_button"))
			self.showBuffEffectsButtonList.append(GetObject("buffeffects_on_button"))
			self.showBuffEffectsButtonList.append(GetObject("buffeffects_off_button"))
			self.renderTarget.append(GetObject("rendertarget_on_button"))
			self.renderTarget.append(GetObject("rendertarget_off_button"))
			self.showPets.append(GetObject("ShowMadaraPetButton_on"))
			self.showPets.append(GetObject("ShowMadaraPetButton_off"))
			self.showMounts.append(GetObject("ShowMadaraMountButton_on"))
			self.showMounts.append(GetObject("ShowMadaraMountButton_off"))
			self.showShops.append(GetObject("ShowMadaraShopButton_on"))
			self.showShops.append(GetObject("ShowMadaraShopButton_off"))

			"""if app.ENABLE_HIDE_COSTUMES_CLIENTSIDE:
				self.showCostumes.append(GetObject("ShowCostumeOn"))
				self.showCostumes.append(GetObject("ShowCostumeOff"))

			if app.ENABLE_HIDE_SHINING_EFFECTS:
				self.showShinings.append(GetObject("ShowShiningsOn"))
				self.showShinings.append(GetObject("ShowShiningsOff"))"""

			if app.ENABLE_DYNASTY_DUELLSTYLE:
				self.showDynastyButtonList.append(GetObject("dynasty_on_button"))
				self.showDynastyButtonList.append(GetObject("dynasty_off_button"))

			"""if app.ENABLE_RELOAD_SKILLS:
				self.showModdedSkillsButtonList.append(GetObject("moddedskills_on_button"))
				self.showModdedSkillsButtonList.append(GetObject("moddedskills_off_button"))"""

			global MOBILE
			if MOBILE:
				self.inputMobileButton = GetObject("input_mobile_button")
				self.deleteMobileButton = GetObject("delete_mobile_button")


		except:
			import exception
			exception.Abort("OptionDialog.__Load_BindObject")

	def __Load(self):
		global MOBILE
		if MOBILE:
			self.__Load_LoadScript("uiscript/gameoptiondialog_formobile.py")
		else:
			self.__Load_LoadScript("uiscript/gameoptiondialog.py")

		self.__Load_BindObject()

		self.SetCenterPosition()

		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))

		self.nameColorModeButtonList[0].SAFE_SetEvent(self.__OnClickNameColorModeNormalButton)
		self.nameColorModeButtonList[1].SAFE_SetEvent(self.__OnClickNameColorModeEmpireButton)

		self.viewTargetBoardButtonList[0].SAFE_SetEvent(self.__OnClickTargetBoardViewButton)
		self.viewTargetBoardButtonList[1].SAFE_SetEvent(self.__OnClickTargetBoardNoViewButton)

		self.pvpModeButtonDict[player.PK_MODE_PEACE].SAFE_SetEvent(self.__OnClickPvPModePeaceButton)
		self.pvpModeButtonDict[player.PK_MODE_REVENGE].SAFE_SetEvent(self.__OnClickPvPModeRevengeButton)
		self.pvpModeButtonDict[player.PK_MODE_GUILD].SAFE_SetEvent(self.__OnClickPvPModeGuildButton)
		self.pvpModeButtonDict[player.PK_MODE_FREE].SAFE_SetEvent(self.__OnClickPvPModeFreeButton)

		self.blockButtonList[0].SetToggleUpEvent(self.__OnClickBlockExchangeButton)
		self.blockButtonList[1].SetToggleUpEvent(self.__OnClickBlockPartyButton)
		self.blockButtonList[2].SetToggleUpEvent(self.__OnClickBlockGuildButton)
		self.blockButtonList[3].SetToggleUpEvent(self.__OnClickBlockWhisperButton)
		self.blockButtonList[4].SetToggleUpEvent(self.__OnClickBlockFriendButton)
		self.blockButtonList[5].SetToggleUpEvent(self.__OnClickBlockPartyRequest)

		self.blockButtonList[0].SetToggleDownEvent(self.__OnClickBlockExchangeButton)
		self.blockButtonList[1].SetToggleDownEvent(self.__OnClickBlockPartyButton)
		self.blockButtonList[2].SetToggleDownEvent(self.__OnClickBlockGuildButton)
		self.blockButtonList[3].SetToggleDownEvent(self.__OnClickBlockWhisperButton)
		self.blockButtonList[4].SetToggleDownEvent(self.__OnClickBlockFriendButton)
		self.blockButtonList[5].SetToggleDownEvent(self.__OnClickBlockPartyRequest)

		self.viewChatButtonList[0].SAFE_SetEvent(self.__OnClickViewChatOnButton)
		self.viewChatButtonList[1].SAFE_SetEvent(self.__OnClickViewChatOffButton)

		self.alwaysShowNameButtonList[0].SAFE_SetEvent(self.__OnClickAlwaysShowNameOnButton)
		self.alwaysShowNameButtonList[1].SAFE_SetEvent(self.__OnClickAlwaysShowNameOffButton)

		self.showDamageButtonList[0].SAFE_SetEvent(self.__OnClickShowDamageOnButton)
		self.showDamageButtonList[1].SAFE_SetEvent(self.__OnClickShowDamageOffButton)
		
		self.showsalesTextButtonList[0].SAFE_SetEvent(self.__OnClickSalesTextOnButton)
		self.showsalesTextButtonList[1].SAFE_SetEvent(self.__OnClickSalesTextOffButton)

		self.showyangTextButtonList[0].SAFE_SetEvent(self.__OnClickYangTextOnButton)
		self.showyangTextButtonList[1].SAFE_SetEvent(self.__OnClickYangTextOffButton)

		self.showMobEffectsButtonList[0].SAFE_SetEvent(self.__OnClickMobEffectsOnButton)
		self.showMobEffectsButtonList[1].SAFE_SetEvent(self.__OnClickMobEffectsOffButton)

		self.showSkillEffectsButtonList[0].SAFE_SetEvent(self.__OnClickSkillEffectsOnButton)
		self.showSkillEffectsButtonList[1].SAFE_SetEvent(self.__OnClickSkillEffectsOffButton)

		self.showBuffEffectsButtonList[0].SAFE_SetEvent(self.__OnClickBuffEffectsOnButton)
		self.showBuffEffectsButtonList[1].SAFE_SetEvent(self.__OnClickBuffEffectsOffButton)

		self.renderTarget[0].SAFE_SetEvent(self.__OnClickRenderTargetOnButton)
		self.renderTarget[1].SAFE_SetEvent(self.__OnClickRenderTargetOffButton)

		self.showPets[0].SAFE_SetEvent(self.__OnClickHidePetsButtonOn)
		self.showPets[1].SAFE_SetEvent(self.__OnClickHidePetsButtonOff)

		self.showMounts[0].SAFE_SetEvent(self.__OnClickHideMountsButtonOn)
		self.showMounts[1].SAFE_SetEvent(self.__OnClickHideMountsButtonOff)	

		self.showShops[0].SAFE_SetEvent(self.__OnClickHideShopsButtonOn)
		self.showShops[1].SAFE_SetEvent(self.__OnClickHideShopsButtonOff)

		"""if app.ENABLE_HIDE_COSTUMES_CLIENTSIDE:
			self.showCostumes[0].SAFE_SetEvent(self.__OnClickHideCostumesButtonOn)
			self.showCostumes[1].SAFE_SetEvent(self.__OnClickHideCostumesButtonOff)

		if app.ENABLE_HIDE_SHINING_EFFECTS:
			self.showShinings[0].SAFE_SetEvent(self.__OnClickHideShiningsButtonOn)
			self.showShinings[1].SAFE_SetEvent(self.__OnClickHideShiningsButtonOff)"""

		if app.ENABLE_DYNASTY_DUELLSTYLE:
			self.showDynastyButtonList[0].SAFE_SetEvent(self.__OnClickDynastyOnButton)
			self.showDynastyButtonList[1].SAFE_SetEvent(self.__OnClickDynastyOffButton)

		"""if app.ENABLE_RELOAD_SKILLS:
			self.showModdedSkillsButtonList[0].SAFE_SetEvent(self.__OnClickModdedSkillsOnButton)
			self.showModdedSkillsButtonList[1].SAFE_SetEvent(self.__OnClickModdedSkillsOffButton)"""

		self.__ClickRadioButton(self.nameColorModeButtonList, constInfo.GET_CHRNAME_COLOR_INDEX())
		self.__ClickRadioButton(self.viewTargetBoardButtonList, constInfo.GET_VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD())
		self.__SetPeacePKMode()

		#global MOBILE
		if MOBILE:
			self.inputMobileButton.SetEvent(ui.__mem_func__(self.__OnChangeMobilePhoneNumber))
			self.deleteMobileButton.SetEvent(ui.__mem_func__(self.__OnDeleteMobilePhoneNumber))

	def __ClickRadioButton(self, buttonList, buttonIndex):
		try:
			selButton=buttonList[buttonIndex]
		except IndexError:
			return

		for eachButton in buttonList:
			eachButton.SetUp()

		selButton.Down()

	def RefreshPets(self):
		if systemSetting.IsHidePets():
			self.showPets[0].SetUp()
			self.showPets[1].Down()
		else:
			self.showPets[0].Down()
			self.showPets[1].SetUp()

	def RefreshMounts(self):
		if systemSetting.IsHideMounts():
			self.showMounts[0].SetUp()
			self.showMounts[1].Down()
		else:
			self.showMounts[0].Down()
			self.showMounts[1].SetUp()

	def RefreshShops(self):
		if systemSetting.IsHideShops():
			self.showShops[0].SetUp()
			self.showShops[1].Down()
		else:
			self.showShops[0].Down()
			self.showShops[1].SetUp()

	"""if app.ENABLE_HIDE_COSTUMES_CLIENTSIDE:
		def RefreshCostumes(self):
			if systemSetting.IsHideCostumes():
				self.showCostumes[0].SetUp()
				self.showCostumes[1].Down()
			else:
				self.showCostumes[0].Down()
				self.showCostumes[1].SetUp()

	if app.ENABLE_HIDE_SHINING_EFFECTS:
		def RefreshShinings(self):
			if systemSetting.IsHideShinings():
				self.showShinings[0].SetUp()
				self.showShinings[1].Down()
			else:
				self.showShinings[0].Down()
				self.showShinings[1].SetUp()"""
			
	def __OnClickHidePetsButtonOn(self):
		systemSetting.SetHidePets(False)
		self.RefreshPets()

	def __OnClickHidePetsButtonOff(self):
		systemSetting.SetHidePets(True)
		self.RefreshPets()

	def __OnClickHideMountsButtonOn(self):
		systemSetting.SetHideMounts(False)
		self.RefreshMounts()	

	def __OnClickHideMountsButtonOff(self):
		systemSetting.SetHideMounts(True)
		self.RefreshMounts()	
		
	def __OnClickHideShopsButtonOn(self):
		systemSetting.SetHideShops(False)
		systemSetting.SetShowSalesTextFlag(True)
		self.RefreshShops()

	def __OnClickHideShopsButtonOff(self):
		systemSetting.SetHideShops(True)
		systemSetting.SetShowSalesTextFlag(False)
		self.RefreshShops()

	def __OnClickHideCostumesButtonOn(self):
		systemSetting.SetHideCostumes(False)
		self.RefreshCostumes()

	def __OnClickHideCostumesButtonOff(self):
		systemSetting.SetHideCostumes(True)
		self.RefreshCostumes()

	def __OnClickHideShiningsButtonOn(self):
		systemSetting.SetHideShinings(False)
		self.RefreshShinings()

	def __OnClickHideShiningsButtonOff(self):
		systemSetting.SetHideShinings(True)
		self.RefreshShinings()

	def __SetNameColorMode(self, index):
		constInfo.SET_CHRNAME_COLOR_INDEX(index)
		self.__ClickRadioButton(self.nameColorModeButtonList, index)

	def __SetTargetBoardViewMode(self, flag):
		constInfo.SET_VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD(flag)
		self.__ClickRadioButton(self.viewTargetBoardButtonList, flag)

	def __OnClickNameColorModeNormalButton(self):
		self.__SetNameColorMode(0)

	def __OnClickNameColorModeEmpireButton(self):
		self.__SetNameColorMode(1)

	def __OnClickTargetBoardViewButton(self):
		self.__SetTargetBoardViewMode(0)

	def __OnClickTargetBoardNoViewButton(self):
		self.__SetTargetBoardViewMode(1)

	def __OnClickCameraModeShortButton(self):
		self.__SetCameraMode(0)

	def __OnClickCameraModeLongButton(self):
		self.__SetCameraMode(1)

	def __OnClickFogModeLevel0Button(self):
		self.__SetFogLevel(0)

	def __OnClickFogModeLevel1Button(self):
		self.__SetFogLevel(1)

	def __OnClickFogModeLevel2Button(self):
		self.__SetFogLevel(2)

	def __OnClickBlockExchangeButton(self):
		self.RefreshBlock()
		global blockMode
		net.SendChatPacket("/setblockmode " + str(blockMode ^ player.BLOCK_EXCHANGE))
	def __OnClickBlockPartyButton(self):
		self.RefreshBlock()
		global blockMode
		net.SendChatPacket("/setblockmode " + str(blockMode ^ player.BLOCK_PARTY))
	def __OnClickBlockGuildButton(self):
		self.RefreshBlock()
		global blockMode
		net.SendChatPacket("/setblockmode " + str(blockMode ^ player.BLOCK_GUILD))
	def __OnClickBlockWhisperButton(self):
		self.RefreshBlock()
		global blockMode
		net.SendChatPacket("/setblockmode " + str(blockMode ^ player.BLOCK_WHISPER))
	def __OnClickBlockFriendButton(self):
		self.RefreshBlock()
		global blockMode
		net.SendChatPacket("/setblockmode " + str(blockMode ^ player.BLOCK_FRIEND))
	def __OnClickBlockPartyRequest(self):
		self.RefreshBlock()
		global blockMode
		net.SendChatPacket("/setblockmode " + str(blockMode ^ player.BLOCK_PARTY_REQUEST))

	def __OnClickViewChatOnButton(self):
		global viewChatMode
		viewChatMode = 1
		systemSetting.SetViewChatFlag(viewChatMode)
		self.RefreshViewChat()
	def __OnClickViewChatOffButton(self):
		global viewChatMode
		viewChatMode = 0
		systemSetting.SetViewChatFlag(viewChatMode)
		self.RefreshViewChat()

	def __OnClickAlwaysShowNameOnButton(self):
		systemSetting.SetAlwaysShowNameFlag(TRUE)
		self.RefreshAlwaysShowName()

	def __OnClickAlwaysShowNameOffButton(self):
		systemSetting.SetAlwaysShowNameFlag(FALSE)
		self.RefreshAlwaysShowName()

	def __OnClickShowDamageOnButton(self):
		systemSetting.SetShowDamageFlag(TRUE)
		self.RefreshShowDamage()

	def __OnClickShowDamageOffButton(self):
		systemSetting.SetShowDamageFlag(FALSE)
		self.RefreshShowDamage()
		
	def __OnClickSalesTextOnButton(self):
		systemSetting.SetShowSalesTextFlag(TRUE)
		self.RefreshShowSalesText()
		uiPrivateShopBuilder.UpdateADBoard()
		
	def __OnClickSalesTextOffButton(self):
		systemSetting.SetShowSalesTextFlag(FALSE)
		self.RefreshShowSalesText()	

	"""if app.ENABLE_RELOAD_SKILLS:
		def __OnClickModdedSkillsOnButton(self):
			systemSetting.SetShowModdedSkillsFlag(True)
			self.RefreshShowModdedSkills()
			skill.LoadSkillData()

		def __OnClickModdedSkillsOffButton(self):
			systemSetting.SetShowModdedSkillsFlag(False)
			self.RefreshShowModdedSkills()
			skill.LoadSkillData()"""

	def __OnClickRenderTargetOnButton(self):
		systemSetting.SetRenderTargetTextFlag(True)
		self.RefreshRenderTarget()

	def __OnClickRenderTargetOffButton(self):
		systemSetting.SetRenderTargetTextFlag(False)
		self.RefreshRenderTarget()	

	def __OnClickYangTextOnButton(self):
		systemSetting.SetShowYang(True)
		self.RefreshShowYangText()
		
	def __OnClickYangTextOffButton(self):
		systemSetting.SetShowYang(False)
		self.RefreshShowYangText()

	def __OnClickMobEffectsOnButton(self):
		systemSetting.SetShowMonsterEffectsFlag(True)
		self.RefreshMobEffects()

	def __OnClickMobEffectsOffButton(self):
		systemSetting.SetShowMonsterEffectsFlag(False)
		self.RefreshMobEffects()

	def __OnClickSkillEffectsOnButton(self):
		systemSetting.SetShowSkillEffectsFlag(True)
		self.RefreshSkillEffects()

	def __OnClickSkillEffectsOffButton(self):
		systemSetting.SetShowSkillEffectsFlag(False)
		self.RefreshSkillEffects()

	def __OnClickBuffEffectsOnButton(self):
		systemSetting.SetShowBuffEffectsFlag(True)
		self.RefreshBuffEffects()

	def __OnClickBuffEffectsOffButton(self):
		systemSetting.SetShowBuffEffectsFlag(False)
		self.RefreshBuffEffects()

	if app.ENABLE_DYNASTY_DUELLSTYLE:
		def __OnClickDynastyOnButton(self):
			systemSetting.SetShowDynastyTextFlag(True)
			self.RefreshDynastyText()
			
		def __OnClickDynastyOffButton(self):
			systemSetting.SetShowDynastyTextFlag(False)
			self.RefreshDynastyText()

	def __CheckPvPProtectedLevelPlayer(self):	
		if player.GetStatus(player.LEVEL)<constInfo.PVPMODE_PROTECTED_LEVEL:
			self.__SetPeacePKMode()
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_PROTECT % (constInfo.PVPMODE_PROTECTED_LEVEL))
			return 1

		return 0

	def __SetPKMode(self, mode):
		for btn in self.pvpModeButtonDict.values():
			btn.SetUp()
		if self.pvpModeButtonDict.has_key(mode):
			self.pvpModeButtonDict[mode].Down()

	def __SetPeacePKMode(self):
		self.__SetPKMode(player.PK_MODE_PEACE)

	def __RefreshPVPButtonList(self):
		self.__SetPKMode(player.GetPKMode())

	def __OnClickPvPModePeaceButton(self):
		if self.__CheckPvPProtectedLevelPlayer():
			return

		self.__RefreshPVPButtonList()

		if constInfo.PVPMODE_ENABLE:
			net.SendChatPacket("/pkmode 0", chat.CHAT_TYPE_TALKING)
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_NOT_SUPPORT)

	def __OnClickPvPModeRevengeButton(self):
		if self.__CheckPvPProtectedLevelPlayer():
			return

		self.__RefreshPVPButtonList()

		if constInfo.PVPMODE_ENABLE:
			net.SendChatPacket("/pkmode 1", chat.CHAT_TYPE_TALKING)
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_NOT_SUPPORT)

	def __OnClickPvPModeFreeButton(self):
		if self.__CheckPvPProtectedLevelPlayer():
			return

		self.__RefreshPVPButtonList()

		if constInfo.PVPMODE_ENABLE:
			net.SendChatPacket("/pkmode 2", chat.CHAT_TYPE_TALKING)
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_NOT_SUPPORT)

	def __OnClickPvPModeGuildButton(self):
		if self.__CheckPvPProtectedLevelPlayer():
			return

		self.__RefreshPVPButtonList()

		if 0 == player.GetGuildID():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_CANNOT_SET_GUILD_MODE)
			return

		if constInfo.PVPMODE_ENABLE:
			net.SendChatPacket("/pkmode 4", chat.CHAT_TYPE_TALKING)
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_NOT_SUPPORT)

	def OnChangePKMode(self):
		self.__RefreshPVPButtonList()

	def __OnChangeMobilePhoneNumber(self):
		global MOBILE
		if not MOBILE:
			return

		import uiCommon
		inputDialog = uiCommon.InputDialog()
		inputDialog.SetTitle(localeInfo.MESSENGER_INPUT_MOBILE_PHONE_NUMBER_TITLE)
		inputDialog.SetMaxLength(13)
		inputDialog.SetAcceptEvent(ui.__mem_func__(self.OnInputMobilePhoneNumber))
		inputDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseInputDialog))
		inputDialog.Open()
		self.inputDialog = inputDialog

	def __OnDeleteMobilePhoneNumber(self):
		global MOBILE
		if not MOBILE:
			return

		import uiCommon
		questionDialog = uiCommon.QuestionDialog()
		questionDialog.SetText(localeInfo.MESSENGER_DO_YOU_DELETE_PHONE_NUMBER)
		questionDialog.SetAcceptEvent(ui.__mem_func__(self.OnDeleteMobile))
		questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
		questionDialog.Open()
		self.questionDialog = questionDialog

	def OnInputMobilePhoneNumber(self):
		global MOBILE
		if not MOBILE:
			return

		text = self.inputDialog.GetText()

		if not text:
			return

		text.replace('-', '')
		net.SendChatPacket("/mobile " + text)
		self.OnCloseInputDialog()
		return TRUE

	def OnInputMobileAuthorityCode(self):
		global MOBILE
		if not MOBILE:
			return

		text = self.inputDialog.GetText()
		net.SendChatPacket("/mobile_auth " + text)
		self.OnCloseInputDialog()
		return TRUE

	def OnDeleteMobile(self):
		global MOBILE
		if not MOBILE:
			return

		net.SendChatPacket("/mobile")
		self.OnCloseQuestionDialog()
		return TRUE

	def OnCloseInputDialog(self):
		self.inputDialog.Close()
		self.inputDialog = None
		return TRUE

	def OnCloseQuestionDialog(self):
		self.questionDialog.Close()
		self.questionDialog = None
		return TRUE

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	def RefreshMobile(self):
		global MOBILE
		if not MOBILE:
			return

		if player.HasMobilePhoneNumber():
			self.inputMobileButton.Hide()
			self.deleteMobileButton.Show()
		else:
			self.inputMobileButton.Show()
			self.deleteMobileButton.Hide()

	def OnMobileAuthority(self):
		global MOBILE
		if not MOBILE:
			return

		import uiCommon
		inputDialog = uiCommon.InputDialogWithDescription()
		inputDialog.SetTitle(localeInfo.MESSENGER_INPUT_MOBILE_AUTHORITY_TITLE)
		inputDialog.SetDescription(localeInfo.MESSENGER_INPUT_MOBILE_AUTHORITY_DESCRIPTION)
		inputDialog.SetAcceptEvent(ui.__mem_func__(self.OnInputMobileAuthorityCode))
		inputDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseInputDialog))
		inputDialog.SetMaxLength(4)
		inputDialog.SetBoardWidth(310)
		inputDialog.Open()
		self.inputDialog = inputDialog

	def RefreshBlock(self):
		global blockMode
		for i in xrange(len(self.blockButtonList)):
			if 0 != (blockMode & (1 << i)):
				self.blockButtonList[i].Down()
			else:
				self.blockButtonList[i].SetUp()

	def RefreshViewChat(self):
		if systemSetting.IsViewChat():
			self.viewChatButtonList[0].Down()
			self.viewChatButtonList[1].SetUp()
		else:
			self.viewChatButtonList[0].SetUp()
			self.viewChatButtonList[1].Down()

	def RefreshAlwaysShowName(self):
		if systemSetting.IsAlwaysShowName():
			self.alwaysShowNameButtonList[0].Down()
			self.alwaysShowNameButtonList[1].SetUp()
		else:
			self.alwaysShowNameButtonList[0].SetUp()
			self.alwaysShowNameButtonList[1].Down()

	def RefreshShowDamage(self):
		if systemSetting.IsShowDamage():
			self.showDamageButtonList[0].Down()
			self.showDamageButtonList[1].SetUp()
		else:
			self.showDamageButtonList[0].SetUp()
			self.showDamageButtonList[1].Down()
			
	def RefreshShowSalesText(self):
		if systemSetting.IsShowSalesText():
			self.showsalesTextButtonList[0].Down()
			self.showsalesTextButtonList[1].SetUp()
		else:
			self.showsalesTextButtonList[0].SetUp()
			self.showsalesTextButtonList[1].Down()

	"""if app.ENABLE_RELOAD_SKILLS:
		def RefreshShowModdedSkills(self):
			if systemSetting.IsShowModdedSkills():
				self.showModdedSkillsButtonList[0].Down()
				self.showModdedSkillsButtonList[1].SetUp()
			else:
				self.showModdedSkillsButtonList[0].SetUp()
				self.showModdedSkillsButtonList[1].Down()"""

	def RefreshMobEffects(self):
		if systemSetting.IsShowMonsterEffects():
			self.showMobEffectsButtonList[0].Down()
			self.showMobEffectsButtonList[1].SetUp()
		else:
			self.showMobEffectsButtonList[0].SetUp()
			self.showMobEffectsButtonList[1].Down()

	def RefreshSkillEffects(self):
		if systemSetting.IsShowSkillEffects():
			self.showSkillEffectsButtonList[0].Down()
			self.showSkillEffectsButtonList[1].SetUp()
		else:
			self.showSkillEffectsButtonList[0].SetUp()
			self.showSkillEffectsButtonList[1].Down()

	def RefreshBuffEffects(self):
		if systemSetting.IsShowBuffEffects():
			self.showBuffEffectsButtonList[0].Down()
			self.showBuffEffectsButtonList[1].SetUp()
		else:
			self.showBuffEffectsButtonList[0].SetUp()
			self.showBuffEffectsButtonList[1].Down()

	def RefreshShowYangText(self):
		if systemSetting.IsShowYang():
			self.showyangTextButtonList[0].Down()
			self.showyangTextButtonList[1].SetUp()
		else:
			self.showyangTextButtonList[0].SetUp()
			self.showyangTextButtonList[1].Down()

	def RefreshRenderTarget(self):
		if systemSetting.IsShowRenderTarget():
			self.renderTarget[0].Down()
			self.renderTarget[1].SetUp()
		else:
			self.renderTarget[0].SetUp()
			self.renderTarget[1].Down()

	if app.ENABLE_DYNASTY_DUELLSTYLE:
		def RefreshDynastyText(self):
			if systemSetting.IsShowDynastyFlag():
				self.showDynastyButtonList[0].Down()
				self.showDynastyButtonList[1].SetUp()
			else:
				self.showDynastyButtonList[0].SetUp()
				self.showDynastyButtonList[1].Down()

	def OnBlockMode(self, mode):
		global blockMode
		blockMode = mode
		self.RefreshBlock()

	def Show(self):
		self.RefreshMobile()
		self.RefreshBlock()
		ui.ScriptWindow.Show(self)

	def Close(self):
		self.Hide()
