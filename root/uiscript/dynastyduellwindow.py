import uiScriptLocale
LOCATION_DIR = "d:/ymir work/ui/dynastyduellsys/window/"
UI_WIDTH = 295
UI_HEIGHT = 184

window = {
	"name" : "DynastyDuellWindow",
	"style" : ("movable", "float",),
	
	"x" : SCREEN_WIDTH / 2 - UI_WIDTH / 2,
	"y" : SCREEN_HEIGHT / 2 - UI_HEIGHT / 2,
	
	"width" : UI_WIDTH,
	"height" : UI_HEIGHT,
	"children" :
	(
		{
			"name" : "Board",
			"type" : "image", "style" : ("attach",),
			
			"x" : 0, "y" : 0,
			"width" : UI_WIDTH,
			"height" : UI_HEIGHT,
			
			"image" : LOCATION_DIR + "background.tga",
			"children" :
			(
				## Titlebar
				{
					"name" : "Titlebar",
					"type" : "image", "style" : ("attach",),
					"x" : 4, "y" : 0,
					
					"width" : 284,
					"height" : 22,
					
					"image" : LOCATION_DIR + "titlebar.tga",
					"children" :
					(
						## Titlebar - Title
						{
							"name" : "Titlebar_Title",
							"type" : "text",
							
							"x" : UI_WIDTH / 2 - 12,
							"y" : 5,
							
							"text_horizontal_align" : "center",
							"text" : uiScriptLocale.dynastyduell_title,
						},
						
						## Titlebar - Close Button
						{
							"name" : "Titlebar_Close",
							"type" : "button",
							
							"x" : 263, 
							"y" : 1,
							
							"default_image" : LOCATION_DIR + "bt_close_01.tga", 
							"over_image" : LOCATION_DIR + "bt_close_02.tga",
							"down_image" : LOCATION_DIR + "bt_close_03.tga",
						},
					),
				},
			),
		},
		## Textlabel
		{
			"name" : "chooseText",
			"type" : "text",
			"x" : UI_WIDTH / 2 - 50,
			"y" : 50,
			"text" : uiScriptLocale.dynastyduell_choosetext,
		},
		## Inputfield
		{
			"name" : "InputSlot",
			"type" : "image",
			"x" : UI_WIDTH / 2 - 95,
			"y" : 69,
			"image" : LOCATION_DIR + "input.tga",
			"children" :
			(
				{
					"name" : "InputValue",
					"type" : "editline",
					"x" : 6, "y" : 4,
					"width" : 200, "height" : 16,
					"input_limit": 38,
					# "text_horizontal_align" : "center",
				},
			),
		},
		## Dynasty Symbol - left
		{
			"name" : "Dynasty_Symbol",
			"type" : "image",
			"x" : 20, "y" : 27,
			"image" : LOCATION_DIR + "dynasty_symbol.tga",
		},
		## Dynasty Symbol - right
		{
			"name" : "Dynasty_Symbol",
			"type" : "image",
			"x" : 235, "y" : 27,
			"image" : LOCATION_DIR + "dynasty_symbol.tga",
		},
		## Textlabel
		{
			"name" : "needText",
			"type" : "text",
			"x" : 77,
			"y" : 110,
			"text_horizontal_align" : "center",
			"text" : uiScriptLocale.dynastyduell_needtext +":",
		},
		# ITEM_SLOT
		{
			"name" : "ItemSlot",
			"type" : "slot",
			"x" : 125, "y" : 105,
			"width" : 36, "height" : 36,
			"image" : LOCATION_DIR + "slot.tga",
			"slot" : ({"index":0, "x":0, "y":0, "width":32, "height":32,},),
		},
		##	ChooseButton
		{
			"name" : "chooseButton",
			"type" : "button",
			"x" : 19,
			"y" : 155,
			"text" : uiScriptLocale.dynastyduell_choosebutton,
			"default_image" : LOCATION_DIR + "button_01.tga", 
			"over_image" : LOCATION_DIR + "button_02.tga",
			"down_image" : LOCATION_DIR + "button_03.tga",
		},
		##	PreviewButton
		{
			"name" : "previewButton",
			"type" : "button",
			"x" : 106,
			"y" : 155,
			"text" : uiScriptLocale.dynastyduell_previewbutton,
			"default_image" : LOCATION_DIR + "button_01.tga", 
			"over_image" : LOCATION_DIR + "button_02.tga",
			"down_image" : LOCATION_DIR + "button_03.tga",
		},
		##	CancelButton
		{
			"name" : "cancelButton",
			"type" : "button",
			"x" : 192,
			"y" : 155,
			"text" : uiScriptLocale.dynastyduell_cancelbutton,
			"default_image" : LOCATION_DIR + "button_01.tga", 
			"over_image" : LOCATION_DIR + "button_02.tga",
			"down_image" : LOCATION_DIR + "button_03.tga",
		},
	),
}