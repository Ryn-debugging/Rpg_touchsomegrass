## ============================================================================
## story/chapter3.rpy — CHAPTER 3: "Beneath the Salt Wastes"
## Sunken Archive Exploration Hub + Hollow Remnant Tactical Stance Duel
## ============================================================================

label chapter3_start:
    $ current_chapter_title = "Chapter 3: Beneath the Salt Wastes"
    $ current_location_name = "Sunken Archive of First Roots"

    call screen chapter_title_card(
        "CHAPTER III",
        "Beneath the Salt Wastes",
        "\"The hymns say all six Paragons ascended into starlight. Nobody asked why their boots were still downstairs.\""
    )

    play music audio.bgm_mystery fadein 1.5
    scene bg sunken_archive
    with Dissolve(1.0)

    narrator "At dawn, Vespera unlocks an overgrown Rootwarden sluice-gate two miles west of Thornwick. Spiral basalt stairs lead three hundred feet below the White Salt Wastes into a cavern held open by petrified world-tree roots."

    show vespera neutral at stage_left
    show bram neutral at stage_center
    show sera neutral at stage_right
    with Dissolve(0.4)

    bram "Keep close to my lantern, folks. My left horn's buzzing like a tuning fork—there's old Resonance pooled down in the nave."
    sera "Look at these walls... That's pre-Concordat architecture. The Choir told me nothing survived down here."
    vespera "The Choir tells Outworlders lots of bedtime stories, Envoy. Let's split the chamber search—the Calibration Vault is just beyond the central archway."

    ## ------------------------------------------------------------------------
    ## INTERACTIVE EXPLORATION HUB 2: SUNKEN ARCHIVE (3 AP)
    ## ------------------------------------------------------------------------
    $ hub_max_actions = 3
    $ hub_actions_left = 3

label ch3_archive_hub:
    scene bg sunken_archive
    play music audio.bgm_mystery if_changed fadein 0.8
    $ current_location_name = "Sunken Archive (Exploration)"

    python:
        ch3_nodes = [
            {
                "id": "arch_pedestals",
                "title": "Aisle of the Six Pedestals",
                "tag": "MAIN LORE REVELATION • Secret History (+INT, +Codex)",
                "subtitle": "Six calcified plinths bearing scratched inscriptions in modern Earth languages.",
                "color": "#ebb963",
                "done": "ch3_pedestals" in visited_nodes,
                "cost": 1,
            },
            {
                "id": "arch_campfire",
                "title": "Root-Spring Lantern Camp",
                "tag": "PARTY REST & BONDING • Restore Full HP/Focus + Companion Moment",
                "subtitle": "Share hot rations beside an underground spring before breaching the vault.",
                "color": "#f29559",
                "done": "ch3_camp" in visited_nodes,
                "cost": 1,
            },
            {
                "id": "arch_alcove",
                "title": "The First Botanist's Alcove",
                "tag": "HIDDEN RELIC • Clover #3 & First-Era Notes",
                "subtitle": "A collapsed root-hollow sealed with copper wire and four-hundred-year-old English.",
                "color": "#7ec876",
                "done": "ch3_alcove" in visited_nodes,
                "cost": 1,
            },
        ]
        ch3_can_advance = ("ch3_pedestals" in visited_nodes) or hub_actions_left <= 0

    call screen exploration_hub(
        "Sunken Archive of First Roots",
        "Investigate the buried truth of past Outworlders and prepare your party before approaching the Calibration Vault.",
        ch3_nodes,
        ch3_can_advance,
        "Breach the Calibration Vault"
    )

    $ arch_choice = _return

    if arch_choice == "__ADVANCE__":
        jump ch3_remnant_duel
    elif arch_choice == "arch_pedestals":
        $ visited_nodes.add("ch3_pedestals")
        $ hub_actions_left -= 1
        call ch3_scene_pedestals
        jump ch3_archive_hub
    elif arch_choice == "arch_campfire":
        $ visited_nodes.add("ch3_camp")
        $ hub_actions_left -= 1
        call ch3_scene_campfire
        jump ch3_archive_hub
    elif arch_choice == "arch_alcove":
        $ visited_nodes.add("ch3_alcove")
        $ hub_actions_left -= 1
        call ch3_scene_alcove
        jump ch3_archive_hub
    else:
        jump ch3_remnant_duel


