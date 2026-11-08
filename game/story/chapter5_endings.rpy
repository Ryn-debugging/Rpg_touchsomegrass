## ============================================================================
## story/chapter5_endings.rpy — CHAPTER 5: "Where the Grass Still Grows"
## Climax Decision & Four Complete Earned Endings + Final Window Reflection
## ============================================================================

label chapter5_start:
    $ current_chapter_title = "Chapter 5: Where the Grass Still Grows"
    $ current_location_name = "Summit of the Crucible"

    call screen chapter_title_card(
        "FINAL CHAPTER",
        "Where the Grass Still Grows",
        "\"A hero is an emergency, lad, like a tourniquet. What a wounded world truly needs is someone willing to tend the soil after.\""
    )

    # If Leo already surrendered to Resonance burnout or seized the Crown early, route to Tragic Climax
    if has_flag("chose_crown_early") or resonance_load >= 55 or tether < 25:
        jump ending_tragic_pillar

    play music audio.bgm_crucible if_changed fadein 1.0
    scene cg crucible_climax
    with flash_astral

    narrator "Lightning hammers the obsidian summit! Bram locks his tower shield into the fractured rock; Vespera bolts the First-Era Calibration Plate across the roaring conduit while her brass astrolabe spins at white-hot velocity!"
    narrator "In my hands vibrates Master Orin's copper-veined spade—the final grounding pin between four hundred years of stored grief and deep living bedrock."

    vespera "LEO! We've got the primary surge bled into Thornwick's copper grid—the valley's going to hold! {i}BUT{/i} the interworld Recall Seam is collapsing behind it!"
    vespera "Listen to me! Once you drive that spade home, the Crucible shuts down! There's enough residual charge for {b}ONE{/b} clean Recall jump back to Earth—unless..."

    if clover_relics_found >= 3 and has_item("recall_astrolabe") and has_flag("trauma_integrated") and tether >= 60:
        vespera "WAIT—your satchel! Those three First-Era Clovers are resonating with my soldered astrolabe at the exact frequency of Orin's Conservatory meadow!"
        orin "Sweet roots below... E. Marrow's Twin-Root Bypass! Leo—if you harmonize the Clovers with the spade, you can dismantle the Summoning Engine forever AND open a gentle dual-return seam for {i}both{/i} Outworlders!"

    narrator "Wind howls across the spire. Everything I was as a lonely kid in the mud, everything I feared in Apartment 4B, and everyone standing beside me now narrows to a single heartbeat."

    menu:
        "{font=fonts/DejaVuSans.ttf}★{/font} (Secret True Path) Harmonize all 3 Forgotten Clovers & the Calibrated Astrolabe: Dismantle the Engine and open the Twin-Root Doors!" if (clover_relics_found >= 3 and has_item("recall_astrolabe") and has_flag("trauma_integrated") and tether >= 60):
            jump ending_secret_two_doors

        "(Hopeful Path) Drive the copper spade into bedrock with everyone together—then take Vespera's Recall home to live my real life!" if tether >= 45:
            jump ending_hopeful_grass

        "(Bittersweet Path) Clip my brass Earth-anchor onto Seraphina's coat so she makes it home to her mom—and stay behind in Solvara to help rebuild.":
            jump ending_bittersweet_gardener

        "(Tragic Temptation) Let go of the spade and step into the Crucible's golden fire—become the invincible Seventh Hero so no threat ever touches them again.":
            jump ending_tragic_pillar


