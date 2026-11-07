## ============================================================================
## assets_manifest.rpy — Centralized Visual & Audio Asset Declarations
## Ensures consistent 1280x720 scaling and clean sprite framing across scenes
## ============================================================================

## Solid Atmospheric Backdrops ------------------------------------------------
image black = Solid("#060a0e")
image white = Solid("#f4f7f5")
image memory_sepia = Solid("#1c1714")

## Environmental Backgrounds (1280x720 Cover) ---------------------------------
image bg childhood_bleachers = Transform("images/bg/bg_childhood_bleachers.png", xysize=(1280, 720), fit="cover")
image bg leo_apartment = Transform("images/bg/bg_leo_apartment.png", xysize=(1280, 720), fit="cover")
image bg rainy_alley = Transform("images/bg/bg_rainy_alley.png", xysize=(1280, 720), fit="cover")
image bg salt_ruins = Transform("images/bg/bg_salt_ruins.png", xysize=(1280, 720), fit="cover")
image bg thornwick_square = Transform("images/bg/bg_thornwick_square.png", xysize=(1280, 720), fit="cover")
image bg crooked_lantern_inn = Transform("images/bg/bg_crooked_lantern_inn.png", xysize=(1280, 720), fit="cover")
image bg orin_conservatory = Transform("images/bg/bg_orin_conservatory.png", xysize=(1280, 720), fit="cover")
image bg old_aqueduct = Transform("images/bg/bg_old_aqueduct.png", xysize=(1280, 720), fit="cover")
image bg sunken_archive = Transform("images/bg/bg_sunken_archive.png", xysize=(1280, 720), fit="cover")
image bg crucible_spire = Transform("images/bg/bg_crucible_spire.png", xysize=(1280, 720), fit="cover")
image bg earth_dawn_park = Transform("images/bg/bg_earth_dawn_park.png", xysize=(1280, 720), fit="cover")

## Cinematic CG Illustrations (1280x720 Cover) --------------------------------
image cg title_meadow = Transform("images/cg/cg_title_meadow.png", xysize=(1280, 720), fit="cover")
image cg puddle_rift = Transform("images/cg/cg_puddle_rift.png", xysize=(1280, 720), fit="cover")
image cg conservatory_clover = Transform("images/cg/cg_conservatory_clover.png", xysize=(1280, 720), fit="cover")
image cg crucible_climax = Transform("images/cg/cg_crucible_climax.png", xysize=(1280, 720), fit="cover")
image cg morning_grass = Transform("images/cg/cg_morning_grass.png", xysize=(1280, 720), fit="cover")

## Character Sprites (Transparent RGBA Cutouts, Scaled for 720p Stage) --------
# Leo Sato
image leo neutral = Transform("images/characters/leo_neutral.png", xysize=(460, 650), fit="contain")
image leo nervous = Transform("images/characters/leo_nervous.png", xysize=(460, 650), fit="contain")
image leo resolute = Transform("images/characters/leo_resolute.png", xysize=(460, 650), fit="contain")
image leo warm = Transform("images/characters/leo_warm.png", xysize=(460, 650), fit="contain")

# Vespera Kael
image vespera neutral = Transform("images/characters/vespera_neutral.png", xysize=(460, 650), fit="contain")
image vespera sharp = Transform("images/characters/vespera_sharp.png", xysize=(460, 650), fit="contain")
image vespera tired = Transform("images/characters/vespera_tired.png", xysize=(460, 650), fit="contain")
image vespera soft = Transform("images/characters/vespera_soft.png", xysize=(460, 650), fit="contain")

# Bramwell "Bram" Thorne
image bram neutral = Transform("images/characters/bram_neutral.png", xysize=(500, 670), fit="contain")
image bram grin = Transform("images/characters/bram_grin.png", xysize=(500, 670), fit="contain")
image bram fierce = Transform("images/characters/bram_fierce.png", xysize=(500, 670), fit="contain")
image bram shaken = Transform("images/characters/bram_shaken.png", xysize=(500, 670), fit="contain")

# Seraphina "Sera" Lin
image sera neutral = Transform("images/characters/sera_neutral.png", xysize=(460, 650), fit="contain")
image sera proud = Transform("images/characters/sera_proud.png", xysize=(460, 650), fit="contain")
image sera fragile = Transform("images/characters/sera_fragile.png", xysize=(460, 650), fit="contain")

# Master Orin Mossbeard
image orin neutral = Transform("images/characters/orin_neutral.png", xysize=(480, 660), fit="contain")
image orin smile = Transform("images/characters/orin_smile.png", xysize=(480, 660), fit="contain")
image orin solemn = Transform("images/characters/orin_solemn.png", xysize=(480, 660), fit="contain")

# High Marshal Cassian Vey
image cassian neutral = Transform("images/characters/cassian_neutral.png", xysize=(480, 670), fit="contain")
image cassian stern = Transform("images/characters/cassian_stern.png", xysize=(480, 670), fit="contain")
image cassian weary = Transform("images/characters/cassian_weary.png", xysize=(480, 670), fit="contain")

# Hollow Remnant (Archive Boss Entity)
image remnant form = Transform("images/characters/remnant_form.png", xysize=(520, 680), fit="contain")

## Audio Track Constants ------------------------------------------------------
define audio.bgm_title = "audio/bgm/title_meadow_echo.ogg"
define audio.bgm_apartment = "audio/bgm/neon_fluorescent_rain.ogg"
define audio.bgm_thornwick = "audio/bgm/thornwick_hearth_and_stone.ogg"
define audio.bgm_conservatory = "audio/bgm/conservatory_green_hymn.ogg"
define audio.bgm_mystery = "audio/bgm/archive_of_salt_and_glass.ogg"
define audio.bgm_combat = "audio/bgm/iron_and_grounding_rod.ogg"
define audio.bgm_crucible = "audio/bgm/seventh_pillar_elegy.ogg"
define audio.bgm_epilogue = "audio/bgm/morning_grass_sunlight.ogg"

define audio.amb_rain = "audio/ambience/rain_alley_loop.ogg"
define audio.amb_wind = "audio/ambience/salt_wind_loop.ogg"
define audio.amb_birds = "audio/ambience/dawn_meadow_birds.ogg"

define audio.sfx_chime = "audio/sfx/ui_chime.ogg"
define audio.sfx_quest = "audio/sfx/quest_journal.ogg"
define audio.sfx_rift = "audio/sfx/rift_tear.ogg"
define audio.sfx_astrolabe = "audio/sfx/astrolabe_lock.ogg"
define audio.sfx_strike = "audio/sfx/spade_clash.ogg"
define audio.sfx_heal = "audio/sfx/meadow_breath.ogg"
define audio.sfx_heartbeat = "audio/sfx/anxious_heartbeat.ogg"
