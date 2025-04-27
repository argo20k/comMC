# Changelog

## TODO

- backup datapacks on github, mainly afk ones, and blaze and caves (doesn't have comMC settings) into /common/forks
- rpc link to YT video
- connected textures
- nametag improvements
- https://modrinth.com/datapack/ly-clumps - https://i.imgur.com/2Jcrtgo.png
- who's contributed to most advancement - interesting stat
- https://i.imgur.com/siCbXOb.png - disable villager death finder
- default datapacks - paxi - outdated
- dh pregen
- disable target fluid f3
- player moved too quickly
- replay mod
- clean up oracle server files - zomboid + boot volume names + storage
- general rule - everything goes - but choose if you don't want to use stuff like iron farms or EXP farms
- added Discord `#faq` to re-enable coordinates - opt out of ping wheel
- changed update instructions & GIF to use Discord server drag & drop message
- separate curseforge tutorial to different file
- added version info to main menu
- update #faq
  - add simpler channel hiding with <id:customize>
  - add "hide most channels" button in onboarding questions
- "don't record me role" - can't join #"🔴│recording" - <id:customize> - #role-info
- nice 1.21.5 seed `-8546090065308567931`

- afk/unafk hotkey - `/trigger afk` - mute sounds
- unbreaking villager + villager home

## 1.7.8

- 🚀 New mods
  - Clumps - instant pickup experience orbs
  - Sodium Extras - customise & new features - `F11` switches between `WINDOWED`, `BORDERLESS_FULLSCREEN`, & `FULLSCREEN`
  - Sodium Options API - improved category menu
  - Reese's Sodium Options - improved category menu
  - Sodium Dynamic Lights - Sodium options support
  - Sodium Shadowy Path Blocks - non-full block smooth lighting
  - ServerCore - dynamic server settings based on performance
- Changes to vanilla mechanics
  - ServerCore.mod - dynamically changes chunk_tick_distance, mobcap, simulation_distance, & render_distance based on server performance
  - ServerCore.mod - static breeding cap for villagers (32) & animals (128) - [details here](https://github.com/Wesley1808/ServerCore/blob/main/docs/config/OPTIMIZED.md#configyml)
- updated Simple Discord RPC.mod - project & version info in Discord status
- all comMC project files are managed in this GitHub repo now - apart from modpacks
- server now runs on **versioned** GitHub repo
- disabled mods not needed server-side

## 1.7.7.2

### Added or Changed

- updated Tab Tweaks.mod - ping now shows correctly
- removed Squishy's Status.mod until AFK Dim Names is compatible

## 1.7.7

### Added or Changed

- 🚀 New mods
  - RightClickHarvest - `RMB` replant automatically - hoe tiers increases radius
  - One Click Join - quick join servers from main menu
  - Death Sorter - restores inventory layout after death
  - Death Finder - coordinates on death screen - distance from death - villager & pet support
  - Death Backup - restore inventories after death (server management)
  - Sodium Extra - visual bug fixes & more performance options
  - BoccHUD - custom permanent debug HUD - axolotol variant name - hive/nest bee/honey count - structure bounding boxes - B + C
  - Forked - Datapack - Detect AFK Players - performant 3 mins AFK timer - `/trigger afk` command - WARNING make `/afk` command?
  - Forked - Datapack - AFK Dim Names
  - Datapack - AFK Message
  - Datapack - AFK Sit
  - Datapack - Pause Day Cycle - day/weather is paused if players are AFK
  - Datapack - AFK Sleep - ignore AFK players when sleeping
  - Forked - Datapack - Sleep - regeneration after sleep - action bar announcement - supports AFK Sleep?
  - Better Safe Bed - sleep if mobs can't target you
  - Squishy's Status - open/DND, recording/streaming status - `U` by default
  - Simple Discord RPC - Discord status while playing
  - Model Gap Fix
  - Simple Snowy Fix - snow generation on tree leaves
  - Tab Tweaks - custom player list HUD
- Updated mods
  - Puzzles Lib - `21.5.6` → `21.5.9`
  - Xaero's Minimap - `25.2.4` → `25.2.5` - fixed crashes - credit @jerry @nish
- updated/cleaned Simple Discord Link /verify message
- updated/cleaned GitHub repo
- ignore modpack update warnings
- ignore specific Xaero's Minimap update warning

## 1.7.6

### Added or Changed

- 🚀 New mods
  - Distant Horizons - further, but simpler render distance - pregenerating & multiplayer LOD sharing support
  - Cut Through - attack foes behind blocks like tall grass
  - Chat Heads
  - Longer Chat History - 100 → 65000 messages - supports Server_Chat_Sync.mod
  - Server Chat Sync - history while offline & rejoining
  - Chat Impressive Animation - & removes message indicator
  - Better "Add Server" - autofill server name - enter to confirm
  - No Chat Reports - disables telemtry, chat, & player reporting
  - Chat Notify - ping sound when your name is mentioned
  - Cherished Worlds - favourite worlds - top of the list - can't be deleted while pinned
  - Delete Worlds To Trash - restore deleted worlds from system recycle bin
  - Configured Defaults - for game settings & resource packs for new installs
- Updated mods
  - Xaero's Minimap - `25.2.0` → `25.2.4` - fixed [warning?](https://i.imgur.com/Jd5OqRE.png) - credit @jerry
  - PlayerRevive - `2.0.32` → `2.0.36`
- Fixed server.properties - updated MOTD date formatting
- Updated comMC Discord bot profile description - see #faq if you're new! - %playerCount% online

## 1.7.5

### Added or Changed

- 🚀 New mods
  - Tree harvester - `CROUCH` + axe trees
  - Ore Harvester - vein miner - `CROUCH` + pickaxe ores - WARNING balance with enchant? - credit @kaito
  - Fast IP Ping - ping/connect to servers faster
- updated server settings to improve performance (supposedly)
- updated server gamerule - one player can sleep to pass the night 🛌
- updated server MOTD - `#faq` & updated date information ℹ️
- updated AppleSkin - disabled food info `F3` debug clutter
- updated changelog - formatting changes & missing [Camerapture changelog](https://github.com/argo20k/comMC/blob/main/CHANGELOG.md#v14---v172), [Xaero's Minimap](https://github.com/argo20k/comMC/blob/main/CHANGELOG.md#v14---v172)
- added timestamp to Discord updates

## 1.7.4

### Added or Changed

- updated [README "Update"](https://github.com/argo20k/comMC?tab=readme-ov-file#update) - GIF tutorial & more steps
- updated [README "Roadmap"](https://github.com/argo20k/comMC?tab=readme-ov-file#roadmap) - hyperlinked references
- fixed Simple Discord Link /verify message
- updated server MOTD
- added server icon

## 1.7.3

### Added or Changed

- added spark - client/server performance profiler
- updated all mods
- updated [README](https://github.com/argo20k/comMC?tab=readme-ov-file#readme-top)

## 1.4 - 1.7.2

### Added or Changed

- added this changelog :) will attempt to keep this per version from now
- added Ping Wheel - credit @nish (`MOUSE_5` by default)
- added Xaero's Minimap - credit @kaito @tarou @yukoi (disabled by default)
- added Spyglass Improvements - spyglass zoom scroll/keybind (`Z` by default)
- added PlayerRevive - revive a player within 60 seconds after death - credit @tsu22
- added Camerapture - take/upload pictures - frame/album - `CROUCH + RMB` GUI
- added shaders by default - Complementary Shaders - Unbound (disable with `K` or through settings)
- added a bunch of quality of life mods
  - AppleSkin - Food/hunger values - inventory tooltips & HUD
  - Durability Tooltip
  - GUI Clock - must be in inventory - `F3` nerf - day counter
  - GUI Compass - must be in inventory - `F3` nerf
  - bad packets - packet messaging between different mod loaders for servers
  - BetterF3 - custom debug HUD - more legible - `F3` nerf - `F3 + M` (disabled coordinates by default - see #faq to re-enable)
  - Held Item Tooltips - item durability, enchants, shulker box contents, potion effects, rocket durations, etc. - WARNING bad Durability Tooltip support
  - What's That Slot? - query item options for slots - LEFT ALT + HOVER
- updated/fixed crash caused by Controlling mod - changing keybinds works now

## 0.0

### Added or Changed

- [Insert note here]

### Removed

- [Insert note here]
