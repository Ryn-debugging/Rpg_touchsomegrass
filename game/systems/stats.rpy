## ============================================================================
## systems/stats.rpy — Character Attributes, Psychological Tether & Toasts
## ============================================================================

default leo_stats = {
    "strength": 2,
    "intelligence": 4,
    "courage": 1,
    "empathy": 4,
    "charisma": 2,
    "reputation": 0,
}

# Reality Tether (0..100): Leo's connection to his real memories, Earth, and humanity.
default tether = 75

# Astral Resonance Load (0..100): Hollow mythic power accumulated by burning memory/soil.
default resonance_load = 0

# Tactical Encounter Vitality
default leo_hp = 100
default leo_max_hp = 100
default leo_focus = 60
default leo_max_focus = 60

# Brass Crowns (Thornwick currency — starts at 0, can go negative after municipal fines!)
default brass_crowns = 0

# Narrative & Psychological Flags (rollback-safe!)
default story_flags = set()

# Toast Notification Queue (displayed non-intrusively via hud_and_toasts.rpy)
default active_toast_title = ""
default active_toast_body = ""
default active_toast_color = "#7ec876"

init python:
    STAT_METADATA = [
        ("strength", "Strength", "#e58f65", "Physical leverage, stamina, and frontline grit. (Starts low—blame six years of desk chairs.)"),
        ("intelligence", "Intelligence", "#73d2de", "Pattern recognition, astrolabe harmonic math, and reading environmental clues."),
        ("courage", "Courage", "#ebb963", "Acting while your hands shake instead of freezing or apologizing to avoid conflict."),
        ("empathy", "Empathy", "#7ec876", "Hearing what wounded people leave unsaid and refusing to treat lives as math."),
        ("charisma", "Charisma", "#c792ea", "Sincere presence, dry humor, and rallying skeptics without fake hero speeches."),
        ("reputation", "Reputation", "#d4dce6", "Civic trust earned among Thornwick's masons, Rootwardens, and borderlanders."),
    ]

    STAT_LABELS = {k: label for k, label, _, _ in STAT_METADATA}
    STAT_COLORS = {k: col for k, _, col, _ in STAT_METADATA}

    def push_toast(title, body="", color="#7ec876"):
        store.active_toast_title = title
        store.active_toast_body = body
        store.active_toast_color = color
        renpy.show_screen("toast_banner")
        renpy.restart_interaction()

    def change_stat(stat_key, delta, reason="", silent=False):
        key = stat_key.lower()
        if key not in store.leo_stats:
            return
        old_val = store.leo_stats[key]
        # Reputation can range -10..30; core attributes 0..20
        if key == "reputation":
            new_val = max(-10, min(30, old_val + delta))
        else:
            new_val = max(0, min(20, old_val + delta))
        store.leo_stats[key] = new_val
        actual = new_val - old_val
        if actual != 0 and not silent:
            sign = "+" if actual > 0 else ""
            label = STAT_LABELS.get(key, key.title())
            col = STAT_COLORS.get(key, "#7ec876") if actual > 0 else "#e06c75"
            push_toast(f"{label} {sign}{actual}", reason, col)

    def get_stat(stat_key):
        return store.leo_stats.get(stat_key.lower(), 0)

    def has_stat(stat_key, threshold):
        return get_stat(stat_key) >= threshold

    def change_tether(delta, reason="", silent=False):
        old_val = store.tether
        new_val = max(0, min(100, old_val + delta))
        store.tether = new_val
        actual = new_val - old_val
        if actual != 0 and not silent:
            sign = "+" if actual > 0 else ""
            col = "#7ec876" if actual > 0 else "#e06c75"
            push_toast(f"Reality Tether {sign}{actual}%", reason, col)

    def change_resonance(delta, reason="", silent=False):
        old_val = store.resonance_load
        new_val = max(0, min(100, old_val + delta))
        store.resonance_load = new_val
        actual = new_val - old_val
        if actual != 0 and not silent:
            sign = "+" if actual > 0 else ""
            col = "#c792ea" if actual > 0 else "#73d2de"
            push_toast(f"Astral Resonance {sign}{actual}%", reason, col)

    def change_crowns(delta, reason="", silent=False):
        store.brass_crowns += delta
        if delta != 0 and not silent:
            sign = "+" if delta > 0 else ""
            col = "#ebb963" if delta > 0 else "#e06c75"
            push_toast(f"{sign}{delta} Brass Crowns", reason, col)

    def restore_vitality(hp_gain=0, focus_gain=0, silent=False):
        store.leo_hp = min(store.leo_max_hp, max(1, store.leo_hp + hp_gain))
        store.leo_focus = min(store.leo_max_focus, max(0, store.leo_focus + focus_gain))
        if not silent and (hp_gain > 0 or focus_gain > 0):
            parts = []
            if hp_gain > 0:
                parts.append(f"+{hp_gain} HP")
            if focus_gain > 0:
                parts.append(f"+{focus_gain} Focus")
            push_toast("Vitality Restored", ", ".join(parts), "#7ec876")

    def set_flag(flag_name):
        store.story_flags.add(flag_name)

    def has_flag(flag_name):
        return flag_name in store.story_flags

    def tether_status_label():
        t = store.tether
        if t >= 80:
            return "Deeply Grounded"
        elif t >= 55:
            return "Steady Human Memory"
        elif t >= 30:
            return "Fraying Edges"
        else:
            return "Hollowing Into Myth"