## ARCHIVE NODE A: THE SIX PEDESTALS (THE PARAGON TWIST!) ---------------------
label ch3_scene_pedestals:
    $ current_location_name = "Aisle of the Six Pedestals"
    scene bg sunken_archive
    with Dissolve(0.4)

    show leo nervous at stage_left
    show sera fragile at stage_right
    with Dissolve(0.3)

    narrator "My flashlight—well, Vespera's brass lantern—sweeps behind the fourth salt-crusted statue. Scratched frantically into the slate with a belt buckle are words in messy, unmistakable English:"
    narrator "{i}'MY NAME IS DANIEL CHO. TACOMA, WA. IF ANOTHER ONE OF US GETS PULLED HERE—DO NOT DRINK THE CRUCIBLE. I KILLED THE THIRD CALAMITY TODAY AND SAW A WRISTWATCH FUSED INSIDE ITS RIBS.'{/i}"
    narrator "{i}'THERE ARE NO DEMON KINGS. IT'S JUST US AFTER WE FORGET HOME.'{/i}"

    play sound audio.sfx_heartbeat
    $ unlock_codex("codex_paragons")
    $ change_stat("intelligence", 1, "Uncovered the horrifying truth of the Six Paragons.")
    $ set_flag("learned_paragon_truth")

    sera "...A wristwatch. No. The Choir hymns say the Hollow Sovereigns crawl up from the Abyss—"
    leo "Every Hero burned their memories until nothing was left except power looking for a fight... and then Aurelia summoned the {i}next{/i} lonely kid from Earth to put them down."
    narrator "Seraphina backs against a petrified root, hand over her mouth. Neither of us speaks for a long moment."
    return


## ARCHIVE NODE B: SUBTERRANEAN SPRING CAMPFIRE -------------------------------
label ch3_scene_campfire:
    $ current_location_name = "Root-Spring Camp"
    scene bg sunken_archive
    with Dissolve(0.4)

    show bram grin at stage_left
    show vespera soft at stage_right
    with Dissolve(0.3)

    bram "Nobody fights ancient salt-ghosts on an empty stomach! Drink up, stretch your calves, and check your copper leads!"
    $ restore_vitality(hp_gain=100, focus_gain=60, silent=False)
    $ add_item("iron_stew", 1, silent=True)

    if get_affinity("vespera") >= get_affinity("bram") and get_affinity("vespera") >= get_affinity("sera"):
        vespera "Hey, Sato. Whatever we find behind that vault door... when this is over, you're going back through that puddle with all your memories intact. Broker's guarantee."
        $ change_affinity("vespera", 1, "Quiet promise by lantern-light.")
    elif get_affinity("sera") > get_affinity("bram"):
        hide bram
        show sera neutral at stage_left
        sera "...Your friend's garlic ration is absurdly salty. Give me half another piece. And don't die in the next room, cubicle guy."
        $ change_affinity("sera", 1, "Shared rations before the vault.")
    else:
        bram "Listen here, Leo: you're still shaped like a shrimp, {i}but{/i} you're the toughest shrimp I've ever shared a shieldwall with! Let's bring that plate back to Orin!"
        $ change_affinity("bram", 1, "Brothers of the Iron Skillet.")
    return


## ARCHIVE NODE C: FIRST BOTANIST'S ALCOVE (CLOVER #3!) -----------------------
label ch3_scene_alcove:
    $ current_location_name = "First Botanist's Alcove"
    scene bg sunken_archive
    with Dissolve(0.4)

    show leo resolute at stage_center
    with Dissolve(0.3)

    narrator "Tucked inside a hollow taproot is a rusted tin biscuit box from seventeenth-century London—wrapped in Rootwarden copper mesh that kept the salt away for four centuries."
    narrator "Inside rests a humming salt-glass prism, schematic notes for a {b}Twin-Root Harmonic Bypass{/b}, and the final mica-pressed three-leaf clover!"

    $ add_item("sixth_seal_shard", 1)
    if not has_item("pressed_clover"):
        $ add_item("pressed_clover", 1)
    $ register_clover_relic("First Botanist's Tin")
    $ change_tether(6, "Read the First Outworlder's farewell note.")

    thought "'Root Three: A hero is just a bridge until regular folks can cross on their own. Plant something green and go home.' — E. Marrow, 1689."
    return


