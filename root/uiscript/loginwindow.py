import uiScriptLocale

PATH = "d:/ymir work/ui/login/logininterface/"
CHITRA = "d:/ymir work/ui/yuma/login_interface/"
BUTTON_CHITRA = "d:/ymir work/ui/yuma/login_interface/button/" 
BUTTON_INTERFACE = "d:/ymir work/ui/yuma/login_interface/buttons/" 
TEXT_INTERFACE = "d:/ymir work/ui/yuma/login_interface/text/" 
INPUT_INTERFACE = "d:/ymir work/ui/yuma/login_interface/input/"

LOGIN_BOARD_MARGIN = 100

if SCREEN_HEIGHT < 800:
	LOGO_MARGIN = 150
	LOGIN_BOARD_MARGIN = 100
	
if SCREEN_HEIGHT < 610:
	LOGO_MARGIN = 350
	LOGIN_BOARD_MARGIN = 250

if SCREEN_WIDTH <= 800:
	SMALL_WINDOW = 0
	SMALL_WINDOW2 = 50
else:
	SMALL_WINDOW = 0
	SMALL_WINDOW2 = 30
	
LOGIN_BOARD_POS_Y = (SCREEN_HEIGHT/2) - LOGIN_BOARD_MARGIN

window = {
	"sytle" : ("movable",),
	"x" : 0, "y" : 0,
	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,
	"children" : 
	(
		{
			"name" : "background", 
			"type" : "expanded_image",
			"x" : 0, "y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1920.0,
			"y_scale" : float(SCREEN_HEIGHT) / 1080.0,
			"image" : PATH + "background.tga",
		},
		{
			"name" : "board_logo",
			"type" : "image",
			'x' : (SCREEN_WIDTH - 630) / 2,
			"y" : 0, #centered middle
			"image" : CHITRA + "logo_background.tga",
			"children" :
			(
				{
					"name" : "kuba_logo",
					"type" : "image",
					'x' : 150,
					"y" : 3,
					"image" : CHITRA + "logo.png",
				},
			),
		},
		{
			"name" : "board_main",
			"type" : "image",
			'x' : (SCREEN_WIDTH - 1150) / 2,
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
					"x" : 79, "y" : 60,
					"horizontal_align" : "center", "vertical_align" : "center",
					"default_image" : PATH + "login/button/button_01.tga", 
					"over_image" : PATH + "login/button/button_02.tga", 
					"down_image" : PATH + "login/button/button_03.tga", 
					"children" : 
					(
						{
							"name" : "login_button_text",
							"type" : "text",
							"x" : 38,
							"y" : 10,
							"color" : 0xff090406,
							"fontsize" : "LARGE",
							"text" : "Login",
						},
					),
				},
				{
					"name" : "save_button",
					"type" : "button",
					"x" : -79, "y" : 60,
					"horizontal_align" : "center", "vertical_align" : "center",
					"default_image" : PATH + "login/button/button_01.tga", 
					"over_image" : PATH + "login/button/button_02.tga", 
					"down_image" : PATH + "login/button/button_03.tga", 
					"children" : 
					(
						{
							"name" : "login_button_text",
							"type" : "text",
							"x" : 38,
							"y" : 10,
							"color" : 0xff090406,
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
				## Lang1
				{
					"name" : "lang_de_button",
					"type" : "button",
					"x" : 500,
					"y" : 375,
					"default_image" : CHITRA + "language/language_de_01.png",
					"over_image" : CHITRA + "language/language_de_02.png",
					"down_image" : CHITRA + "language/language_de_03.png",
				},
				## Lang2
				{
					"name" : "lang_en_button",
					"type" : "button",
					"x" : 720,
					"y" : 375,
					"default_image" : CHITRA + "language/language_en_01.png",
					"over_image" : CHITRA + "language/language_en_02.png",
					"down_image" : CHITRA + "language/language_en_03.png",
				},
				#######################################
			),
		},
	),
}