## ============================================================================
## ENDING I (HOPEFUL): "WHERE THE GRASS STILL GROWS"
## ============================================================================
label ending_hopeful_grass:
    $ current_chapter_title = "Epilogue: Where the Grass Still Grows"
    play sound audio.sfx_astrolabe
    scene cg crucible_climax
    with flash_meadow

    leo "NOBODY TURNS INTO SALT TONIGHT! ON THREE, BRAM—ONE, TWO, GROUND IT!"
    narrator "Together—my muddy sneakers, Bram's armored boot, Vespera's scarred hands, Seraphina's steadying grip, Cassian's gauntleted fist, and forty frontier masons holding the copper line down the mountain—we drive the grounding pin straight into Solvara's living stone!"
    narrator "No city-flattening explosion. No Latin choir. Just a deep, resonant bell-tone like rain soaking into parched earth as the violet storm unravels into warm silver mist."

    stop ambience fadeout 1.5
    stop music fadeout 1.5
    play music audio.bgm_epilogue fadein 2.0

    scene bg salt_ruins
    with Dissolve(1.2)

    $ current_location_name = "Cindervale Ridge • Dawn"
    show vespera soft at stage_left
    show bram grin at stage_center
    show orin smile at stage_right
    with Dissolve(0.5)

    narrator "With the Crucible's parasitic draw broken—and Marshal Cassian's Vigil already laying permanent Rootwarden conduits along Bastion—the last shimmering puddle-seam hovers six inches above the ridge."
    narrator "Sera has already been cleared by Orin's second Concordat mirror to return to Chicago next full moon, her memories of Mei-Ling intact. My turn is right now: forty seconds before the puddle closes."

    bram "Oi! Don't you dare slouch when you get back there, Leo Sato! Eat hot stew! Lift something heavier than a pencil twice a week!"
    orin "Remember, lad: courage isn't the absence of shaking knees. It's showing up anyway."

    narrator "I pull my taped-together fourth-grade {i}Chronicles of Sir Valorian{/i} sketchbook out of my pocket and press it into Vespera's hands."
    leo "Keep this in the Conservatory for me. I don't think I need Sir Valorian anymore."
    vespera "...Idiot. Half these drawings don't even have proper elbow joints."
    narrator "Her voice cracks on the last word. She steps forward, taps my collarbone lightly with her brass astrolabe, and gives me a real, unguarded smile."
    vespera "Go home, Leo. Breathe through your nose."

    scene black
    with flash_white
    pause 0.8

    ## EARTH RETURN — DAWN PARK
    $ hud_visible = False
    play ambience audio.amb_birds fadein 1.8
    scene bg rainy_alley
    with Dissolve(1.2)

    narrator "6:12 AM. Eastside Coin Laundry."
    narrator "Rain has stopped. Through the glass, Dryer #4 sits quiet, my gray hoodie neatly folded on top by an early-shift grandmother. My knees still click when I stand up. My checking account still has forty-three dollars and eighteen cents."
    narrator "Half a block toward Apartment 4B, a middle-school kid in an oversized backpack trips on the curb—scattering tangerines and geometry flashcards across the wet sidewalk while two older boys by the bus stop snicker and pull out their phones."

    play sound audio.sfx_heartbeat
    narrator "My stomach knots automatically. Old muscle memory whispers: {i}Cross the street. Don't make eye contact.{/i}"
    narrator "No sword. No copper spade. Just me in a damp olive windbreaker."
    narrator "I walk right over, crouch down beside the kid, and start gathering tangerines."

    leo "Hey—none of 'em split open. Here's your protractor. You good?"
    kid "...Y-yeah. Thanks, mister."
    narrator "I glance calmly up at the two teenagers by the bus shelter. My hands tremble maybe half a millimeter—and they mutter, pocket their phones, and look away."

    scene cg morning_grass
    with Dissolve(1.5)

    narrator "On the walk back, instead of climbing straight up to Apartment 4B, I turn into the small neighborhood park at the corner."
    narrator "Morning sun breaks warm and gold across the apartment rooftops. I set my backpack on the wet bench, untie my worn canvas sneakers, and step barefoot onto the cool, dewy green clover."
    narrator "Tomorrow I'll call my mom back—and tell her the truth this time. Maybe apply for that municipal forestry crew posting downtown."
    narrator "There are no dragons out here."
    narrator "Just cold morning dew between my toes, sunlight on my face, and a whole real life still waiting to be lived."

    $ unlock_achievement("ach_end_hopeful")
    call final_window_reflection("ENDING I OF IV — WHERE THE GRASS STILL GROWS (Hopeful Ending)")
    return


