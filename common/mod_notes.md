Performance

- spark - client/server performance profiler
- ImmediatelyFast - Speed up immediate mode rendering
- AI Improvements - disable look at goal (player or attack target) AI task - cause AIs to not face targets or walking directions - replaces default look controller with a more efficient version
- Alternate Current - efficient & non-locational redstone dust fix
- FerriteCore - RAM optimisations
- Let Me Despawn - despawns unintentional persistent mobs - drops their picked up or equipped items - configurable whitelist
- Get It Together, Drops! - dropped item stacks combine - do_not_combine specific items whitelist option - 2 radius including vertical (configurable)
- Entity Culling - hide Block-/Entities that aren't visible
- More Culling - hide Block-/Entities that aren't visible
- C2ME - chunk loading - vanilla parity
- Sodium - optimised terrain, entities, GUIs, block entities, etc. renderer
- Sodium Extra - visual bug fixes & more performance options
- Sodium Extras - customise & new features
- Sodium Options API - improved category menu
- Reese's Sodium Options - improved category menu
- Sodium Dynamic Lights - Sodium options support
- Sodium Shadowy Path Blocks - non-full block smooth lighting
- Lithium - optimised game physics, mob AI, block ticking, etc.
- Fast IP Ping - ping/connect to servers faster
- missing version - Better chunk loading - chunk loading - predictive chunkloading based on player movement - prevent players entering unloaded chunks
- missing version - Connectivity - solves Login-Timeouts, Packet size limits, Ghostblocks, Payload too large, etc - network / packet traffic analysis command
- missing version - Client Crafting - eliminates server delay when crafting - syncing afterwards
- missing version - Chunk Sending - seamless login/teleport/respawn/dimension - nearby chunks load first & distributes them over time - improving people with slow connections
- missing version - Fast Async World Save - data saves asynchronously during world save every 5 mins - prevents lag spike
- missing version - Fix GPU Memory Leak - fixes bugs which leak GPU memory resources
- missing version - Leaky - detects and removes excessive item stack counts - alerts 100+ stacks every 30s of position & count in chat & items glow - kills items at 500+ stacks
- missing version - Limited Chunkloading - loaded chunks only stay 10 mins after player logout - IDK chunkloaders are only active if players are online - WARNING chunks / loaders don't auto-load on start
- missing version - Recipe Essentials - optimises recipes - caching / sorting prioritises craftable & recent recipes - Shows all recipes immediately, including modded ones
- missing version - Server Performance - Saves chunks continuously over time on a delay - preventing lagspikes from saving lots of chunks at once - reduces vanilla chunks unload per tick
- missing version - Structure Essentials - optimises structure searches & placement - Faster structure locate command - /getStructuresNearby - Custom search radii for maps & locate commands - Auto biome compatibility for better structure spawning - prevents missing registry entries & random generator crashes - reduces lag spikes during map generation
- missing version - Embeddium - optimised terrain, entities, GUIs, block entities, etc. renderer
- missing version - Embeddium++ - option screen dynamic lights, entity distance culling, true dim darkness, fast models, fast language reload, borderless fullscreen, toggle fog, text shadows - WARNING FPS display - WARNING zoom key - WARNING hide JEI
- missing version - Starlight - performant light engine
- missing version - Radium - game logic optimisation
- missing version - ModernFix - RAM optimisations - bug fixes - loads block and item models dynamically - WARNING crashes or missing textures
- missing version - Memory Leak Fix - fixes random memory leaks
- missing version - Log Begone - remove configurable logs from your log
- missing version - Krypton Reforged - networking stack optimisations
- missing version - Get It Together, Drops! - dropped item stacks combine - do_not_combine specific items whitelist option - 2 radius including vertical (configurable)
- missing version - Fastload - worlds loading improvements
- missing version - Chunk Pregenerator – multi-threading pre generate chunks - concurrent multiple dimensions - runs in the background - retrogen - progress stats - large-scale - modded environment support
- missing version - Palladium - Deduplicates resources - RAM - shader/chunk/nbt - mob AI - WARNING shader/-packs buggy?
- missing version - Noisium - worldgen - vanilla parity
- missing version - Mobtimizations - AI pathfinding, targeting, & scanning - WARNING minimal gameplay impact

Management

- Better Modlist - synitra connector fabric mod support
- Controlling - search keybinds - WARNING assign keybind crash
- Configured - GUI mod config settings

Zoom

