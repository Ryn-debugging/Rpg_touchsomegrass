## ============================================================================
## systems/achievements.rpy — Cross-Playthrough Persistent Achievements
## ============================================================================

default persistent.tsg_achievements = set()

init python:
    if persistent.tsg_achievements is None:
        persistent.tsg_achievements = set()

    ACHIEVEMENT_DB = [
        ("ach_kidnapped", "No Truck Required", "Survived an interdimensional abduction through an Eastside laundromat puddle.", "#73d2de"),
        ("ach_fined", "Public Hazard Citation", "Got fined under Thornwick's Anti-Deliverance Ordinance on your very first day.", "#ebb963"),
        ("ach_harmonic", "Harmonic Natural", "Stabilized the Old Aqueduct Resonance leak with zero astrolabe misfires.", "#7ec876"),
        ("ach_stew_brother", "Peel the Garlic", "Earned Bram's frontline respect and uncovered the truth behind his chipped horn.", "#f29559"),
        ("ach_remnant_mercy", "Laid to Rest, Not Slain", "Quieted the Sunken Archive's Hollow Remnant by restoring its human name.", "#c792ea"),
        ("ach_clover_finder", "Three Blades of Forgotten Clover", "Discovered all three hidden Earth-clover relics scattered across Solvara.", "#7ec876"),
        ("ach_sera_saved", "Her Mother's Voice", "Stopped Seraphina Lin from burning away her last memory of home.", "#c792ea"),
        ("ach_marcus_faced", "Out From Under the Bleachers", "Faced the echo of childhood humiliation without shrinking or turning cruel.", "#ebb963"),
        ("ach_end_hopeful", "Ending I: Where the Grass Still Grows", "Returned home and stood barefoot in the real morning grass.", "#7ec876"),
        ("ach_end_bittersweet", "Ending II: The Quiet Gardener of Thornwick", "Gave your return anchor away and grew a new meadow in Solvara.", "#73d2de"),
        ("ach_end_tragic", "Ending III: The Seventh Pillar of Salt", "Became the invincible hero of your childhood dreams—and lost everyone inside.", "#e06c75"),
        ("ach_end_secret", "Secret Ending: The Two Doors", "Dismantled the Crucible and bridged two worlds without sacrificing a single soul.", "#ffd166"),
    ]

    ACHIEVEMENT_MAP = {aid: (title, desc, col) for aid, title, desc, col in ACHIEVEMENT_DB}

    def unlock_achievement(ach_id):
        if persistent.tsg_achievements is None:
            persistent.tsg_achievements = set()
        if ach_id not in ACHIEVEMENT_MAP:
            return
        if ach_id not in persistent.tsg_achievements:
            persistent.tsg_achievements.add(ach_id)
            renpy.save_persistent()
            title, desc, col = ACHIEVEMENT_MAP[ach_id]
            renpy.sound.play("audio/sfx/ui_chime.ogg")
            push_toast(f"Achievement: {title}", desc, col)

    def has_achievement(ach_id):
        if persistent.tsg_achievements is None:
            return False
        return ach_id in persistent.tsg_achievements

    def achievement_count():
        if persistent.tsg_achievements is None:
            return 0
        return len(persistent.tsg_achievements)
