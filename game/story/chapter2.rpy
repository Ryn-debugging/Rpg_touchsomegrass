## ============================================================================
## story/chapter2.rpy — CHAPTER 2: "The Girl Who Forgot Rain"
## ============================================================================

label chapter2_start:
    stop ambience fadeout 1.0
    $ current_chapter_title = "Chapter 2: The Girl Who Forgot Rain"
    $ current_location_name = "Crooked Lantern War-Room"

    call screen chapter_title_card(
        "CHAPTER II",
        "The Girl Who Forgot Rain",
        "\"Nobody burns faster than someone terrified of what happens when the applause stops.\""
    )

    play music audio.bgm_mystery fadein 1.5
    scene bg crooked_lantern_inn
    with Dissolve(1.0)

    narrator "By nine o'clock, the Crooked Lantern's back parlor has been requisitioned into an impromptu war-room. Outside, Ashen Vigil sentries pace the wet cobbles in disciplined pairs."

    show cassian neutral at stage_left
    show sera neutral at stage_center
    show vespera sharp at stage_right
    with Dissolve(0.4)

    cassian "Look at the survey charcoal, Broker Kael. I am not here to arrest you for an unlicensed Recall, nor to fine Master Sato for his... unusual footwear."
    narrator "High Marshal Cassian Vey unrolls a salt-stained map of northern Cindervale. His voice isn't booming or theatrical; he sounds like an ER surgeon on hour thirty-six."
    cassian "Twenty years ago, I carried the Sixth Paragon's shield to Fort Bastion. I watched a nineteen-year-old boy from Osaka pour every memory in his skull into that cliffside so thirty thousand refugees could live."
    cassian "Tonight, that seal is failing. If the Hollow Tide breaks into the valley before winter, Thornwick and six charter villages vanish."

    vespera "And your brilliant solution from the Eastern Choir is to march {i}another{/i} twenty-one-year-old into the Crucible of Crowns?!"
    vespera "Look at Envoy Lin's hands, Marshal! Tell me she isn't already fraying!"

    show sera proud at stage_center, hop
    sera "Keep my hands out of your mouth, salt-smuggler. Unlike your desk-clerk mistake over there, I actually {i}chose{/i} to answer when Aurelia called."

    narrator "Seraphina reaches for a pewter mug of Master Orin's hot herbal water, pauses, and frowns faintly at the saucer."
    sera "Innkeeper—do you have a slice of... of that sour yellow citrus? From home. Round, dimpled peel, goes in hot tea when your throat hurts..."

    show sera fragile at stage_center
    narrator "Silence drops over the table like lead."
    narrator "Her fingers tighten around the porcelain handle until her knuckles blanch. Beside her collar, two tiny motes of silver Starlight flicker—and vanish."

    thought "She just forgot the word 'lemon.' She's twenty-one years old, speaking English, and the magic literally ate the word 'lemon' out of her head."

    sera "...Never mind. Plain water is fine."

    menu:
        "Quietly say, \"Lemon. With a spoonful of cheap honey in a chipped mug.\" (Without pity or smugness)":
            $ change_stat("empathy", 1, "Returned a stolen word without humiliating her.")
            $ change_affinity("sera", 2, "Startled that you didn't gloat.")
            $ change_affinity("cassian", 1, "Noted your quiet compassion.")
            leo "Lemon, Seraphina. Usually the plastic squeeze bottle shaped like one because real lemons go moldy in the crisper drawer."
            narrator "For half a heartbeat, Seraphina stares at me like a drowning swimmer spotting a pier—before her chin snaps back up."
            show sera neutral at stage_center
            sera "...Right. Lemon. Obviously. I've been speaking High Aurelian all week."

        "Confront Marshal Cassian directly: \"You see what that magic is doing to her! You can't feed another person to a furnace!\"":
            $ change_stat("courage", 1, "Stood up to a High Marshal of the Vigil.")
            $ change_affinity("vespera", 2, "Backed her argument without flinching.")
            $ change_affinity("cassian", 1, "Respected your moral spine—even while disagreeing.")
            show cassian weary at stage_left
            cassian "Do you think I sleep well, Master Sato? My late brother's eight-year-old daughter lives in Bastion Ward Three. Tell me what math saves both Envoy Lin {i}and{/i} thirty thousand sleeping families, and I will kneel to you myself."

        "Study Cassian's map and ask Vespera: \"Wait—if the Aqueduct copper-spade grounded a small seam, couldn't a bigger array ground Bastion?\"":
            $ change_stat("intelligence", 1, "Connected municipal Root-craft to the northern seal.")
            $ change_affinity("vespera", 1, "Followed her exact engineering hunch.")
            $ change_affinity("cassian", 1, "Intrigued by a practical question.")
            show vespera neutral at stage_right
            vespera "Give the clerk a gold star. If we had the First Era's Original Calibration Plate from the Sunken Archive, a distributed copper array {i}could{/i} bleed pressure off the Crucible without cooking a human brain."

    show cassian stern at stage_left
    cassian "The Sunken Archive beneath the Salt Wastes has been sealed since the Fourth Dawn. Yet... the Vigil requires dawn until noon to reinforce the outer Causeway."
    cassian "You have twenty-four hours, Broker Kael. Bring me working First-Era proof from beneath the salt—or at tomorrow's twilight bell, Envoy Lin and I ascend the Spire."

    $ set_flag("cassian_understood")
    $ complete_quest("mq_02_envoy", "Secured a 24-hour reprieve from Marshal Cassian to search the Sunken Archive.")
    $ start_quest("mq_03_archive", "Prepare tonight in Thornwick, then descend into the Sunken Archive at dawn.")
    $ start_quest("cq_sera_rain", "Check on Seraphina outside the Conservatory before midnight.")
    $ start_quest("cq_vespera_oakhaven", "Join Vespera at the salt-bluff watchpost.")

    hide cassian
    hide sera
    hide vespera
    with Dissolve(0.4)

    ## ------------------------------------------------------------------------
    ## NIGHT WATCH SCENE 2A: SERAPHINA IN THE RAIN-MIST
    ## ------------------------------------------------------------------------
    $ current_location_name = "Outside the Conservatory • 11:30 PM"
    play music audio.bgm_conservatory fadein 1.4
    scene bg orin_conservatory
    with Dissolve(0.8)

    narrator "Near midnight, unable to sleep on the inn's straw cot, I step out behind the Conservatory eaves—and nearly walk straight into a rapier-thin beam of cold starlight."

    show leo nervous at stage_left
    show sera proud at stage_right
    with Dissolve(0.35)

    narrator "Seraphina stands barefoot on the wet flagstones, running sword-forms at punishing speed. A thin ribbon of luminous silver dust drips from her nostril; she wipes it furiously on her sleeve before turning."

    sera "Do they not teach knocking in whatever cubicle farm Vespera dragged you from?"
    leo "Technically there isn't a door out here. You're bleeding... glitter."

    show sera fragile at stage_right
    sera "It's calcified ether. Happens when you hold three provincial wards up while half the Concordat Senate argues over wine tariffs."
    narrator "She lowers her practice blade, breathing hard, and looks through the steamed glass at Master Orin's patch of ordinary green clover."
    sera "Back home—Chicago, I think it was Chicago, near a big cold lake—I got a 99.4 average, first chair violin, early admission. And the one semester I burned out and dropped a class, everybody looked right through me like I'd died."
    sera "Here, when I raise my hand, armies cheer. Children paint wooden stars on their doors. ...So why are you looking at me like I'm the one losing, Sato?!"

    menu:
        "Sit on the wet step six feet away and describe the sound of rain on Chicago asphalt—and tell her she doesn't owe anyone her whole mind.":
            $ change_stat("empathy", 2, "Anchored Seraphina with an ordinary human memory.")
            $ change_stat("charisma", 1, "Spoke without preaching.")
            $ change_affinity("sera", 3, "Held onto the memory you described.")
            $ set_flag("sera_opened_up")
            $ complete_quest("cq_sera_rain", "Shared an Earth memory that steadied Seraphina's Tether.")
            show leo warm at stage_left
            leo "Lakeshore buses hiss when they kneel at the curb in November rain. Wet brakes, roasted peanuts on State Street, and radiator pipes clanking at five in the morning."
            leo "Nobody deserves to be turned into a lighthouse just because people like the view, Sera. Even if you dropped every sword tomorrow, you'd still be a real person."
            narrator "Seraphina stands completely still for five seconds. Then she sits down on the opposite end of the stone step, pulls her knees to her chest, and whispers to herself."
            sera "'Lakeshore buses hiss at the curb...' Don't let me forget that one tomorrow, okay, cubicle guy?"

        "Tell her bluntly: \"Because applause isn't warmth, Sera. Look at those statues in town—nobody visits a monument once the war's over.\"":
            $ change_stat("courage", 1, "Refused to flatter her armor.")
            $ change_affinity("sera", 1, "Stung—but respected your honesty.")
            $ set_flag("sera_opened_up")
            $ complete_quest("cq_sera_rain", "Forced Seraphina to confront the cost of her title.")
            sera "...God, I hate that you sound like my older sister. Get some sleep, Sato. If you slow me down in the Archive tomorrow, I won't carry you."

        "\"Teach me how you channel Starlight. Even a little. If things go wrong tomorrow, a garden spade won't be enough.\"":
            $ change_resonance(18, "Invited raw Astral Resonance into your veins.")
            $ change_tether(-10, "What color was your childhood bicycle? ...Gone.")
            $ change_stat("strength", 2, "Astral surge hardened your strike.")
            $ complete_quest("cq_sera_rain", "Traded a childhood memory for Seraphina's Resonance primer.")
            show sera neutral at stage_right
            sera "...Careful what you ask for. Hold out your palm."
            play sound audio.sfx_rift
            with flash_astral
            narrator "Cold violet fire threads into my wrist. Instantly my shoulders feel lighter, sharper, fearless—and when I try to picture the bicycle I rode in third grade, there's only white static."

    ## ------------------------------------------------------------------------
    ## NIGHT WATCH SCENE 2B: VESPERA ON THE OAKHAVEN BLUFF (+ CLOVER #2!)
    ## ------------------------------------------------------------------------
    $ current_location_name = "Oakhaven Overlook • Midnight"
    play ambience audio.amb_wind fadein 1.2
    scene bg salt_ruins
    with Dissolve(0.9)

    show leo neutral at stage_left
    show vespera tired at stage_right
    with Dissolve(0.35)

    narrator "Before turning in, I find Vespera kneeling at the western salt-bluff with a small iron hammer, driving a brass survey marker into the frost-white crust."

    vespera "My father mapped orchard boundaries across this ridge. Every autumn I move the stake back three inches where Master Orin's compost worms manage to eat the salt."
    show vespera soft at stage_right
    vespera "Twenty years ago, when the Sixth Hero flew overhead in golden armor, nine-year-old me waved a little paper flag and screamed 'Save us!' Ten minutes later, my parents' apple trees rang like crystal wineglasses and shattered."
    vespera "That's why I pull Outworlders {i}out{/i} of Solvara, Leo. Not because I hate heroes. Because no frightened kid from Earth should ever be handed a button that deletes a valley—or deletes themselves."

    $ set_flag("vespera_opened_up")
    $ change_affinity("vespera", 2, "Stood vigil with her above vanished Oakhaven.")
    $ complete_quest("cq_vespera_oakhaven", "Helped Vespera place her annual Oakhaven boundary marker.")

    menu:
        "Help her steady the lantern—and inspect the carved stone protruding beside the old orchard marker.":
            $ change_stat("intelligence", 1, "Spotted First-Era script under the frost.")
            narrator "As my lantern beam grazes the ancient boundary stone beneath Vespera's boots, a familiar glint of mica-glass catches the amber light!"
            leo "Vespera—hold on! Look wedged inside the old surveyor's benchmark!"
            narrator "Together we lift out a second tiny mica-sealed three-leaf clover, etched on the reverse in faded English: {i}'Root Two: Where orchards remember rain.'{/i}"
            if not has_item("pressed_clover"):
                $ add_item("pressed_clover", 1)
            $ register_clover_relic("Oakhaven Orchard Benchmark")
            vespera "...Four-hundred-year-old First-Era glass. Right on my father's survey line. Keep that safe in your satchel, Leo."

        "Take off my olive windbreaker and drape it over her shivering shoulders while she finishes hammering the stake.":
            $ change_stat("empathy", 1, "Shared warmth without making a speech.")
            $ change_affinity("vespera", 2, "Quietly pulled the oversized nylon collar up against the wind.")
            vespera "...What even is this fabric, woven frog-skin? It blocks wind better than oiled wool. ...Thanks, Question-Mark."

    stop ambience fadeout 1.0
    stop music fadeout 1.0
    pause 0.5
    return
