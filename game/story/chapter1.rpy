## ============================================================================
## story/chapter1.rpy — CHAPTER 1: "No Heroes Allowed in Thornwick"
## ============================================================================

label chapter1_start:
    stop ambience fadeout 1.0
    $ current_chapter_title = "Chapter 1: No Heroes Allowed"
    $ current_location_name = "White Salt Ruins • Cindervale"

    call screen chapter_title_card(
        "CHAPTER I",
        "No Heroes Allowed in Thornwick",
        "\"Every ballad ends right after the dragon falls. Nobody writes verses about who has to shovel up the ash.\""
    )

    play ambience audio.amb_wind fadein 1.5
    scene bg salt_ruins
    with eye_blink

    narrator "When my eyes open, the sky is the color of tarnished pewter, and two pale broken moon-rings hang crooked above a horizon of crystalline white ash."
    narrator "No telephone wires. No sirens. Just ruined basalt arches half-swallowed by glittering salt drifts."

    show leo nervous at stage_left
    with Dissolve(0.35)

    thought "Hold on."
    thought "Broken moons. Ancient stone pillars. Mysterious robed kidnapper—okay, coat-wearing kidnapper—kneeling five feet away swearing at a brass sphere."
    thought "Wait a second. Wait just one second. Did it actually happen?!"

    show leo resolute at stage_left, hop
    leo "I'm... in another world."
    thought "Twenty-six years! Twenty-six years of eating microwave rice over the sink, and finally—FINALLY—the universe read my file!"

    show vespera tired at stage_right
    with Dissolve(0.35)

    vespera "Stop grinning like a concussed turnip and hold still while I read your mass index."
    narrator "My kidnapper taps her smoking brass astrolabe with a wrench. A thin cyan beam sweeps from my damp sneakers to my hairline, then lets out a sound like a deflating bagpipe."

    show vespera sharp at stage_right, hop
    vespera "...Strength: two. Martial Resonance: zero. Lower-lumbar curvature: alarming."
    vespera "Explain yourself! When I cast the net from the Cindervale seam, your 'Unfulfilled Heroic Longing' spiked higher than a Royal Templar's! What were you doing on the other side, leading a doomed rebellion?!"

    show leo nervous at stage_left, flinch
    leo "I was waiting for my hoodies to finish spin-cycle!"
    vespera "Your {i}what{/i}?!"
    leo "Wait—aren't you a princess, or a court mage summoning the Seventh Hero to defeat a Demon King?!"

    narrator "For three full seconds, the wind whistles across the salt plain while she stares at me as though I just offered to lick a plague rat."

    show vespera tired at stage_right
    vespera "Kid. Look behind you."
    narrator "She points a scarred gloved thumb toward the miles of dead, chalk-white wasteland stretching west where forests clearly used to stand."
    vespera "See all that dead salt? That {i}used{/i} to be Oakhaven Valley before the Sixth 'Chosen Hero' unleashed his glorious final sword-beam twenty years ago."
    vespera "My name is Vespera Kael. I'm a Recall Broker. I get paid—badly—to {i}shut down{/i} summoning seams and send delusional Outworlders home before they 'save' another province into glass."

    $ meet_character("vespera")
    $ unlock_codex("codex_resonance", silent=True)
    $ start_quest("mq_01_audit", "Follow Vespera into Thornwick and inspect the leaking Aqueduct seam.")

    menu:
        "\"So... there's no legendary sword waiting for me? At all?\" (Be honest about the disappointment)":
            $ change_affinity("vespera", 1, "Appreciated that you didn't fake bravado.")
            $ change_tether(3, "Admitted the embarrassment out loud.", silent=True)
            show vespera neutral at stage_right
            vespera "Honestly? The fact that your face just crumpled instead of shouting about destiny is the first reassuring thing about you."
            vespera "Come on. My astrolabe cracked on re-entry, which means neither of us is sending you back to your 'spin-cycle' until Master Orin solders the lens."

        "\"Hey! You kidnapped ME! The least you can do is drop the attitude!\" (Push back)":
            $ change_stat("courage", 1, "Talked back to an armed stranger.")
            $ change_affinity("vespera", 1, "Surprised you actually have a spine.")
            show leo resolute at stage_left
            show vespera neutral at stage_right
            vespera "...Huh. There's a pulse under the wet cardigan after all."
            vespera "Fair point. Unlawful abduction, botched coordinates—my fault. Help me plug the Thornwick seam so the town doesn't calcify tonight, and I'll solder this rig and drop you right back on your sidewalk. Deal?"

        "Quietly notice the crystalline burn scars peeking past her cuffs. \"Your wrists... was that from Oakhaven?\"":
            $ change_stat("empathy", 1, "Noticed the person behind the cynicism.")
            $ change_affinity("vespera", 2, "Caught off guard by quiet perceptiveness.")
            show vespera soft at stage_right
            narrator "Vespera's fingers twitch, tugging her leather cuff down over the translucent glass veins."
            vespera "...Observant, aren't you? Yeah. Grade-two Hero-Scar. Keeps me honest about who pays the bill for miracles."

    ## ------------------------------------------------------------------------
    ## ENTERING THORNWICK SQUARE & THE MUNICIPAL CITATION
    ## ------------------------------------------------------------------------
    stop ambience fadeout 1.0
    play music audio.bgm_thornwick fadein 1.5
    $ current_location_name = "Thornwick Charter Square"

    scene bg thornwick_square
    with Dissolve(1.0)

    narrator "Twenty minutes down the ridge, the white salt gives way to terraced dark stone, slate roofs, waterwheels, and the mouthwatering smell of wood-fired barley bread."
    narrator "Thornwick doesn't look like an elven capital from a painting. It looks lived-in, muddy, stubborn, and busy."
    narrator "A seven-foot horned smith argues mortar prices with a bark-skinned herbalist; two kids chase a plump moss-beetle past a wooden signboard nailed prominently to the gatehouse:"
    narrator "{b}NOTICE: UNAUTHORIZED CHOSEN ONES, PROPHECY BEARERS & DOOM-SLAYERS MUST REGISTER SURETY DEPOSIT (40 CROWNS). VIOLATORS WILL SHOVEL DRAINAGE DITCH B.{/b}"

    show leo neutral at stage_left
    show vespera neutral at stage_right
    with Dissolve(0.3)

    clerk "Halt right there, Kael! Don't think I didn't see the ozone flash on the salt ridge!"

    narrator "A nearsighted municipal clerk with an ink-stained tabard and an iron clipboard marches out from the weigh-station, squinting straight at my nylon windbreaker."
    clerk "Unnatural synthetic weave! Slouched shoulders! Starry-eyed bewilderment! That's an unregistered Outworlder!"

    menu:
        "Panic and strike what my brain thinks is a reassuringly noble stance. \"Fear not, good citizen!\"":
            $ change_crowns(-40, "Anti-Deliverance Ordinance Citation #884.")
            $ change_stat("reputation", -1, "Declared heroic intent near municipal masonry.", silent=True)
            $ unlock_achievement("ach_fined")
            $ start_quest("sq_turnip_ordinance", "Work off your 40-Crown citation in Thornwick Square.")
            show leo nervous at stage_left, flinch
            clerk "'FEAR NOT'?! Section Four—verbal threats of unsolicited deliverance! Forty Brass Crowns, payable by sundown!"
            show vespera tired at stage_right, sink_sigh
            vespera "I look away for {i}four seconds{/i} and you say 'Fear not' in a charter town. Incredible."

        "(Charisma / Honesty) Hold up my plastic laundry bag. \"Sir, I'm an underpaid data clerk. If a monster attacked, I'd file a ticket and hide.\"":
            $ change_stat("charisma", 1, "Disarmed bureaucracy with pathetic honesty.")
            $ change_stat("reputation", 1, "Thornwick respects self-aware civilians.")
            $ start_quest("sq_turnip_ordinance", "Check in with Clerk Fen or Mistress Halda to earn honest keep.")
            clerk "...A clerk? Let me see your hands."
            narrator "Clerk Fen inspects my soft, keyboard-calloused palms and nods approvingly."
            clerk "Not a sword-blister in sight! Refreshing! Still, unregistered portal transit carries a ten-crown administrative stamp—see Mistress Halda at the ovens if you want to work it off."
            $ change_crowns(-10, "Portal Transit Stamp Fee.")

        "(Intelligence 5+) Cite the sign's wording: \"Wait—'Chosen Ones.' Vespera's astrolabe logged me at zero Resonance. Legally I'm cargo, not a Hero!\"" if has_stat("intelligence", 5):
            $ change_stat("intelligence", 1, "Out-clause'd a frontier bureaucrat!")
            $ change_stat("reputation", 2, "Impressed Clerk Fen with charter law.")
            $ change_affinity("vespera", 1, "Delighted by your legal loophole.")
            $ start_quest("sq_turnip_ordinance", "Optional: Help Fen & Mistress Halda in the Square for bonus pay.")
            clerk "...Sub-clause seven: 'Inert Cross-Planar Ballast.' Well I'll be salted. An Outworlder who reads municipal signage!"
            vespera "Ha! Take notes, Fen—my ballast knows how to read!"

    ## ------------------------------------------------------------------------
    ## MEETING BRAM & MASTER ORIN IN THE LAST MEADOW CONSERVATORY
    ## ------------------------------------------------------------------------
    play sound audio.sfx_strike
    narrator "Before Clerk Fen can dry his quill, a heavy iron tower-shield {i}clangs{/i} onto the cobblestones beside us—followed by the aroma of toasted cumin and garlic."

    hide vespera
    show bram grin at stage_right
    with Dissolve(0.35)

    $ meet_character("bram")
    $ unlock_codex("codex_peoples", silent=True)

    bram "Oi, Vespera! Orin said your astrolabe popped a lens again! Is {i}this{/i} the anchor you fished out? Look at him, a stiff breeze off the salt flats'll fold him like a crepe!"
    show leo nervous at stage_left
    leo "H-hi. Sorry for being foldable."
    show bram fierce at stage_right, hop
    bram "Agh, there it is! Apologizing for existing! Rule one of Cindervale, string-bean: save 'sorry' for when you step on somebody's tail, and stand with your ribs over your hips! Name's Bram!"

    narrator "Despite the volume, the broad-shouldered Korrigan shoves a warm waxed-paper parcel into my freezing hands—fresh flatbread smeared with roasted marrow-butter."
    $ add_item("iron_stew", 1)

    bram "Eat that before your teeth rattle loose. Orin's waiting up in the glasshouse."

    ## THE CONSERVATORY SCENE -------------------------------------------------
    stop music fadeout 1.0
    play music audio.bgm_conservatory fadein 1.8
    $ current_location_name = "The Last Meadow Conservatory"

    scene cg conservatory_clover
    with flash_meadow

    narrator "Stepping through Master Orin's steamed cedar doors feels like walking straight into a childhood summer I'd forgotten existed."
    narrator "Inside the salvaged glass dome, shielded from Cindervale's ash winds, stretches a living carpet of ordinary, vibrant {b}green grass{/b} and white three-leaf clover."
    narrator "Warm loam. Damp earthworms. Sunlight refracted through misted panes."

    leo "...It's just grass. Regular park grass."

    scene bg orin_conservatory
    with Dissolve(0.8)

    show leo warm at stage_left
    show orin smile at stage_center
    show vespera neutral at stage_right
    with Dissolve(0.4)

    $ meet_character("orin")
    $ unlock_codex("codex_meadow", silent=True)
    $ unlock_codex("codex_grounding", silent=True)

    orin "Not 'just' grass here, Master Leo. Four hundred winters ago, those seeds rode into Solvara wedged in the mud of the First Outworlder's heel."
    orin "Go on. Kneel down. Press your palm to it."

    narrator "Self-consciously, I crouch and rest my bare fingers in the cool blades. My racing pulse slows for the first time since 2:38 AM."
    $ change_tether(6, "Touched real living grass in Orin's Conservatory.")

    show orin solemn at stage_center
    orin "Every flashy spell cast by a 'Hero' drinks the green life out of soil—or drinks the caster's own memories when the soil runs dry."
    orin "Vespera tells me you grew up wishing to be a hero, lad. Tell an old chronicler truthfully: {i}why{/i}?"

    menu:
        "\"Because I was tired of feeling weak and humiliated. I wanted people to finally look up to me.\"":
            $ change_stat("courage", 1, "Told an unflattering truth without dressing it up.")
            $ change_affinity("orin", 2, "Deeply respected your rare honesty.")
            show orin smile at stage_center
            orin "Bless you for not lying to an old poet. Half the tragedies in my history books started with men who felt small and mistook applause for medicine."

        "\"Because nobody ever showed up when I needed help. I wanted to be the person who actually shows up.\"":
            $ change_stat("empathy", 1, "Named the wound underneath the daydream.")
            $ change_affinity("orin", 2, "Moved by your quiet sincerity.")
            $ change_affinity("vespera", 1, "Listened quietly from the workbench.")
            show orin smile at stage_center
            orin "Ah. Now {i}that{/i} requires neither a glowing blade nor a prophecy, lad. Only two boots that refuse to walk past."

        "\"Honestly? Because fantasy worlds looked simpler than paying rent and disappointing everyone.\"":
            $ change_stat("intelligence", 1, "Diagnosed your own escapism clearly.")
            $ change_tether(4, "Recognized the trap of fantasy.")
            $ change_affinity("vespera", 2, "Let out an actual laugh.")
            show vespera soft at stage_right
            vespera "Careful, Orin, keep him talking and I might actually start liking him."

    narrator "Master Orin lifts a sturdy ash-wood trenching spade inlaid with spirals of dull copper wire and rests it across my palms."
    $ add_item("grounding_spade", 1)

    orin "No Excalibur in my shed, Leo. Only a Rootwarden's Grounding Spade. Instead of cutting monsters in half, copper-craft conducts wild Resonance safely back into deep stone."
    vespera "And we're going to need it by dusk. The Old Aqueduct seam is humming, and Orin needs an hour for the silver-solder to set on my astrolabe."
    vespera "Look around town, get your bearings, don't shout any battle cries—and meet Bram and me at the Old Aqueduct before sundown."

    $ advance_quest("mq_01_audit", "Explore Thornwick (up to 4 actions), then meet Vespera & Bram at the Old Aqueduct.")
    $ start_quest("sq_astrolabe_mend", "Help calibrate Vespera's astrolabe at the Conservatory workbench.")
    $ start_quest("cq_bram_skillet", "Check on Bram in the Crooked Lantern Inn kitchen.")
    $ start_quest("cq_orin_ballad", "Ask Master Orin about his crossed-out ballad scrolls.")

    ## ------------------------------------------------------------------------
    ## INTERACTIVE EXPLORATION HUB 1: THORNWICK FRONTIER (4 AP)
    ## ------------------------------------------------------------------------
    $ hub_max_actions = 4
    $ hub_actions_left = 4

