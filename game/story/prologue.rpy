## ============================================================================
## story/prologue.rpy — PROLOGUE: "Fluorescent Rain"
## ============================================================================

label prologue_start:
    $ current_chapter_title = "Prologue: Fluorescent Rain"
    $ current_location_name = "Eastside Elementary (17 Years Ago)"

    scene black
    with Dissolve(0.8)

    call screen chapter_title_card(
        "PROLOGUE",
        "Fluorescent Rain",
        "\"Before I knew the word 'escapism,' I just knew the mud smelled better if you pretended it was a battlefield.\""
    )

    play ambience audio.amb_rain fadein 1.5
    scene bg childhood_bleachers
    with Dissolve(1.2)

    narrator "Wet clover has a very specific taste when someone shoves your chin into it."
    narrator "Bitter. Like chewed dandelion stems and rusted chain-link fence."

    play sound audio.sfx_strike
    with vpunch

    marcus "Hey, look at page twelve! 'Sir Valorian of the Dawn!' Did you draw yourself with abs, Sato? You can't even climb the gym rope!"

    narrator "Laughter cracks overhead—three sixth-graders standing dry under the aluminum bleachers while October rain drips off their sneaker soles onto the back of my neck."
    narrator "Paper tears. A slow, deliberate {i}riiiip{/i}."
    narrator "A crayon-gold cape flutters down into a puddle beside my nose and immediately turns soggy gray."

    thought "Don't cry. If your shoulders shake, they stay another five minutes. That's the rule. Statues don't get kicked twice."

    marcus "C'mon, leave it. My mom's picking us up. Later, 'Sir Valorian.'"

    narrator "Their footsteps splash away across the gravel lot. Nobody from the faculty room looks out the frosted window. Nobody ever does."
    narrator "I stay flat in the crushed clover for another sixty seconds, counting raindrops until my breathing stops stuttering, then reach out with mud-caked fingers to rescue the torn page."

    menu:
        "Smooth the torn paper cape carefully onto my knee. \"Someday I'll be strong enough that nobody laughs.\"":
            $ set_flag("childhood_vow_power")
            $ change_stat("courage", 1, "Refused to throw the torn page away.", silent=True)
            thought "Someday, a door will open. A real sword. Real monsters you're actually allowed to swing at. Someday, I'm going to become a hero."

        "Count their footsteps and memorize which gate they took so I can walk home the long way.":
            $ set_flag("childhood_vow_watchful")
            $ change_stat("intelligence", 1, "Learned early to map exits and footsteps.", silent=True)
            thought "Heroes in books always know when an ambush is coming. Until I'm brave, I'll settle for noticing everything first."

        "Stare at a crushed earthworm in the mud and move it onto dry grass under the bench.":
            $ set_flag("childhood_vow_kindness")
            $ change_stat("empathy", 1, "Protected something smaller than yourself.", silent=True)
            thought "If a hero ever showed up here, they wouldn't just beat up Marcus. They'd sit down first and ask if your lip was bleeding."

    stop ambience fadeout 1.2
    scene black
    with chapter_wipe

    ## ------------------------------------------------------------------------
    ## SEVENTEEN YEARS LATER — APARTMENT 4B
    ## ------------------------------------------------------------------------
    $ current_location_name = "Apartment 4B • 2:14 AM"
    play music audio.bgm_apartment fadein 1.8
    play ambience audio.amb_rain fadein 1.5

    scene bg leo_apartment
    with Dissolve(1.2)

    narrator "Seventeen years later, the golden portal still hasn't opened."
    narrator "Unless you count the neon {b}24H MART{/b} sign across the alley, which flickers bright magenta through my blinds every four seconds like a dying mana crystal."

    show leo neutral at stage_center
    with Dissolve(0.35)

    thought "Okay. Let's review the heroism scoreboard at age twenty-six."
    thought "Dragons slain: zero. Kingdoms liberated: zero. Times today I rehearsed telling my shift supervisor he mispronounced my name for eight months before smiling and saying 'No worries!': three."

    show leo nervous at stage_center, sink_sigh
    narrator "On my folding desk sits a half-price convenience-store curry udon. Cold. Without chopsticks, because the teenaged clerk forgot to toss a pair in the bag and I didn't want to ruin his night by asking."
    narrator "Beside the udon sits a pink rent-adjustment notice, my night-shift moderation headset, and—tucked halfway under the radiator—that same taped-together fourth-grade sketchbook."

    menu:
        "Check my phone: an unread text from Mom asking if I'm eating vegetables.":
            $ change_tether(5, "Replied to Mom—even if it was a harmless white lie.", silent=True)
            $ change_stat("empathy", 1, "Kept a thread to someone who cares.", silent=True)
            show leo warm at stage_center
            narrator "I type out: {i}'Doing great! Made stew tonight.'{/i} Stare at the cold convenience-store udon in shame. Delete 'Made stew.' Send: {i}'Doing okay! Raining hard here, stay warm.'{/i}"
            thought "Not exactly Arthur pulling Caliburn from the anvil. Still, my chest feels slightly less like wet concrete."

        "Drop down and attempt twenty midnight push-ups to prove I haven't completely given up.":
            $ change_stat("strength", 1, "Nine and a half push-ups count as rounding up to ten.", silent=True)
            show leo resolute at stage_center
            narrator "One. Two. Three... By eight, my left shoulder clicks like a rusty stapler. At eleven, the floorboards groan and my downstairs neighbor taps a broom handle against the ceiling."
            show leo nervous at stage_center, flinch
            leo "S-sorry! Dropped a dictionary!"
            thought "Why did I apologize out loud to a plaster floor? Good lord, Leo."

        "Pull the battered hero sketchbook out from under the radiator for a minute.":
            $ change_stat("intelligence", 1, "Still remember every margin note.", silent=True)
            $ change_tether(3, "Held onto who you used to be.", silent=True)
            narrator "The crayon gold on 'Sir Valorian' has faded to mustard yellow. Somewhere around age nineteen, I started using the back pages for grocery math and electric bills."
            thought "It's embarrassing how stubbornly a stupid childhood wish hangs on. Like gum on the sole of your last decent pair of sneakers."

    narrator "Across the room, my laundry basket overflows with damp hoodies. If I don't dry at least one collared shirt before tomorrow's 9 AM video check-in, I'll look like an unmade bed with eyebags."
    narrator "I slip the battered sketchbook into my coat pocket—purely because the radiator pipe is leaking, obviously, no other reason—grab my last brass dryer token, and head downstairs."

    ## ------------------------------------------------------------------------
    ## THE LAUNDROMAT ALLEY & ABDUCTION
    ## ------------------------------------------------------------------------
    $ current_location_name = "Eastside Laundromat Alley"
    scene bg rainy_alley
    with Dissolve(0.9)

    show leo neutral at stage_left
    with Dissolve(0.3)

    narrator "2:38 AM. Rain needles the asphalt outside the Eastside Coin Laundry."
    narrator "Inside the steamed window, Dryer #4 tumbles my gray hoodie in hypnotic circles. Forty minutes to kill. Just me, a vending machine humming in B-flat, and a wide rainwater puddle reflecting the streetlamp."

    leo "Someday..."

    show leo nervous at stage_left
    thought "Did I just whisper 'Someday' at a storm drain? I need vitamins. Or sunlight. Possibly an exorcism."

    play sound audio.sfx_heartbeat
    narrator "Wait."
    narrator "The rain stops hitting the puddle."
    narrator "Not the sidewalk—rain is still drumming on my umbrella and soaking my cuffs—just that six-foot oval of dirty water by the curb. Every droplet striking its surface freezes mid-splash, hanging like glass beads on invisible wire."

    leo "...Okay. No. Hang on. Let me look left and right."
    narrator "Empty street. No runaway delivery van. No rogue bakery truck."
    leo "Good. Nobody's getting reincarnated by freight logistics tonight. I'm just sleep-deprived and walking steadily back inside—"

    play sound audio.sfx_rift
    stop music fadeout 0.4
    scene cg puddle_rift
    with flash_astral

    narrator "The puddle splits open like torn silk, exhaling a gale of bone-dry white salt and ozone!"
    narrator "A woman lunges upward out of the upside-down sky inside the asphalt—rain-slicked iron-buckled coat, soot-streaked cheek, wrist wrapped in scarred crystalline veins, clutching a spinning three-ring brass astrolabe that is actively throwing sparks."

    unknown_voice "Ha! Locked the tether! Peak heroic yearning at ninety-eight kelvins—come here, you glorious bastard, before the Concordat—"

    narrator "Her fingers clamp onto the front of my discount windbreaker. For half a second, our eyes meet."
    narrator "She looks at my wire-rimmed glasses. My plastic convenience-store bag. My posture."
    narrator "The triumphant grin vanishes from her face like chalk under a hose."

    unknown_voice "...Wait. Where's your armor?! Why are you holding a fabric-softener sheet?!"
    leo "I—excuse me, ma'am, you're standing in a pothole—"
    unknown_voice "Oh, gods damn my cheap solder! The beacon locked onto {i}daydreaming{/i}, not combat mass! Let go of my coat!"
    leo "YOU'RE HOLDING {i}MY{/i} COAT!"
    unknown_voice "Don't breathe through your mouth, shrimp-spine, the salt-shear will peel your tongue!"

    play sound audio.sfx_rift
    scene black
    with vpunch

    narrator "Gravity inverts."
    narrator "The neon {b}24H MART{/b} sign stretches into a thin violet thread overhead—and snaps."

    $ unlock_achievement("ach_kidnapped")
    pause 0.8
    return
