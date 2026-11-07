## ============================================================================
## screens/custom_menus.rpy — Status, Relationships, Journal/Codex, Satchel & Awards
## ============================================================================

default journal_tab = "quests"
default selected_codex_id = "codex_solvara"

## 1. CHARACTER STATUS SCREEN -------------------------------------------------
screen character_status_screen():
    tag menu
    use game_menu(_("Character Status"), scroll="viewport"):
        vbox:
            spacing 18
            xsize 880

            # Top Psychological Summary Card
            frame:
                xfill True
                background Solid("#12212be8")
                padding (20, 16)

                hbox:
                    spacing 22
                    xfill True

                    frame:
                        xsize 120
                        ysize 145
                        background Solid("#0c161e")
                        padding (6, 6)
                        add Transform("images/characters/leo_neutral.png", xysize=(108, 133), fit="contain") xalign 0.5 yalign 1.0

                    vbox:
                        spacing 6
                        xfill True
                        hbox:
                            xfill True
                            text "[leo_display_name] Sato" font "fonts/LiberationSerif-Bold.ttf" size 26 color "#ebb963"
                            text "Brass Crowns: [brass_crowns]" size 16 color "#ebb963" xalign 1.0 yalign 0.5

                        text "Accidental Outworlder • State: [tether_status_label()]" size 15 color "#9ec4d8"

                        hbox:
                            spacing 12
                            text "Reality Tether:" size 15 color "#7ec876" xsize 145
                            bar value tether range 100 xsize 320 ysize 16 yalign 0.5
                            text "[tether]%" size 15 font "fonts/Roboto-Bold.ttf" color "#eaeef2"

                        hbox:
                            spacing 12
                            text "Astral Resonance:" size 15 color "#c792ea" xsize 145
                            bar value resonance_load range 100 xsize 320 ysize 16 yalign 0.5
                            text "[resonance_load]%" size 15 font "fonts/Roboto-Bold.ttf" color "#dfc2f7"

                        hbox:
                            spacing 24
                            text "Vitality (HP): [leo_hp] / [leo_max_hp]" size 14 color "#a7e8a1"
                            text "Breath Focus: [leo_focus] / [leo_max_focus]" size 14 color "#73d2de"
                            text "Clover Relics: [clover_relics_found] / 3" size 14 color "#ebb963"

            text "Core Attributes" font "fonts/LiberationSerif-Bold.ttf" size 22 color "#ebb963"

            # 6 Core Stats List
            vbox:
                spacing 10
                for key, label, col, desc in STAT_METADATA:
                    $ val = leo_stats.get(key, 0)
                    $ disp_bar = max(0, val) if key != "reputation" else max(0, val + 5)
                    $ disp_max = 12 if key != "reputation" else 20
                    frame:
                        xfill True
                        background Solid("#101c24dc")
                        padding (16, 10)
                        vbox:
                            spacing 4
                            hbox:
                                xfill True
                                text "[label]" font "fonts/Roboto-Bold.ttf" size 18 color col xsize 160
                                bar value disp_bar range disp_max xsize 340 ysize 14 yalign 0.5
                                text "  [val]" font "fonts/Roboto-Bold.ttf" size 18 color "#ffffff"
                            text "[desc]" size 14 color "#a5b7c4"


## 2. RELATIONSHIPS / BONDS SCREEN --------------------------------------------
screen relationships_screen():
    tag menu
    use game_menu(_("Companions & Bonds"), scroll="viewport"):
        vbox:
            spacing 14
            xsize 880

            text "The people of Solvara have lives, regrets, and loyalties that do not revolve around you. Choices determine whether you remain a stranger—or become someone's anchor." size 15 color "#a9bcc9" xsize 835

            for cid in CHARACTER_ORDER:
                $ meta = CHARACTER_PROFILES[cid]
                $ is_met = cid in met_characters
                $ aff = get_affinity(cid)
                $ rank_txt = affinity_rank(cid)

                frame:
                    xfill True
                    background Solid("#12202ae8" if is_met else "#0e171ecc")
                    padding (18, 14)

                    if is_met:
                        hbox:
                            spacing 18
                            frame:
                                xsize 96
                                ysize 118
                                background Solid("#0a1218")
                                padding (4, 4)
                                add Transform(meta["sprite"], xysize=(88, 110), fit="contain") xalign 0.5 yalign 1.0

                            vbox:
                                spacing 5
                                xfill True
                                hbox:
                                    xfill True
                                    text meta["name"] font "fonts/LiberationSerif-Bold.ttf" size 22 color meta["color"]
                                    text "[rank_txt]  (Affinity: [aff])" font "fonts/Roboto-Bold.ttf" size 15 color "#ebb963" xalign 1.0 yalign 0.5

                                text meta["role"] size 14 color "#8fb0c4"
                                bar value (aff + 5) range 18 xsize 380 ysize 12
                                text meta["summary"] size 14 color "#d6e0e8"

                                if has_flag(meta["secret_flag"]):
                                    text "{font=fonts/DejaVuSans.ttf}★{/font} " + meta["secret_note"] size 13 color "#7ec876"
                    else:
                        hbox:
                            spacing 16
                            text "???" font "fonts/LiberationSerif-Bold.ttf" size 22 color "#5f7280"
                            text "Unmet figure in Solvara. Continue the story to cross paths." size 15 color "#6d808f" yalign 0.5


