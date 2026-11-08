## ============================================================================
## screens.rpy — Custom Indie UI: Title Screen, Dialogue, Choices & Core Menus
## WHERE THE GRASS STILL GROWS (1280x720 HD)
## ============================================================================

init offset = -1

################################################################################
## Styles Foundation
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5

style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")

style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"

style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)


################################################################################
## In-Game Screens: Say (Dialogue), Input, Choice & Quick Menu
################################################################################

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who" style "say_label"

        text what id "what" style "say_dialogue"

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue
style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    adjust_spacing False


## Input Screen ---------------------------------------------------------------
screen input(prompt):
    style_prefix "input"

    window:
        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default
style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice Screen --------------------------------------------------------------
screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            button:
                xsize 840
                background Solid("#101d27eb")
                hover_background Solid("#1e3b34f5")
                insensitive_background Solid("#0d151cc8")
                padding (24, 13)
                action i.action

                hbox:
                    spacing 14
                    yalign 0.5
                    text "❖" font "fonts/DejaVuSans.ttf" size 17 color "#ebb963" yalign 0.5
                    text i.caption:
                        font "fonts/Roboto-Medium.ttf"
                        size 19
                        color "#eaeef2"
                        hover_color "#ffdf9a"
                        insensitive_color "#6b7b88"
                        yalign 0.5

style choice_vbox is vbox
style choice_vbox:
    xalign 0.5
    ypos 295
    yanchor 0.5
    spacing 12


## Quick Menu Screen ----------------------------------------------------------
screen quick_menu():
    zorder 100

    if quick_menu and not main_menu and not is_any_menu_open():
        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 0.992
            spacing 8

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Status") action ShowMenu('character_status_screen')
            textbutton _("Journal") action ShowMenu('journal_screen')
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Settings") action ShowMenu('preferences')

init python:
    if "quick_menu" not in config.overlay_screens:
        config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Main Menu & Game Menu Navigation
################################################################################

screen navigation():
    vbox:
        style_prefix "navigation"
        xpos 32
        ypos (308 if main_menu else 108)
        yanchor 0.0
        spacing 7

        if main_menu:
            textbutton _("Begin Journey") action Start()
            textbutton _("Load Chronicle") action ShowMenu("load")
            textbutton _("Achievements ([achievement_count()]/[len(ACHIEVEMENT_DB)])") action ShowMenu("achievements_screen")
            textbutton _("Settings") action ShowMenu("preferences")
            textbutton _("About") action ShowMenu("about")
            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                textbutton _("Controls & Help") action ShowMenu("help")
            if renpy.variant("pc"):
                textbutton _("Exit to Real World") action Quit(confirm=False)
        else:
            textbutton _("Character Status") action ShowMenu("character_status_screen")
            textbutton _("Companions & Bonds") action ShowMenu("relationships_screen")
            textbutton _("Journal & Codex") action ShowMenu("journal_screen")
            textbutton _("Satchel ([len(inventory_items)])") action ShowMenu("inventory_screen")
            textbutton _("Achievements") action ShowMenu("achievements_screen")
            add Solid("#29434f") xsize 190 ysize 1
            textbutton _("Dialogue Log") action ShowMenu("history")
            textbutton _("Save Game") action ShowMenu("save")
            textbutton _("Load Game") action ShowMenu("load")
            textbutton _("Settings") action ShowMenu("preferences")
            textbutton _("Title Screen") action MainMenu()
            if renpy.variant("pc"):
                textbutton _("Quit") action Quit(confirm=True)

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    hover_background Solid("#1e3933a8")
    padding (12, 6)

style navigation_button_text:
    properties gui.text_properties("navigation_button")
    font "fonts/Roboto-Medium.ttf"
    size 18
    idle_color "#c6d5e0"
    hover_color "#ffdf9a"
    selected_color "#7ec876"


