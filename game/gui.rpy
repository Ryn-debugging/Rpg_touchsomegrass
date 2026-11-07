## ============================================================================
## gui.rpy — Visual Identity, Palette & Typography (1280x720 HD)
## Palette: Deep Storm-Slate, Conservatory Moss, Living Meadow & Lantern Amber
## ============================================================================

init offset = -2

init python:
    gui.init(1280, 720)

define config.check_conflicting_properties = True

## Theme Colors ---------------------------------------------------------------
define gui.accent_color = '#7ec876'          # Living Meadow Green
define gui.idle_color = '#a8b8c4'            # Soft Mist Slate
define gui.idle_small_color = '#93a5b3'      # Muted Slate
define gui.hover_color = '#ebb963'           # Warm Lantern Amber
define gui.selected_color = '#ffffff'        # Crisp White
define gui.insensitive_color = '#60707c7f'   # Disabled Slate
define gui.muted_color = '#1b312b'           # Conservatory Moss
define gui.hover_muted_color = '#2b4c3f'     # Highlighted Moss
define gui.text_color = '#eaeef2'            # Warm Ivory
define gui.interface_text_color = '#dde5ec'  # Crisp Interface Ivory

## Typography -----------------------------------------------------------------
define gui.text_font = "fonts/Roboto-Regular.ttf"
define gui.name_text_font = "fonts/LiberationSerif-Bold.ttf"
define gui.interface_text_font = "fonts/Roboto-Medium.ttf"

define gui.text_size = 22
define gui.name_text_size = 26
define gui.interface_text_size = 20
define gui.label_text_size = 24
define gui.notify_text_size = 17
define gui.title_text_size = 46

## Backgrounds ----------------------------------------------------------------
define gui.main_menu_background = "images/cg/cg_title_meadow.png"
define gui.game_menu_background = "gui/game_menu.png"

## Dialogue Box Layout --------------------------------------------------------
define gui.textbox_height = 185
define gui.textbox_yalign = 1.0

define gui.name_xpos = 128
define gui.name_ypos = -14
define gui.name_xalign = 0.0
define gui.namebox_width = None
define gui.namebox_height = 40
define gui.namebox_borders = Borders(18, 6, 18, 6)
define gui.namebox_tile = False

define gui.dialogue_xpos = 132
define gui.dialogue_ypos = 40
define gui.dialogue_width = 1016
define gui.dialogue_text_xalign = 0.0

## Buttons --------------------------------------------------------------------
define gui.button_width = None
define gui.button_height = None
define gui.button_borders = Borders(6, 4, 6, 4)
define gui.button_tile = False
define gui.button_text_font = gui.interface_text_font
define gui.button_text_size = gui.interface_text_size
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color
define gui.button_text_xalign = 0.0

define gui.radio_button_borders = Borders(24, 4, 6, 4)
define gui.check_button_borders = Borders(24, 4, 6, 4)
define gui.confirm_button_text_xalign = 0.5
define gui.page_button_borders = Borders(12, 4, 12, 4)

define gui.quick_button_borders = Borders(10, 4, 10, 0)
define gui.quick_button_text_size = 14
define gui.quick_button_text_idle_color = '#9eb2c0'
define gui.quick_button_text_hover_color = '#ebb963'
define gui.quick_button_text_selected_color = '#7ec876'

## Choice Menu Buttons --------------------------------------------------------
define gui.choice_button_width = 820
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(42, 10, 32, 10)
define gui.choice_button_text_font = "fonts/Roboto-Medium.ttf"
define gui.choice_button_text_size = 20
define gui.choice_button_text_xalign = 0.0
define gui.choice_button_text_idle_color = '#e4ebf1'
define gui.choice_button_text_hover_color = '#ffdf9a'
define gui.choice_button_text_insensitive_color = '#6c7a86'

## File Save/Load Slots -------------------------------------------------------
define gui.slot_button_width = 276
define gui.slot_button_height = 206
define gui.slot_button_borders = Borders(12, 12, 12, 12)
define gui.slot_button_text_size = 14
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

define config.thumbnail_width = 252
define config.thumbnail_height = 142

define gui.file_slot_cols = 3
define gui.file_slot_rows = 2

## Positioning & Spacing ------------------------------------------------------
define gui.navigation_xpos = 42
define gui.skip_ypos = 12
define gui.notify_ypos = 52

define gui.choice_spacing = 12
define gui.navigation_spacing = 6
define gui.pref_spacing = 10
define gui.pref_button_spacing = 2
define gui.page_spacing = 4
define gui.slot_spacing = 12

define gui.main_menu_text_xalign = 0.0

## Frames ---------------------------------------------------------------------
define gui.frame_borders = Borders(12, 12, 12, 12)
define gui.confirm_frame_borders = Borders(36, 36, 36, 36)
define gui.skip_frame_borders = Borders(16, 6, 36, 6)
define gui.notify_frame_borders = Borders(18, 8, 36, 8)
define gui.frame_tile = False

## Bars, Scrollbars & Sliders -------------------------------------------------
define gui.bar_size = 25
define gui.scrollbar_size = 12
define gui.slider_size = 25
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

define gui.bar_borders = Borders(4, 4, 4, 4)
define gui.scrollbar_borders = Borders(4, 4, 4, 4)
define gui.slider_borders = Borders(4, 4, 4, 4)
define gui.vbar_borders = Borders(4, 4, 4, 4)
define gui.vscrollbar_borders = Borders(4, 4, 4, 4)
define gui.vslider_borders = Borders(4, 4, 4, 4)
define gui.unscrollable = "hide"

## Dialogue History -----------------------------------------------------------
define config.history_length = 250
define gui.history_height = None
define gui.history_spacing = 8
define gui.history_name_xpos = 155
define gui.history_name_ypos = 0
define gui.history_name_width = 155
define gui.history_name_xalign = 1.0
define gui.history_text_xpos = 175
define gui.history_text_ypos = 2
define gui.history_text_width = 710
define gui.history_text_xalign = 0.0

## NVL-Mode -------------------------------------------------------------------
define gui.nvl_borders = Borders(0, 10, 0, 20)
define gui.nvl_list_length = 6
define gui.nvl_height = 115
define gui.nvl_spacing = 10
define gui.nvl_name_xpos = 430
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 150
define gui.nvl_name_xalign = 1.0
define gui.nvl_text_xpos = 450
define gui.nvl_text_ypos = 8
define gui.nvl_text_width = 590
define gui.nvl_text_xalign = 0.0
define gui.nvl_thought_xpos = 240
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 780
define gui.nvl_thought_xalign = 0.0
define gui.nvl_button_xpos = 450
define gui.nvl_button_xalign = 0.0

define gui.language = "unicode"
