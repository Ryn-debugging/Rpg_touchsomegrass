## ============================================================================
## systems/relationships.rpy — Companion & Foil Affinity System
## ============================================================================

default char_affinity = {
    "vespera": 1,
    "bram": 0,
    "sera": -1,
    "orin": 2,
    "cassian": 0,
}

default met_characters = {"vespera"}

init python:
    CHARACTER_PROFILES = {
        "vespera": {
            "name": "Vespera Kael",
            "role": "Disgraced Recall Broker • Rootwardens",
            "color": "#73d2de",
            "sprite": "images/characters/vespera_neutral.png",
            "summary": "A sharp-tongued cartographer's daughter from vitrified Oakhaven. Runs illegal unsummoning contracts with a cracked brass astrolabe and too much bitter chicory.",
            "secret_flag": "vespera_opened_up",
            "secret_note": "Unlocked Bond Insight: She blames herself for leaving Oakhaven's eastern ward three minutes before the Sixth Paragon's light turned the orchards to salt.",
        },
        "bram": {
            "name": "Bramwell 'Bram' Thorne",
            "role": "Former Vigil Shield-Bearer • Camp Cook",
            "color": "#f29559",
            "sprite": "images/characters/bram_neutral.png",
            "summary": "An Ironhorn Korrigan who carries a cast-iron skillet alongside his tower shield. Loudly allergic to self-pity, cowardly posture, and under-seasoned broth.",
            "secret_flag": "bram_opened_up",
            "secret_note": "Unlocked Bond Insight: His horn was chipped saving two recruits in a mine collapse—before a panic attack cost him his Vigil commission.",
        },
        "sera": {
            "name": "Seraphina 'Sera' Lin",
            "role": "Concordat Starlight Envoy • Outworlder",
            "color": "#c792ea",
            "sprite": "images/characters/sera_neutral.png",
            "summary": "Summoned from Earth eighteen months ago. Radiant, immaculate, and dangerously overworked—the golden savior everyone compares Leo against.",
            "secret_flag": "sera_opened_up",
            "secret_note": "Unlocked Bond Insight: High Resonance has already burned away her mother's voice; she clings to being a 'Hero' because she's terrified of becoming nobody.",
        },
        "orin": {
            "name": "Master Orin Mossbeard",
            "role": "Keeper of the Last Meadow • Former Chronicler",
            "color": "#8fd687",
            "sprite": "images/characters/orin_neutral.png",
            "summary": "An elderly Moss-Kin herbalist and blade-mender tending real Earth-strain meadow grass inside Thornwick's glass conservatory.",
            "secret_flag": "orin_opened_up",
            "secret_note": "Unlocked Bond Insight: Forty years ago he authored the famous Ballad of the Fifth Dawn—and has spent decades trying to undo the martyrdom cult his poetry inspired.",
        },
        "cassian": {
            "name": "High Marshal Cassian Vey",
            "role": "Commander of the Ashen Vigil",
            "color": "#d4dce6",
            "sprite": "images/characters/cassian_neutral.png",
            "summary": "Once the teenaged squire of the Sixth Paragon. A quiet, courteous commander willing to make monstrous calculations to keep thirty thousand borderlanders alive.",
            "secret_flag": "cassian_understood",
            "secret_note": "Unlocked Bond Insight: He keeps the Sixth Paragon's rusted wooden practice sword—not the legendary blade—to remind himself a real boy died inside that seal.",
        },
    }

    CHARACTER_ORDER = ["vespera", "bram", "sera", "orin", "cassian"]

    def meet_character(char_id):
        if char_id in CHARACTER_PROFILES:
            store.met_characters.add(char_id)

    def get_affinity(char_id):
        return store.char_affinity.get(char_id, 0)

    def affinity_rank(char_id):
        val = get_affinity(char_id)
        if val <= -3:
            return "Bitter Friction"
        elif val <= -1:
            return "Guarded Skeptic"
        elif val <= 2:
            return "Wary Acquaintance"
        elif val <= 5:
            return "Reluctant Ally"
        elif val <= 8:
            return "Trusted Companion"
        else:
            return "True Anchor"

    def change_affinity(char_id, delta, note="", silent=False):
        if char_id not in store.char_affinity:
            return
        store.met_characters.add(char_id)
        old_val = store.char_affinity[char_id]
        new_val = max(-10, min(15, old_val + delta))
        store.char_affinity[char_id] = new_val
        actual = new_val - old_val
        if actual != 0 and not silent:
            meta = CHARACTER_PROFILES[char_id]
            sign = "+" if actual > 0 else ""
            col = meta["color"] if actual > 0 else "#e06c75"
            push_toast(f"{tr(meta['name'])} {sign}{actual}", note or affinity_rank(char_id), col)