## Custom Title Screen --------------------------------------------------------
screen main_menu():
    tag menu

    add "cg title_meadow" at slow_pan_zoom
    add "gui/overlay/main_menu.png"

    # Left dark botanical glass sidebar
    frame:
        xpos 0
        ypos 0
        xsize 430
        ysize 720
        background Solid("#091219d8")
        padding (36, 38)

        vbox:
            spacing 8
            ypos 4
            yanchor 0.0

            text _("AN UNWANTED HERO'S CHRONICLE"):
                font "fonts/Roboto-Bold.ttf"
                size 13
                color "#7ec876"

            text _("Where the Grass\nStill Grows"):
                font "fonts/LiberationSerif-Bold.ttf"
                size 40
                color "#f4f7fa"
                line_spacing 2

            add Solid("#ebb963") xsize 165 ysize 2

            text _("\"This world does not need another savior.\nIt needs someone willing to stay human.\""):
                font "fonts/LiberationSerif-Italic.ttf"
                size 15
                color "#afc2d0"
                ypos 4

    use navigation

    # Top-right Language / Bahasa Switcher Pill
    frame:
        xalign 0.98
        ypos 18
        background Solid("#0c161fe0")
        padding (14, 7)
        hbox:
            spacing 10
            yalign 0.5
            text _("Language:") size 14 color "#9ab0bf" yalign 0.5
            textbutton "English":
                action Language(None)
                text_size 14
                text_font "fonts/Roboto-Bold.ttf"
                text_idle_color "#9eb2c0"
                text_hover_color "#ffdf9a"
                text_selected_color "#7ec876"
                yalign 0.5
            text "|" size 14 color "#3a505d" yalign 0.5
            textbutton "Bahasa Indonesia":
                action Language("indonesian")
                text_size 14
                text_font "fonts/Roboto-Bold.ttf"
                text_idle_color "#9eb2c0"
                text_hover_color "#ffdf9a"
                text_selected_color "#7ec876"
                yalign 0.5

    # Bottom-right version & milestone pill
    frame:
        xalign 0.98
        yalign 0.96
        background Solid("#0c161fd4")
        padding (16, 8)
        hbox:
            spacing 14
            text _("{font=fonts/DejaVuSans.ttf}★{/font} Milestones: [achievement_count()] / [len(ACHIEVEMENT_DB)]") size 14 color "#ebb963"
            text "•" size 14 color "#4a6170"
            text "v[config.version]" size 14 color "#9ab0bf"


## Game Menu Wrapper ----------------------------------------------------------
screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):
    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    add "gui/overlay/game_menu.png"

    frame:
        style "game_menu_outer_frame"

        hbox:
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True

                        vbox:
                            spacing spacing
                            transclude

                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        spacing spacing
                        transclude

                else:
                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"
        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar
style game_menu_label is gui_label
style game_menu_label_text is gui_label_text
style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 24
    top_padding 82

style game_menu_navigation_frame:
    xsize 255
    yfill True

style game_menu_content_frame:
    left_margin 24
    right_margin 24
    top_margin 6

style game_menu_viewport:
    xsize 940

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 280
    ysize 76

style game_menu_label_text:
    font "fonts/LiberationSerif-Bold.ttf"
    size 34
    color "#ebb963"
    yalign 0.5

style return_button:
    xpos 32
    yalign 1.0
    yoffset -22


################################################################################
## Standard Utility Screens: About, Save/Load, Preferences, History, Help, Confirm
################################################################################

screen about():
    tag menu
    use game_menu(_("About"), scroll="viewport"):
        style_prefix "about"
        vbox:
            spacing 12
            xsize 860
            label "[config.name!t]"
            text _("Version [config.version!t]\n") color "#7ec876"
            if gui.about:
                text "[gui.about!t]\n" line_spacing 5
            text _("Engine: {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n[renpy.license!t]") size 15 color "#93a7b6"

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text


screen save():
    tag menu
    use file_slots(_("Save Chronicle"))

screen load():
    tag menu
    use file_slots(_("Load Chronicle"))

screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic Saves"), quick=_("Quick Saves"))

    use game_menu(title):
        fixed:
            order_reverse True

            button:
                style "page_label"
                key_events True
                xalign 0.5
                action page_name_value.Toggle()
                input:
                    style "page_label_text"
                    value page_name_value

            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                xalign 0.5
                yalign 0.48
                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1
                    button:
                        action FileAction(slot)
                        has vbox
                        add FileScreenshot(slot) xalign 0.5
                        text FileTime(slot, format=_("{#file_time}%b %d, %Y — %H:%M"), empty=_("Empty Slot")):
                            style "slot_time_text"
                        text FileSaveName(slot):
                            style "slot_name_text"
                        key "save_delete" action FileDelete(slot)

            hbox:
                style_prefix "page"
                xalign 0.5
                yalign 0.98
                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()
                key "save_page_prev" action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}Auto") action FilePage("auto")
                if config.has_quicksave:
                    textbutton _("{#quick_page}Quick") action FilePage("quick")

                for page in range(1, 9):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()
                key "save_page_next" action FilePageNext()

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text
style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 30
    ypadding 3

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Settings / Preferences Screen ----------------------------------------------
screen preferences():
    tag menu

    use game_menu(_("Settings"), scroll="viewport"):
        vbox:
            xsize 860
            spacing 24

            hbox:
                box_wrap True
                spacing 40

                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Windowed") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip Options")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                vbox:
                    style_prefix "radio"
                    label _("Language")
                    textbutton "English" action Language(None)
                    textbutton "Bahasa Indonesia" action Language("indonesian")

            hbox:
                style_prefix "slider"
                box_wrap True
                spacing 40

                vbox:
                    spacing 12
                    label _("Text Speed")
                    bar value Preference("text speed")

                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time")

                vbox:
                    spacing 12
                    if config.has_music:
                        label _("Music Volume")
                        bar value Preference("music volume")

                    if config.has_sound:
                        label _("Sound & Ambience Volume")
                        hbox:
                            spacing 12
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)

                    textbutton _("Mute All Audio"):
                        action Preference("all mute", "toggle")
                        style "mute_all_button"

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox
style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox
style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox
style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox
style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin 6
    bottom_margin 2

