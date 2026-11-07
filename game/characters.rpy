## ============================================================================
## characters.rpy — Cast Definitions, Dynamic Nameplates & Stage Transforms
## ============================================================================

default leo_display_name = "Leo"
default current_chapter_title = "Prologue: Fluorescent Rain"
default current_location_name = "Eastside Laundromat"
default hud_visible = False

## Core Narrative Voices ------------------------------------------------------
define narrator = Character(None, what_color="#e8eef3", what_line_spacing=4)

define thought = Character(
    None,
    what_italic=True,
    what_color="#b8d4e8",
    what_prefix="(",
    what_suffix=")",
    what_line_spacing=4,
)

## Major Cast -----------------------------------------------------------------
define leo = Character(
    "[leo_display_name]",
    color="#ebb963",
    who_outlines=[(2, "#091017", 0, 0)],
    what_line_spacing=4,
)

define vespera = Character(
    "Vespera",
    color="#73d2de",
    who_outlines=[(2, "#091017", 0, 0)],
    what_line_spacing=4,
)

define bram = Character(
    "Bram",
    color="#f29559",
    who_outlines=[(2, "#091017", 0, 0)],
    what_line_spacing=4,
)

define sera = Character(
    "Seraphina",
    color="#c792ea",
    who_outlines=[(2, "#091017", 0, 0)],
    what_line_spacing=4,
)

define orin = Character(
    "Master Orin",
    color="#8fd687",
    who_outlines=[(2, "#091017", 0, 0)],
    what_line_spacing=4,
)

define cassian = Character(
    "Marshal Cassian",
    color="#d4dce6",
    who_outlines=[(2, "#091017", 0, 0)],
    what_line_spacing=4,
)

## Supporting World Voices ----------------------------------------------------
define unknown_voice = Character("???", color="#9fb1bf", who_outlines=[(2, "#091017", 0, 0)])
define clerk = Character("Clerk Fen", color="#d6c28f", who_outlines=[(2, "#091017", 0, 0)])
define marcus = Character("Marcus", color="#e06c75", who_outlines=[(2, "#091017", 0, 0)])
define baker = Character("Mistress Halda", color="#e5b181", who_outlines=[(2, "#091017", 0, 0)])
define remnant = Character("Hollow Remnant", color="#b892ff", what_color="#dcd0ff", who_outlines=[(2, "#091017", 0, 0)])
define kid = Character("Dropped-Bag Kid", color="#a3d9a5", who_outlines=[(2, "#091017", 0, 0)])

## Stage Transforms & Cinematics ----------------------------------------------
transform stage_left:
    xanchor 0.5 yanchor 1.0
    xpos 0.20 ypos 1.02
    easein 0.25 xpos 0.20 ypos 1.0

transform stage_midleft:
    xanchor 0.5 yanchor 1.0
    xpos 0.33 ypos 1.02
    easein 0.25 xpos 0.33 ypos 1.0

transform stage_center:
    xanchor 0.5 yanchor 1.0
    xpos 0.50 ypos 1.02
    easein 0.25 xpos 0.50 ypos 1.0

transform stage_midright:
    xanchor 0.5 yanchor 1.0
    xpos 0.67 ypos 1.02
    easein 0.25 xpos 0.67 ypos 1.0

transform stage_right:
    xanchor 0.5 yanchor 1.0
    xpos 0.80 ypos 1.02
    easein 0.25 xpos 0.80 ypos 1.0

transform hop:
    easein 0.10 yoffset -16
    easeout 0.12 yoffset 0

transform flinch:
    easein 0.06 xoffset -18 yoffset 6
    easeout 0.16 xoffset 0 yoffset 0

transform tremble:
    linear 0.04 xoffset -5
    linear 0.04 xoffset 5
    linear 0.04 xoffset -4
    linear 0.04 xoffset 4
    linear 0.04 xoffset 0

transform sink_sigh:
    ease 0.28 yoffset 14
    pause 0.15
    ease 0.30 yoffset 0

transform screen_shake:
    linear 0.04 xoffset -12 yoffset 6
    linear 0.04 xoffset 12 yoffset -6
    linear 0.04 xoffset -8 yoffset -4
    linear 0.04 xoffset 8 yoffset 4
    linear 0.04 xoffset 0 yoffset 0

transform slow_pan_zoom:
    subpixel True
    xalign 0.5 yalign 0.5
    zoom 1.0
    ease 12.0 zoom 1.05

## Named Transitions ----------------------------------------------------------
define flash_white = Fade(0.12, 0.08, 0.45, color="#ffffff")
define flash_astral = Fade(0.10, 0.10, 0.50, color="#73d2de")
define flash_crimson = Fade(0.08, 0.05, 0.35, color="#9e2a3b")
define flash_meadow = Fade(0.25, 0.15, 0.65, color="#cfead0")
define chapter_wipe = Fade(0.65, 0.45, 0.65, color="#080d12")
define eye_blink = Fade(0.25, 0.15, 0.40, color="#000000")
