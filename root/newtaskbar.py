import uiScriptLocale

window = {
	"name" : "NewTaskBar",

	"x" : (SCREEN_WIDTH / 2) - (714/2),
	"y" : SCREEN_HEIGHT - 100,

	"width" : 714,
	"height" : 100,
	
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