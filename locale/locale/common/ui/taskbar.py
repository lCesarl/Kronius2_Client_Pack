import uiScriptlocale
import app

ROOT = "d:/ymir work/ui/game/"

#Y_ADD_POSITION = -2
Y_ADD_POSITION = 0

window = {
	"name" : "TaskBar",

	"x" : (SCREEN_WIDTH - 960) / 2,
	"y" : SCREEN_HEIGHT - 80,

	"width" : 971,
	"height" : 85,

	"children" :
	(
		## Board
		{
			"name" : "Base_Board_01",
			"type" : "expanded_image",

			"x" : 0,
			"y" : 0,

			"image" : "d:/ymir work/ui/yuma/TaskBar_Base.tga"
		},
		{
			## HP BAR
			"name" : "HPGauge_Board",
			"type" : "window",

			"x" : 100,
			"y" : 18,

			"width" : 136,
			"height" : 20,

			"children" :
			(
				{
					"name" : "HPRecoveryGaugeBar",
					"type" : "bar",

					"x" : 0,
					"y" : 0,
					"width" : 136,
					"height" : 19,
					"color" : 0x55ff0000,
				},
				{
					"name" : "HPGauge",
					"type" : "ani_image",

					"x" : 0,
					"y" : 0,

					"delay" : 3,
					"images" :
					(
						"d:/ymir work/ui/yuma/taskbar/hpgauge/00.tga",
						"d:/ymir work/ui/yuma/taskbar/hpgauge/01.tga",
						"d:/ymir work/ui/yuma/taskbar/hpgauge/02.tga",
						"d:/ymir work/ui/yuma/taskbar/hpgauge/03.tga",
						"d:/ymir work/ui/yuma/taskbar/hpgauge/04.tga",
						"d:/ymir work/ui/yuma/taskbar/hpgauge/05.tga",
						"d:/ymir work/ui/yuma/taskbar/hpgauge/06.tga",
					),
				},

				{
					"name" : "HPPoisonRecoveryGaugeBar",
					"type" : "bar",
					"x" : 0,
					"y" : 0,
					"width" : 136,
					"height" : 19,
					"color" : 0x55008000,
				},
				{
					"name" : "HPPoisonGauge",
					"type" : "ani_image",
					"x" : 0,
					"y" : 0,
					"delay" : 3,
					"images" :
					(
						"d:/ymir work/ui/yuma/taskbar/poison/00.tga",
						"d:/ymir work/ui/yuma/taskbar/poison/01.tga",
						"d:/ymir work/ui/yuma/taskbar/poison/02.tga",
						"d:/ymir work/ui/yuma/taskbar/poison/03.tga",
						"d:/ymir work/ui/yuma/taskbar/poison/04.tga",
						"d:/ymir work/ui/yuma/taskbar/poison/05.tga",
						"d:/ymir work/ui/yuma/taskbar/poison/06.tga",
					),
				},

				{
					"name" : "HPGauge_Perc_Text",
					"type" : "text",
					"x" : (136/2) - 8, "y" : (20/2) - 8,
					"text" : "100%",
				},
			),
		},
		{
			## SP BAR
			"name" : "SPGauge_Board",
			"type" : "window",

			"x" : 100,
			"y" : 38,

			"width" : 136,
			"height" : 20,

			"children" :
			(
				{
					"name" : "SPRecoveryGaugeBar",
					"type" : "bar",

					"x" : 3,
					"y" : 3,
					"width" : 133,
					"height" : 17,
					"color" : 0x550000ff,
				},
				{
					"name" : "SPGauge",
					"type" : "ani_image",

					"x" : 1,
					"y" : 1,

					"delay" : 4,
					"images" :
					(
						"d:/ymir work/ui/yuma/taskbar/spgauge/00.tga",
						"d:/ymir work/ui/yuma/taskbar/spgauge/01.tga",
						"d:/ymir work/ui/yuma/taskbar/spgauge/02.tga",
						"d:/ymir work/ui/yuma/taskbar/spgauge/03.tga",
						"d:/ymir work/ui/yuma/taskbar/spgauge/04.tga",
						"d:/ymir work/ui/yuma/taskbar/spgauge/05.tga",
						"d:/ymir work/ui/yuma/taskbar/spgauge/06.tga",
					),
				},
				{
					"name" : "SPGauge_Perc_Text",
					"type" : "text",
					"x" : (136/2) - 8, "y" : (20/2) - 8,
					"text" : "100%",
				},
			),
		},
		{
			## ENERGY BAR
			"name" : "STGauge_Board",
			"type" : "window",

			"x" : 125,
			"y" : 60,

			"width" : 95,
			"height" : 6,

			"children" :
			(
				{
					"name" : "STGauge",
					"type" : "ani_image",

					"x" : 0,
					"y" : 0,

					"delay" : 6,

					"images" :
					(
						"D:/Ymir Work/UI/Pattern/STGauge/01.tga",
						"D:/Ymir Work/UI/Pattern/STGauge/02.tga",
						"D:/Ymir Work/UI/Pattern/STGauge/03.tga",
						"D:/Ymir Work/UI/Pattern/STGauge/04.tga",
						"D:/Ymir Work/UI/Pattern/STGauge/05.tga",
						"D:/Ymir Work/UI/Pattern/STGauge/06.tga",
						"D:/Ymir Work/UI/Pattern/STGauge/07.tga",
					),
				},
			),
		},
		# EXP BAR
		{
			"name" : "EXP_Gauge_Base",
			"type" : "expanded_image_vertical",
			"x" : 250,
			"y" : 18,
			"image" : "d:/ymir work/ui/yuma/taskbar/expgauge/00.tga",
			"children" :
			(
				{
					"name" : "EXP_Gauge",
					"type" : "expanded_image_vertical",
					"x" : 0,
					"y" : 0,
					"image" : "d:/ymir work/ui/yuma/taskbar/expgauge/01.tga",
				},
			),
		},

		## QuickBar
		{
			"name" : "quickslot_board",
			"type" : "window",

			"x" : 305,
			"y" : 21,

			"width" : 330,
			"height" : 35,

			"children" :
			(
				{
					"name" : "quick_slot_1",
					"type" : "grid_table",

					"start_index" : 0,

					"x" : 0,
					"y" : 3,

					"x_count" : 4,
					"y_count" : 1,
					"x_step" : 32,
					"y_step" : 32,
					"x_blank" : 10,

					"image" : "d:/ymir work/ui/yuma/taskbar/quickslot/slot.tga",
					"image_r" : 1.0,
					"image_g" : 1.0,
					"image_b" : 1.0,
					"image_a" : 1.0,
				},

				{ "name" : "quickslot_label_1", "type" : "text", "x" : 1, "y" : 3, "text" : "1", },
				{ "name" : "quickslot_label_2", "type" : "text", "x" : 1*43, "y" : 3, "text" : "2", },
				{ "name" : "quickslot_label_3", "type" : "text", "x" : 2*43, "y" : 3, "text" : "3", },
				{ "name" : "quickslot_label_4", "type" : "text", "x" : 3*43, "y" : 3, "text" : "4", },

				{
					"name" : "quick_slot_2",
					"type" : "grid_table",

					"start_index" : 4,

					"x" : 168,
					"y" : 3,

					"x_count" : 4,
					"y_count" : 1,
					"x_step" : 32,
					"y_step" : 32,
					"x_blank" : 10,

					"image" : "d:/ymir work/ui/yuma/taskbar/quickslot/slot.tga",
					"image_r" : 1.0,
					"image_g" : 1.0,
					"image_b" : 1.0,
					"image_a" : 1.0,
				},

				{ "name" : "quickslot_label_5", "type" : "text", "x" : 170, "y" : 3, "text" : "F1", },
				{ "name" : "quickslot_label_6", "type" : "text", "x" : 212, "y" : 3, "text" : "F2", },
				{ "name" : "quickslot_label_7", "type" : "text", "x" : 254, "y" : 3, "text" : "F3", },
				{ "name" : "quickslot_label_8", "type" : "text", "x" : 296, "y" : 3, "text" : "F4", },
			),
		},
		{
			"name" : "QuickSlotBoard",
			"type" : "window",

			"x" : 643,
			"y" : 21,
			"width" : 11,
			"height" : 37,
			"children" :
			(
				{
					"name" : "QuickPageUpButton",
					"type" : "button",
					"tooltip_text" : uiScriptlocale.TASKBAR_PREV_QUICKSLOT,
					"x" : 1,
					"y" : 5,
					"default_image" : "d:/ymir work/ui/yuma/taskbar/quickslot/upbutton_01.tga",
					"over_image" : "d:/ymir work/ui/yuma/taskbar/quickslot/upbutton_02.tga",
					"down_image" : "d:/ymir work/ui/yuma/taskbar/quickslot/upbutton_03.tga",
				},

				{ 
					"name" : "QuickPageNumber", 
					"type" : "image", 							
					"x" : 3, "y" : 15, "image" : "d:/ymir work/ui/yuma/taskbar/quickslot/background.tga",
				},
				{
					"name" : "QuickPageDownButton",
					"type" : "button",
					"tooltip_text" : uiScriptlocale.TASKBAR_NEXT_QUICKSLOT,

					"x" : 1,
					"y" : 25,

					"default_image" : "d:/ymir work/ui/yuma/taskbar/quickslot/downbutton_01.tga",
					"over_image" : "d:/ymir work/ui/yuma/taskbar/quickslot/downbutton_02.tga",
					"down_image" : "d:/ymir work/ui/yuma/taskbar/quickslot/downbutton_03.tga",
				},

			),
		},

		## decoration
		{ 
			"name" : "decoration_right_01", 
			"type" : "expanded_image", 							
			"x" : 870, "y" : -10, "image" : "d:/ymir work/ui/yuma/taskbar/decoration/decoration_right_01.tga",
		},
		{ 
			"name" : "decoration_right_02", 
			"type" : "expanded_image", 							
			"x" : 900, "y" : -10, "image" : "d:/ymir work/ui/yuma/taskbar/decoration/decoration_right_02.tga",
		},

		{ 
			"name" : "decoration_left_01", 
			"type" : "expanded_image", 							
			"x" : 5, "y" : -10, "image" : "d:/ymir work/ui/yuma/taskbar/decoration/decoration_left_01.tga",
		},
		{ 
			"name" : "decoration_left_02", 
			"type" : "expanded_image", 							
			"x" : 0, "y" : -10, "image" : "d:/ymir work/ui/yuma/taskbar/decoration/decoration_left_02.tga",
		},

		## Mouse Button
		{
			"name" : "LeftMouseButton",
			"type" : "button",

			"x" : 660,
			"y" : 18,

			"default_image" : ROOT + "TaskBar/Mouse_Button_Move_01.sub",
			"over_image" : ROOT + "TaskBar/Mouse_Button_Move_02.sub",
			"down_image" : ROOT + "TaskBar/Mouse_Button_Move_03.sub",
		},
		{
			"name" : "RightMouseButton",
			"type" : "button",

			"x" : 695,
			"y" : 18,

			"default_image" : ROOT + "TaskBar/Mouse_Button_Move_01.sub",
			"over_image" : ROOT + "TaskBar/Mouse_Button_Move_02.sub",
			"down_image" : ROOT + "TaskBar/Mouse_Button_Move_03.sub",
		},

		## Button
		{
			"name" : "CharacterButton",
			"type" : "button",

			"x" : 730,
			"y" : 18,

			"tooltip_text" : uiScriptlocale.TASKBAR_CHARACTER,

			"default_image" : "d:/ymir work/ui/yuma/taskbar/button/character/character_button_01.tga",
			"over_image" : "d:/ymir work/ui/yuma/taskbar/button/character/character_button_02.tga",
			"down_image" : "d:/ymir work/ui/yuma/taskbar/button/character/character_button_03.tga",
		},
		{
			"name" : "InventoryButton",
			"type" : "button",

			"x" : 730 + 40,
			"y" : 18,

			"tooltip_text" : uiScriptlocale.TASKBAR_INVENTORY,

			"default_image" : "d:/ymir work/ui/yuma/taskbar/button/inventory/inventory_button_01.tga",
			"over_image" : "d:/ymir work/ui/yuma/taskbar/button/inventory/inventory_button_02.tga",
			"down_image" : "d:/ymir work/ui/yuma/taskbar/button/inventory/inventory_button_03.tga",
		},
		{
			"name" : "MessengerButton",
			"type" : "button",

			"x" : 730 + 40 + 40,
			"y" : 18,

			"tooltip_text" : uiScriptlocale.TASKBAR_MESSENGER,

			"default_image" : "d:/ymir work/ui/yuma/taskbar/button/community/community_button_01.tga",
			"over_image" : "d:/ymir work/ui/yuma/taskbar/button/community/community_button_02.tga",
			"down_image" : "d:/ymir work/ui/yuma/taskbar/button/community/community_button_03.tga",
		},
		{
			"name" : "SystemButton",
			"type" : "button",

			"x" : 730 + 40 +40 +40,
			"y" : 18,

			"tooltip_text" : uiScriptlocale.TASKBAR_SYSTEM,

			"default_image" : "d:/ymir work/ui/yuma/taskbar/button/system/system_button_01.tga",
			"over_image" : "d:/ymir work/ui/yuma/taskbar/button/system/system_button_02.tga",
			"down_image" : "d:/ymir work/ui/yuma/taskbar/button/system/system_button_03.tga",
		},
		{
			"name" : "ChatButton",
			"type" : "button",

			"x" : (971 - 130) / 2,
			"y" : -10,
			"tooltip_text" : uiScriptlocale.TASKBAR_EXPAND,
			
			"default_image" : "d:/ymir work/ui/yuma/taskbar/button/chat/chat_button_01.tga",
			"over_image" : "d:/ymir work/ui/yuma/taskbar/button/chat/chat_button_02.tga",
			"down_image" : "d:/ymir work/ui/yuma/taskbar/button/chat/chat_button_03.tga",
		},
	),
}
