## ============================================================================
## systems/minigames.rpy — Interactive Gameplay Systems
## 1) Astrolabe Harmonic Tuning (Real-time / Precision Grounding Seal Puzzle)
## 2) Tactical Stance Encounter (Turn-based Narrative-Tactical Combat)
## ============================================================================

## ----------------------------------------------------------------------------
## MINI-GAME 1: ASTROLABE HARMONIC TUNING
## ----------------------------------------------------------------------------
default astro_ring_index = 0
default astro_cursor = 15
default astro_dir = 1
default astro_stability = 100
default astro_misfires = 0
default astro_log = "Align the brass harmonic needle inside the emerald Grounding Band and lock all 3 rings!"

init python:
    def init_astrolabe_game():
        store.astro_ring_index = 0
        store.astro_cursor = 12
        store.astro_dir = 1
        store.astro_stability = 100
        store.astro_misfires = 0
        int_bonus = get_stat("intelligence")
        store.astro_log = tr("Intelligence ([int_bonus]) widens your Grounding Band. Press LOCK HARMONIC (or SPACE) inside the green zone!").replace("[int_bonus]", str(int_bonus))

    def astro_zone_bounds(ring_idx):
        # Higher Intelligence widens the target sweet spot!
        half_width = min(20, 9 + get_stat("intelligence") * 2 - ring_idx * 2)
        centers = [50, 62, 42]
        c = centers[min(2, ring_idx)]
        return max(10, c - half_width), min(90, c + half_width)

    def astro_step_tick():
        speeds = [4, 6, 7]
        spd = speeds[min(2, store.astro_ring_index)]
        nxt = store.astro_cursor + store.astro_dir * spd
        if nxt >= 98:
            nxt = 98
            store.astro_dir = -1
        elif nxt <= 2:
            nxt = 2
            store.astro_dir = 1
        store.astro_cursor = nxt

    def astro_attempt_lock():
        lo, hi = astro_zone_bounds(store.astro_ring_index)
        pos = store.astro_cursor
        if lo <= pos <= hi:
            renpy.sound.play("audio/sfx/astrolabe_lock.ogg")
            store.astro_ring_index += 1
            if store.astro_ring_index >= 3:
                return "perfect" if store.astro_misfires == 0 else "stabilized"
            store.astro_log = tr("Ring [ring]/3 grounded! Tune the next harmonic band!").replace("[ring]", str(store.astro_ring_index))
            return None
        else:
            renpy.sound.play("audio/sfx/rift_tear.ogg")
            store.astro_misfires += 1
            store.astro_stability = max(0, store.astro_stability - 25)
            if store.astro_stability <= 0:
                return "overload"
            store.astro_log = tr("Harmonic backlash! (-25% Seal Stability). Steady your breathing and strike the emerald band!")
            return None


