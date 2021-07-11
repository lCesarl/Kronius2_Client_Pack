import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()

window = {
	"name" : "SwitchChannelDialog",
	"style" : ("movable", "float", "ltr"),
	
	"x" : (SCREEN_WIDTH/2) - (190/2),
	"y" : (SCREEN_HEIGHT/2) - 100,	

	"width" : 0,
	"height" : 0,
	
	"children" :
	(
		## MainBoard
		{
			"name" : "SwitchChannelBoard",
			"type" : "board",
			"style" : ("attach", "ltr"),

			"x" : 0,
			"y" : 0,

			"width" : 0,
			"height" : 0,
			
			"children" :
			(
				## Title Bar
				{
					"name" : "SwitchChannelTitle",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 6, "y" : 7, "width" : 190 - 13,
					
					"children" :
					(
						{
							"name" : "TitleName", 
							"type" : "text", 
							
							"x" : 0, 
							"y" : 0, 
							
							"text": "Channel Wechseln",
							"all_align":"center" },
					),
				},
				
				{
					"name" : "BlackBoard",
					"type" : "thinboard",
					"x" : 13, "y" : 36, "width" : 0, "height" : 0,
				},
			),
		}, ## MainBoard End
	),
}
