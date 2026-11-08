## ============================================================================
## systems/exploration.rpy — Interactive Hub Exploration Screen
## ============================================================================

default visited_nodes = set()
default hub_actions_left = 4
default hub_max_actions = 4

## Reusable Exploration Hub Screen --------------------------------------------
## nodes: list of dicts:
##   {"id": str, "title": str, "subtitle": str, "tag": str, "color": str, "done": bool, "cost": int}
## proceed_label: text for the button that advances main story once ready (or anytime if min_required met)
screen exploration_hub(hub_title, hub_subtitle, nodes, can_advance=True, advance_hint="Proceed to Main Objective"):
    modal True
    zorder 40

    # Subtle dark gradient vignette on top of current scene background
    add Solid("#070d139e")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1120
        ysize 590
        background Frame("images/ui/panel_frame.png", 16, 16)
        padding (32, 26)

        vbox:
            spacing 14
            xfill True

            # Header Row
            hbox:
                xfill True
                vbox:
                    spacing 2
                    text tr(hub_title) font "fonts/LiberationSerif-Bold.ttf" size 30 color "#ebb963"
                    text tr(hub_subtitle) size 17 color "#a9bcc9"

                frame:
                    xalign 1.0
                    yalign 0.5
                    background Solid("#14262f")
                    padding (16, 8)
                    hbox:
                        spacing 12
                        text _("Exploration Actions:") size 16 color "#9eb2c0" yalign 0.5
                        text "[hub_actions_left] / [hub_max_actions]" font "fonts/Roboto-Bold.ttf" size 20 color "#7ec876" yalign 0.5

            add Solid("#2c4652") xsize 1056 ysize 2

            # Interactive Location Grid (2 columns)
            viewport:
                xfill True
                ysize 395
                scrollbars "vertical"
                mousewheel True

                vpgrid:
                    cols 2
                    spacing 16
                    xfill True

                    for node in nodes:
                        $ is_done = node.get("done", False)
                        $ cost = node.get("cost", 1)
                        $ affordable = (not is_done) and (hub_actions_left >= cost or cost == 0)
                        $ border_col = "#364954" if is_done else (node.get("color", "#7ec876") if affordable else "#45525c")
                        $ bg_col = "#0f1921cc" if is_done else ("#152632ee" if affordable else "#111b23cc")

                        button:
                            xsize 512
                            ysize 116
                            background Solid(bg_col)
                            hover_background Solid("#1f3a36f5")
                            padding (18, 14)
                            sensitive affordable
                            action Return(node["id"])

                            vbox:
                                spacing 5
                                xfill True
                                hbox:
                                    xfill True
                                    text tr(node["title"]):
                                        font "fonts/LiberationSerif-Bold.ttf"
                                        size 21
                                        color ("#7c8d99" if is_done else "#f0f4f8")
                                    if is_done:
                                        text _("{font=fonts/DejaVuSans.ttf}✓{/font} Visited") size 14 color "#7ec876" xalign 1.0 yalign 0.5
                                    elif cost == 0:
                                        text _("Free Inspect") size 14 color "#73d2de" xalign 1.0 yalign 0.5
                                    else:
                                        text "-[cost] AP" size 14 color node.get("color", "#ebb963") xalign 1.0 yalign 0.5

                                text tr(node["tag"]) size 13 color border_col font "fonts/Roboto-Bold.ttf"
                                text tr(node["subtitle"]) size 15 color ("#6d7e8a" if is_done else "#b8c7d4")

            # Bottom Footer: Quick Utility + Advance Story Button
            hbox:
                xfill True
                yalign 1.0
                spacing 14

                textbutton _("Status & Stats") action ShowMenu("character_status_screen") text_size 16
                textbutton _("Bonds") action ShowMenu("relationships_screen") text_size 16
                textbutton _("Journal & Codex") action ShowMenu("journal_screen") text_size 16
                textbutton _("Satchel ([len(inventory_items)])") action ShowMenu("inventory_screen") text_size 16

                if can_advance:
                    button:
                        xalign 1.0
                        background Solid("#264a3e")
                        hover_background Solid("#356856")
                        padding (22, 10)
                        action Return("__ADVANCE__")
                        text "[advance_hint!t]  {font=fonts/DejaVuSans.ttf}→{/font}" font "fonts/Roboto-Bold.ttf" size 18 color "#ffdf9a"
                else:
                    text _("Explore at least one key location first") xalign 1.0 yalign 0.5 size 16 color "#8ea2b0"