label ch1_thornwick_hub:
    scene bg thornwick_square
    play music audio.bgm_thornwick if_changed fadein 1.0
    $ current_location_name = "Thornwick Frontier (Exploration)"

    python:
        ch1_nodes = [
            {
                "id": "node_inn_bram",
                "title": "The Crooked Lantern Kitchen",
                "tag": "CHARACTER QUEST • Bram (+Affinity, +STR/EMP, Rations)",
                "subtitle": "Steam, cast-iron skillets, and Bram prepping stew for the aqueduct watch.",
                "color": "#f29559",
                "done": "ch1_inn" in visited_nodes,
                "cost": 1,
            },
            {
                "id": "node_conservatory_work",
                "title": "Conservatory Workbench & Scrolls",
                "tag": "SIDE & MENTOR QUEST • Vespera & Orin (+INT, Astrolabe, Tea)",
                "subtitle": "Calibrate Vespera's brass lens and examine Orin's abandoned heroic epics.",
                "color": "#8fd687",
                "done": "ch1_conservatory" in visited_nodes,
                "cost": 1,
            },
            {
                "id": "node_square_ovens",
                "title": "Town Ovens & Weigh-Station",
                "tag": "SIDE QUEST • Civic Standing (+Reputation, +Crowns)",
                "subtitle": "Settle your standing with Mistress Halda and Clerk Fen in the market square.",
                "color": "#ebb963",
                "done": "ch1_square" in visited_nodes,
                "cost": 1,
            },
            {
                "id": "node_broken_shrine",
                "title": "Vandalized Shrine of the Third Dawn",
                "tag": "SECRET EXPLORATION • Environmental Mystery",
                "subtitle": "An overgrown monument at the salt-wall edge that townsfolk deliberately ignore.",
                "color": "#7ec876",
                "done": "ch1_shrine" in visited_nodes,
                "cost": 1,
            },
        ]
        ch1_can_advance = len(visited_nodes) >= 1 or hub_actions_left <= 0

    call screen exploration_hub(
        "Thornwick Charter Town",
        "Spend time getting to know the frontier, mending gear, and uncovering hidden history before dusk.",
        ch1_nodes,
        ch1_can_advance,
        "Head to the Old Aqueduct (Dusk)"
    )

    $ chosen_node = _return

    if chosen_node == "__ADVANCE__":
        jump ch1_aqueduct_climax
    elif chosen_node == "node_inn_bram":
        $ visited_nodes.add("ch1_inn")
        $ hub_actions_left -= 1
        call ch1_scene_inn_bram
        jump ch1_thornwick_hub
    elif chosen_node == "node_conservatory_work":
        $ visited_nodes.add("ch1_conservatory")
        $ hub_actions_left -= 1
        call ch1_scene_conservatory
        jump ch1_thornwick_hub
    elif chosen_node == "node_square_ovens":
        $ visited_nodes.add("ch1_square")
        $ hub_actions_left -= 1
        call ch1_scene_square
        jump ch1_thornwick_hub
    elif chosen_node == "node_broken_shrine":
        $ visited_nodes.add("ch1_shrine")
        $ hub_actions_left -= 1
        call ch1_scene_shrine
        jump ch1_thornwick_hub
    else:
        jump ch1_aqueduct_climax