## ============================================================================
## ENDING II (BITTERSWEET): "THE QUIET GARDENER OF THORNWICK"
## ============================================================================
label ending_bittersweet_gardener:
    $ current_chapter_title = "Epilogue: The Quiet Gardener"
    play sound audio.sfx_astrolabe
    scene cg crucible_climax
    with flash_meadow

    narrator "As the copper spade locks into bedrock and the storm breaks into silver mist, Vespera's astrolabe screams a warning—only {i}one{/i} Earth-tether slot remains stable before the Recall ring fuses shut forever!"
    narrator "Five feet away, Seraphina clutches her temples, whispering 'Mei-Ling, Mei-Ling' under her breath in terror that one more week in Solvara will steal her mother's face again."

    leo "Vespera—lock the return ring onto Sera!"
    vespera "Leo, wait—if I fire my last silver lens on her coordinates, this seam seals permanent! There won't {i}be{/i} another puddle back to your apartment!"
    leo "My mom knows my voice, Vespera. Sera's about to lose hers. Send her home!"

    stop ambience fadeout 1.5
    stop music fadeout 1.5
    play music audio.bgm_conservatory fadein 2.0

    scene bg orin_conservatory
    with flash_white

    $ hud_visible = False
    narrator "Before Seraphina vanishes into the warm rain-scented light, I press my brass Eastside Laundromat token into her palm—with my mother's phone number scribbled on a slip of sketchbook paper—asking her to send one postcard saying I found good work in a quiet town."

    narrator "Three autumns pass in Cindervale."

    scene cg conservatory_clover
    with Dissolve(1.4)

    narrator "Nobody in Thornwick calls me 'Sir Leo' or sings ballads when I walk through Charter Square. Honestly, Clerk Fen still audits my compost receipts twice a month."
    narrator "Sometimes late on rainy Tuesday nights, lying awake above the Crooked Lantern, a quiet ache settles in my chest for fluorescent convenience stores, the hum of refrigerators, and a small kitchen table on a world I can never walk back to."
    narrator "Then morning comes."

    scene bg thornwick_square
    with Dissolve(1.0)

    show vespera soft at stage_left
    show bram grin at stage_center
    show orin smile at stage_right
    with Dissolve(0.4)

    bram "OI, LEO! Quit daydreaming in the clover bed—Halda's pulling rye loaves out of Oven Two and Vespera made chicory that's actually drinkable!"
    vespera "Ignore the horned slander, Gardener. Come on—that western salt-acre past my father's survey stake sprouted three new inches of green fescue overnight."

    narrator "I brush dark, living soil off my knees, sling Orin's worn copper spade over my shoulder, and walk down into town beside the people I chose."
    narrator "I never became a legendary hero."
    narrator "I became a neighbor. And five miles west of Thornwick, where dead white salt stood for twenty years, the grass is growing back."

    $ unlock_achievement("ach_end_bittersweet")
    call final_window_reflection("ENDING II OF IV — THE QUIET GARDENER OF THORNWICK (Bittersweet Ending)")
    return


## ============================================================================
## ENDING III (TRAGIC): "THE SEVENTH PILLAR OF SALT"
## ============================================================================
label ending_tragic_pillar:
    $ current_chapter_title = "Epilogue: The Seventh Pillar"
    stop music fadeout 0.6
    play sound audio.sfx_rift
    play music audio.bgm_crucible fadein 1.0

    scene bg crucible_spire
    with flash_astral

    narrator "No more shaking knees. No more being small, ordinary, forgettable Leo Sato."
    narrator "Letting Master Orin's wooden spade clatter onto the rock, I step straight across the threshold into the roaring golden heart of the Crucible of Crowns."

    vespera "LEO! GRAB MY HAND—GET OUT OF THE RING!"

    narrator "For ten glorious, intoxicating seconds, my nine-year-old dream comes completely true."
    narrator "Blinding celestial armor weaves itself across my shoulders! Strength beyond every ballad floods my veins! Down along the Bastion cliffs, three thousand Ashen Vigil soldiers drop to their knees in awe as a single sweep of my radiant hand vaporizes the entire Hollow Tide from horizon to horizon!"

    thought "Look at me, Marcus. Look at me, everybody. Nobody can ever laugh at me again."
    thought "...Wait. Who was Marcus?"

    play sound audio.sfx_heartbeat
    with flash_white

    narrator "Something warm slips out of my chest like sand through torn pockets."
    thought "Wait—Apartment 4B. No, 4... something. There was a girl with scarred wrists shouting my name. What was her name? Vespera? Why is she crying?"

    $ leo_display_name = "The Seventh Paragon"

    leo "FEAR NOT, CITIZENS OF CINDERVALE. THE DELIVERANCE IS COMPLETE."
    thought "That wasn't my voice. Wait—what did grass smell like? Mom? Hold on, please, give me back just one—"

    stop music fadeout 2.0
    play ambience audio.amb_wind fadein 1.5
    scene bg salt_ruins
    with Fade(0.8, 1.0, 1.5, color="#ffffff")

    $ hud_visible = False
    show vespera tired at stage_center
    with Dissolve(0.6)

    narrator "Northern Cindervale is saved."
    narrator "Where the Hollow Seam once tore the sky stands a two-hundred-foot monument of silent, radiant white salt-crystal—armored, winged, flawless, and utterly still."
    narrator "Every spring, Concordat pilgrims lay gilded wreaths at its base and sing hymns to the Glorious Seventh Paragon."
    narrator "Only Vespera Kael comes alone in the rain, setting an old taped-together paper notebook and a cheap brass laundry token against the cold crystal heel of a statue that can no longer hear her."

    vespera "...Told you not to breathe through your mouth, idiot."

    $ unlock_achievement("ach_end_tragic")
    call final_window_reflection("ENDING III OF IV — THE SEVENTH PILLAR OF SALT (Tragic Ending)")
    return


