import app, uiScriptLocale, os, sys, re

ME_KEY = 0

Day_Night = 0

BLEND_TXT = """#적상액						
section						
	item_vnum	50821				
	apply_type	124				
	apply_value	5	5	5	5	5
	apply_duration	1200	1200	1200	1200	1200
end						
						
#홍상액						
section						
	item_vnum	50822				
	apply_type	16		
	apply_value	20	20	20	20	20
	apply_duration	1200	1200	1200	1200	1200
end						
						
#황상액						
section						
	item_vnum	50823				
	apply_type	126
	apply_value	5	5	5	5	5
	apply_duration	1200	1200	1200	1200	1200
end						
						
#녹상액						
section						
	item_vnum	50824				
	apply_type	17			
	apply_value	20	20	20	20	20
	apply_duration	1200	1200	1200	1200	1200
end						

#청상액						
section						
	item_vnum	50825				
	apply_type	63				
	apply_value	30	30	30	30	30
	apply_duration	1200	1200	1200	1200	1200
end						

#백상액						
section						
	item_vnum	50826				
	apply_type	54				
	apply_value	350	350	350	350	350
	apply_duration	1200	1200	1200	1200	1200
end

#	Drachengott-Leben
section
	item_vnum	71027
	apply_type	69
	apply_value	20	20	20	20	20
	apply_duration	1200	1200	1200	1200	1200
end

#	Drachengott-Angriff
section
	item_vnum	71028
	apply_type	64
	apply_value	20	20	20	20	20
	apply_duration	1200	1200	1200	1200	1200
end

#	Drachengott-Intelligenz
section
	item_vnum	71029
	apply_type	70
	apply_value	20	20	20	20	20
	apply_duration	1200	1200	1200	1200	1200
end

#	Drachengott-Verteidigung
section
	item_vnum	71030
	apply_type	65
	apply_value	20	20	20	20	20
	apply_duration	1200	1200	1200	1200	1200
end

#	Krit-Kampf
section
	item_vnum	71044
	apply_type	15
	apply_value	20	20	20	20	20
	apply_duration	1200	1200	1200	1200	1200
end

#	Db-Kampf
section
	item_vnum	71045
	apply_type	16
	apply_value	20	20	20	20	20
	apply_duration	1200	1200	1200	1200	1200
end

#	Geschwindigkeitstrank
section
	item_vnum	71050
	apply_type	8
	apply_value	60	60	60	60	60
	apply_duration	1200	1200	1200	1200	1200
end

#	Angriffsgeschwindigkeitstrank
section
	item_vnum	27112
	apply_type	7
	apply_value	30	30	30	30	30
	apply_duration	1200	1200	1200	1200	1200
end

#충기환
section
	item_vnum	51002
	apply_type	82
	apply_value	1	3	5	7	10
	apply_duration	1800	1800	1800	1800	1800
end

#	Anti EXP Ring
section
	item_vnum	72501
	apply_type	POINT_ANTI_EXP
	apply_value	1	1	1	1	1
	apply_duration	9999	9999	9999	9999	9999
end
#	Magietrank
section
	item_vnum	31163
	apply_type	37
	apply_value	15	15	15	15	15
	apply_duration	1200	1200	1200	1200	1200
end
section
	item_vnum	51002
	apply_type	82
	apply_value	1	3	5	7	10
	apply_duration	1800	1800	1800	1800	1800
end
"""

regengenerator = "0/0/0/0"

if app.ENABLE_HIDE_COSTUME_SYSTEM:
	HIDDEN_BODY_COSTUME = 0
	HIDDEN_HAIR_COSTUME = 0
	HIDDEN_ACCE_COSTUME = 0
	HIDDEN_WEAPON_COSTUME = 0

finder_counts = 0
finder_items = {}

def load_blend():
	data = []
	for i, line in enumerate(BLEND_TXT.split('\n')):
		if "section" in line:
			data.append([])	
		elif "item_vnum" in line or "apply_type" in line:
			data[len(data)-1].append(line.split()[1])
		elif "apply_value" in line:
			attr_value = []
			for value in line.split()[1:]:
				attr_value.append(value)
			data[len(data)-1].append(attr_value)
		elif "apply_duration" in line:
			times_in_seconds = []
			for time in line.split()[1:]:
				times_in_seconds.append(time)
			data[len(data)-1].append(times_in_seconds)
	return data

