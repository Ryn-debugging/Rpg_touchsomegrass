## ============================================================================
## screens/hud_and_toasts.rpy — Top Gameplay HUD, Toast Popups & Chapter Cards
## ============================================================================

init python:
    if "gameplay_hud" not in config.overlay_screens:
        config.overlay_screens.append("gameplay_hud")

    MENU_SCREEN_NAMES = (
        "character_status_screen", "relationships_screen", "journal_screen",
        "inventory_screen", "achievements_screen", "save", "load",
        "preferences", "history", "about", "help",
        "exploration_hub", "astrolabe_minigame", "tactical_duel", "chapter_title_card",
    )

    def is_any_menu_open():
        return any(renpy.get_screen(s) is not None for s in MENU_SCREEN_NAMES)

transform toast_appear:
    alpha 0.0 yoffset -14
    easein 0.20 alpha 1.0 yoffset 0

## Top-of-Screen Gameplay Bar -------------------------------------------------
screen gameplay_hud():
    zorder 30

    if hud_visible and not main_menu and not is_any_menu_open():
        frame:
            xalign 0.5
            ypos 8
            xsize 1244
            ysize 42
            background Solid("#0b141cd9")
            padding (16, 6)

            hbox:
                xfill True
                yalign 0.5

                # Left: Chapter & Location
                hbox:
                    spacing 12
                    yalign 0.5
                    text "{font=fonts/DejaVuSans.ttf}❖{/font} [current_chapter_title!t]" font "fonts/LiberationSerif-Bold.ttf" size 15 color "#ebb963" yalign 0.5
                    text "•" size 14 color "#516b78" yalign 0.5
                    text "[current_location_name!t]" size 14 color "#bfd0dc" yalign 0.5

                # Right: Tether Pill + RPG Menu Shortcuts
                hbox:
                    xalign 1.0
                    spacing 12
                    yalign 0.5

                    text _("Tether [tether]%") size 14 font "fonts/Roboto-Bold.ttf" color ("#7ec876" if tether >= 50 else "#e06c75") yalign 0.5
                    text _("Crowns: [brass_crowns]") size 14 color "#ebb963" yalign 0.5
                    text "|" size 14 color "#3a505d" yalign 0.5

                    textbutton _("Status") action ShowMenu("character_status_screen") text_size 14 text_idle_color "#b4c8d6" text_hover_color "#ebb963" yalign 0.5
                    textbutton _("Bonds") action ShowMenu("relationships_screen") text_size 14 text_idle_color "#b4c8d6" text_hover_color "#ebb963" yalign 0.5
                    textbutton _("Journal") action ShowMenu("journal_screen") text_size 14 text_idle_color "#b4c8d6" text_hover_color "#ebb963" yalign 0.5
                    textbutton _("Satchel") action ShowMenu("inventory_screen") text_size 14 text_idle_color "#b4c8d6" text_hover_color "#ebb963" yalign 0.5


## Animated Feedback Toast ----------------------------------------------------
screen toast_banner():
    zorder 95
    timer 3.4 action Hide("toast_banner", transition=Dissolve(0.25))

    if active_toast_title and not is_any_menu_open():
        frame at toast_appear:
            xalign 0.985
            ypos 58
            xmaximum 430
            background Solid("#101e27f2")
            padding (16, 10)

            hbox:
                spacing 10
                add Solid(active_toast_color) xsize 4 ysize 38 yalign 0.5
                vbox:
                    spacing 2
                    text "[active_toast_title!q]" font "fonts/Roboto-Bold.ttf" size 16 color active_toast_color
                    if active_toast_body:
                        text "[active_toast_body!q]" size 13 color "#d3dfe8"


## Cinematic Full-Screen Chapter Title Card -----------------------------------
screen chapter_title_card(chap_label, chap_name, epigraph):
    modal True
    zorder 80

    add Solid("#070c11")
    timer 3.6 action Return()

    button:
        xfill True
        yfill True
        background None
        action Return()

        vbox:
            xalign 0.5
            yalign 0.48
            spacing 14

            text tr(chap_label):
                font "fonts/Roboto-Bold.ttf"
                size 17
                color "#7ec876"
                xalign 0.5

            text tr(chap_name):
                font "fonts/LiberationSerif-Bold.ttf"
                size 46
                color "#f2f5f8"
                xalign 0.5

            add Solid("#ebb963") xsize 220 ysize 2 xalign 0.5

            text tr(epigraph):
                font "fonts/LiberationSerif-Italic.ttf"
                size 20
                color "#b5c6d4"
                xalign 0.5
                text_align 0.5
                xmaximum 780

        text _("Click anywhere to continue") size 13 color "#607382" xalign 0.5 yalign 0.92