## 3. JOURNAL & WORLDBUILDING CODEX SCREEN ------------------------------------
screen journal_screen():
    tag menu
    use game_menu(_("Journal & Codex")):
        vbox:
            spacing 14
            xsize 890
            ysize 540

            # Tab Switcher
            hbox:
                spacing 14
                button:
                    background Solid("#264a3e" if journal_tab == "quests" else "#13212b")
                    hover_background Solid("#336353")
                    padding (20, 8)
                    action SetVariable("journal_tab", "quests")
                    text "Quests & Objectives ([len(quest_states)])" font "fonts/Roboto-Bold.ttf" size 17 color ("#ffdf9a" if journal_tab == "quests" else "#9eb2c0")

                button:
                    background Solid("#264a3e" if journal_tab == "codex" else "#13212b")
                    hover_background Solid("#336353")
                    padding (20, 8)
                    action SetVariable("journal_tab", "codex")
                    text "Solvara World Codex ([len(unlocked_codex)]/[len(CODEX_ORDER)])" font "fonts/Roboto-Bold.ttf" size 17 color ("#ffdf9a" if journal_tab == "codex" else "#9eb2c0")

            add Solid("#29434f") xsize 880 ysize 2

            if journal_tab == "quests":
                viewport:
                    xfill True
                    ysize 465
                    scrollbars "vertical"
                    mousewheel True

                    vbox:
                        spacing 12
                        xfill True
                        if not quest_states:
                            text "No quests recorded yet. Survive tonight first." size 16 color "#8ea2b0"
                        for qid in QUEST_ORDER:
                            if qid in quest_states:
                                $ qmeta = QUEST_DB[qid]
                                $ qstate = quest_states[qid]
                                $ done = qstate["status"] == "completed"
                                frame:
                                    xfill True
                                    background Solid("#112320e6" if done else "#13212be8")
                                    padding (18, 12)
                                    vbox:
                                        spacing 4
                                        hbox:
                                            xfill True
                                            text "[qmeta['title']]" font "fonts/LiberationSerif-Bold.ttf" size 20 color ("#7ec876" if done else qmeta["color"])
                                            text ("[qmeta['category']] • {font=fonts/DejaVuSans.ttf}✓{/font} COMPLETED" if done else "[qmeta['category']] • ACTIVE") size 13 font "fonts/Roboto-Bold.ttf" color ("#7ec876" if done else "#ebb963") xalign 1.0 yalign 0.5
                                        text "[qmeta['summary']]" size 14 color "#b8c7d4"
                                        text "{font=fonts/DejaVuSans.ttf}▸{/font} Current Note: [qstate['step']]" size 14 font "fonts/Roboto-Medium.ttf" color "#eaeef2"
            else:
                hbox:
                    spacing 18
                    xfill True
                    ysize 465

                    # Left Codex List
                    viewport:
                        xsize 320
                        ysize 465
                        scrollbars "vertical"
                        mousewheel True
                        vbox:
                            spacing 6
                            for cid in CODEX_ORDER:
                                $ ctitle, ccat, _ = CODEX_DB[cid]
                                $ is_open = cid in unlocked_codex
                                button:
                                    xsize 302
                                    background Solid("#224238" if selected_codex_id == cid and is_open else "#111d26")
                                    hover_background Solid("#2b4f44")
                                    padding (12, 9)
                                    sensitive is_open
                                    action SetVariable("selected_codex_id", cid)
                                    vbox:
                                        text (ctitle if is_open else "Locked Entry") size 15 font "fonts/Roboto-Bold.ttf" color ("#ffdf9a" if selected_codex_id == cid and is_open else ("#d5e0e8" if is_open else "#5c6d7a"))
                                        text (ccat if is_open else "Explore Solvara to unlock") size 12 color "#8399a8"

                    # Right Codex Reader
                    frame:
                        xsize 540
                        ysize 465
                        background Solid("#101b24eb")
                        padding (22, 18)
                        if selected_codex_id in unlocked_codex and selected_codex_id in CODEX_DB:
                            $ rtitle, rcat, rbody = CODEX_DB[selected_codex_id]
                            vbox:
                                spacing 10
                                text "[rcat]" size 13 font "fonts/Roboto-Bold.ttf" color "#7ec876"
                                text "[rtitle]" font "fonts/LiberationSerif-Bold.ttf" size 25 color "#ebb963"
                                add Solid("#29434f") xsize 490 ysize 2
                                text "[rbody]" size 17 color "#e2eaf0" line_spacing 6