if app.ENABLE_MULTI_LANGUAGE_SYSTEM:
	LOCALE_LANG_DICT = {
			app.LOCALE_EN : { "name" : uiScriptLocale.LANGUAGE_EN, "locale" : "en", "code_page" : 1252 },
			app.LOCALE_DE : { "name" : uiScriptLocale.LANGUAGE_DE, "locale" : "de", "code_page" : 1252 },
			#app.LOCALE_PT : { "name" : uiScriptLocale.LANGUAGE_PT, "locale" : "pt", "code_page" : 1252 },
			# app.LOCALE_ES : { "name" : uiScriptLocale.LANGUAGE_ES, "locale" : "es", "code_page" : 1252 },
			# app.LOCALE_FR : { "name" : uiScriptLocale.LANGUAGE_FR, "locale" : "fr", "code_page" : 1252 },
			# app.LOCALE_RO : { "name" : uiScriptLocale.LANGUAGE_RO, "locale" : "ro", "code_page" : 1250 },
			# app.LOCALE_PL : { "name" : uiScriptLocale.LANGUAGE_PL, "locale" : "pl", "code_page" : 1250 },
			# app.LOCALE_IT : { "name" : uiScriptLocale.LANGUAGE_IT, "locale" : "it", "code_page" : 1252 },
			# app.LOCALE_CZ : { "name" : uiScriptLocale.LANGUAGE_CZ, "locale" : "cz", "code_page" : 1250 },
			# app.LOCALE_HU : { "name" : uiScriptLocale.LANGUAGE_HU, "locale" : "hu", "code_page" : 1250 },
			# app.LOCALE_TR : { "name" : uiScriptLocale.LANGUAGE_TR, "locale" : "tr", "code_page" : 1254 },
		}

DYNASTY_COUNT = 0

if app.ENABLE_CHANNEL_SWITCHER:
	CHANNELS = 4

def getLogText(exception):
	exc_type, exc_obj, exc_tb = sys.exc_info()
	fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
	return 'File: %s(%s)\nFunction: %s\nError: %s\nException: %s\n' % (fname, str(exc_tb.tb_lineno), sys._getframe().f_code.co_name, str(exc_type), str(exception))

if app.ENABLE_TARGET_INFO:
	MONSTER_INFO_DATA = {}

IS_AUTO_REFINE = False
AUTO_REFINE_TYPE = 0
AUTO_REFINE_DATA = {
	"ITEM" : [-1, -1],
	"NPC" : [0, -1, -1, 0]
}

DISABLE_MODEL_PREVIEW = 0
PICKUP_MODE = 0
PICKUP_FLAG = 0
IN_GAME_SHOP_ENABLE = 1
CONSOLE_ENABLE = 0

PVPMODE_ENABLE = 1
PVPMODE_TEST_ENABLE = 0
PVPMODE_ACCELKEY_ENABLE = 1
PVPMODE_ACCELKEY_DELAY = 0.5
PVPMODE_PROTECTED_LEVEL = 30

INPUT_IGNORE = 0

FOG_LEVEL0 = 4800.0
FOG_LEVEL1 = 9600.0
FOG_LEVEL2 = 12800.0
FOG_LEVEL = FOG_LEVEL0
FOG_LEVEL_LIST=[FOG_LEVEL0, FOG_LEVEL1, FOG_LEVEL2]		

CAMERA_MAX_DISTANCE_SHORT = 4000.0
CAMERA_MAX_DISTANCE_LONG = 6000.0
CAMERA_MAX_DISTANCE_LIST=[CAMERA_MAX_DISTANCE_SHORT, CAMERA_MAX_DISTANCE_LONG]
CAMERA_MAX_DISTANCE = CAMERA_MAX_DISTANCE_SHORT

GET_ITEM_DROP_QUESTION_DIALOG_STATUS = 1

CHRNAME_COLOR_INDEX = 0

SET_MAINTENANCE_SHOW = 1

bIsDEV = False
SERVER_LIVE = True
SERVER_DEV = False
SERVER_LOCAL = False

ENVIRONMENT_NIGHT="d:/ymir work/environment/moonlight04.msenv"

# constant
HIGH_PRICE = 500000
MIDDLE_PRICE = 50000
ERROR_METIN_STONE = 28960
EXPANDED_COMBO_ENABLE = 1
CONVERT_EMPIRE_LANGUAGE_ENABLE = 1
USE_ITEM_WEAPON_TABLE_ATTACK_BONUS = 0
ADD_DEF_BONUS_ENABLE = 1
LOGIN_COUNT_LIMIT_ENABLE = 0

USE_SKILL_EFFECT_UPGRADE_ENABLE = 1

VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD = 1
GUILD_MONEY_PER_GSP = 100
GUILD_WAR_TYPE_SELECT_ENABLE = 1
TWO_HANDED_WEAPON_ATT_SPEED_DECREASE_VALUE = 0