## ============================================================================
## CHAPTER 3 CLIMAX: TACTICAL DUEL AGAINST THE HOLLOW REMNANT
## ============================================================================
label ch3_remnant_duel:
    stop music fadeout 0.6
    play music audio.bgm_combat fadein 0.8
    $ current_location_name = "Calibration Vault Threshold"

    scene bg sunken_archive
    with Dissolve(0.5)

    play sound audio.sfx_rift
    with vpunch

    show remnant form at stage_center
    with Dissolve(0.5)

    narrator "Before the bronze Calibration Plate rises a nine-foot figure of fractured white salt-armor. Weeping violet starlight spills through its cracked visor as a broken halberd scrapes across the flagstones."
    remnant "...WHO... CALLS... FOR... DELIVERANCE...?"

    if has_flag("learned_paragon_truth"):
        leo "Wait—don't blast it! Look at the tarnished buckle under the crystal—that's Daniel Cho! The Fourth Paragon!"
    else:
        vespera "Watch out! That's a calcified Paragon husk—centuries of burned Resonance locked on autopilot! Ready stances!"

    $ init_tactical_duel("Hollow Remnant (Paragon IV)", 120)
    call screen tactical_duel
    $ duel_outcome = _return

    if duel_outcome == "pacified":
        $ unlock_achievement("ach_remnant_mercy")
        $ change_stat("empathy", 2, "Restored Daniel Cho's human name instead of shattering him.")
        $ change_stat("courage", 1, "Lowered your weapon in front of a nine-foot calamity.")
        $ change_affinity("sera", 2, "Watched you save an Outworlder everyone else wrote off.")
        $ change_affinity("vespera", 2, "Saw proof that hollowing isn't the only ending.")
        $ change_tether(6, "Refused to forget a predecessor's humanity.")

        play sound audio.sfx_heal
        hide remnant with flash_meadow

        leo "Daniel! Daniel Cho from Tacoma! The fight's over—nobody's asking you to carry the sky anymore!"
        narrator "The giant halberd freezes an inch above Bram's dented shield."
        remnant "...Tacoma...? Rain... on... cedar...?"
        narrator "Instead of exploding into lethal salt, the crystalline armor sighs—crumbling into soft, dark, living loam across the cavern floor as a single pale green shoot uncurls between the stones."

    else:
        $ change_stat("strength", 1, "Shattered calcified Fourth-Era armor.")
        $ change_stat("courage", 1, "Stood firm in the Archive vanguard.")
        $ change_affinity("bram", 2, "Fought shoulder-to-shoulder until the end.")

        play sound audio.sfx_strike
        hide remnant with flash_astral

        narrator "With Bram locking the halberd shaft against his tower shield, I drive Orin's copper spade straight through the breastplate's central fissure—conducting four centuries of trapped static harmlessly into the cavern floor!"
        narrator "As the empty salt-helm clatters onto the stone, a faint whisper exhales: {i}'...Thank you...'{/i}"

    stop music fadeout 1.2
    play music audio.bgm_mystery fadein 1.2

    show vespera sharp at stage_left
    show bram fierce at stage_right
    with Dissolve(0.35)

    narrator "Vespera wrenches the heavy bronze **First-Era Calibration Plate** free from the altar—just as the entire cavern ceiling shudders violently, showering white dust down the stairs!"
    play sound audio.sfx_rift
    with vpunch

    bram "Uh-oh. My horn just rang like a church bell! That wasn't down here—that was {i}up top{/i}!"
    vespera "The northern sky! The Sixth Seal didn't wait for sunset—Cassian's Ascending the Crucible Spire RIGHT NOW! Move!"

    $ complete_quest("mq_03_archive", "Recovered the First-Era Calibration Plate and witnessed the fate of Paragon IV.")
    $ start_quest("mq_04_crucible", "Race up the Crucible Spire before the Hollow Tide—or the Crucible itself—claims another soul.")
    pause 0.6
    return