## HUB SCENE 1A: THE CROOKED LANTERN INN (BRAM) -------------------------------
label ch1_scene_inn_bram:
    $ current_location_name = "The Crooked Lantern Inn"
    scene bg crooked_lantern_inn
    with Dissolve(0.5)

    show leo neutral at stage_left
    show bram grin at stage_right
    with Dissolve(0.3)

    bram "Aha! The human question-mark wanders into my kitchen! Apron's on the peg—grab that paring knife and skin six bulbs of black garlic before the stock boils!"
    leo "Wait, isn't a Vanguard shield-bearer supposed to be sharpening greatswords or brooding in a corner booth?"
    bram "Brooding doesn't keep twenty cold masons alive on night-watch, Leo! Bad soup kills morale faster than goblins!"

    narrator "For ten surprisingly peaceful minutes, we chop root vegetables side by side—until an iron grain-chute slams shut in the cellar below with a deafening {i}BOOM{/i}."
    play sound audio.sfx_strike
    with vpunch

    show bram shaken at stage_right, tremble
    narrator "Bram's paring knife clatters onto the butcher block. Both of his huge hands grip the edge of the table, knuckles chalk-white, chest heaving as his chipped left horn hums with sub-audible panic."

    menu:
        "Don't stare or make a scene—quietly slide a mug of cool water next to his elbow and count four-second breaths out loud.":
            $ change_stat("empathy", 1, "Recognized a panic spike from your own sleepless nights.")
            $ change_affinity("bram", 3, "Never forgot that you didn't humiliate him.")
            $ set_flag("bram_opened_up")
            $ unlock_achievement("ach_stew_brother")
            leo "In for four... hold four... out for six. It was just the grain chute in the cellar, Bram. Ceiling's solid oak."
            narrator "Ten seconds pass. Slowly, Bram's shoulders drop. He takes a shaky swig of water and wipes his brow with his forearm."
            show bram neutral at stage_right
            bram "...How'd an office shrimp know breath-pacing?"
            leo "Try riding a crowded subway car when you haven't slept in thirty hours. Panic's panic, horns or not."
            bram "Heh. Bastion Mine collapse, two winters back. Held a timber beam on my horn till the rookies crawled clear, then froze cold for an hour after. Vigil called it 'unfit nerves.'"
            bram "Thanks for not gawking, Leo. Here—take an extra ration pack for tonight."
            $ add_item("iron_stew", 1)

        "Clap his shoulder firmly and haul the heavy stockpot off the boil myself so it doesn't scorch.":
            $ change_stat("strength", 1, "Hauled a forty-pound cast-iron stockpot!")
            $ change_affinity("bram", 2, "Saved the night-watch broth without fuss.")
            show leo resolute at stage_left
            narrator "My forearms scream in protest, but I wrestle the forty-pound iron pot onto the trivet before the barley burns."
            show bram grin at stage_right
            bram "Ha! Saved the broth! Sorry about that—loud cellar bangs still rattle my horn-nerves from my Vigil days. You've got decent grip strength when you forget to overthink!"
            $ add_item("iron_stew", 1)

    $ complete_quest("cq_bram_skillet", "Prepped night-watch stew and earned Bram's trust.")
    return


