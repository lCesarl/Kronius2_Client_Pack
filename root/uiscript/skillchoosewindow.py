import uiScriptLocale

UI_WIDTH	= 306
UI_HEIGHT	= 90

window = {
	"name" : "MainWindow",
	"style" : ("movable", "float",),
	"x" : SCREEN_WIDTH / 2 - UI_WIDTH / 2,
	"y" : SCREEN_HEIGHT / 2 - UI_HEIGHT / 2,
	"width" : UI_WIDTH,
	"height" : UI_HEIGHT,
	"children" :
	(
		{
			"name" : "Board",
			"type" : "board",
			"style" : ("attach",),
			"x" : 0,
			"y" : 0,
			"width" : UI_WIDTH,
			"height" : UI_HEIGHT,
			"children" :
			(
				{
					"name" : "ChooseText",
					"type" : "text",
					"x" : 103,
					"y" : 27,
					"text" : uiScriptLocale.skillchoose_text,
				},
				{
					"name" : "SelectButton1",
					"type" : "button",
					"x" : 12,
					"y" : 55,
					"text" : "",
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				{
					"name" : "SelectButton2",
					"type" : "button",
					"x" : 109,
					"y" : 55,
					"text" : "",
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				{
					"name" : "CloseButton",
					"type" : "button",
					"x" : 204,
					"y" : 55,
					"text" : uiScriptLocale.skillchoose_cancel,
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
			),
		},
	),
}