style pref_label_text:
    font "fonts/LiberationSerif-Bold.ttf"
    size 22
    color "#ebb963"
    yalign 1.0

style pref_vbox:
    xsize 240

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 340


## Dialogue History Screen ----------------------------------------------------
screen history():
    tag menu
    predict False

    use game_menu(_("Dialogue Log"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):
        style_prefix "history"

        for h in _history_list:
            window:
                has fixed:
                    yfit True
                if h.who:
                    label h.who:
                        style "history_name"
                        substitute False
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The chronicle log is currently empty.")

define gui.history_allow_tags = {"alt", "noalt", "rt", "rb", "art", "i", "b"}

style history_window is empty
style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text
style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign
    font "fonts/LiberationSerif-Bold.ttf"
    size 19

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")


## Help Screen ----------------------------------------------------------------
screen help():
    tag menu
    default device = "keyboard"

    use game_menu(_("Controls & Help"), scroll="viewport"):
        style_prefix "help"
        vbox:
            spacing 14
            xsize 860

            hbox:
                spacing 16
                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")
                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help

screen keyboard_help():
    hbox:
        label _("Enter / Space")
        text _("Advance dialogue, select choices, and lock Astrolabe rings.")
    hbox:
        label _("Escape")
        text _("Open Character Status, Journal, Save, and Settings menu.")
    hbox:
        label _("Ctrl")
        text _("Hold to fast-skip dialogue.")
    hbox:
        label _("Page Up / Wheel Up")
        text _("Roll back to previous dialogue and decisions.")
    hbox:
        label _("H")
        text _("Hide UI to admire artwork and backgrounds.")

screen mouse_help():
    hbox:
        label _("Left Click")
        text _("Advance dialogue, inspect exploration locations, and choose stances.")
    hbox:
        label _("Right Click")
        text _("Open or close the RPG menu.")
    hbox:
        label _("Scroll Wheel")
        text _("Roll back or forward through seen dialogue.")

screen gamepad_help():
    hbox:
        label _("A / Bottom Button")
        text _("Advance dialogue and confirm selections.")
    hbox:
        label _("Start / Guide")
        text _("Open the RPG menu.")
    hbox:
        label _("Calibration")
        textbutton _("Calibrate Gamepad") action GamepadCalibrate()

style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_label:
    xsize 240
    right_padding 20

style help_label_text:
    size 18
    color "#ebb963"
    xalign 1.0
    textalign 1.0


## Confirm Dialog Screen ------------------------------------------------------
screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 28

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 80
                textbutton _("Confirm") action yes_action
                textbutton _("Cancel") action no_action

    key "game_menu" action no_action

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame("gui/frame.png", gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"


## Skip & Notify Screens ------------------------------------------------------
screen skip_indicator():
    zorder 100
    style_prefix "skip"

    frame:
        hbox:
            spacing 6
            text _("Fast-Forwarding")
            text "▸" style "skip_triangle"

style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    font "fonts/DejaVuSans.ttf"


screen notify(message):
    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')

transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos
    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL Screen -----------------------------------------------------------------
screen nvl(dialogue, items=None):
    window:
        style "nvl_window"
        has vbox:
            spacing gui.nvl_spacing
        use nvl_dialogue(dialogue)
        vbox:
            for i in items:
                textbutton i.caption:
                    action i.action
                    style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0

screen nvl_dialogue(dialogue):
    for d in dialogue:
        window:
            id d.window_id
            fixed:
                yfit gui.nvl_height is None
                if d.who is not None:
                    text d.who:
                        id d.who_id
                text d.what:
                    id d.what_id

style nvl_window is default
style nvl_entry is default
style nvl_label is say_label
style nvl_dialogue is say_dialogue
style nvl_button is button
style nvl_button_text is button_text