## HUB SCENE 1B: CONSERVATORY WORKBENCH (VESPERA & ORIN) ----------------------
label ch1_scene_conservatory:
    $ current_location_name = "Conservatory Workbench"
    scene bg orin_conservatory
    play music audio.bgm_conservatory fadein 0.8
    with Dissolve(0.5)

    show vespera neutral at stage_right
    show orin neutral at stage_left
    with Dissolve(0.3)

    narrator "At the potting bench, Vespera holds magnifying goggles over one eye while threading molten silver-solder along her astrolabe's outer ring. Beside her lies a stack of parchment covered in fierce ink strikethroughs."

    vespera "Steady the Vernier dial for me, Leo. Three millimeters clockwise—don't sneeze."

    $ change_stat("intelligence", 1, "Learned harmonic ring tolerances from Vespera.")
    $ add_item("recall_astrolabe", 1)
    $ complete_quest("sq_astrolabe_mend", "Calibrated Vespera's Recall Astrolabe.")

    narrator "The brass rings chime in clear, resonant fifths. As Vespera tests the latch, I glance at Master Orin's crossed-out poem: {i}'The Lay of the Fifth Dawn.'{/i}"
    orin "You're looking at my old sin, lad. Forty years ago, my verses convinced a baker's daughter from Eastford that dying gloriously at seventeen was nobler than growing gray."
    show orin solemn at stage_left
    orin "When you face that seam tonight, promise me something: do not try to look impressive. Try to come back for breakfast."

    $ set_flag("orin_opened_up")
    $ change_affinity("orin", 2, "Listened to the lesson behind his crossed-out ballads.")
    $ change_affinity("vespera", 1, "Helped repair her Recall Astrolabe.")
    $ add_item("meadow_tea", 1)
    $ complete_quest("cq_orin_ballad", "Learned why Master Orin stopped writing heroic ballads.")
    return