- Spyglass Improvements - spyglass zoom scroll - zoom keybind - accessories support - WARNING no model support multiplayer? (https://github.com/juancarloscp52/spyglass-improvements/issues/43)
- Camerapture - take/upload pictures - frame/album - CROUCH + RMB GUI
- version missing - Useful Spyglass - Hwyla like entity health & armour info - marking enchant glowing effect when attacking - precision enchant perfect accuracy & no gravity CROUCH + RANGE WEAPON
- version missing - Camera Overhaul - player movement visual feedback - camera rotations/shake
- version missing - Camera Utils - tripod detatch camera - extra/custom 3rd person - WARNING little clashing with Better Third Person
- version missing - Better Third Person - 360 freecam while moving
- version missing - Accessories - extra wearable inventories for accessories
- version missing - Curios Compat Layer for Accessories
  > Spyglass Improvements - hat spyglass
  > Horse Expert - belt monocle

HUD

- AppleSkin - Food/hunger values - inventory tooltips & HUD
- Durability Tooltip
- GUI Clock - must be in inventory - F3 nerf - day counter
- GUI Compass - must be in inventory - F3 nerf
- bad packets - packet messaging between different mod loaders for servers
- BetterF3 - custom debug HUD - more legible - F3 nerf - F3 + M
- Held Item Tooltips - item durability, enchants, shulker box contents, potion effects, rocket durations, etc. - WARNING bad Durability Tooltip support
- What's That Slot? - query item options for slots - LEFT ALT + HOVER
- BoccHUD - custom permanent debug HUD - axolotol variant name - hive/nest bee/honey count - structure bounding boxes - B + C
- 1.21.4 - MiniHUD Extra - configure colours for all BoccHUD - mod integration & support - N + C
- 1.21.4 - ServuxForged - server support for BoccHUD & structure bounding boxes - WARNING Tobi fork to fix pack.mcmeta
- 1.21.1 - SUPPLEMENTARIES - TWEAKS - tooltips for banner patterns
- 1.21.1 - SUPPLEMENTARIES - TWEAKS - tooltips for paintings & sherds
- 1.21.4 - Food Effect Tooltips - status effect tooltips for food - supports % chance like rotten flesh
- 1.21.4 - Equipment Compare - compare items with currently held/equipped tools - CTRL + HOVER
- 1.21.4 - Item Highlighter - animated star inventory icons on newly-picked up items
- 1.21.4 - Iceberg - required for Equipment Compare & Item Highlighter - WARNING prism dependency download is unreliable (manually download instead)
- 1.21.4 - Legendary Tooltips - fancy default tooltips for items - 3d preview for equipment - customisable item tooltips - OP ITEMS - WARNING annoying for tools (maybe only enable for armour)

comMC

- Simple Discord Link - Discord & Minecraft whitelist integration

Kaito

- Xaero's Minimap
- Tree harvester - CROUCH + LMB
- Ore Harvester - CROUCH + LMB - WARNING balance with enchant?
- RightClickHarvest - `RMB` replant automatically - hoe tiers increases radius
- Screenshot to Clipboard
- version missing - Bigger Stacks - hold more than 64
- version missing - Butchery
- version missing - Better Combat
- version missing - Basic Weapons / Simply Swords
- 1.21.1 - Fishing Real - reel live mobs when fishing

Rui

- teleport way stones
- watch together in game
- furnace variations
- tnt variations
- smaller crosshair

Dan

- yakutbutsu
- boat jump

nish

- Ping Wheel
- get your own mob spawners
- prox chat

Tobi

- PlayerRevive - revive a player within 60 seconds after death
- Chat Heads
- Longer Chat History - 100 → 65000 messages - supports Server_Chat_Sync.mod
- Server Chat Sync - history while offline & rejoining
- Chat Impressive Animation - & removes message indicator
- Better "Add Server" - autofill server name - enter to confirm
- No Chat Reports - disables telemtry, chat, & player reporting
- Chat Notify - ping sound when your name is mentioned
- Cut Through - attack foes behind blocks like tall grass
- Cherished Worlds - favourite worlds - top of the list - can't be deleted while pinned
- Delete Worlds To Trash - restore deleted worlds from system recycle bin
- One Click Join - quick join servers from main menu
- Death Sorter - restores inventory layout after death
- Death Finder - coordinates on death screen - distance from death - villager & pet support
- Death Backup - restore inventories after death (server management)
- AFK & sleep
  - Forked - Datapack - Detect AFK Players - performant 3 mins AFK timer - `/trigger afk` command - WARNING make `/afk` command?
  - Forked - Datapack - AFK Dim Names
  - Datapack - AFK Message
  - Datapack - AFK Sit
  - Datapack - Pause Day Cycle - day/weather is paused if players are AFK
  - Datapack - AFK Sleep - ignore AFK players when sleeping
  - Forked - Datapack - Sleep - regeneration after sleep - action bar announcement - supports AFK Sleep?
  - Better Safe Bed - sleep if mobs can't target you
  - Squishy's Status - open/DND, recording/streaming status - `U` by default
  - 1.20.4 - Sleep Tight - cooldown sleeping - consecutive sleep nightmare (dread, prevent with dream essence) - dark place sleep encounter (place lights) - repeat single bed rewards, configurable saturation & XP gaining effect (bed bug destroys home bed, prevent with dream essence) - WARNING nightmares still reset sleep rework tiredness (unintended)
  - 1.20.1 - Sleep Rework - tiredness level (0–10000%) - "zzz" inventory icon - phantoms start spawning & increases over 100%, 60 mins - potions effecting tiredness - WARNING wake up effect / benefit, timeout to rest without skipping the night on servers (sleep tight doesn't consider it sleeping), tutorial GUI lies (says you need 100% tiredness to sleep, but sleep tight handles cooldowns https://i.imgur.com/tH7EOVU.png)
- Simple Discord RPC - Discord status while playing
  - https://modrepo.de/minecraft/voicechat/wiki/server_setup
  - https://modrepo.de/minecraft/voicechat/addons
- Model Gap Fix
- Simple Snowy Fix - snow generation on tree leaves
- Tab Tweaks - custom player list HUD

- Grabby Mobs
- Chestpack Backpacks
- beta testing discord rpc
- wearing heads / pumpkin hides username
- miniboss & enemy variants
- natural leaf piles
- adjust single sounds - villager
- multi mine - mine the same block with others
- tablist ping
- better looking savana mod
- connected textures
- taiga night sweeper moment
- not added - WARNING crashes - ChatImage - hover over chat message to show image/GIF

Ben

- Distant Horizons - further, but simpler render distance - pregenerating & multiplayer LOD sharing support
- ServerCore - dynamic server settings based on performance
- Clumps - instant pickup experience orbs
- villager trade recycle
- visual clutter textures - lower fire
- translator with subtitles
- wisdom / more experience enchant

Jerry

- brain rot mod
- Archimedes ships
