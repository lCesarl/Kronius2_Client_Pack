import uiScriptLocale

BOARD_WIDTH = 200
BOARD_HEIGHT = 125

LINE_STEP = 16

window = {
	"name" : "WaveDungeonAttributeWindow",

	"x" : SCREEN_WIDTH - BOARD_WIDTH,
	"y" : SCREEN_HEIGHT / 2,

	"style" : ("float",),

	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,

	"children" :
	(
		{
			"name" : "board",
			"type" : "thinboard",

			"x" : 0,
			"y" : 0,

			"width" : BOARD_WIDTH,
			"height" : BOARD_HEIGHT,
		
			"children" :
			(
				{ 
					"name":"Title", 
					"type":"text", 
					"x": (BOARD_WIDTH / 2), 
					"y": 6, 
					"text":"Modifikationen", 
					"text_horizontal_align":"center" 
				},
				{ 
					"name":"Attr_0", 
					"type":"text", 
					"x": (BOARD_WIDTH / 2), 
					"y": 6 + (LINE_STEP * 1), 
					"text":"", 
					"text_horizontal_align":"center" 
				},
				{ 
					"name":"Attr_1", 
					"type":"text", 
					"x": (BOARD_WIDTH / 2), 
					"y": 6 + (LINE_STEP * 2),
					"text":"", 
					"text_horizontal_align":"center" 
				},
				{ 
					"name":"Attr_2", 
					"type":"text", 
					"x": (BOARD_WIDTH / 2), 
					"y": 6 + (LINE_STEP * 3),
					"text":"", 
					"text_horizontal_align":"center" 
				},
				{ 
					"name":"Attr_3", 
					"type":"text", 
					"x": (BOARD_WIDTH / 2), 
					"y": 6 + (LINE_STEP * 4),
					"text":"", 
					"text_horizontal_align":"center" 
				},
				{ 
					"name":"Attr_4", 
					"type":"text", 
					"x": (BOARD_WIDTH / 2), 
					"y": 6 + (LINE_STEP * 5),
					"text":"", 
					"text_horizontal_align":"center" 
				},
				{ 
					"name":"Attr_5", 
					"type":"text", 
					"x": (BOARD_WIDTH / 2), 
					"y": 6 + (LINE_STEP * 6),
					"text":"", 
					"text_horizontal_align":"center" 
				},
			),
		},
	),
}