## HUB SCENE 1C: TOWN OVENS & WEIGH-STATION -----------------------------------
label ch1_scene_square:
    $ current_location_name = "Thornwick Ovens"
    scene bg thornwick_square
    with Dissolve(0.5)

    show leo neutral at stage_left
    with Dissolve(0.3)

    baker "You're the Outworlder who didn't blow up my chimney! Come here—either stack those salt-insulated kiln bricks, or check Fen's grain tallies before the Concordat tax-rider cheats us again!"

    menu:
        "Roll up my sleeves and haul kiln bricks alongside the apprentice masons (+Strength, +Reputation).":
            $ change_stat("strength", 1, "Stacked kiln stone until your palms toughened.")
            $ change_stat("reputation", 2, "Worked an honest afternoon shift in Thornwick.")
            $ change_crowns(45, "Kiln labor wages + waived citation!")
            narrator "By the twentieth brick, dust coats my eyebrows and my back aches—a clean, honest ache completely different from hunching over spreadsheets."
            baker "Ha! Slow as an ox, twice as careful! Clerk Fen, tear up his ticket and pay the boy five crowns on top!"

        "Audit Clerk Fen's Concordat grain-tithe ledger with six years of spreadsheet muscle memory (+Intelligence, +Charisma).":
            $ change_stat("intelligence", 1, "Spotted duplicate tare-weight deductions in three minutes.")
            $ change_stat("charisma", 1, "Explained tax fraud politely enough that Fen beamed.")
            $ change_stat("reputation", 2, "Saved Thornwick's bakers thirty crowns in overcharges.")
            $ change_crowns(50, "Municipal audit bounty!")
            leo "Hold on—row fourteen double-counts sack weight on wet barley. You've been overpaying the eastern capital by eleven percent."
            clerk "Eleven—?! Sweet merciful mortar! Mistress Halda, give this Outworlder a loaf and fifty brass crowns!"

    $ unlock_codex("codex_concordat", silent=True)
    $ complete_quest("sq_turnip_ordinance", "Earned honest wages and civic respect in Thornwick.")
    return


