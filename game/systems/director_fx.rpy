## ============================================================================
## systems/director_fx.rpy — Visual Kineticism, Psychological Overlays,
## Custom Text Tags ({shake}, {glitch}, {echo}) & Atmospheric Weather System
## Inspired by DDLC & Slay the Princess stage direction
## ============================================================================

default panic_intensity = 0
default active_whispers = []
default active_weather = None
default active_phantom_choice = None
default phantom_choice_dismissed = False
default crucible_temptation_count = 0

init -2 python:
    import random
    import math

    class KineticWordDisplayable(renpy.Displayable):
        """
        Renders a single word with real-time per-frame kinetic jitter ('shake')
        or memory-corruption chromatic flicker ('glitch').
        Word-level granularity allows Ren'Py to wrap long sentences naturally!
        """
        GLITCH_CHARS = "░▒▓█⊹╱╲"

        def __init__(self, word_text, mode="shake", **kwargs):
            super(KineticWordDisplayable, self).__init__(**kwargs)
            self.word_text = word_text
            self.mode = mode
            self.seed = sum(ord(c) * (i + 1) for i, c in enumerate(word_text))

            if mode == "glitch":
                self.base_text = Text(word_text, color="#dcd0ff")
                self.cyan_ghost = Text(word_text, color="#73d2deaa")
                self.red_ghost = Text(word_text, color="#e06c75aa")
            elif mode == "echo":
                self.base_text = Text(word_text, color="#e57388", italic=True)
                self.cyan_ghost = None
                self.red_ghost = Text(word_text, color="#4a121f88", italic=True)
            else:
                self.base_text = Text(word_text)
                self.cyan_ghost = None
                self.red_ghost = None

        def render(self, width, height, st, at):
            base_render = renpy.render(self.base_text, width, height, st, at)
            w, h = base_render.get_size()
            rv = renpy.Render(w + 6, h + 4)

            # Deterministic pseudo-random phase from st + word seed
            phase = st * 28.0 + self.seed

            if self.mode == "shake":
                dx = int(math.sin(phase * 1.7) * 2.2 + math.cos(phase * 2.9) * 1.2)
                dy = int(math.cos(phase * 2.3) * 1.8)
                rv.blit(base_render, (3 + dx, 2 + dy))
                renpy.redraw(self, 0.04)

            elif self.mode == "glitch":
                tick = int(st * 16.0 + self.seed) % 19
                if tick in (0, 1, 7):
                    gx = int(math.sin(phase * 3.1) * 4.0)
                    gy = int(math.cos(phase * 2.0) * 2.0)
                    if self.cyan_ghost is not None:
                        c_ren = renpy.render(self.cyan_ghost, width, height, st, at)
                        rv.blit(c_ren, (3 - gx, 2))
                    if self.red_ghost is not None:
                        r_ren = renpy.render(self.red_ghost, width, height, st, at)
                        rv.blit(r_ren, (3 + gx, 2 + gy))
                    rv.blit(base_render, (3 + (gx // 2), 2))
                else:
                    rv.blit(base_render, (3, 2))
                renpy.redraw(self, 0.05)

            elif self.mode == "echo":
                dx = int(math.sin(phase * 0.9) * 1.5)
                dy = int(math.cos(phase * 1.1) * 1.5)
                if self.red_ghost is not None:
                    r_ren = renpy.render(self.red_ghost, width, height, st, at)
                    rv.blit(r_ren, (4 - dx, 3 - dy))
                rv.blit(base_render, (3 + dx, 2 + dy))
                renpy.redraw(self, 0.05)

            return rv

        def visit(self):
            nodes = [self.base_text]
            if self.cyan_ghost:
                nodes.append(self.cyan_ghost)
            if self.red_ghost:
                nodes.append(self.red_ghost)
            return nodes

    def _make_kinetic_tag(mode):
        def _tag_fn(tag, argument, contents):
            rv = []
            for kind, text in contents:
                if kind == renpy.TEXT_TEXT:
                    tokens = text.split(" ")
                    for idx, tok in enumerate(tokens):
                        if tok:
                            rv.append((renpy.TEXT_DISPLAYABLE, KineticWordDisplayable(tok, mode=mode)))
                        if idx < len(tokens) - 1:
                            rv.append((renpy.TEXT_TEXT, " "))
                else:
                    rv.append((kind, text))
            return rv
        return _tag_fn

    config.custom_text_tags["shake"] = _make_kinetic_tag("shake")
    config.custom_text_tags["glitch"] = _make_kinetic_tag("glitch")
    config.custom_text_tags["echo"] = _make_kinetic_tag("echo")

init python:
    def set_panic(level=1, whispers=None, sfx=None):
        """
        Activates the psychological tunnel-vision vignette & floating intrusive whispers.
        level 0: clear
        level 1: mild anxiety vignette
        level 2: acute panic pulse + floating intrusive thoughts
        level 3: Resonance memory-burn static & heavy distortion
        """
        store.panic_intensity = max(0, min(3, int(level)))
        if whispers is not None:
            store.active_whispers = list(whispers)
        elif level == 0:
            store.active_whispers = []

        if sfx == "tinnitus":
            renpy.sound.play(audio.sfx_tinnitus)
        elif sfx == "static":
            renpy.sound.play(audio.sfx_static)
        elif sfx == "heartbeat":
            renpy.sound.play(audio.sfx_heartbeat)
        elif sfx == "subdrop":
            renpy.sound.play(audio.sfx_subdrop)

    def clear_panic():
        store.panic_intensity = 0
        store.active_whispers = []

    def set_atmosphere(weather_name=None):
        """
        Sets continuous stage particle overlay:
        'rain', 'salt_ash', 'meadow_spores', 'crucible_sparks', or None.
        """
        store.active_weather = weather_name

    def set_phantom_choice(caption_text):
        """
        Queues a DDLC / Slay-the-Princess style intrusive phantom choice
        at the top of the next menu.
        """
        store.active_phantom_choice = caption_text
        store.phantom_choice_dismissed = False

    def dismiss_phantom_choice():
        store.phantom_choice_dismissed = True
        renpy.sound.play(audio.sfx_static)

    if "atmosphere_fx_screen" not in config.overlay_screens:
        config.overlay_screens.append("atmosphere_fx_screen")
    if "psychological_overlay_screen" not in config.overlay_screens:
        config.overlay_screens.append("psychological_overlay_screen")


## ============================================================================
## CAMERA & CINEMATIC STAGE TRANSFORMS
## ============================================================================
transform cam_reset:
    subpixel True
    align (0.5, 0.5)
    rotate_pad False
    ease 0.55 zoom 1.0 xoffset 0 yoffset 0 rotate 0

transform cam_push_in:
    subpixel True
    align (0.5, 0.5)
    rotate_pad False
    easein 0.65 zoom 1.12 xoffset 0 yoffset -10 rotate 0

transform cam_closeup:
    subpixel True
    align (0.5, 0.5)
    rotate_pad False
    easein 0.45 zoom 1.20 xoffset 0 yoffset -14 rotate 0

transform cam_focus_left:
    subpixel True
    align (0.5, 0.5)
    rotate_pad False
    easein 0.55 zoom 1.12 xoffset 48 yoffset -8 rotate 0

transform cam_focus_right:
    subpixel True
    align (0.5, 0.5)
    rotate_pad False
    easein 0.55 zoom 1.12 xoffset -48 yoffset -8 rotate 0

transform cam_dutch_unease:
    subpixel True
    align (0.5, 0.5)
    rotate_pad False
    easein 0.60 zoom 1.08 xoffset 0 yoffset 0 rotate -1.4

transform cam_dutch_panic:
    subpixel True
    align (0.5, 0.5)
    rotate_pad False
    easein 0.35 zoom 1.14 xoffset 0 yoffset 0 rotate 1.6

transform cam_heartbeat_zoom:
    subpixel True
    align (0.5, 0.5)
    rotate_pad False
    block:
        easein 0.16 zoom 1.09 yoffset -6
        easeout 0.24 zoom 1.05 yoffset -2
        easein 0.14 zoom 1.07 yoffset -4
        easeout 0.55 zoom 1.03 yoffset 0
        pause 0.55
        repeat

transform cam_heavy_quake:
    subpixel True
    align (0.5, 0.5)
    rotate_pad False
    zoom 1.05
    linear 0.04 xoffset -14 yoffset 8
    linear 0.04 xoffset 14 yoffset -8
    linear 0.04 xoffset -10 yoffset -6
    linear 0.04 xoffset 10 yoffset 6
    linear 0.04 xoffset -6 yoffset 3
    linear 0.05 xoffset 0 yoffset 0

transform sprite_shiver_loop:
    block:
        linear 0.05 xoffset -3
        linear 0.05 xoffset 3
        linear 0.05 xoffset -2
        linear 0.05 xoffset 2
        linear 0.05 xoffset 0
        pause 0.15
        repeat

transform sprite_glitch_jolt:
    linear 0.03 xoffset -14 alpha 0.75
    linear 0.03 xoffset 14 alpha 0.95
    linear 0.03 xoffset -6 alpha 0.85
    linear 0.03 xoffset 0 alpha 1.0

transform sprite_step_closer:
    easein 0.30 zoom 1.06 yoffset 8

transform sprite_step_back:
    easeout 0.30 zoom 0.96 yoffset 0


## ============================================================================
## ATMOSPHERIC PARTICLE & WEATHER TRANSFORMS
## ============================================================================
transform rain_drop_fall(start_x, delay_t, speed_t):
    subpixel True
    xpos start_x ypos -90 alpha 0.0 rotate 12
    pause delay_t
    block:
        xpos start_x ypos -90 alpha 0.55
        linear speed_t xpos (start_x - 110) ypos 760 alpha 0.20
        repeat

transform salt_mote_drift(start_x, start_y, delay_t, speed_t):
    subpixel True
    xpos start_x ypos start_y alpha 0.0
    pause delay_t
    block:
        xpos start_x ypos start_y alpha 0.0
        linear (speed_t * 0.25) xpos (start_x - 60) ypos (start_y - 12) alpha 0.65
        linear (speed_t * 0.50) xpos (start_x - 190) ypos (start_y + 10) alpha 0.55
        linear (speed_t * 0.25) xpos (start_x - 280) ypos (start_y - 6) alpha 0.0
        repeat

transform spore_rise(start_x, start_y, delay_t, speed_t):
    subpixel True
    xpos start_x ypos start_y alpha 0.0
    pause delay_t
    block:
        xpos start_x ypos start_y alpha 0.0
        easein (speed_t * 0.35) xpos (start_x + 18) ypos (start_y - 45) alpha 0.70
        easeout (speed_t * 0.65) xpos (start_x - 14) ypos (start_y - 130) alpha 0.0
        repeat

transform spark_ascend(start_x, delay_t, speed_t):
    subpixel True
    xpos start_x ypos 740 alpha 0.0
    pause delay_t
    block:
        xpos start_x ypos 740 alpha 0.85
        linear (speed_t * 0.5) xpos (start_x + 35) ypos 360 alpha 0.65
        linear (speed_t * 0.5) xpos (start_x - 25) ypos -40 alpha 0.0
        repeat


## ============================================================================
## SCREEN: ATMOSPHERE & WEATHER PARTICLES
## ============================================================================
screen atmosphere_fx_screen():
    zorder 12

    if not main_menu and not is_any_menu_open() and active_weather:
        if active_weather == "rain":
            add Solid("#09131d22")
            for idx, rx in enumerate((80, 175, 290, 380, 495, 610, 720, 835, 940, 1050, 1160, 1240, 130, 440, 770, 1090)):
                add Solid("#a8c8e640") xsize 2 ysize 64 at rain_drop_fall(rx, (idx % 7) * 0.14, 0.55 + (idx % 4) * 0.08)

        elif active_weather == "salt_ash":
            add Solid("#d8e2eb0c")
            for idx, (sx, sy) in enumerate(((1180, 110), (1050, 240), (1220, 390), (920, 160), (840, 470), (1120, 520), (680, 290), (540, 130), (990, 340), (760, 430), (1250, 210), (620, 510))):
                text "•" size (12 + (idx % 3) * 4) color "#e8eef355" at salt_mote_drift(sx, sy, (idx % 6) * 0.45, 4.2 + (idx % 4) * 0.6)

        elif active_weather == "meadow_spores":
            add Solid("#7ec8760a")
            for idx, (mx, my) in enumerate(((160, 560), (290, 480), (430, 590), (580, 510), (730, 550), (880, 470), (1040, 580), (1150, 490), (350, 390), (660, 410), (950, 380))):
                text "✦" font "fonts/DejaVuSans.ttf" size (11 + (idx % 3) * 3) color "#d4f2b860" at spore_rise(mx, my, (idx % 5) * 0.55, 4.8 + (idx % 3) * 0.8)

        elif active_weather == "crucible_sparks":
            add Solid("#2411361c")
            for idx, cx in enumerate((95, 210, 330, 450, 570, 690, 810, 930, 1050, 1170, 150, 510, 870, 1110)):
                text "❖" font "fonts/DejaVuSans.ttf" size (10 + (idx % 3) * 3) color ("#ebb96380" if idx % 2 == 0 else "#c792ea80") at spark_ascend(cx, (idx % 7) * 0.25, 1.9 + (idx % 4) * 0.35)


## ============================================================================
## SCREEN: PSYCHOLOGICAL TUNNEL VISION & INTRUSIVE WHISPERS
## ============================================================================
transform panic_vignette_pulse(base_alpha, peak_alpha):
    alpha base_alpha
    block:
        easein 0.22 alpha peak_alpha
        easeout 0.35 alpha base_alpha
        easein 0.18 alpha (peak_alpha * 0.85)
        easeout 0.65 alpha base_alpha
        repeat

transform whisper_float(wx, wy, delay_t):
    subpixel True
    xpos wx ypos wy xanchor 0.5 yanchor 0.5 alpha 0.55
    pause (delay_t * 0.2)
    block:
        easein 0.55 alpha 0.88 xoffset -4 yoffset -3
        linear 0.06 xoffset 4 yoffset 2
        linear 0.06 xoffset -3 yoffset -2
        easeout 0.90 alpha 0.35 xoffset 0 yoffset 0
        pause 0.20
        repeat

transform static_bar_flicker(by, delay_t):
    xpos 0 ypos by alpha 0.36
    pause (delay_t * 0.15)
    block:
        linear 0.06 ypos (by + 16) alpha 0.45
        linear 0.06 ypos (by - 8) alpha 0.18
        pause 0.35
        alpha 0.32
        pause 0.45
        repeat

screen psychological_overlay_screen():
    zorder 22

    if not main_menu and not is_any_menu_open() and panic_intensity > 0:
        # Top, Bottom, Left, Right dark claustrophobic tunnel-vision borders
        $ border_col = "#1a070fe6" if panic_intensity == 2 else ("#1d0e2ee6" if panic_intensity == 3 else "#060b10d8")
        $ inner_col = "#1a070f77" if panic_intensity == 2 else ("#1d0e2e77" if panic_intensity == 3 else "#060b1055")
        $ p_base = 0.35 if panic_intensity == 1 else (0.58 if panic_intensity == 2 else 0.72)
        $ p_peak = 0.55 if panic_intensity == 1 else (0.88 if panic_intensity == 2 else 0.96)

        fixed at panic_vignette_pulse(p_base, p_peak):
            add Solid(border_col) xsize 1280 ysize 46 xpos 0 ypos 0
            add Solid(inner_col) xsize 1280 ysize 38 xpos 0 ypos 46
            add Solid(border_col) xsize 1280 ysize 54 xpos 0 ypos 666
            add Solid(inner_col) xsize 1280 ysize 36 xpos 0 ypos 630
            add Solid(border_col) xsize 64 ysize 720 xpos 0 ypos 0
            add Solid(inner_col) xsize 48 ysize 720 xpos 64 ypos 0
            add Solid(border_col) xsize 64 ysize 720 xpos 1216 ypos 0
            add Solid(inner_col) xsize 48 ysize 720 xpos 1168 ypos 0

        # Level 3 Resonance Memory-Erase Glitch Scanlines
        if panic_intensity >= 3:
            add Solid("#c792ea44") xsize 1280 ysize 3 at static_bar_flicker(140, 0.1)
            add Solid("#73d2de44") xsize 1280 ysize 2 at static_bar_flicker(310, 0.7)
            add Solid("#ffffff38") xsize 1280 ysize 4 at static_bar_flicker(460, 1.3)

        # Floating Intrusive Whispers around the periphery of vision
        if active_whispers:
            $ whisper_coords = ((230, 118), (1040, 132), (210, 445), (1055, 430), (640, 96))
            for idx, w_text in enumerate(active_whispers[:5]):
                $ wx, wy = whisper_coords[idx % len(whisper_coords)]
                text tr(w_text) substitute False at whisper_float(wx, wy, idx * 0.42):
                    font "fonts/LiberationSerif-Italic.ttf"
                    size 19
                    color ("#e57388" if panic_intensity == 2 else "#d6b8ff")
                    outlines [(2, "#05080c", 0, 0)]
