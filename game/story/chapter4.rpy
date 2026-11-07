## ============================================================================
## story/chapter4.rpy — CHAPTER 4: "The Crucible of Crowns"
## The Bleacher Shadow Trial, Sera at the Brink & Spire Summit Confrontation
## ============================================================================

label chapter4_start:
    stop ambience fadeout 0.8
    $ current_chapter_title = "Chapter 4: The Crucible of Crowns"
    $ current_location_name = "Crucible Causeway • Stormfall"

    call screen chapter_title_card(
        "CHAPTER IV",
        "The Crucible of Crowns",
        "\"The hardest monster you will ever face wears your own voice and tells you why you don't count.\""
    )

    play music audio.bgm_crucible fadein 1.5
    play ambience audio.amb_wind fadein 1.2
    scene bg crucible_spire
    with Dissolve(1.0)

    narrator "Above Fort Bastion, the sky has torn open into a cathedral of swirling violet ash and blinding gold rings. Every breath tastes of static and cold pennies."

    show vespera sharp at stage_left
    show bram fierce at stage_right
    with Dissolve(0.35)

    vespera "Look at the outer Causeway—Cassian's engineers opened the Crucible vents! And Seraphina broke off from our rear guard ten minutes ago to beat us to the altar!"
    bram "Hold up! Look down the ridge toward Thornwick—are those torches?!"

    if get_stat("reputation") >= 3:
        narrator "Winding up the switchback road behind us march Mistress Halda, Clerk Fen, Master Orin, and forty frontier masons hauling coils of heavy copper drainage cable on their shoulders!"
        hide bram
        show orin solemn at stage_right
        orin "Did you think Thornwick would let four youngsters shovel its ash alone, Master Leo?! Keep climbing—we're stringing a municipal grounding grid right up the mountain!"
        $ set_flag("town_rallied")
    else:
        hide bram
        show orin solemn at stage_right
        narrator "Master Orin catches up to us at the gatehouse, pressing coils of copper grounding wire into Bram's hands."
        orin "I've wired the Conservatory's deep cisterns to the lower conduit! Get that Calibration Plate to the summit—and watch your minds inside the Hollow mist!"

    ## ------------------------------------------------------------------------
    ## THE HOLLOW THRESHOLD: CHILDHOOD BLEACHER ECHO (MARCUS)
    ## ------------------------------------------------------------------------
    play sound audio.sfx_rift
    scene bg childhood_bleachers
    with flash_crimson

    $ current_location_name = "Echo Within the Hollow Seam"
    narrator "One step across the Spire's inner ward, Solvara vanishes."
    narrator "Cold October rain soaks through my knees. Rust. Wet aluminum bleachers. The torn mustard-yellow page of {i}Sir Valorian{/i} floats in a muddy puddle two inches from my face."

    play sound audio.sfx_heartbeat
    show leo nervous at stage_left, tremble
    with Dissolve(0.3)

    marcus "Seriously, Sato? Twenty-six years old and you {i}still{/i} carry that pathetic notebook around?"

    narrator "A figure coalesces out of grey rain and salt-static—wearing Marcus's sixth-grade letter jacket, speaking in a voice braided from every manager, landlord, and late-night intrusive thought I've ever had."
    marcus "Look at you. Couldn't make friends, couldn't ask for chopsticks, couldn't build a real life—so you prayed for a magic world where strangers have to care about you!"

    if has_flag("childhood_vow_power"):
        marcus "Remember what you swore in the mud? 'Someday I'll be strong enough that nobody laughs!' Well, the Crucible's right upstairs! Drink the fire! Show everybody!"
    elif has_flag("childhood_vow_watchful"):
        marcus "Still counting footsteps and looking for the back exit, coward? Keep running home the long way!"
    else:
        marcus "Still moving earthworms out of puddles so you can pretend being weak is the same thing as being kind?"

    narrator "My chest constricts. That awful, familiar heat stings behind my nose—twenty-six years old, and a hallucination of sixth grade still makes my hands shake."
    thought "Wait. Look at my hands. Yes, they're shaking. They shook at the Aqueduct too. They shook in the Archive."

    menu:
        "Pick up the muddy notebook page—shaking hands and all—and refuse to hate the kid who drew it. \"Yeah, it hurt. And I don't need a crown to stand up anymore.\"":
            $ set_flag("trauma_integrated")
            $ unlock_achievement("ach_marcus_faced")
            $ change_stat("courage", 2, "Stood up without pretending the scar never hurt.")
            $ change_tether(12, "Accepted both the wounded kid and the flawed adult.")
            show leo resolute at stage_left
            leo "You're right about one thing: I spent way too many years waiting for a fantasy story to fix my life."
            leo "That nine-year-old kid in the mud wasn't pathetic for wanting someone to save him. He was just lonely. And he doesn't live under these bleachers anymore."
            narrator "I fold the wet paper carefully, slip it into my pocket beside my brass laundry token, and walk straight through the rain-shadow."

        "Seize the ambient Astral Resonance swirling in the mist and blast the memory to ash! (Costs -18%% Tether, +28%% Resonance)":
            $ change_resonance(28, "Drank the Spire's raw Resonance to silence humiliation!")
            $ change_tether(-18, "Incinerated the memory of Eastside Elementary—and half your childhood with it.")
            $ change_stat("strength", 2, "Surging mythic power fills your limbs.")
            play sound audio.sfx_rift
            with flash_astral
            leo "SHUT UP!"
            narrator "Blinding violet fire erupts from my fist, vaporizing bleachers, rain, fence, and Marcus alike! No shaking. No fear. Only cold, weightless silence where fourth grade used to be."

        "Keep my head down, clutch Orin's copper spade like a lifeline, and push blindly through the mist (-5%% Tether, +1 Courage).":
            $ change_stat("courage", 1, "Forced one boot in front of the other through panic.")
            $ change_tether(-5, "The echo's barbs drew blood, but didn't stop you.")
            leo "Vespera and Bram are waiting upstairs. Talk all you want—I'm walking."

    ## ------------------------------------------------------------------------
    ## SUMMIT THRESHOLD: SERAPHINA AT THE BRINK
    ## ------------------------------------------------------------------------
    $ current_location_name = "Crucible Altar Ring"
    scene bg crucible_spire
    with flash_white

    show cassian weary at stage_left
    show sera fragile at stage_center
    show vespera sharp at stage_right
    with Dissolve(0.4)

    narrator "We burst onto the summit ring just as the Crucible's central column roars skyward—a thirty-foot cylinder of hungry white-gold light!"
    narrator "High Marshal Cassian stands with bare steel lowered in salute; three paces ahead of him, Seraphina stands on the lip of the dais, her cobalt coat already dissolving into motes of silver ash at the hem."

    cassian "Step back, Broker Kael! The northern cliff just dropped into the sea—if the Crucible isn't fed an anchor within two minutes, Bastion falls!"
    sera "Stay back, Sato! Don't ruin the one thing I'm actually good for!"
    narrator "Tears spill down Seraphina's cheeks, evaporating into white salt before they reach her chin."
    sera "I can't remember my mom's first name anymore! If I go back to Earth like this, who am I?! At least if I burn here, thirty thousand people live and {i}somebody{/i} remembers Seraphina!"

    menu:
        "(Remind Her of Home) \"Chicago! Lakeshore buses hissing in November rain—and hot tea with LEMON! Step off that ledge, Sera—we brought the First-Era Plate!\"" if has_flag("sera_opened_up") or has_stat("empathy", 6):
            $ set_flag("sera_anchored")
            $ unlock_achievement("ach_sera_saved")
            $ change_affinity("sera", 4, "Pulled her back from total self-erasure!")
            $ change_stat("charisma", 2, "Cut through four centuries of martyrdom.")
            leo "Your mom's waiting in a kitchen that smells like lemon and ginger, Sera! And Vespera dragged a three-hundred-pound bronze plate up six hundred stairs so {i}nobody{/i} has to turn into a statue tonight!"
            narrator "Seraphina freezes on the very edge of the golden fire. Her lip trembles—and when Vespera lunges forward, Sera grabs her outstretched scarred wrist with both hands and stumbles back onto solid stone!"
            show sera neutral at stage_center
            sera "...Lemon. Her name is Mei-Ling. Oh god—her name is Mei-Ling!"

        "(Rally With Grit) Plant Orin's copper spade right between Sera and the fire! \"Marshal Cassian! Help us bolt this Calibration Plate down—we're grounding the Crucible, not feeding it!\"":
            if has_stat("courage", 4) or get_affinity("cassian") >= 1:
                $ set_flag("sera_anchored")
                $ unlock_achievement("ach_sera_saved")
                $ change_stat("courage", 1, "Forced a third option onto the summit.")
                show cassian stern at stage_left
                cassian "...First-Era bronze?! Guards—sheathe blades! Help the Rootwarden bolt those leads into the stone!"
                narrator "Bram bodily scoops a stunned Seraphina back from the ledge behind his tower shield as Cassian drops to one knee beside Vespera's wrench!"
            else:
                narrator "Bram lunges forward, hooking Seraphina's collar back from the flames just as a shockwave cracks the altar stone in half!"

        "(Temptation of the Crown) Step past Seraphina toward the golden pillar myself. \"Get back, Sera. My longing reading was higher than yours—let me take it.\"":
            $ set_flag("chose_crown_early")
            $ change_resonance(35, "Stepped willingly toward the Mythic Crown.")
            $ change_tether(-25, "Surrendered human smallness for blinding power.")
            vespera "LEO, NO! WHAT ARE YOU DOING?!"

    $ complete_quest("mq_04_crucible", "Reached the Crucible summit for the final reckoning.")
    pause 0.5
    return
