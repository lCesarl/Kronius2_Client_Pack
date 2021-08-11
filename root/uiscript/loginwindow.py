import uiScriptLocale

PATH = "d:/ymir work/ui/login/logininterface/"

LOGIN_BOARD_MARGIN = 100
LOGIN_BOARD_MARGIN_X = 0

if SCREEN_HEIGHT < 800:
	LOGIN_BOARD_MARGIN = 100
	LOGIN_BOARD_MARGIN_X = 50
	
if SCREEN_HEIGHT < 610:
	LOGIN_BOARD_MARGIN = 130
	LOGIN_BOARD_MARGIN_X = 130
	
LOGIN_BOARD_POS_X = (SCREEN_WIDTH - 1150) / 2 + LOGIN_BOARD_MARGIN_X
LOGIN_BOARD_POS_Y = (SCREEN_HEIGHT/2) - LOGIN_BOARD_MARGIN

window = {
	"sytle" : ("movable",),
	"x" : 0, "y" : 0,
	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,
	"children" : 
	(
		## Background
		{
			"name" : "background", 
			"type" : "expanded_image",
			"x" : 0, "y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1920.0,
			"y_scale" : float(SCREEN_HEIGHT) / 1080.0,
			"image" : PATH + "background.tga",
		},
		###################################################
		## Logo
		{
			"name" : "kuba_logo",
			"type" : "image",
			'x' : ((SCREEN_WIDTH) / 2) - 400,
			"y" : (SCREEN_HEIGHT/2) - 275,
			"image" : PATH + "k2_logo.png",
		},
		#######################################
		## Board_Main
		{
			"name" : "board_main",
			"type" : "image",
			'x' : LOGIN_BOARD_POS_X,
			"y" : (LOGIN_BOARD_POS_Y - 20),
			"image" : PATH + "window.png",
			"children" :
			(
				{
					"name" : "saveacc_img",
					"type" : "image", 
					'x' : 133,
					"y" : 159,
					"image" : PATH + "account_save/window.png",
				},
				{
					"name" : "id_slotbar",
					"type" : "image",
					"x" : 0, "y" : -50,
					"horizontal_align" : "center",
					"vertical_align" : "center",
					"image" : PATH + "login/input_login.tga",
					"children" : 
					(
						{
							"name" : "id",
							"type" : "editline",
							"x" : 45, "y" : 11,
							"width" : 200, "height" : 16,
							"color" : 0xfff2d8c2,
							"input_limit": 16,
						},
					),
				},
				{
					"name" : "pwd_slotbar",
					"type" : "image",
					"x" : 0, "y" : -3,
					"horizontal_align" : "center",
					"vertical_align" : "center",
					"image" : PATH + "login/input_pw.tga",
					"children" : 
					(
						{
							"name" : "pwd",
							"type" : "editline",
							"x" : 45, "y" : 11,
							"width" : 200, "height" : 16,
							"color" : 0xfff2d8c2,
							"input_limit": 16,
							"secret_flag": 1,
						},
					),
				},
				{
					"name" : "login_button",
					"type" : "button",
					"x" : 90, "y" : 130,
					"horizontal_align" : "center", "vertical_align" : "center",
					"default_image" : PATH + "login/button/button_01.png", 
					"over_image" : PATH + "login/button/button_02.png", 
					"down_image" : PATH + "login/button/button_03.png", 
					"children" : 
					(
						{
							"name" : "login_button_text",
							"type" : "text",
							"x" : 65,
							"y" : 25,
							"color" : 0xffcccccc,
							"fontsize" : "LARGE",
							"text" : "Login",
						},
					),
				},
				{
					"name" : "save_button",
					"type" : "button",
					"x" : -79, "y" : 130,
					"horizontal_align" : "center", "vertical_align" : "center",
					"default_image" : PATH + "login/button/button_01.png", 
					"over_image" : PATH + "login/button/button_02.png", 
					"down_image" : PATH + "login/button/button_03.png", 
					"children" : 
					(
						{
							"name" : "login_button_text",
							"type" : "text",
							"x" : 65,
							"y" : 25,
							"color" : 0xffcccccc,
							"fontsize" : "LARGE",
							"text" : "Save",
						},
					),
				},
				## Channels
				{
					"name" : "ch1",
					"type" : "radio_button",
					"x" : 245, "y" : -18,
					"horizontal_align" : "center",
					"vertical_align" : "center",
					"default_image" : PATH + "checkbox/checkbox_01.tga",
					"over_image" : PATH + "checkbox/checkbox_02.tga",
					"down_image" : PATH + "checkbox/checkbox_03.tga",
				},
				{
					"name" : "ch2",
					"type" : "radio_button",
					"x" : 245, "y" : 43,
					"horizontal_align" : "center",
					"vertical_align" : "center",
					"default_image" : PATH + "checkbox/checkbox_01.tga",
					"over_image" : PATH + "checkbox/checkbox_02.tga",
					"down_image" : PATH + "checkbox/checkbox_03.tga",
				},
				{
					"name" : "ch3",
					"type" : "radio_button",
					"x" : 245, "y" : 100,
					"horizontal_align" : "center",
					"vertical_align" : "center",
					"default_image" : PATH + "checkbox/checkbox_01.tga",
					"over_image" : PATH + "checkbox/checkbox_02.tga",
					"down_image" : PATH + "checkbox/checkbox_03.tga",
				},
				{
					"name" : "ch4",
					"type" : "radio_button",
					"x" : 245, "y" : 150,
					"horizontal_align" : "center",
					"vertical_align" : "center",
					"default_image" : PATH + "checkbox/checkbox_01.tga",
					"over_image" : PATH + "checkbox/checkbox_02.tga",
					"down_image" : PATH + "checkbox/checkbox_03.tga",
				},
				###########################################################
				# # # # # # # # # 1 # #  # # # # # #
				{
					"name" : "saved_accs_acc1",
					"type" : "text",
					"x" : -365, 
					"y" : -30,
					"color" : 0xffcccccc,
					"horizontal_align" : "center",
					"vertical_align" : "center",
					"text": uiScriptLocale.LOGIN_INTERFACE_FREE_SPACE,
				},
				{
					"name" : "saved_accs_acc1_use",
					"type" : "button",
					"x" : -485, 
					"y" : -20,
					"default_image" : PATH + "checkbox/channel/checkbox_01.tga",
					"over_image" : PATH + "checkbox/channel/checkbox_02.tga",
					"down_image" : PATH + "checkbox/channel/checkbox_03.tga",
					"horizontal_align" : "center",
					"vertical_align" : "center",
				},
				{
					"name" : "saved_accs_acc1_del",
					"type" : "button",
					"x" : -435, 
					"y" : -20,
					"default_image" : PATH + "checkbox/channel/checkbox_x_01.tga",
					"over_image" : PATH + "checkbox/channel/checkbox_x_02.tga",
					"down_image" : PATH + "checkbox/channel/checkbox_x_03.tga",
					"horizontal_align" : "center",
					"vertical_align" : "center",
				},
				# # # # # # # # # 2 # #  # # # # # #
				{
					"name" : "saved_accs_acc2",
					"type" : "text",
					"x" : -365, 
					"y" : 26,
					"color" : 0xffcccccc,
					"horizontal_align" : "center",
					"vertical_align" : "center",
					"text": uiScriptLocale.LOGIN_INTERFACE_FREE_SPACE,
				},
				{
					"name" : "saved_accs_acc2_use",
					"type" : "button",
					"x" : -485, 
					"y" : 36,
					"default_image" : PATH + "checkbox/channel/checkbox_01.tga",
					"over_image" : PATH + "checkbox/channel/checkbox_02.tga",
					"down_image" : PATH + "checkbox/channel/checkbox_03.tga",
					"horizontal_align" : "center",
					"vertical_align" : "center",
				},
				{
					"name" : "saved_accs_acc2_del",
					"type" : "button",
					"x" : -435, 
					"y" : 36,
					"default_image" : PATH + "checkbox/channel/checkbox_x_01.tga",
					"over_image" : PATH + "checkbox/channel/checkbox_x_02.tga",
					"down_image" : PATH + "checkbox/channel/checkbox_x_03.tga",
					"horizontal_align" : "center",
					"vertical_align" : "center",
				},
				# # # # # # # # # 3 # #  # # # # # #
				{
					"name" : "saved_accs_acc3",
					"type" : "text",
					"x" : -365, 
					"y" : 87,
					"color" : 0xffcccccc,
					"horizontal_align" : "center",
					"vertical_align" : "center",
					"text": uiScriptLocale.LOGIN_INTERFACE_FREE_SPACE,
				},
				{
					"name" : "saved_accs_acc3_use",
					"type" : "button",
					"x" : -485, 
					"y" : 97,
					"default_image" : PATH + "checkbox/channel/checkbox_01.tga",
					"over_image" : PATH + "checkbox/channel/checkbox_02.tga",
					"down_image" : PATH + "checkbox/channel/checkbox_03.tga",
					"horizontal_align" : "center",
					"vertical_align" : "center",
				},
				{
					"name" : "saved_accs_acc3_del",
					"type" : "button",
					"x" : -435, 
					"y" : 97,
					"default_image" : PATH + "checkbox/channel/checkbox_x_01.tga",
					"over_image" : PATH + "checkbox/channel/checkbox_x_02.tga",
					"down_image" : PATH + "checkbox/channel/checkbox_x_03.tga",
					"horizontal_align" : "center",
					"vertical_align" : "center",
				},
				# # # # # # # # # 4 # #  # # # # # #
				{
					"name" : "saved_accs_acc4",
					"type" : "text",
					"x" : -365, 
					"y" : 143,
					"color" : 0xffcccccc,
					"horizontal_align" : "center",
					"vertical_align" : "center",
					"text": uiScriptLocale.LOGIN_INTERFACE_FREE_SPACE,
				},
				{
					"name" : "saved_accs_acc4_use",
					"type" : "button",
					"x" : -485, 
					"y" : 153,
					"default_image" : PATH + "checkbox/channel/checkbox_01.tga",
					"over_image" : PATH + "checkbox/channel/checkbox_02.tga",
					"down_image" : PATH + "checkbox/channel/checkbox_03.tga",
					"horizontal_align" : "center",
					"vertical_align" : "center",
				},
				{
					"name" : "saved_accs_acc4_del",
					"type" : "button",
					"x" : -435, 
					"y" : 153,
					"default_image" : PATH + "checkbox/channel/checkbox_x_01.tga",
					"over_image" : PATH + "checkbox/channel/checkbox_x_02.tga",
					"down_image" : PATH + "checkbox/channel/checkbox_x_03.tga",
					"horizontal_align" : "center",
					"vertical_align" : "center",
				},
				##################################################
				{
					"name" : "ServerSelectLabel",
					"type" : "text",
					"x" : 55,
					"y" : 400,
					"text" : "Serverauswahl: (Für Teamler)",
				},
				{
					"name" : "SERVER_LIVE_BUTTON",
					"type" : "radio_button",
					"x" : 40,
					"y" : 415,
					"text" : "Liveserver",
					"default_image" : "d:/ymir work/ui/public/Middle_Button_01.sub",
					"over_image"	: "d:/ymir work/ui/public/Middle_Button_02.sub",
					"down_image"	: "d:/ymir work/ui/public/Middle_Button_03.sub",
				},
				{
					"name" : "SERVER_TEST_BUTTON",
					"type" : "radio_button",
					"x" : 40 + 65,
					"y" : 415,
					"text" : "Testserver",
					"default_image" : "d:/ymir work/ui/public/Middle_Button_01.sub",
					"over_image"	: "d:/ymir work/ui/public/Middle_Button_02.sub",
					"down_image"	: "d:/ymir work/ui/public/Middle_Button_03.sub",
				},
				{
					"name" : "SERVER_LOCAL_BUTTON",
					"type" : "radio_button",
					"x" : 40 + 65 + 65,
					"y" : 415,
					"text" : "Localserver",
					"default_image" : "d:/ymir work/ui/public/Middle_Button_01.sub",
					"over_image"	: "d:/ymir work/ui/public/Middle_Button_02.sub",
					"down_image"	: "d:/ymir work/ui/public/Middle_Button_03.sub",
				},
				#######################################################
			),
		},
		## Lang1
		{
			"name" : "lang_de_button",
			"type" : "button",
			"x" : ((SCREEN_WIDTH) / 2) - 230,
			"y" : (SCREEN_HEIGHT/2) + 300,
			"default_image" : PATH + "lang/de_01.png",
			"over_image" : PATH + "lang/de_02.png",
			"down_image" : PATH + "lang/de_03.png",
		},
		## Lang2
		{
			"name" : "lang_en_button",
			"type" : "button",
			"x" : ((SCREEN_WIDTH) / 2) - 230 + (75),
			"y" : (SCREEN_HEIGHT/2) + 300,
			"default_image" : PATH + "lang/en_01.png",
			"over_image" : PATH + "lang/en_02.png",
			"down_image" : PATH + "lang/en_03.png",
		},
		## Lang2
		{
			"name" : "lang_tr_button",
			"type" : "button",
			"x" : ((SCREEN_WIDTH) / 2) - 230 + (75+75),
			"y" : (SCREEN_HEIGHT/2) + 300,
			"default_image" : PATH + "lang/tr_01.png",
			"over_image" : PATH + "lang/tr_02.png",
			"down_image" : PATH + "lang/tr_03.png",
		},
		{
			"name" : "lang_esp_button",
			"type" : "button",
			"x" : ((SCREEN_WIDTH) / 2) - 230 + (75+75+75),
			"y" : (SCREEN_HEIGHT/2) + 300,
			"default_image" : PATH + "lang/esp_01.png",
			"over_image" : PATH + "lang/esp_02.png",
			"down_image" : PATH + "lang/esp_03.png",
		},
		{
			"name" : "discord",
			"type" : "button",
			"x" : ((SCREEN_WIDTH) / 2) - 230 + (75+75+75+75),
			"y" : (SCREEN_HEIGHT/2) + 300,
			"default_image" : PATH + "lang/dc_01.png",
			"over_image" : PATH + "lang/dc_02.png",
			"down_image" : PATH + "lang/dc_03.png",
		},
		#######################################
	),
}