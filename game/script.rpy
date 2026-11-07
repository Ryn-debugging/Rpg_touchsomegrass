## ============================================================================
## script.rpy — Master Narrative Orchestrator
## WHERE THE GRASS STILL GROWS (An Unwanted Hero's Chronicle)
## ============================================================================

label start:
    stop music fadeout 1.0
    $ leo_display_name = "Leo"
    $ hud_visible = False

    # Prologue: Childhood trauma, 2 AM adult loneliness, and the puddle abduction
    call prologue_start

    # Enable RPG HUD once Leo awakens in Solvara
    $ hud_visible = True

    # Chapter 1: No Heroes Allowed in Thornwick (Exploration Hub + Astrolabe Mini-Game)
    call chapter1_start

    # Chapter 2: The Girl Who Forgot Rain (Seraphina & Marshal Cassian)
    call chapter2_start

    # Chapter 3: Beneath the Salt Wastes (Sunken Archive Hub + Tactical Duel)
    call chapter3_start

    # Chapter 4: The Crucible of Crowns (Trauma Trial, Sera's Brink & Route Lock)
    call chapter4_start

    # Chapter 5: Final Confrontation & Four Earned Endings
    jump chapter5_start