HAIR_COLOR_ENABLE = 1
CONVERT_EMPIRE_LANGUAGE_ENABLE = 0
ARMOR_SPECULAR_ENABLE = 1
WEAPON_SPECULAR_ENABLE = 1
SEQUENCE_PACKET_ENABLE = 0
KEEP_ACCOUNT_CONNETION_ENABLE = 1
MINIMAP_POSITIONINFO_ENABLE = 1
USE_ITEM_WEAPON_TABLE_ATTACK_BONUS = 0
ADD_DEF_BONUS_ENABLE = 0
LOGIN_COUNT_LIMIT_ENABLE = 0
PVPMODE_PROTECTED_LEVEL = 15
TWO_HANDED_WEAPON_ATT_SPEED_DECREASE_VALUE = 10

isItemQuestionDialog = 0

#### Battle Pass System #####
missions_bp = {}
info_missions_bp = {}
rewards_bp = {}
final_rewards = []
size_battle_pass = 0
status_battle_pass = 0
#### Battle Pass System END #####

def GET_ITEM_QUESTION_DIALOG_STATUS():
	global isItemQuestionDialog
	return isItemQuestionDialog

def SET_ITEM_QUESTION_DIALOG_STATUS(flag):
	global isItemQuestionDialog
	isItemQuestionDialog = flag

import app
import net

def SET_DEFAULT_FOG_LEVEL():
	global FOG_LEVEL
	app.SetMinFog(FOG_LEVEL)

def SET_FOG_LEVEL_INDEX(index):
	global FOG_LEVEL
	global FOG_LEVEL_LIST
	try:
		FOG_LEVEL=FOG_LEVEL_LIST[index]
	except IndexError:
		FOG_LEVEL=FOG_LEVEL_LIST[0]
	app.SetMinFog(FOG_LEVEL)

def GET_FOG_LEVEL_INDEX():
	global FOG_LEVEL
	global FOG_LEVEL_LIST
	return FOG_LEVEL_LIST.index(FOG_LEVEL)

def SET_DEFAULT_CAMERA_MAX_DISTANCE():
	global CAMERA_MAX_DISTANCE
	app.SetCameraMaxDistance(CAMERA_MAX_DISTANCE)

def SET_CAMERA_MAX_DISTANCE_INDEX(index):
	global CAMERA_MAX_DISTANCE
	global CAMERA_MAX_DISTANCE_LIST
	try:
		CAMERA_MAX_DISTANCE=CAMERA_MAX_DISTANCE_LIST[index]
	except:
		CAMERA_MAX_DISTANCE=CAMERA_MAX_DISTANCE_LIST[0]

	app.SetCameraMaxDistance(CAMERA_MAX_DISTANCE)

def GET_CAMERA_MAX_DISTANCE_INDEX():
	global CAMERA_MAX_DISTANCE
	global CAMERA_MAX_DISTANCE_LIST
	return CAMERA_MAX_DISTANCE_LIST.index(CAMERA_MAX_DISTANCE)

import chrmgr
import player
import app

def SET_DEFAULT_CHRNAME_COLOR():
	global CHRNAME_COLOR_INDEX
	chrmgr.SetEmpireNameMode(CHRNAME_COLOR_INDEX)

def SET_CHRNAME_COLOR_INDEX(index):
	global CHRNAME_COLOR_INDEX
	CHRNAME_COLOR_INDEX=index
	chrmgr.SetEmpireNameMode(index)

def GET_CHRNAME_COLOR_INDEX():
	global CHRNAME_COLOR_INDEX
	return CHRNAME_COLOR_INDEX

def SET_VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD(index):
	global VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD
	VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD = index

def GET_VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD():
	global VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD
	return VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD

def SET_DEFAULT_CONVERT_EMPIRE_LANGUAGE_ENABLE():
	global CONVERT_EMPIRE_LANGUAGE_ENABLE
	net.SetEmpireLanguageMode(CONVERT_EMPIRE_LANGUAGE_ENABLE)

def SET_DEFAULT_USE_ITEM_WEAPON_TABLE_ATTACK_BONUS():
	global USE_ITEM_WEAPON_TABLE_ATTACK_BONUS
	player.SetWeaponAttackBonusFlag(USE_ITEM_WEAPON_TABLE_ATTACK_BONUS)

def SET_DEFAULT_USE_SKILL_EFFECT_ENABLE():
	global USE_SKILL_EFFECT_UPGRADE_ENABLE
	app.SetSkillEffectUpgradeEnable(USE_SKILL_EFFECT_UPGRADE_ENABLE)

def SET_TWO_HANDED_WEAPON_ATT_SPEED_DECREASE_VALUE():
	global TWO_HANDED_WEAPON_ATT_SPEED_DECREASE_VALUE
	app.SetTwoHandedWeaponAttSpeedDecreaseValue(TWO_HANDED_WEAPON_ATT_SPEED_DECREASE_VALUE)

