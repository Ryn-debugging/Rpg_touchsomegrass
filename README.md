# Where the Grass Still Grows
### *An Unwanted Hero's Chronicle*

A complete, standalone psychological fantasy visual novel and narrative RPG built in **Ren'Py 8** (`1280×720` HD).

---

## Story Premise

For twenty-six years, **Leo Sato** secretly held onto a ridiculous childhood wish born in the mud behind his elementary school bleachers:

> *"Someday, I want to become a hero."*

Instead, adulthood gave him social anxiety, graveyard-shift spreadsheet work, cold convenience-store udon, and a flickering neon sign outside Apartment 4B—until a disgraced **Recall Broker** named **Vespera Kael** accidentally drags him through a rain puddle into **Solvara**.

There is only one problem: Solvara has already survived **Six Summoned Heroes** over the past four centuries—and their unchecked, memory-burning magic turned half the continent into dead white crystal (**Hero-Scars**). In the frontier charter town of **Thornwick**, proclaiming yourself a Chosen Hero carries a 40-Crown municipal fine and ditch-digging duty.

Equipped with a copper-veined Rootwarden spade instead of a legendary sword, Leo must navigate a world recovering from too many saviors, confront the scars he brought with him from Earth, and discover what courage actually means when nobody is cheering.

---

## Key Features & Gameplay Systems

- **Prologue + 5 Full Chapters & 4 Distinct Earned Endings:**
  - **Ending I (Hopeful):** *Where the Grass Still Grows*
  - **Ending II (Bittersweet):** *The Quiet Gardener of Thornwick*
  - **Ending III (Tragic):** *The Seventh Pillar of Salt*
  - **Ending IV (Secret True Ending):** *The Two Doors (Touch Some Grass)*
- **Character Development & Psychological Balance (`game/systems/stats.rpy`):**
  - Six core stats (**Strength**, **Intelligence**, **Courage**, **Empathy**, **Charisma**, **Reputation**) plus **Reality Tether** (`0–100%`) and **Astral Resonance Load**.
- **Deep Companion & Foil Relationships (`game/systems/relationships.rpy`):**
  - Build or strain bonds with **Vespera Kael**, **Bramwell "Bram" Thorne**, **Seraphina "Sera" Lin**, **Master Orin Mossbeard**, and **High Marshal Cassian Vey**, unlocking dynamic bond ranks and hidden backstory insights.
- **Interactive Exploration Hubs (`game/systems/exploration.rpy`):**
  - Manage exploration actions across **Thornwick Charter Town** and the **Sunken Archive of First Roots**, uncovering optional character scenes, civic work, and environmental storytelling.
- **Quest & Worldbuilding Codex Journal (`game/systems/quests.rpy`):**
  - Track **Main Quests**, **Side Quests**, **Character Quests**, and **Hidden Quests** (*Three Blades of Forgotten Clover*), alongside a 10-entry unlockable **Solvara World Codex**.
- **Satchel Inventory & Usable Relics (`game/systems/inventory.rpy`):**
  - Inspect keepsakes and consume field rations/tea to restore Vitality, Focus, and Reality Tether.
- **Two Custom Interactive Mini-Games (`game/systems/minigames.rpy`):**
  - **Astrolabe Harmonic Tuning:** Real-time harmonic seal calibration widened by **Intelligence**.
  - **Tactical Stance Encounter:** Turn-based narrative combat against the **Hollow Remnant** allowing victory through either frontline force (**Armor Integrity**) or empathy (**Memory Peace**).
- **Persistent Achievements (`game/systems/achievements.rpy`):**
  - 12 cross-playthrough milestones and ending badges tracked right from the Title Screen and in-game menu.
- **Original Visual & Audio Suite:**
  - Cohesive anime key-art CGs, atmospheric painted backgrounds, 22 transparent character expression sprites, custom dark-botanical & lantern-amber UI, 8 loopable stereo `.ogg` BGM tracks, 3 ambient soundscapes, and 7 custom SFX.

---

## Project Structure

```text
game/
  script.rpy                 # Master narrative entry point
  options.rpy                # Project, window, transition & audio channel config
  gui.rpy                    # 1280x720 palette & typography tokens
  characters.rpy             # Speaker definitions, dynamic nameplates & ATL transforms
  assets_manifest.rpy        # Centralized background, CG, sprite & audio declarations
  screens.rpy                # Custom Title Screen, Dialogue Box, Choices & Core Menus
  screens/
    hud_and_toasts.rpy       # Top gameplay HUD, animated toast popups & chapter cards
    custom_menus.rpy         # Status, Bonds, Journal/Codex, Satchel & Achievements UI
  systems/
    stats.rpy                # 6 core stats, Tether, Resonance & state flags
    relationships.rpy        # Companion affinity & unlockable bond insights
    quests.rpy               # Multi-category Quest tracker & Worldbuilding Codex
    inventory.rpy            # Usable & inspectable Satchel items
    achievements.rpy         # Cross-save persistent Achievements
    exploration.rpy          # Reusable Hub Exploration engine
    minigames.rpy            # Astrolabe Tuning & Tactical Stance Duel systems
  story/
    prologue.rpy             # Prologue: "Fluorescent Rain"
    chapter1.rpy             # Chapter 1: "No Heroes Allowed in Thornwick"
    chapter2.rpy             # Chapter 2: "The Girl Who Forgot Rain"
    chapter3.rpy             # Chapter 3: "Beneath the Salt Wastes"
    chapter4.rpy             # Chapter 4: "The Crucible of Crowns"
    chapter5_endings.rpy     # Chapter 5 & All 4 Earned Endings
  images/                    # bg/, cg/, characters/, ui/
  audio/                     # bgm/, ambience/, sfx/ (.ogg Vorbis)
  fonts/                     # Bundled open-source serif & sans-serif fonts
docs/
  GAME_DESIGN_BIBLE.md       # Complete Phase 1 Narrative & Systems Design Bible
```

---

## How to Play

1. Open the **Ren'Py 8 Launcher** (Ren'Py `8.0+` / `8.5+` recommended).
2. Point your Projects Directory to the parent folder containing `Rpg_touchsomegrass` (or run directly via CLI):
   ```bash
   /path/to/renpy-sdk/renpy.sh /path/to/Rpg_touchsomegrass
   ```
3. Click **Launch Project** -> **Begin Journey**.