## HUB SCENE 1D: VANDALIZED SHRINE (HIDDEN CLOVER #1) -------------------------
label ch1_scene_shrine:
    $ current_location_name = "Edge of the Salt Wall"
    scene bg salt_ruins
    with Dissolve(0.5)

    show leo neutral at stage_center
    with Dissolve(0.3)

    narrator "Just outside Thornwick's western drainage wall stands a headless marble pedestal labeled {i}PARAGON III — DELIVERER OF THE IRON VALE{/i}. Someone has hung wet laundry line from its sword-hilt."
    narrator "Crouching to inspect the cracked base, I notice tiny English block letters scratched upside-down beneath the plinth—completely invisible unless you're kneeling at mud-level."

    thought "Wait... that's modern ballpoint script carved into stone: 'IF YOU'RE READING THIS DOWN IN THE DIRT, CHECK BEHIND THE LOOSE BRICK.'"

    narrator "My heart thumps. I pry free a moss-wedged stone and pull out a small mica-glass locket holding a four-hundred-year-old pressed three-leaf clover."
    $ add_item("pressed_clover", 1)
    $ register_clover_relic("Third Paragon's Plinth")
    $ change_tether(5, "Found proof another homesick human stood right here.")

    thought "'Don't forget to go home when the rain stops.' Whoever the First Outworlder was... they missed Earth too."
    return


