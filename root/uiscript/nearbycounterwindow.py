import uiScriptLocale
UI_WIDTH = 278
UI_HEIGHT = 175

window = {
	"name" : "NearbyCounterWindow",
	"style" : ("movable", "float",),

	"x" : SCREEN_WIDTH / 2 - UI_WIDTH / 2, 
	"y" : SCREEN_HEIGHT / 2 - UI_HEIGHT / 2,

	"width" : UI_WIDTH, "height" : UI_HEIGHT,
	
	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0, 
			"y" : 0,

			"width" : UI_WIDTH,
			"height" : UI_HEIGHT,

			"children" :
			(
				## Title
				{
					"name" : "titlebar",
					"type" : "titlebar",
					"style" : ("attach",),
					"x" : 8, "y" : 8,
					"width" : UI_WIDTH-10,
					"children" :
					(
						{ 
							"name":"titlename", "type":"text", "x":0, "y":3, 
							"horizontal_align":"center", "text_horizontal_align":"center",
							"text": "translateME", 
						},
					),
				},
			),
		},
	),
}