## ============================================================================
## options.rpy — Core Project Configuration
## WHERE THE GRASS STILL GROWS (An Unwanted Hero's Chronicle)
## ============================================================================

define config.name = _("Where the Grass Still Grows")
define gui.show_name = True
define config.version = "1.0.0"

define gui.about = _p("""
{b}Where the Grass Still Grows{/b} — {i}An Unwanted Hero's Chronicle{/i}

A psychological fantasy visual novel and narrative RPG about childhood scars, escapist dreams, a scarred world recovering from too many saviors, and the quiet courage it takes to live an ordinary human life.

Built with Ren'Py 8. Every choice shapes Leo's stats, relationships, reality tether, and which of the four endings you earn.
""")

define build.name = "touchsomegrass"

## Audio Channels & Mixers ----------------------------------------------------
define config.has_sound = True
define config.has_music = True
define config.has_voice = False

init -5 python:
    renpy.music.register_channel("ambience", mixer="sfx", loop=True, stop_on_mute=True, tight=True)

define config.main_menu_music = "audio/bgm/title_meadow_echo.ogg"
define config.sample_sound = "audio/sfx/ui_chime.ogg"

## Transitions ----------------------------------------------------------------
define config.enter_transition = Dissolve(0.22)
define config.exit_transition = Dissolve(0.22)
define config.intra_transition = Dissolve(0.18)
define config.after_load_transition = Dissolve(0.35)
define config.end_game_transition = Dissolve(0.6)

## Dialogue Window Management -------------------------------------------------
define config.window = "auto"
define config.window_show_transition = Dissolve(0.18)
define config.window_hide_transition = Dissolve(0.18)

## Default Player Preferences -------------------------------------------------
default preferences.text_cps = 48
default preferences.afm_time = 14
default preferences.music_volume = 0.72
default preferences.sfx_volume = 0.80

## Save Directory & Window Icon -----------------------------------------------
define config.save_directory = "touchsomegrass-1792835215"
define config.window_icon = "gui/window_icon.png"

## Build Packaging Rules ------------------------------------------------------
init python:
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.documentation('*.html')
    build.documentation('*.txt')
    build.documentation('docs/*.md')