screen astrolabe_minigame(crisis_title="Resonance Leak: Old Aqueduct Seam"):
    modal True
    zorder 55

    timer 0.06 repeat True action Function(astro_step_tick)
    key "K_SPACE" action [
        SetLocalVariable("_res", None),
        If(
            astro_zone_bounds(astro_ring_index)[0] <= astro_cursor <= astro_zone_bounds(astro_ring_index)[1] and astro_ring_index == 2,
            true=[Play("sound", "audio/sfx/astrolabe_lock.ogg"), Return("perfect" if astro_misfires == 0 else "stabilized")],
            false=Function(astro_attempt_lock),
        ),
    ]

    add Solid("#060c12dc")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 920
        ysize 500
        background Frame("images/ui/panel_frame.png", 16, 16)
        padding (36, 28)

        vbox:
            spacing 16
            xfill True

            hbox:
                xfill True
                vbox:
                    text tr(crisis_title) font "fonts/LiberationSerif-Bold.ttf" size 28 color "#73d2de"
                    text _("Rootwarden Grounding Calibration • Rings Locked: [astro_ring_index] / 3") size 16 color "#b4c5d2"

                vbox:
                    xalign 1.0
                    text _("Seal Stability: [astro_stability]%") font "fonts/Roboto-Bold.ttf" size 18 color ("#7ec876" if astro_stability >= 50 else "#e06c75") xalign 1.0
                    bar value astro_stability range 100 xsize 210 ysize 16 xalign 1.0

            add Solid("#27414d") xsize 848 ysize 2

            # Ring progress badges
            hbox:
                xalign 0.5
                spacing 28
                for idx in range(3):
                    $ r_done = idx < astro_ring_index
                    $ r_curr = idx == astro_ring_index
                    frame:
                        xsize 230
                        ysize 62
                        background Solid("#1d3b32" if r_done else ("#1a2f3d" if r_curr else "#101a22"))
                        padding (12, 8)
                        vbox:
                            xalign 0.5
                            yalign 0.5
                            text _("Harmonic Ring [idx + 1]") size 15 font "fonts/Roboto-Bold.ttf" color ("#7ec876" if r_done else ("#ebb963" if r_curr else "#6f808c")) xalign 0.5
                            text (_("{font=fonts/DejaVuSans.ttf}✓{/font} GROUNDED") if r_done else (_("ACTIVE TARGET") if r_curr else _("LOCKED"))) size 13 color ("#a7e8a1" if r_done else "#b8c7d4") xalign 0.5

            # Interactive Gauge Track (800px wide)
            $ lo_b, hi_b = astro_zone_bounds(astro_ring_index)
            $ track_w = 800
            $ zone_x = int(track_w * (lo_b / 100.0))
            $ zone_w = max(24, int(track_w * ((hi_b - lo_b) / 100.0)))
            $ needle_x = int(track_w * (astro_cursor / 100.0))

            frame:
                xalign 0.5
                xsize 824
                ysize 92
                background Solid("#0b131a")
                padding (12, 16)

                fixed:
                    xsize 800
                    ysize 60

                    # Base brass rail
                    add Solid("#223442") xsize 800 ysize 22 ypos 19

                    # Target Emerald Grounding Zone
                    add Solid("#3d8c52") xsize zone_w ysize 38 xpos zone_x ypos 11
                    add Solid("#7ec876") xsize zone_w ysize 6 xpos zone_x ypos 11

                    # Moving Harmonic Needle
                    add Solid("#ffdf85") xsize 8 ysize 56 xpos max(0, min(792, needle_x - 4)) ypos 2

            text "[astro_log!q]" size 17 color "#dce6ee" xalign 0.5 text_align 0.5

            # Action Controls
            hbox:
                xalign 0.5
                spacing 24
                yoffset 4

                button:
                    xsize 310
                    ysize 54
                    background Solid("#295443")
                    hover_background Solid("#39735c")
                    action If(
                        lo_b <= astro_cursor <= hi_b and astro_ring_index >= 2,
                        true=[Play("sound", "audio/sfx/astrolabe_lock.ogg"), Return("perfect" if astro_misfires == 0 else "stabilized")],
                        false=If(
                            not (lo_b <= astro_cursor <= hi_b) and astro_stability <= 25,
                            true=[Play("sound", "audio/sfx/rift_tear.ogg"), Return("overload")],
                            false=Function(astro_attempt_lock),
                        ),
                    )
                    text _("{font=fonts/DejaVuSans.ttf}⚡{/font} GROUND HARMONIC RING") font "fonts/Roboto-Bold.ttf" size 19 color "#ffdf9a" xalign 0.5 yalign 0.5

                if has_stat("empathy", 5) or has_item("grounding_spade"):
                    button:
                        xsize 270
                        ysize 54
                        background Solid("#1d3342")
                        hover_background Solid("#2b4b61")
                        action [Play("sound", "audio/sfx/astrolabe_lock.ogg"), Return("stabilized")]
                        text _("Steady Spade Anchor (Auto-Seal)") size 15 color "#73d2de" xalign 0.5 yalign 0.5