########################
import item

ACCESSORY_MATERIAL_LIST = [50623, 50624, 50625, 50626, 50627, 50628, 50629, 50630, 50631, 50632, 50633, 50634, 50635, 50636, 50637, 50638, 50639]
#ACCESSORY_MATERIAL_LIST = [50623, 50623, 50624, 50624, 50625, 50625, 50626, 50627, 50628, 50629, 50630, 50631, 50632, 50633, 
#			    50623, 50623, 50624, 50624, ]
JewelAccessoryInfos = [
		# jewel		wrist	neck	ear
		[ 50634,	14420,	16220,	17220 ],	
		[ 50635,	14500,	16500,	17500 ],	
		[ 50636,	14520,	16520,	17520 ],	
		[ 50637,	14540,	16540,	17540 ],	
		[ 50638,	14560,	16560,	17560 ],	
		[ 50639,	14570,	16570,	17570 ],	
	]
def GET_ACCESSORY_MATERIAL_VNUM(vnum, subType):
	ret = vnum
	item_base = (vnum / 10) * 10
	for info in JewelAccessoryInfos:
		if item.ARMOR_WRIST == subType:	
			if info[1] == item_base:
				return info[0]
		elif item.ARMOR_NECK == subType:	
			if info[2] == item_base:
				return info[0]
		elif item.ARMOR_EAR == subType:	
			if info[3] == item_base:
				return info[0]
 
	if vnum >= 16210 and vnum <= 16219:
		return 50625

	if item.ARMOR_WRIST == subType:	
		WRIST_ITEM_VNUM_BASE = 14000
		ret -= WRIST_ITEM_VNUM_BASE
	elif item.ARMOR_NECK == subType:
		NECK_ITEM_VNUM_BASE = 16000
		ret -= NECK_ITEM_VNUM_BASE
	elif item.ARMOR_EAR == subType:
		EAR_ITEM_VNUM_BASE = 17000
		ret -= EAR_ITEM_VNUM_BASE

	type = ret/20

	if type<0 or type>=len(ACCESSORY_MATERIAL_LIST):
		type = (ret-170) / 20
		if type<0 or type>=len(ACCESSORY_MATERIAL_LIST):
			return 0

	return ACCESSORY_MATERIAL_LIST[type]

##################################################################
## 새로 추가된 '벨트' 아이템 타입과, 벨트의 소켓에 꽂을 아이템 관련.. 
## 벨트의 소켓시스템은 악세서리와 동일하기 때문에, 위 악세서리 관련 하드코딩처럼 이런식으로 할 수밖에 없다..

def GET_BELT_MATERIAL_VNUM(vnum, subType = 0):
	# 현재는 모든 벨트에는 하나의 아이템(#18900)만 삽입 가능
	return 18900

##################################################################
## 자동물약 (HP: #72723 ~ #72726, SP: #72727 ~ #72730)

def IS_NEW_POTION(itemVnum):
	return IS_NEW_POTION_BACKEND(itemVnum)

def IS_NEW_POTION_BACKEND(itemVnum):
	if 50821 == itemVnum or 50822 == itemVnum or 50823 == itemVnum or 50824 == itemVnum or 50825 == itemVnum or 50826 == itemVnum:
		return 1
	if 71044 == itemVnum or 71045 == itemVnum or 71050 == itemVnum:
		return 1
	if 27112 == itemVnum:
		return 1
	if 31163 == itemVnum:
		return 1
	if 72501 == itemVnum: # AntiEXP
		return 1
	return 0

# 해당 vnum이 자동물약인가?
def IS_AUTO_POTION(itemVnum):
	return IS_AUTO_POTION_HP(itemVnum) or IS_AUTO_POTION_SP(itemVnum)
	
# 해당 vnum이 HP 자동물약인가?
def IS_AUTO_POTION_HP(itemVnum):
	if 72723 <= itemVnum and 72726 >= itemVnum:
		return 1
	elif itemVnum >= 76021 and itemVnum <= 76022:		## 새로 들어간 선물용 화룡의 축복
		return 1
	elif itemVnum == 79012:
		return 1
		
	return 0
	
# 해당 vnum이 SP 자동물약인가?
def IS_AUTO_POTION_SP(itemVnum):
	if 72727 <= itemVnum and 72730 >= itemVnum:
		return 1
	elif itemVnum >= 76004 and itemVnum <= 76005:		## 새로 들어간 선물용 수룡의 축복
		return 1
	elif itemVnum == 79013:
		return 1
				
	return 0

