## ============================================================================
## systems/inventory.rpy — Satchel Inventory, Keepsakes & Usable Field Supplies
## ============================================================================

# Maps item_id -> quantity
default inventory_items = {
    "hero_sketchbook": 1,
    "laundry_token": 1,
}

default selected_item_id = "hero_sketchbook"

init python:
    ITEM_DB = {
        "hero_sketchbook": {
            "name": "Battered Hero Sketchbook",
            "category": "Keepsake",
            "icon": "images/ui/icon_sketchbook.png",
            "usable": True,
            "consumable": False,
            "desc": "A taped-together spiral notebook from fourth grade titled 'Chronicles of Sir Valorian.' Half the pages still have dried mud stains from behind the school bleachers; the newer margins are filled with convenience-store budgets and sketches of Thornwick.",
        },
        "laundry_token": {
            "name": "Eastside Laundromat Token",
            "category": "Keepsake",
            "icon": "images/ui/icon_token.png",
            "usable": True,
            "consumable": False,
            "desc": "A grooved brass dryer token stamped 'NO CASH REFUNDS.' Cold, cheap, undeniably real—rubbing your thumb over the ridge reminds you of warm detergent steam on rainy Tuesday nights.",
        },
        "grounding_spade": {
            "name": "Orin's Copper-Veined Spade",
            "category": "Tool / Weapon",
            "icon": "images/ui/icon_spade.png",
            "usable": False,
            "consumable": False,
            "desc": "Definitely not Excalibur. A sturdy ash-wood trenching spade inlaid with Rootwarden copper wire designed to channel wild Resonance safely into bedrock (+2 Tactical Guard & Grounding bonus).",
        },
        "recall_astrolabe": {
            "name": "Calibrated Recall Astrolabe",
            "category": "Relic",
            "icon": "images/ui/icon_astrolabe.png",
            "usable": False,
            "consumable": False,
            "desc": "Vespera's three-ring brass astrolabe, freshly silver-soldered in Orin's workshop. Capable of reading both Memory Tether frequencies and interworld seams.",
        },
        "iron_stew": {
            "name": "Bram's Iron-Skillet Ration",
            "category": "Supply",
            "icon": "images/ui/icon_stew.png",
            "usable": True,
            "consumable": True,
            "desc": "Smoked root-marrow, roasted garlic, and barley wrapped in waxed parchment. Restores +35 HP and +20 Focus when eaten.",
        },
        "meadow_tea": {
            "name": "Conservatory Clover Tea",
            "category": "Supply",
            "icon": "images/ui/icon_tea.png",
            "usable": True,
            "consumable": True,
            "desc": "A warm flask steeped with Master Orin's real green meadow-mint and white clover. Restores +10% Reality Tether and +25 Focus.",
        },
        "pressed_clover": {
            "name": "Pressed First-Era Clover",
            "category": "Hidden Relic",
            "icon": "images/ui/icon_clover_item.png",
            "usable": False,
            "consumable": False,
            "desc": "A four-hundred-year-old three-leaf clover preserved inside thin mica glass, etched with English handwriting on the back: 'Don't forget to go home when the rain stops.'",
        },
        "sixth_seal_shard": {
            "name": "Resonant Salt-Glass Shard",
            "category": "Relic",
            "icon": "images/ui/icon_shard.png",
            "usable": False,
            "consumable": False,
            "desc": "A humming fragment from the Sunken Archive. Warm to the touch, whispering faint fragments of someone else's forgotten summer vacation.",
        },
    }

    ITEM_ORDER = [
        "hero_sketchbook", "laundry_token", "grounding_spade", "recall_astrolabe",
        "iron_stew", "meadow_tea", "pressed_clover", "sixth_seal_shard",
    ]

    def add_item(item_id, qty=1, silent=False):
        if item_id not in ITEM_DB or qty <= 0:
            return
        store.inventory_items[item_id] = store.inventory_items.get(item_id, 0) + qty
        store.selected_item_id = item_id
        if not silent:
            meta = ITEM_DB[item_id]
            suffix = f" x{qty}" if qty > 1 else ""
            push_toast(f"Item Acquired: {meta['name']}{suffix}", meta["category"], "#ebb963")

    def has_item(item_id, qty=1):
        return store.inventory_items.get(item_id, 0) >= qty

    def item_count(item_id):
        return store.inventory_items.get(item_id, 0)

    def remove_item(item_id, qty=1):
        cur = store.inventory_items.get(item_id, 0)
        if cur <= qty:
            store.inventory_items.pop(item_id, None)
        else:
            store.inventory_items[item_id] = cur - qty

    def use_satchel_item(item_id):
        if not has_item(item_id):
            return
        meta = ITEM_DB.get(item_id)
        if not meta or not meta["usable"]:
            return

        if item_id == "iron_stew":
            remove_item("iron_stew", 1)
            renpy.sound.play("audio/sfx/meadow_breath.ogg")
            restore_vitality(hp_gain=35, focus_gain=20, silent=True)
            push_toast("Ate Bram's Ration", "+35 HP, +20 Focus. Heavy on the garlic—just right.", "#f29559")
        elif item_id == "meadow_tea":
            remove_item("meadow_tea", 1)
            renpy.sound.play("audio/sfx/meadow_breath.ogg")
            restore_vitality(hp_gain=15, focus_gain=25, silent=True)
            change_tether(10, "Warm scent of real clover and mint.", silent=False)
        elif item_id == "hero_sketchbook":
            if not has_flag("reflected_sketchbook"):
                set_flag("reflected_sketchbook")
                change_tether(4, "Remembered who drew those crooked capes.", silent=False)
            else:
                push_toast("Battered Sketchbook", "Your childhood drawings look smaller now—and kinder.", "#ebb963")
        elif item_id == "laundry_token":
            if not has_flag("reflected_token"):
                set_flag("reflected_token")
                change_tether(4, "Dryer #4 always squeaked on spin cycle.", silent=False)
            else:
                push_toast("Laundromat Token", "Cool brass in your palm. Earth is still waiting.", "#73d2de")