## ============================================================================
## ENDING IV (SECRET TRUE ENDING): "THE TWO DOORS (TOUCH SOME GRASS)"
## ============================================================================
label ending_secret_two_doors:
    $ current_chapter_title = "True Epilogue: The Two Doors"
    play sound audio.sfx_astrolabe
    scene cg crucible_climax
    with flash_meadow

    leo "Vespera—clip all three First-Era Clovers into the outer ring! Orin, open the Conservatory sluice! Bram, Sera, Marshal—ON ME!"
    narrator "Instead of shattering the sky or demanding a martyr, E. Marrow's four-hundred-year-old botanical cipher sings through the copper array in a warm emerald wave!"
    narrator "Across the summit, the predatory Choir Summoning Engine cracks down its golden spine—dissolving forever so no lonely daydreamer on Earth can ever be harvested as fuel again—while the stolen Verdance pours back down the mountainside like warm spring rain!"

    stop ambience fadeout 1.2
    stop music fadeout 1.2
    play music audio.bgm_epilogue fadein 2.0

    scene bg thornwick_square
    with flash_meadow

    $ hud_visible = False
    show vespera soft at stage_left
    show bram grin at stage_center
    show cassian neutral at stage_right
    with Dissolve(0.5)

    narrator "Along the salt-cliffs of Thornwick, masons freeze in disbelief as pale green shoots of wild clover push up through twenty-year-old white crust."
    cassian "...Four centuries of war, ended with copper drainage wire and three weeds. Master Orin—the Ashen Vigil is hereby transferring its charter to agricultural reconstruction."
    bram "WHICH MEANS YOU'RE ALL EATING MY GARLIC BARLEY STEW TONIGHT BEFORE YOU GO HOME!"

    narrator "Because the Twin-Root Bypass harmonized gently with Master Orin's Conservatory, nobody gets left behind: both Seraphina and I walk calmly through the warm cedar-framed seam the next morning—carrying all our memories, and leaving behind a tiny six-inch 'Postbox Seam' beneath Orin's potting bench."

    scene bg earth_dawn_park
    with Dissolve(1.4)

    play ambience audio.amb_birds fadein 1.5
    show leo warm at stage_left
    show sera neutral at stage_right
    with Dissolve(0.4)

    narrator "Six months later. Saturday, 7:30 AM. Eastside Community Garden, Earth."
    narrator "I still get nervous before phone interviews. My left knee still clicks on stairs. Last month I stuttered asking the hardware-store guy where the trowels were—and survived."

    sera "Unbelievable, Sato. I take an early train all the way from campus with real lemon scones my mom baked, and you've already got potting soil on your glasses."
    leo "Hey, respect the uniform, Sera. Check underneath the third terracotta pot by the rosemary bed."

    narrator "Beside a thriving patch of white three-leaf clover sits a small waxed-parchment envelope smelling faintly of toasted cumin and silver-solder:"
    narrator "{i}'Question-Mark & Starlight: Ditch B passed inspection. Twenty acres of Oakhaven grew real apple blossoms this week. Bram says peel your garlic properly, and Orin says step outside before noon. — V.K.'{/i}"

    scene cg morning_grass
    with Dissolve(1.5)

    narrator "I kick off my canvas sneakers beside the wooden bench, step barefoot into the cool morning grass, and breathe in the smell of wet earth, coffee, and ordinary sunlight."
    narrator "Childhood me wanted a magic world because the real one hurt too much."
    narrator "Adult me knows a better secret: the real world isn't finished yet—and you don't need a legendary sword to show up for it."

    $ unlock_achievement("ach_end_secret")
    call final_window_reflection("SECRET TRUE ENDING — THE TWO DOORS (Touch Some Grass)")
    return


## ============================================================================
## FINAL QUIET PLAYER REFLECTION SCREEN
## ============================================================================
label final_window_reflection(ending_banner_text):
    stop ambience fadeout 2.5
    scene black
    with Dissolve(1.8)

    pause 0.6
    centered "{color=#ebb963}{font=fonts/LiberationSerif-Bold.ttf}{size=28}[ending_banner_text!t]{/size}{/font}{/color}"
    pause 0.4
    centered "{color=#cbd8e2}{size=21}Thank you for playing {i}Where the Grass Still Grows{/i}.{/size}{/color}"
    centered "{color=#9eb4c4}{size=19}Before starting another route—or moving on to your next tab—\ntake ten quiet seconds.{/size}{/color}"
    centered "{color=#7ec876}{font=fonts/LiberationSerif-Italic.ttf}{size=22}Look out your window.\nDrink a glass of water.\nThere is still a real world waiting outside for you.{/size}{/font}{/color}"

    stop music fadeout 2.5
    pause 1.0
    return