## ----------------------------------------------------------------------------
## MINI-GAME 2: TACTICAL STANCE ENCOUNTER
## ----------------------------------------------------------------------------
default duel_enemy_name = "Hollow Remnant"
default duel_enemy_hp = 120
default duel_enemy_max_hp = 120
default duel_enemy_composure = 0
default duel_enemy_max_composure = 100
default duel_turn = 1
default duel_intent = "charging"
default duel_intent_desc = "Gathering calcified salt-spears for a heavy sweep!"
default duel_guarding = False
default duel_analyzed = False
default duel_log = "The calcified figure raises a forgotten hero's broken halberd. Choose your stance!"

init python:
    DUEL_INTENTS = [
        ("charging", "Telegraph: Gathering calcified salt-spears for a crushing sweep! (Guard & Ground strongly counters)"),
        ("weeping", "Telegraph: Crystalline visor trembles, echoing a forgotten lullaby... (Reach Out / Empathy resonates!)"),
        ("warded", "Telegraph: Braced behind a mirrored Resonance barrier! (Analyze Seam or Copper Spade Strike pierces)"),
    ]

    def init_tactical_duel(enemy_name="Hollow Remnant of the Fourth Dawn", enemy_hp=120):
        store.duel_enemy_name = enemy_name
        store.duel_enemy_hp = enemy_hp
        store.duel_enemy_max_hp = enemy_hp
        store.duel_enemy_composure = 0
        store.duel_enemy_max_composure = 100
        store.duel_turn = 1
        store.duel_guarding = False
        store.duel_analyzed = False
        store.leo_hp = max(65, store.leo_hp)
        store.leo_focus = max(40, store.leo_focus)
        store.duel_intent, store.duel_intent_desc = DUEL_INTENTS[0]
        store.duel_log = tr("[enemy] blocks the Archive archway! Defeat it by depleting HP OR filling its Memory Peace (100%)!").replace("[enemy]", tr(enemy_name))

    def duel_advance_enemy_turn(action_summary):
        # Check win conditions immediately
        if store.duel_enemy_composure >= 100:
            return "pacified"
        if store.duel_enemy_hp <= 0:
            return "vanquished"

        # Enemy acts based on current intent
        if store.duel_intent == "charging":
            raw_dmg = 24
            if store.duel_guarding:
                dmg = 5
                counter = 18 + (8 if has_item("grounding_spade") else 0)
                store.duel_enemy_hp = max(0, store.duel_enemy_hp - counter)
                store.duel_enemy_composure = min(100, store.duel_enemy_composure + 15)
                enemy_msg = tr("Your Grounding stance channels its salt-sweep into bedrock (-[dmg] HP, -[counter] Enemy HP, +15% Peace)!").replace("[dmg]", str(dmg)).replace("[counter]", str(counter))
            else:
                dmg = raw_dmg
                enemy_msg = tr("The salt-spear sweep clips your shoulder (-[dmg] HP)!").replace("[dmg]", str(dmg))
            store.leo_hp = max(0, store.leo_hp - dmg)
        elif store.duel_intent == "weeping":
            dmg = 8 if store.duel_guarding else 14
            store.leo_hp = max(0, store.leo_hp - dmg)
            enemy_msg = tr("Waves of hollow static ache behind your eyes (-[dmg] HP).").replace("[dmg]", str(dmg))
        else:
            dmg = 6 if store.duel_guarding else 15
            store.leo_hp = max(0, store.leo_hp - dmg)
            enemy_msg = tr("Reflected shards graze the Vanguard shieldline (-[dmg] HP).").replace("[dmg]", str(dmg))

        store.duel_guarding = False

        if store.duel_enemy_composure >= 100:
            return "pacified"
        if store.duel_enemy_hp <= 0:
            return "vanquished"
        if store.leo_hp <= 0:
            # Bram's shield intervenes at 1 HP once, or triggers gritty survival
            store.leo_hp = 25
            store.duel_log = action_summary + " " + tr("Bram slams his tower shield in front of you at the last second! ('Eyes up, Leo!')")
        else:
            store.duel_log = f"{action_summary}  •  {enemy_msg}"

        store.duel_turn += 1
        nxt = DUEL_INTENTS[(store.duel_turn - 1) % len(DUEL_INTENTS)]
        store.duel_intent, store.duel_intent_desc = nxt
        return None

    def duel_player_move(move_id):
        bonus_mult = 1.5 if store.duel_analyzed else 1.0
        store.duel_analyzed = False

        if move_id == "strike":
            renpy.sound.play("audio/sfx/spade_clash.ogg")
            base = 22 + get_stat("strength") * 4 + (8 if has_item("grounding_spade") else 0)
            if store.duel_intent == "warded":
                base += 10
            dmg = int(base * bonus_mult)
            store.duel_enemy_hp = max(0, store.duel_enemy_hp - dmg)
            return duel_advance_enemy_turn(tr("You drive your copper-veined spade into the fissure for [dmg] damage!").replace("[dmg]", str(dmg)))

        elif move_id == "guard":
            renpy.sound.play("audio/sfx/astrolabe_lock.ogg")
            store.duel_guarding = True
            store.leo_focus = min(store.leo_max_focus, store.leo_focus + 15)
            store.leo_hp = min(store.leo_max_hp, store.leo_hp + 8)
            return duel_advance_enemy_turn(tr("You plant your boots alongside Bram, grounding the stone (+8 HP, +15 Focus, Braced)!"))

        elif move_id == "analyze":
            renpy.sound.play("audio/sfx/ui_chime.ogg")
            store.duel_analyzed = True
            peace_gain = 12 + get_stat("intelligence") * 3
            store.duel_enemy_composure = min(100, store.duel_enemy_composure + peace_gain)
            store.duel_guarding = True
            return duel_advance_enemy_turn(tr("You read the inscription on its breastplate (+[gain]% Peace, Braced, Next Move 1.5x)!").replace("[gain]", str(peace_gain)))

        elif move_id == "empathize":
            renpy.sound.play("audio/sfx/meadow_breath.ogg")
            store.leo_focus = max(0, store.leo_focus - 10)
            gain = 24 + get_stat("empathy") * 4 + get_stat("courage") * 2
            if store.duel_intent == "weeping":
                gain += 18
            gain = int(gain * bonus_mult)
            store.duel_enemy_composure = min(100, store.duel_enemy_composure + gain)
            return duel_advance_enemy_turn(tr("You speak to the person trapped inside the salt-armor (+[gain]% Memory Peace)!").replace("[gain]", str(gain)))

        elif move_id == "resonance":
            renpy.sound.play("audio/sfx/rift_tear.ogg")
            change_tether(-8, "Burned personal memory to unleash Astral Resonance!", silent=True)
            change_resonance(12, silent=True)
            dmg = 52
            store.duel_enemy_hp = max(0, store.duel_enemy_hp - dmg)
            return duel_advance_enemy_turn(tr("Violet Astral light erupts from your palm for [dmg] damage—at the cost of -8% Reality Tether!").replace("[dmg]", str(dmg)))

        elif move_id == "stew":
            use_satchel_item("iron_stew")
            store.duel_guarding = True
            return duel_advance_enemy_turn(tr("You wolf down Bram's hot garlic ration behind cover (+35 HP, +20 Focus)!"))

        return None


