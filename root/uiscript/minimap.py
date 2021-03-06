import app

ROOT = "d:/ymir work/ui/minimap/"


if app.ENABLE_PINGTIME:
		window = {
		"name" : "MiniMap",

		"x" : SCREEN_WIDTH - 175,
		"y" : 0,

		"width" : 170,
		"height" : 175,

		"children" :
		(
			## OpenWindow
			{
				"name" : "OpenWindow",
				"type" : "window",

				"x" : 0,
				"y" : 0,

				"width" : 170,
				"height" : 175,

				"children" :
				(
					{
						"name" : "OpenWindowBGI",
						"type" : "image",
						"x" : 0,
						"y" : 0,
						"image" : "d:/ymir work/ui/one_work/minimap.png",
					},
					## MiniMapWindow
					{
						"name" : "MiniMapWindow",
						"type" : "window",

						"x" : 22,
						"y" : 20,

						"width" : 132,
						"height" : 132,
					},
					## ScaleUpButton
					{
						"name" : "ScaleUpButton",
						"type" : "button",

						"x" : 142,
						"y" : 85,

						"default_image" : "d:/ymir work/ui/one_work/minimap_max.png",
						"over_image" : "d:/ymir work/ui/one_work/minimap_max.png",
						"down_image" : "d:/ymir work/ui/one_work/minimap_max.png",
					},
					## ScaleDownButton
					{
						"name" : "ScaleDownButton",
						"type" : "button",

						"x" : 133,
						"y" : 111,

						"default_image" : "d:/ymir work/ui/one_work/minimap_min.png",
						"over_image" : "d:/ymir work/ui/one_work/minimap_min.png",
						"down_image" : "d:/ymir work/ui/one_work/minimap_min.png",
					},
					## MiniMapHideButton
					{
						"name" : "MiniMapHideButton",
						"type" : "button",

						"x" : 134,
						"y" : 16,

						"default_image" : "d:/ymir work/ui/one_work/minimap_close.png",
						"over_image" : "d:/ymir work/ui/one_work/minimap_close.png",
						"down_image" : "d:/ymir work/ui/one_work/minimap_close.png",
					},
					## AtlasShowButton
					{
						"name" : "AtlasShowButton",
						"type" : "button",

						"x" : 0,
						"y" : 95,

						"default_image" : "d:/ymir work/ui/one_work/minimap_map.png",
						"over_image" : "d:/ymir work/ui/one_work/minimap_map.png",
						"down_image" : "d:/ymir work/ui/one_work/minimap_map.png",
					},
					## ServerInfo
					{
						"name" : "ServerInfo",
						"type" : "text",
						
						"text_horizontal_align" : "center",

						"outline" : 1,

						"x" : 70,
						"y" : 140,

						"text" : "",
					},
					## TIME
					{
						"name" : "TIME",
						"type" : "text",
						
						"text_horizontal_align" : "center",

						"outline" : 1,

						"x" : 65,
						"y" : 179,

						"text" : "",
					},
					## FPS
					{
						"name" : "FPS",
						"type" : "text",
						
						"text_horizontal_align" : "center",

						"outline" : 1,

						"x" : 40,
						"y" : 195,

						"text" : "",
					},
					## PING
					{
						"name" : "PING",
						"type" : "text",
						
						"text_horizontal_align" : "center",

						"outline" : 1,

						"x" : 90,
						"y" : 195,

						"text" : "",
					},

					## PositionInfo
					{
						"name" : "PositionInfo",
						"type" : "text",
						
						"text_horizontal_align" : "center",

						"outline" : 1,

						"x" : 70,
						"y" : 160,

						"text" : "",
					},
					## ObserverCount
					{
						"name" : "ObserverCount",
						"type" : "text",
						
						"text_horizontal_align" : "center",

						"outline" : 1,

						"x" : 70,
						"y" : 180,

						"text" : "",
					},
				),
			},
			{
				"name" : "CloseWindow",
				"type" : "window",

				"x" : 0,
				"y" : 0,

				"width" : 132,
				"height" : 48,

				"children" :
				(
					## ShowButton
					{
						"name" : "MiniMapShowButton",
						"type" : "button",

						"x" : 100,
						"y" : 4,

						"default_image" : ROOT + "minimap_open_default.sub",
						"over_image" : ROOT + "minimap_open_default.sub",
						"down_image" : ROOT + "minimap_open_default.sub",
					},
				),
			},
		),
	}
