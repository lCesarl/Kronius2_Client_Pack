import uiScriptLocale

window = {
	"name" : "GameWindow",
	"style" : ("not_pick",),

	"x" : 0,
	"y" : 0,

	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,

	"children" :
	(
		{ 
			"name":"HelpButton", 
			"type":"button", 
			"x" : 50,
			"y" : SCREEN_HEIGHT-170,
			"default_image" : "d:/ymir work/interface/Illumina_vegas/button/stats_increase_01_normal.tga",
			"over_image" : "d:/ymir work/interface/Illumina_vegas/button/stats_increase_02_hover.tga",
			"down_image" : "d:/ymir work/interface/Illumina_vegas/button/stats_increase_03_active.tga",

			"children" : 
			(
				{ 
					"name":"HelpButtonLabel", 
					"type":"text", 
					"x": 16, 
					"y": 40, 
					"text":uiScriptLocale.GAME_HELP, 
					"r":1.0, "g":1.0, "b":1.0, "a":1.0, 
					"text_horizontal_align":"center" 
				},
			),
		},
		{ 
			"name":"QuestButton", 
			"type":"button", 
			"x" : SCREEN_WIDTH-50-32,
			"y" : SCREEN_HEIGHT-170,
			"default_image" : "d:/ymir work/interface/Illumina_vegas/button/stats_increase_01_normal.tga",
			"over_image" : "d:/ymir work/interface/Illumina_vegas/button/stats_increase_02_hover.tga",
			"down_image" : "d:/ymir work/interface/Illumina_vegas/button/stats_increase_03_active.tga",

			"children" : 
			(
				{ 
					"name":"QuestButtonLabel", 
					"type":"text", 
					"x": 16, 
					"y": 40, 
					"text":uiScriptLocale.GAME_QUEST, 
					"r":1.0, "g":1.0, "b":1.0, "a":1.0, 
					"text_horizontal_align":"center" 
				},
			),
		},
		{ 
			"name":"StatusPlusButton", 
			"type" : "button", 
			"x" : 80-50, ## 68
			"y" : SCREEN_HEIGHT-160, 
			"default_image" : "d:/ymir work/ui/yuma/status_points/char_points/char_points_button_01.tga",
			"over_image" : "d:/ymir work/ui/yuma/status_points/char_points/char_points_button_02.tga",
			"down_image" : "d:/ymir work/ui/yuma/status_points/char_points/char_points_button_03.tga",
		},			
		{ 
			"name":"SkillPlusButton", 
			"type" : "button", 
			"x" : SCREEN_WIDTH-50-25,
			"y" : SCREEN_HEIGHT-160,
			"default_image" : "d:/ymir work/ui/yuma/status_points/level_points/level_points_button_01.tga",
			"over_image" : "d:/ymir work/ui/yuma/status_points/level_points/level_points_button_02.tga",
			"down_image" : "d:/ymir work/ui/yuma/status_points/level_points/level_points_button_03.tga",
		},	


		{
			"name" : "BattlePass",
			"type" : "button",

			"x" : SCREEN_WIDTH-115,
			"y" : 220, 
			"default_image" : "d:/ymir work/battle_pass/open_battlepass.tga",
			"over_image" : "d:/ymir work/battle_pass/open_battlepass.tga",
			"down_image" : "d:/ymir work/battle_pass/open_battlepass.tga",
		},		

		{ 
			"name":"ExitObserver", 
			"type" : "button", 
			"x" : SCREEN_WIDTH-50-32,
			"y" : SCREEN_HEIGHT-170,
			"default_image" : "d:/ymir work/interface/Illumina_vegas/button/stats_increase_01_normal.tga",
			"over_image" : "d:/ymir work/interface/Illumina_vegas/button/stats_increase_02_hover.tga",
			"down_image" : "d:/ymir work/interface/Illumina_vegas/button/stats_increase_03_active.tga",

			"children" : 
			(
				{ 
					"name":"ExitObserverButtonName", 
					"type":"text", 
					"x": 16, 
					"y": 40, 
					"text": uiScriptLocale.GAME_EXIT_OBSERVER, 
					"r":1.0, "g":1.0, "b":1.0, "a":1.0, 
					"text_horizontal_align":"center" 
				},	
			),
		},
		{ 
			"name":"BuildGuildBuilding",
			"type" : "button",
			"x" : SCREEN_WIDTH-50-32,
			"y" : SCREEN_HEIGHT-170,
			"default_image" : "d:/ymir work/interface/Illumina_vegas/button/stats_increase_01_normal.tga",
			"over_image" : "d:/ymir work/interface/Illumina_vegas/button/stats_increase_02_hover.tga",
			"down_image" : "d:/ymir work/interface/Illumina_vegas/button/stats_increase_03_active.tga",

			"children" : 
			(
				{ 
					"name":"BuildGuildBuildingButtonName",
					"type":"text",
					"x": 16,
					"y": 40,
					"text": uiScriptLocale.GUILD_BUILDING_TITLE,
					"r":1.0, "g":1.0, "b":1.0, "a":1.0,
					"text_horizontal_align":"center"
				},	
			),
		},
	),
}