screen tactical_duel():
    modal True
    zorder 55

    add Solid("#060b11d8")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1080
        ysize 580
        background Frame("images/ui/panel_frame.png", 16, 16)
        padding (30, 24)

        vbox:
            spacing 14
            xfill True

            # Top Combatant Bars
            hbox:
                xfill True
                spacing 30

                # Enemy Status Panel
                frame:
                    xsize 500
                    ysize 122
                    background Solid("#171f2b")
                    padding (16, 12)
                    vbox:
                        spacing 6
                        hbox:
                            xfill True
                            text "[duel_enemy_name!t]" font "fonts/LiberationSerif-Bold.ttf" size 20 color "#c792ea"
                            text _("Turn [duel_turn]") size 14 color "#9eb2c0" xalign 1.0 yalign 0.5
                        hbox:
                            spacing 10
                            text _("Armor Integrity:") size 14 color "#e06c75" xsize 125
                            bar value duel_enemy_hp range duel_enemy_max_hp xsize 260 ysize 16 yalign 0.5
                            text "[duel_enemy_hp]/[duel_enemy_max_hp]" size 14 color "#eaeef2"
                        hbox:
                            spacing 10
                            text _("Memory Peace:") size 14 color "#7ec876" xsize 125
                            bar value duel_enemy_composure range duel_enemy_max_composure xsize 260 ysize 16 yalign 0.5
                            text "[duel_enemy_composure]%" size 14 color "#a7e8a1"

                # Leo Status Panel
                frame:
                    xsize 490
                    ysize 122
                    background Solid("#13252c")
                    padding (16, 12)
                    vbox:
                        spacing 6
                        hbox:
                            xfill True
                            text _("Leo & Vanguard Line") font "fonts/LiberationSerif-Bold.ttf" size 20 color "#ebb963"
                            text _("Tether: [tether]%") size 14 color "#7ec876" xalign 1.0 yalign 0.5
                        hbox:
                            spacing 10
                            text _("Vitality (HP):") size 14 color "#7ec876" xsize 115
                            bar value leo_hp range leo_max_hp xsize 260 ysize 16 yalign 0.5
                            text "[leo_hp]/[leo_max_hp]" size 14 color "#eaeef2"
                        hbox:
                            spacing 10
                            text _("Breath Focus:") size 14 color "#73d2de" xsize 115
                            bar value leo_focus range leo_max_focus xsize 260 ysize 16 yalign 0.5
                            text "[leo_focus]/[leo_max_focus]" size 14 color "#b8e3ea"

            # Enemy Telegraph Banner
            frame:
                xfill True
                background Solid("#221b30")
                padding (16, 10)
                text "{font=fonts/DejaVuSans.ttf}⚠{/font}  [duel_intent_desc!tq]" size 16 font "fonts/Roboto-Medium.ttf" color "#e5c9ff"

            # Narrative Combat Log
            frame:
                xfill True
                ysize 84
                background Solid("#0c151d")
                padding (16, 12)
                text "[duel_log!q]" size 17 color "#e8eef3" yalign 0.5

            # Stance Action Grid (2x3)
            vpgrid:
                cols 2
                spacing 12
                xfill True

                # 1. Copper Spade Strike
                button:
                    xsize 504
                    ysize 72
                    background Solid("#1d2f3a")
                    hover_background Solid("#2c4a59")
                    padding (16, 10)
                    action [
                        If(
                            duel_enemy_hp <= int((22 + get_stat("strength") * 4 + (8 if has_item("grounding_spade") else 0) + (10 if duel_intent == "warded" else 0)) * (1.5 if duel_analyzed else 1.0)),
                            true=[Play("sound", "audio/sfx/spade_clash.ogg"), Return("vanquished")],
                            false=Function(duel_player_move, "strike"),
                        )
                    ]
                    vbox:
                        text _("{font=fonts/DejaVuSans.ttf}⚔{/font}  Grounding Spade Strike  (STR [leo_stats['strength']])") font "fonts/Roboto-Bold.ttf" size 17 color "#ebb963"
                        text _("Shatters calcified armor; extra damage vs Warded barriers.") size 14 color "#b4c5d2"

                # 2. Brace & Ground
                button:
                    xsize 504
                    ysize 72
                    background Solid("#1a352e")
                    hover_background Solid("#285247")
                    padding (16, 10)
                    action [
                        If(
                            duel_intent == "charging" and duel_enemy_composure + 15 >= 100,
                            true=[Play("sound", "audio/sfx/astrolabe_lock.ogg"), Return("pacified")],
                            false=If(
                                duel_intent == "charging" and duel_enemy_hp <= (18 + (8 if has_item("grounding_spade") else 0)),
                                true=[Play("sound", "audio/sfx/astrolabe_lock.ogg"), Return("vanquished")],
                                false=Function(duel_player_move, "guard"),
                            ),
                        )
                    ]
                    vbox:
                        text _("{font=fonts/DejaVuSans.ttf}◈{/font}  Brace & Conduct Into Bedrock") font "fonts/Roboto-Bold.ttf" size 17 color "#7ec876"
                        text _("Heavily reduces damage, restores +8 HP/+15 Focus, and reflects sweeps!") size 14 color "#b4c5d2"

                # 3. Analyze Seam
                button:
                    xsize 504
                    ysize 72
                    background Solid("#192c3b")
                    hover_background Solid("#25455c")
                    padding (16, 10)
                    action [
                        If(
                            duel_enemy_composure + 12 + get_stat("intelligence") * 3 >= 100,
                            true=[Play("sound", "audio/sfx/ui_chime.ogg"), Return("pacified")],
                            false=Function(duel_player_move, "analyze"),
                        )
                    ]
                    vbox:
                        text _("{font=fonts/DejaVuSans.ttf}❖{/font}  Read Crest & Harmonic Seam  (INT [leo_stats['intelligence']])") font "fonts/Roboto-Bold.ttf" size 17 color "#73d2de"
                        text _("Guards lightly, adds Peace, and empowers your next action by 1.5x!") size 14 color "#b4c5d2"

                # 4. Reach Through (Mercy / Empathy)
                button:
                    xsize 504
                    ysize 72
                    background Solid("#22382d")
                    hover_background Solid("#315442")
                    padding (16, 10)
                    sensitive (leo_focus >= 10)
                    action [
                        If(
                            duel_enemy_composure + int((24 + get_stat("empathy") * 4 + get_stat("courage") * 2 + (18 if duel_intent == "weeping" else 0)) * (1.5 if duel_analyzed else 1.0)) >= 100,
                            true=[Play("sound", "audio/sfx/meadow_breath.ogg"), Return("pacified")],
                            false=Function(duel_player_move, "empathize"),
                        )
                    ]
                    vbox:
                        text _("{font=fonts/DejaVuSans.ttf}♣{/font}  Speak Their Forgotten Name  (EMP [leo_stats['empathy']]) (-10 Focus)") font "fonts/Roboto-Bold.ttf" size 17 color "#a7e8a1"
                        text _("Quiets the soul trapped inside the salt-armor. Huge bonus while Weeping.") size 14 color "#b4c5d2"

                # 5. Burn Astral Resonance (Temptation!)
                button:
                    xsize 504
                    ysize 72
                    background Solid("#2d1b38")
                    hover_background Solid("#452757")
                    padding (16, 10)
                    action [
                        If(
                            duel_enemy_hp <= 52,
                            true=[Play("sound", "audio/sfx/rift_tear.ogg"), Function(change_tether, -8, "Burned memory for Resonance!", True), Function(change_resonance, 12, "", True), Return("vanquished")],
                            false=Function(duel_player_move, "resonance"),
                        )
                    ]
                    vbox:
                        text _("{font=fonts/DejaVuSans.ttf}✦{/font}  Unleash Raw Astral Resonance  (Costs -8 Tether!)") font "fonts/Roboto-Bold.ttf" size 17 color "#d79bf7"
                        text _("Massive 52 damage blast—but permanently burns away a sliver of memory.") size 14 color "#cbb5db"

                # 6. Satchel Ration
                button:
                    xsize 504
                    ysize 72
                    background Solid("#2b241d" if has_item("iron_stew") else "#161c22")
                    hover_background Solid("#42362a")
                    padding (16, 10)
                    sensitive has_item("iron_stew")
                    action Function(duel_player_move, "stew")
                    vbox:
                        text _("{font=fonts/DejaVuSans.ttf}✚{/font}  Eat Bram's Iron-Skillet Ration ([item_count('iron_stew')] left)") font "fonts/Roboto-Bold.ttf" size 17 color ("#f29559" if has_item("iron_stew") else "#6c7a86")
                        text _("Restores +35 HP, +20 Focus, and braces behind cover.") size 14 color "#b4c5d2"