else:
	window = {
		"name" : "MiniMap",

		"x" : SCREEN_WIDTH - 136,
		"y" : 0,

		"width" : 136,
		"height" : 137,

		"children" :
		(
			## OpenWindow
			{
				"name" : "OpenWindow",
				"type" : "window",

				"x" : 0,
				"y" : 0,

				"width" : 136,
				"height" : 137,

				"children" :
				(
					{
						"name" : "OpenWindowBGI",
						"type" : "image",
						"x" : 0,
						"y" : 0,
						"image" : ROOT + "minimap.sub",
					},
					## MiniMapWindow
					{
						"name" : "MiniMapWindow",
						"type" : "window",

						"x" : 4,
						"y" : 5,

						"width" : 128,
						"height" : 128,
					},
					## ScaleUpButton
					{
						"name" : "ScaleUpButton",
						"type" : "button",

						"x" : 101,
						"y" : 116,

						"default_image" : ROOT + "minimap_scaleup_default.sub",
						"over_image" : ROOT + "minimap_scaleup_over.sub",
						"down_image" : ROOT + "minimap_scaleup_down.sub",
					},
					## ScaleDownButton
					{
						"name" : "ScaleDownButton",
						"type" : "button",

						"x" : 115,
						"y" : 103,

						"default_image" : ROOT + "minimap_scaledown_default.sub",
						"over_image" : ROOT + "minimap_scaledown_over.sub",
						"down_image" : ROOT + "minimap_scaledown_down.sub",
					},
					## MiniMapHideButton
					{
						"name" : "MiniMapHideButton",
						"type" : "button",

						"x" : 111,
						"y" : 6,

						"default_image" : ROOT + "minimap_close_default.sub",
						"over_image" : ROOT + "minimap_close_over.sub",
						"down_image" : ROOT + "minimap_close_down.sub",
					},
					## AtlasShowButton
					{
						"name" : "AtlasShowButton",
						"type" : "button",

						"x" : 12,
						"y" : 12,

						"default_image" : ROOT + "atlas_open_default.sub",
						"over_image" : ROOT + "atlas_open_over.sub",
						"down_image" : ROOT + "atlas_open_down.sub",
					},
					## ServerInfo
					{
						"name" : "ServerInfo",
						"type" : "text",
						
						"text_horizontal_align" : "center",

						"outline" : 1,

						"x" : 70,
						"y" : 140,

						"text" : "",
					},
					## PositionInfo
					{
						"name" : "PositionInfo",
						"type" : "text",
						
						"text_horizontal_align" : "center",

						"outline" : 1,

						"x" : 70,
						"y" : 160,

						"text" : "",
					},
					## ObserverCount
					{
						"name" : "ObserverCount",
						"type" : "text",
						
						"text_horizontal_align" : "center",

						"outline" : 1,

						"x" : 70,
						"y" : 180,

						"text" : "",
					},
				),
			},
			{
				"name" : "CloseWindow",
				"type" : "window",

				"x" : 0,
				"y" : 0,

				"width" : 132,
				"height" : 48,

				"children" :
				(
					## ShowButton
					{
						"name" : "MiniMapShowButton",
						"type" : "button",

						"x" : 100,
						"y" : 4,

						"default_image" : ROOT + "minimap_open_default.sub",
						"over_image" : ROOT + "minimap_open_default.sub",
						"down_image" : ROOT + "minimap_open_default.sub",
					},
				),
			},
		),
	}
