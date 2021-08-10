import uiScriptLocale

window = {
	"name" : "TaskBar",

	"x" : (SCREEN_WIDTH / 2) - (751/2),
	"y" : SCREEN_HEIGHT - 106,

	"width" : 751,
	"height" : 96,
	
	"children" :
	(
		## Board
		{
			"name" : "Taskbar_Base",
			"type" : "image",

			"x" : 0,
			"y" : 0,
			
			# "horizontal_align" : "center",
			
			"image" : "taskbar/taskbar_base.png",
		},
	),
}