## ============================================================================
## CHAPTER 1 CLIMAX: CRISIS AT THE OLD AQUEDUCT (ASTROLABE MINI-GAME)
## ============================================================================
label ch1_aqueduct_climax:
    stop music fadeout 0.8
    play music audio.bgm_combat fadein 1.0
    $ current_location_name = "Old Aqueduct • Dusk"

    scene bg old_aqueduct
    with Dissolve(0.8)

    play sound audio.sfx_rift
    with vpunch

    narrator "At the base of Thornwick's stone aqueduct, violet-white lightning spiderwebs out of a fractured drainage arch! Everywhere the mist touches wet grass along the canal bank, green blades stiffen into brittle white salt."

    show vespera sharp at stage_right
    show bram fierce at stage_left
    with Dissolve(0.3)

    bram "Back from the bank, masons! Shieldline up! Vespera, the seam's pulsing twice as hard as last week—if that wave hits the grain terraces, Thornwick starves by winter!"
    vespera "I see it! The harmonic pressure's splitting three ways—I can hold the copper leads open, but somebody with zero Resonance bleed has to lock the three astrolabe rings on beat!"
    vespera "Leo! Get your question-mark spine over here and plant Orin's spade in the conduit!"

    show leo resolute at stage_center
    with Dissolve(0.25)

    thought "My knees are shaking so hard my dryer token is jingling in my pocket. Every instinct from twenty-six years says step back and let the real adults handle it."
    thought "No. Bram's holding a hundred pounds of iron against burning salt-wind. Vespera's wrists are bleeding crystal dust. Breathe in four—and LOCK THE RINGS!"

    $ init_astrolabe_game()
    call screen astrolabe_minigame("Aqueduct Resonance Rupture")
    $ seal_result = _return

    if seal_result == "perfect":
        $ unlock_achievement("ach_harmonic")
        $ change_stat("courage", 2, "Locked all three harmonic rings without flinching!")
        $ change_stat("reputation", 3, "Saved the Aqueduct terraces cleanly!")
        $ change_affinity("vespera", 2, "Stunned by your dead-calm calibration.")
        $ change_affinity("bram", 2, "Cheered loud enough to rattle the arches.")
        play sound audio.sfx_heal
        with flash_astral

        narrator "{i}CLANG—HUMMM.{/i} All three brass rings snap into alignment on the first pass! Copper wire along Orin's spade glows warm amber, drinking the violent purple arc straight down into deep granite until only harmless steam rises off the canal!"
        show bram grin at stage_left, hop
        bram "WOOO! DID YOU SEE THAT?! Not a single turnip salted! Have my babies—wait, no, have my second-best skillet, string-bean!"
        show vespera soft at stage_right
        vespera "...Three rings, zero backlash. Okay, Sato. Maybe my astrolabe didn't miss after all."

    elif seal_result == "stabilized":
        $ change_stat("courage", 1, "Held your ground until the seam sealed!")
        $ change_stat("reputation", 2, "Helped ground the Old Aqueduct rupture.")
        $ change_affinity("vespera", 1, "Got the job done under fire.")
        $ change_affinity("bram", 1, "Held the line together.")
        play sound audio.sfx_heal
        with flash_astral

        narrator "Sparks singe my knuckles on the second ring, nearly bucking the spade out of my grip—but I jam my heel into the mud, brace against Bram's shoulder, and slam the final brass latch home!"
        narrator "The violet shriek collapses into harmless steam. My hands won't stop trembling, and smell faintly of toasted wool—but the canal water runs clear."
        show bram grin at stage_left
        bram "Ha! Ugly stance, crooked elbows, ten-out-of-ten finish! Look—the grass on the terrace is still green!"

    else:
        # Overload fallback — dramatic sacrifice/teamwork consequence, story continues organically!
        $ change_stat("courage", 1, "Refused to let go even when the seal bucked!")
        $ change_stat("reputation", 1, "Took the brunt of the discharge with Bram.")
        $ restore_vitality(hp_gain=-25, focus_gain=-15, silent=True)
        $ change_tether(-5, "Resonance static grazed your memories during the backlash.")
        with flash_crimson

        narrator "The third ring slips—violet static explodes across the arch! Rather than dive clear and let the wave hit the terraces, I throw my weight over the copper spade while Bram slams his tower shield over us both!"
        narrator "For one terrifying second I forget the name of my elementary school—then Vespera kicks the emergency ground-spike home, snuffing the rift in a cloud of white steam."
        show vespera tired at stage_right
        vespera "Idiot! You took half that arc through your ribs instead of letting go! ...Drink some water. You kept the terraces green."

    $ complete_quest("mq_01_audit", "Grounded the Old Aqueduct rupture before Thornwick's fields calcified.")

    ## CLIFFHANGER: ARRIVAL OF SERAPHINA & MARSHAL CASSIAN --------------------
    stop music fadeout 1.2
    play ambience audio.amb_wind fadein 1.0

    narrator "For a moment, the masons along the canal bank actually cheer—tossing caps in the air, clapping soot off Bram's armored shoulders, even nodding warmly at my mud-splattered sneakers."
    thought "Wait. Nobody's laughing. Nobody's calling me Sir Valorian. My hands hurt, my shoes are soaked, and... I actually helped."

    narrator "Then three silver war-horns split the twilight from the northern ridge."
    play music audio.bgm_mystery fadein 1.5

    hide bram
    show leo nervous at stage_left
    show vespera sharp at stage_center
    with Dissolve(0.3)

    vespera "...No. Not already. Those are Aurelian Concordat pennants—and Ashen Vigil outriders."

    show sera proud at stage_right
    with Dissolve(0.5)

    $ meet_character("sera")
    $ meet_character("cassian")
    $ unlock_codex("codex_vigil", silent=True)

    narrator "Down the stone causeway strides a young woman in an immaculate cobalt-and-silver envoy coat, starlight motes orbiting her fingertips effortless and blinding—flanked by a tall, silver-templed commander whose grey cloak smells of northern salt-storms."
    narrator "She glances once at the smoking copper spade in my muddy hands, then speaks—in crisp, unmistakable twenty-first-century English."

    sera "You've got to be kidding me, Marshal. {i}This{/i} is the anomalous tether signature from Tuesday night? He looks like he apologizes to automatic doors."

    hide vespera
    show cassian neutral at stage_center
    with Dissolve(0.35)

    cassian "Forgive Envoy Lin's bluntness, Master Sato. I am High Marshal Cassian Vey of the Ashen Vigil."
    cassian "Three hours ago, the Sixth Paragon's seal at Fort Bastion fractured by forty cubits. Whether by fate or Broker Kael's meddling... Cindervale is out of time."

    $ start_quest("mq_02_envoy", "Confront Envoy Seraphina Lin and High Marshal Cassian Vey in Chapter 2.")
    pause 0.6
    return
