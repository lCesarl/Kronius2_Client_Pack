import uiScriptLocale
import item
COSTUME_START_INDEX = item.COSTUME_SLOT_START
window = {
	"name" : "CostumeEquipmentDialog",

	"x" : 0,
	"y" : 0,

	# "width" : 139,
	# "height" : 145,
	"width" : 140,
	"height" : 180 + 47,

	"children" :
	(
		{
			"name" : "ExpandButton",
			"type" : "button",

			"x" : 2,
			"y" : 20,

			"default_image" : "d:/ymir work/ui/game/belt_inventory/btn_expand_normal.tga",
			"over_image" : "d:/ymir work/ui/game/belt_inventory/btn_expand_over.tga",
			"down_image" : "d:/ymir work/ui/game/belt_inventory/btn_expand_down.tga",
			"disable_image" : "d:/ymir work/ui/game/belt_inventory/btn_expand_disabled.tga",
		},

		{
			"name" : "CostumeEquipmentLayer",

			"x" : 5,
			"y" : 0,

			"width" : 140,
			"height" : 180 + 47,

			"children" :
			(
				{
					"name" : "MinimizeButton",
					"type" : "button",

					"x" : 2,
					"y" : 17,

					"default_image" : "d:/ymir work/ui/game/belt_inventory/btn_minimize_normal.tga",
					"over_image" : "d:/ymir work/ui/game/belt_inventory/btn_minimize_over.tga",
					"down_image" : "d:/ymir work/ui/game/belt_inventory/btn_minimize_down.tga",
					"disable_image" : "d:/ymir work/ui/game/belt_inventory/btn_minimize_disabled.tga",
				},

				{
					"name" : "CostumeEquipmentBoard",
					"type" : "board",
					"style" : ("attach", "float"),

					"x" : 10,
					"y" : 0,

					"width" : 129,
					"height" : 195,

					"children" :
					(
						{
							"name" : "Costume_Base",
							"type" : "image",

							"x" : 8,
							"y" : 8,

							"image" : "d:/ymir work/ui/costume_New.dds",

							"children" :
							(
								{
									"name" : "CostumeEquipmentSlot",
									"type" : "slot",

									"x" : 3,
									"y" : 3,

									"width" : 127,
									"height" : 195,

									"slot" : (
										{"index":11, "x":61, "y":45, "width":32, "height":64},
										{"index":12, "x":61, "y": 8, "width":32, "height":32},
										{"index":13, "x":61, "y":125, "width":32, "height":32},
										{"index":14, "x":13, "y":125, "width":32, "height":32},
										{"index":15, "x":13, "y":20, "width":32, "height":96},
									),
								},
							),
						},
					),
				},
			),
		},
	),
}
