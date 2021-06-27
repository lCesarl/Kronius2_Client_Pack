# Cesar

import uiScriptLocale

BASE = "d:/ymir work/ui/pincode_sys/"
BOARD_WIDTH = 266
BOARD_HEIGHT = 185

window = {
	"name" : "PinCodeDialogCreate",
	"x" : 0, "y" : 0,
	"style" : ("movable", "float",),
	"width" : BOARD_WIDTH, "height" : BOARD_HEIGHT,
	
	"children" :
	(
		{
			"name" : "board_0",
			"type" : "image",
			"x" : 0, "y" : 0,
			"width" : BOARD_WIDTH, "height" : BOARD_HEIGHT,
			
			"image" : BASE + "background_create.tga",
			"children" :
			(
				## LABEL TEXT 01
				{
					"name" : "text_01",
					"type" : "text",
					"x" : (BOARD_WIDTH - 110) / 2, "y" : 25,
					"text" : uiScriptLocale.PINCODE_CREATE,
				},
				## LABEL TEXT 02
				{
					"name" : "text_01",
					"type" : "text",
					"x" : (BOARD_WIDTH - 42) / 2, "y" : (BOARD_HEIGHT - 88),
					"text" : uiScriptLocale.PINCODE_CONFIRM,
				},
				## LOCK SYMBOL 01
				{
					"name" : "lock_symbol2",
					"type" : "image",
					"x" : 7, "y" : 15,
					"image" : BASE + "lock_symbol.tga",
				},
				## LOCK SYMBOL 02
				{
					"name" : "lock_symbol2",
					"type" : "image",
					"x" : BOARD_WIDTH - 37, "y" : 15,
					"image" : BASE + "lock_symbol.tga",
				},
				## BUTTON CANCEL
				{
					"name" : "cancel_button",
					"type" : "button",
					"x" : 10, "y" : 158,
					"default_image" : BASE + "button_01.tga", 
					"over_image" : BASE + "button_02.tga",
					"down_image" : BASE + "button_03.tga",
					"text" : uiScriptLocale.PINCODE_CANCEL,
				},
				## BUTTON CONFIRM
				{
					"name" : "confirm_button",
					"type" : "button",
					"x" : BOARD_WIDTH - 90, "y" : 158,
					"default_image" : BASE + "button_01.tga", 
					"over_image" : BASE + "button_02.tga",
					"down_image" : BASE + "button_03.tga",
					"text" : uiScriptLocale.PINCODE_GO
				},
				## INPUT SLOT 01
				{
					"name" : "pin_slotbar_01",
					"type" : "image",
					"x" : (BOARD_WIDTH - 77) / 2, "y" : (BOARD_HEIGHT - 130),
					"image" : BASE + "input.tga",
					"children" : 
					(
						{
							"name" : "pin_value_01",
							"type" : "editline",
							"x" : 22, "y" : 13,
							"width" : 200, "height" : 16,
							"input_limit": 5,
						},
					),
				},
				## INPUT SLOT 02
				{
					"name" : "pin_slotbar_02",
					"type" : "image",
					"x" : (BOARD_WIDTH - 77) / 2, "y" : (BOARD_HEIGHT - 70),
					"image" : BASE + "input.tga",
					"children" : 
					(
						{
							"name" : "pin_value_02",
							"type" : "editline",
							"x" : 22, "y" : 13,
							"width" : 200, "height" : 16,
							"input_limit": 5,
						},
					),
				},
			),
		},
	),
}