## 4. INVENTORY / SATCHEL SCREEN ----------------------------------------------
screen inventory_screen():
    tag menu
    use game_menu(_("Satchel & Relics")):
        hbox:
            spacing 20
            xsize 890
            ysize 520

            # Left Item List
            viewport:
                xsize 380
                ysize 520
                scrollbars "vertical"
                mousewheel True
                vbox:
                    spacing 8
                    for iid in ITEM_ORDER:
                        if has_item(iid):
                            $ imeta = ITEM_DB[iid]
                            $ qty = item_count(iid)
                            button:
                                xsize 360
                                background Solid("#224038" if selected_item_id == iid else "#121f29")
                                hover_background Solid("#2d5248")
                                padding (12, 10)
                                action SetVariable("selected_item_id", iid)
                                hbox:
                                    spacing 12
                                    add imeta["icon"] xysize (44, 44) yalign 0.5
                                    vbox:
                                        yalign 0.5
                                        text "[imeta['name']]" size 16 font "fonts/Roboto-Bold.ttf" color "#f0f4f8"
                                        text "[imeta['category']]  •  Qty: [qty]" size 13 color "#9ab0bf"

            # Right Inspector Panel
            frame:
                xsize 485
                ysize 520
                background Solid("#101c25eb")
                padding (24, 22)

                if selected_item_id in ITEM_DB and has_item(selected_item_id):
                    $ sel = ITEM_DB[selected_item_id]
                    vbox:
                        spacing 14
                        hbox:
                            spacing 16
                            add sel["icon"] xysize (56, 56) yalign 0.5
                            vbox:
                                text "[sel['name']]" font "fonts/LiberationSerif-Bold.ttf" size 24 color "#ebb963"
                                text "[sel['category']]  (Owned: [item_count(selected_item_id)])" size 14 color "#7ec876"

                        add Solid("#28424f") xsize 435 ysize 2
                        text "[sel['desc']!q]" size 16 color "#dce6ee" line_spacing 5

                        if sel["usable"] and not main_menu:
                            button:
                                ypos 12
                                background Solid("#285244")
                                hover_background Solid("#38705d")
                                padding (20, 10)
                                action Function(use_satchel_item, selected_item_id)
                                text ("Consume Supply" if sel["consumable"] else "Hold & Reflect") font "fonts/Roboto-Bold.ttf" size 17 color "#ffdf9a"
                else:
                    text "Select an item from your satchel to inspect its history and effects." size 16 color "#8ea2b0" yalign 0.5


## 5. ACHIEVEMENTS / MILESTONES SCREEN ----------------------------------------
screen achievements_screen():
    tag menu
    use game_menu(_("Achievements"), scroll="viewport"):
        vbox:
            spacing 12
            xsize 880

            hbox:
                xfill True
                text "Cross-Playthrough Milestones & Endings" font "fonts/LiberationSerif-Bold.ttf" size 22 color "#ebb963"
                text "Unlocked: [achievement_count()] / [len(ACHIEVEMENT_DB)]" font "fonts/Roboto-Bold.ttf" size 17 color "#7ec876" xalign 1.0 yalign 0.5

            for aid, atitle, adesc, acol in ACHIEVEMENT_DB:
                $ unlocked = has_achievement(aid)
                frame:
                    xfill True
                    background Solid("#132524eb" if unlocked else "#0e171fd0")
                    padding (16, 12)
                    hbox:
                        spacing 14
                        text ("★" if unlocked else "◇") font "fonts/DejaVuSans.ttf" size 24 color (acol if unlocked else "#4e606d") yalign 0.5
                        vbox:
                            spacing 2
                            text "[atitle]" font "fonts/Roboto-Bold.ttf" size 17 color (acol if unlocked else "#708290")
                            text (adesc if unlocked else "Hidden milestone — continue exploring choices and routes to unlock.") size 14 color ("#d8e3ec" if unlocked else "#5d6e7b")
