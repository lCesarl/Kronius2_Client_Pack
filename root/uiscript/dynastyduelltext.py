ROOT_DIR = "d:/ymir work/ui/dynastyduellsys/line/"

window = {
	"name" : "DynastyDuellText",
	"style" : ("float",),
	"x" : 15,
	"y" : (SCREEN_HEIGHT / 2) + 150,
	"width" : 560,
	"height" : 150,
	"children" :
	(
		{
			"name" : "line",
			"type" : "image",
			"style" : ("attach",),
			"x" : 0,
			"y" : 0,
			"image" : ROOT_DIR + "main.tga",
			"children" : 
			(
				{
					"name" : "Player_Name",
					"type" : "text",
					"x" : 150,
					"y" : 98,
					"text" : "Testplayer:",
					"color" : 0xffffdd9b,
				},
				{
					"name" : "Status_Text",
					"type" : "text",
					"x" : 150,
					"y" : 115,
					"text" : "PLAYERNAME: I'll kill you!",
					"color" : 0xff9bd1ff,
				},
				{
					"name" : "faceIMG",
					"type" : "image",
					"style" : ("attach",),
					"x" : 45,
					"y" : 33,
					"image" : ROOT_DIR + "warrior_m.tga",
				},
			),
		},
	),
}