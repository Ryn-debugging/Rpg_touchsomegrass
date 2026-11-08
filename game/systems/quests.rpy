## ============================================================================
## systems/quests.rpy — Quest Tracker (Main, Side, Character, Hidden) & Codex
## ============================================================================

# Maps quest_id -> {"status": "active"|"completed"|"failed", "step": str}
default quest_states = {}

# Set of unlocked codex entry IDs
default unlocked_codex = {"codex_solvara", "codex_ordinance"}

# Counter for Hidden Clover Relics found (0..3)
default clover_relics_found = 0

init python:
    QUEST_DB = {
        # MAIN QUESTS
        "mq_01_audit": {
            "title": "Wrong Coordinates, Wrong Hero",
            "category": "Main Quest",
            "color": "#ebb963",
            "summary": "Vespera Kael accidentally dragged you into Cindervale expecting a Null-Anchor relic. Survive your arrival in Thornwick and seal the leaking Aqueduct seam before the town floods with salt.",
        },
        "mq_02_envoy": {
            "title": "The Starlight Envoy & The Iron Marshal",
            "category": "Main Quest",
            "color": "#ebb963",
            "summary": "Concordat prodigy Seraphina Lin and High Marshal Cassian Vey have arrived in Thornwick. Navigate their clash over the failing Sixth Seal without getting conscripted as fuel.",
        },
        "mq_03_archive": {
            "title": "Roots Beneath the White Salt",
            "category": "Main Quest",
            "color": "#ebb963",
            "summary": "Descend into the Sunken Archive of First Roots to uncover what truly happened to the Six Paragons of legend—and retrieve the original Recall Calibration Plate.",
        },
        "mq_04_crucible": {
            "title": "Where the Grass Still Grows",
            "category": "Main Quest",
            "color": "#ebb963",
            "summary": "The Sixth Seal is fracturing above Cindervale. Decide what kind of courage—and what kind of sacrifice—will answer the Crucible of Crowns.",
        },

        # SIDE QUESTS
        "sq_turnip_ordinance": {
            "title": "Civic Damages & Bread Debt",
            "category": "Side Quest",
            "color": "#73d2de",
            "summary": "Clerk Fen cited your unauthorized interdimensional arrival. Help Mistress Halda at the town square ovens or audit the municipal ledger to clear your name in Thornwick.",
        },
        "sq_astrolabe_mend": {
            "title": "Hairline Fractures in Brass",
            "category": "Side Quest",
            "color": "#73d2de",
            "summary": "Vespera's Recall Astrolabe has a cracked harmonic lens. Find silver-solder and calibrate it in Orin's Conservatory workshop.",
        },

        # CHARACTER QUESTS
        "cq_bram_skillet": {
            "title": "Iron Horn, Shaking Hands",
            "category": "Character Quest",
            "color": "#f29559",
            "summary": "Help Bram prepare night-watch rations at the Crooked Lantern Inn and stand beside him when memories of the Bastion tunnel collapse resurface.",
        },
        "cq_vespera_oakhaven": {
            "title": "Cartography of Glass",
            "category": "Character Quest",
            "color": "#73d2de",
            "summary": "Uncover why Vespera wears gloves over her wrists and help her lay an overdue survey marker for the vanished orchards of Oakhaven.",
        },
        "cq_orin_ballad": {
            "title": "Unwriting the Fifth Dawn",
            "category": "Character Quest",
            "color": "#8fd687",
            "summary": "Examine Master Orin's unfinished manuscript in the Conservatory and learn why the continent's greatest poet stopped writing about heroes.",
        },
        "cq_sera_rain": {
            "title": "The Sound of Rain on Asphalt",
            "category": "Character Quest",
            "color": "#c792ea",
            "summary": "Seraphina can no longer recall the sound of traffic or her mother's kitchen. Share an ordinary memory of Earth before the Crucible takes the rest of her.",
        },

        # HIDDEN QUEST
        "hq_three_clovers": {
            "title": "Three Blades of Forgotten Clover",
            "category": "Hidden Quest",
            "color": "#7ec876",
            "summary": "Centuries ago, the First Outworlder hid three pressed clover tokens marking a harmless seam between worlds. Finding all three may reveal an impossible fourth path.",
        },
    }

    QUEST_ORDER = [
        "mq_01_audit", "mq_02_envoy", "mq_03_archive", "mq_04_crucible",
        "sq_turnip_ordinance", "sq_astrolabe_mend",
        "cq_bram_skillet", "cq_vespera_oakhaven", "cq_orin_ballad", "cq_sera_rain",
        "hq_three_clovers",
    ]

    CODEX_DB = {
        "codex_solvara": (
            "Solvara: Year 412 Post-Deliverance",
            "Geography & Era",
            "Once a lush continent of river-kingdoms, nearly half of western Solvara now lies calcified beneath the White Salt Wastes—sterile crystalline plains left behind by four centuries of apocalyptic 'Deliverances.' In the current Era of Reconstruction, frontier charters value stonemasons, soil-healers, and drainage engineers infinitely higher than wandering swordsmen.",
        ),
        "codex_ordinance": (
            "The Anti-Deliverance Ordinance",
            "Politics & Law",
            "Enacted by the Free Charter of Thornwick seventeen years ago after a self-styled 'Reborn Paladin' shattered the municipal aqueduct trying to awaken a dormant sword-beam. Publicly proclaiming oneself a Chosen Hero within town limits carries an automatic 40-crown surety bond and mandatory ditch-digging duty.",
        ),
        "codex_resonance": (
            "Astral Resonance & Hero-Scars",
            "Magic System",
            "High magic in Solvara is never free. Casting Astral Resonance consumes either local Verdance—bleaching living soil into dead white salt—or the caster's personal Tether (autobiographical memories and emotional anchors). Those who cast recklessly shine like stars, right up until they forget why they started fighting.",
        ),
        "codex_grounding": (
            "Earthen Grounding (Root-Craft)",
            "Magic System",
            "Practiced by the Rootwardens and Moss-Kin apothecaries. Instead of amplifying energy into destructive blasts, Grounding uses copper-veined spades, harmonic astrolabes, and steady breathing to conduct wild magic harmlessly down into deep bedrock.",
        ),
        "codex_peoples": (
            "Peoples of Cindervale",
            "Cultures",
            "Thornwick is a crossroads of Humans, Ironhorn Korrigans (stone-blooded vanguard smiths whose horns resonate near subterranean tremors), Moss-Kin Sylvari (botanical archivists sensitive to soil health), and the Glass-Touched—survivors of past Heroic wars whose skin bears faint crystalline filigree.",
        ),
        "codex_concordat": (
            "The Aurelian Concordat & Choir of Glass",
            "Factions",
            "Ruling from the eastern alabaster spires of Aurelia, the Concordat views summoned Outworlders as strategic state assets. Rather than reforming destructive industrial Resonance mines, the Choir historically preferred summoning desperate strangers from another world to clean up each crisis.",
        ),
        "codex_vigil": (
            "The Ashen Vigil & The Hollow Seam",
            "Factions",
            "Stationed along the northern salt-cliffs of Fort Bastion under High Marshal Cassian Vey, the Vigil guards the twenty-year-old seal containing the Hollow Tide—a psychic storm of condensed grief and forgotten names.",
        ),
        "codex_paragons": (
            "The Six Paragons of Legend",
            "Secret History",
            "Official Concordat hymns claim the Six Summoned Heroes ascended to heaven after saving Solvara. Archaeological strata in the Sunken Archive tell a darker truth: stripped of every human memory by Resonance burnout, each former Paragon calcified into the very Hollow Sovereign the next generation was summoned to destroy.",
        ),
        "codex_meadow": (
            "The Last Meadow Conservatory",
            "Locations",
            "Tended by Master Orin Mossbeard behind steamed panes of salvaged glass, Thornwick's conservatory shelters genuine non-magical green fescue and white clover—descended from seeds stuck to the First Outworlder's muddy boots four hundred years ago.",
        ),
        "codex_two_roots": (
            "Twin Root-Worlds Hypothesis",
            "Secret History",
            "Notes penned by the First Outworlder suggest Earth and Solvara are adjacent ecological membranes. Summoning beacons do not lock onto martial prowess; they lock onto 'unfulfilled heroic longing'—meaning the loneliest daydreamers on Earth hear the call loudest.",
        ),
    }

    CODEX_ORDER = [
        "codex_solvara", "codex_ordinance", "codex_resonance", "codex_grounding",
        "codex_peoples", "codex_concordat", "codex_vigil", "codex_meadow",
        "codex_paragons", "codex_two_roots",
    ]

    def start_quest(qid, step_text, silent=False):
        if qid not in QUEST_DB:
            return
        store.quest_states[qid] = {"status": "active", "step": step_text}
        if not silent:
            renpy.sound.play("audio/sfx/quest_journal.ogg")
            q = QUEST_DB[qid]
            push_toast(f"{tr('New')} {tr(q['category'])}: {tr(q['title'])}", tr(step_text), q["color"])

    def advance_quest(qid, step_text, silent=False):
        if qid not in QUEST_DB:
            return
        store.quest_states[qid] = {"status": "active", "step": step_text}
        if not silent:
            q = QUEST_DB[qid]
            push_toast(f"{tr('Updated')}: {tr(q['title'])}", tr(step_text), q["color"])

    def complete_quest(qid, summary_step="Completed.", silent=False):
        if qid not in QUEST_DB:
            return
        store.quest_states[qid] = {"status": "completed", "step": summary_step}
        if not silent:
            renpy.sound.play("audio/sfx/quest_journal.ogg")
            q = QUEST_DB[qid]
            push_toast(f"{tr('Completed')}: {tr(q['title'])}", tr(summary_step), "#7ec876")

    def quest_status(qid):
        if qid not in store.quest_states:
            return "unstarted"
        return store.quest_states[qid]["status"]

    def unlock_codex(cid, silent=False):
        if cid in CODEX_DB and cid not in store.unlocked_codex:
            store.unlocked_codex.add(cid)
            if not silent:
                title, _cat, _body = CODEX_DB[cid]
                push_toast(tr("Codex Unlocked"), tr(title), "#73d2de")

    def register_clover_relic(location_hint=""):
        store.clover_relics_found = min(3, store.clover_relics_found + 1)
        count = store.clover_relics_found
        step_msg = f"Found {count}/3 pressed Earth-clover relics." if not location_hint else f"{count}/3 ({location_hint})"
        if quest_status("hq_three_clovers") == "unstarted":
            start_quest("hq_three_clovers", step_msg)
        elif count < 3:
            advance_quest("hq_three_clovers", step_msg)
        else:
            complete_quest("hq_three_clovers", "All 3 Forgotten Clover relics recovered! A hidden resonance path stirs.")
            unlock_codex("codex_two_roots")
            unlock_achievement("ach_clover_finder")
