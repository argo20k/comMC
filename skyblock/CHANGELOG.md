# Changelog

## TODO

- set up watch party in game for new video
- update #faq
  - add simpler channel hiding with <id:customize>
  - add "hide most channels" button in onboarding questions
  - add getting spammed by advancements, just relog
  - added Discord `#faq` to re-enable coordinates - opt out of ping wheel
  - waypoints disappeared? just do this
  - glitch core error? do this
- banner equip as cape with accessories compat & overrides minecraftcapes.mod
- connect directly to the server via QuickPlay
  - `Select Instance>Edit>Settings>Miscellaneous>Set server to join on launch`
- Server Side:
  Can't find your horse? Get Horse Trumpet (highlights your horse) or Horse Whistle (horse runs/tps to you)
  Stop banging your head into stuff and taking damage VehicleFix Ride through forests with ease
  Horse stat overhaul (horses get better the more you use them) Superb Steeds
- performance modpack mods for inspo
  - simply optimised
  - adrenaline
- e4mc local world hosting mod but make sure its safe against griefer groups
- event ideas
  - Apotheosis
- make independent skyblock comMC Discord application / bot
- enable bundles

- fixed entity render distance, like seeing players and mobs from further
- sleep datapack - sleeping person name is wrong
- make held item tooltips use same durability colouring as enhanced tooltips
- bluemap - rendered world map mod with command-line version for non-server world renders
- spawners haunt you when mined mod
- photon shader - add popular shaders
- configured defaults for options etc.
- Redstone Tweaks - owo observer probably when it activates
- <details><summary><strong>🔧 flowstate mods</strong></summary>

  - ambient sound
  - adaptive tooltip
  - amendments
  - anvil repairing
  - bad optimisations
  - bette rclimbing
  - bountiful - bounty board quests
  - camera overhaul - customisable camera tilt
  - cave dust
  - chat animation
  - chat image
  - clumps - xp clumps
  - colourful hearts - overflowing hearts
  - cool rian
  - countered terrain slabs
  - creative fly
  - creeper / enderman overhaul
  - cull less leaves
  - disable custom worlds advice
  - target dummy
  - dungeon now loading 1%
  - emojiful
  - enhanced block entities
  - entity culling
  - exposure - a fully fletched out camera mod - could be an event by itself
  - extra sounds - ui sounds
  - falling leaves
  - fast item frames
  - goblin traders
  - horse buff
  - immediately fast
  - immersive armours
  - immersive paintings - custom images for paintings
  - immersive thunder - new thunder sounds
  - indium
  - inmis inmis addon
  - items displayed
  - krypton
  - leaf me alone
  - levelz - skill progression system
  - lithium
  - lootr - player specific loot - everyone has loot
  - luck perms
  - macaw's doors / fences / paintings / paths / stairs / trapdoors
  - memory leak fix
  - mighty mail
  - mob player animator
  - modernfix
  - more culling
  - more mob variants
  - mouse tweaks
  - mouse wheelie
  - multi world border
  - nifty carts
  - noisium
  - not enough animations
  - presence footsteps
  - pufferfish skills - skill tree progression
  - right click harvest
  - sawmill - wood version of stone cutter
  - scout - backpack mod
  - simpy skills - skill tree
  - smooth swapping
  - sodium
  - soul fire'd
  - sound physics remastered
  - stack to nearby chests
  - structory
  - supplementaries
  - table top craft
  - tectonic
  - tiny item animations
  - tieredz
  - tide
  - tiny skeletons
  - universal bone meal
  - vanilla tweaks - new enchants & game mechanic tweaks
  - vin url music
  - yung's better structures
  - chested companions + cat loaf
  - inventory profiles next
  - dynamic crosshairs
  - infinity buttons
  - vanilla constructs
  - stellarity
  - bedspreads
  - keep some inventory
  - vtweaks
  - rain particle
  - pandas extra details
  - mastercutter - wood cutter
  - progressive bosses
  - break free + multi mine
  - advancement tracker
  - beans backpacks
  - spawners+
  - pet cemetery
  - bed spreads
  - fancy beds
  - back weapon slot
  - ydm weapon master
  - horse expert
  - portable wardrobes
  - hotbar swapper or cycler for pulling out different variants of items easily to
  - the hot bar without opening the inventory
  - model shifter
  - visual workbench
  - easel does it painting chooser mod
  - item borders
  - more mob variants
  - item highlighter
  - stack to nearby chests
  - repo speaking heads
  - pet your pets mod
  - recipe tweaks - trapdoor 6 planks into 8 trapdoor instead of 2
  - andesite stones can be used as cobblestone recipes
  - vein miner but animation is block by block
  </details>

- add icon.png (for prism launcher instance image), options.txt, servers.dat (for default comMC-SkyBlock server)
  - Forked - Datapack - Detect AFK Players - performant 3 mins AFK timer - `/trigger afk` command - WARNING make `/afk` command?
  - Forked - Datapack - AFK Dim Names
  - Datapack - Pause Day Cycle - day/weather is paused if players are AFK
  - Datapack - AFK Sleep - ignore AFK players when sleeping
  - Forked - Datapack - Sleep - regeneration after sleep - action bar announcement - supports AFK Sleep?
  - Nice Sitting Players - sit anywhere by holding `STRAFE LEFT` + `STRAFE RIGHT` for 2 seconds

## 2.2.0

- check all mod WARNINGs & see if they are fixable with fix.fork
- Check mods from [2.1.0](#210)
  - Cherished Worlds - set comMC-SkyBlock server as favourites
  - One Click Join - set up comMC-SkyBlock as the quick join server
  - Accessories - default_layout.fork
  - (Better) Shared Advancements - make sure advancements are syncing new/offline players
  - Simple Voice Chat - [server side set up](https://modrepo.de/minecraft/voicechat/wiki/server_setup)
    - Open the voice chat port (24454 UDP by default) In your servers firewall
  - Simple Voice Chat Enhanced Groups - verify if `/instantgroup`, `/persistentgroup`, etc. work
  - Subtle Effects - check server side functionality
  - Simple Discord RPC - [server config override set up](https://srpc.fdd-docs.com/server-config/)
  - Visuality Reforged - check if armour sparkle works in multiplayer
  - Resource Pack Overrides - make sure resource packs are enabled by default
  - RollingGate - check server side functionality
  - BetterTab - check if TPS & MSPT functionality on the server
  - Simple Discord Link - server side set up, update modded to SkyBlock info
  - Bookshelf - check if needed on server side
  - Prickle - check if needed on server side
  - ServuxForged - install server side
- Server Set Up

  - add all datapacks
  - [remove server seeker scraping](https://github.com/Funtimes909/ServerSeekerV2?tab=readme-ov-file#for-people-just-looking-to-not-be-scanned-anymore)
  - don't enforce chat signing with `enforce-secure-profile` in `server.properties`
  - <details><summary>pregenerate chunks with Distant Horizons</summary>

    - 4 for pregen - 2 when players are online
    - `numberOfThreads = 4`
    - 0.25 for pregen - 0.15 when players are online
    - `threadRunTimeRatio = "0.25"`
    </details>

## 2.1.0

- SkyBlock
  - SkyBlock Island Standard.dp - SkyBlock with biome map & structure bounding boxes according to its seed
  - SkyBlock Structures Worldgen.dp - generate structures (excluding ones disabled with Structurify.mod), including blocks, entities, & bounding boxes
  - SkyBlock Advancements.dp - modifies advancements to suit SkyBlock
  - SkyBlock Advancements.rp - image support for SkyBlock_Advancements.dp
- QoL & doesn't change mechanics
  - AdvancementInfo Reloaded - improved advancement menu UI
  - AppleSkin - Food/hunger values - inventory tooltips & HUD
  - Better "Add Server" - autofill server name - enter to confirm
  - Boat Item View - see held items like maps while using boats
  - Cherished Worlds - favourite worlds - top of the list - can't be deleted while pinned
  - Concentration - borderless fullscreen support
  - Controlling - key-bindings menu search bar
  - Delete Worlds To Trash - restore deleted worlds from system recycle bin
  - Eating Animation
  - Enchantment Descriptions - enchant descriptions, strictly within enchanting infusers from Enchanting_Infuser.mod - WARNING no item tooltip support because of EnhancedTooltips.mod - WARNING no Useful_Spyglass.mod support
  - Enchantment Level Language Patch - high level enchantments & potions are easier to read & numerical
  - Held Item Tooltips - item durability, enchants, shulker box contents, potion effects, rocket durations, etc. - WARNING doesn't integrate Durability_Tooltip.mod
  - One Click Join - quick join servers from main menu
  - Screenshot to Clipboard - copies automatically to the clipboard
  - Search Stats - search bar for statistics menu
  - What's That Slot? - query item options for slots - `LEFT ALT + HOVER`
  - YDM's Weapon Master - hotbar items show on your character - customise with `.`
- Improved mechanics

  - Accessories - extra wearable inventories for accessories - cosmetic armour - WARNING default layout config not supported
  - Curios Compat Layer for Accessories - Curios API support
  - BetterF3 - custom debug HUD - more legible - `F3` nerf - `F3 + M` (disabled coordinates by default - see #faq to re-enable)
  - Better Safe Bed - sleep if mobs can't target you
  - (Better) Shared Advancements - sync advancements (including offline players)
  - Better Statistics Screen - better statistics menu & pin specific statistics to your HUD
  - <details><summary>BoccHUD</summary>

    - custom permanent debug HUD
    - axolotol variant name
    - hive/nest bee/honey count
    - structure bounding boxes renderer
    - beacon/conduit range renderer
    - biome border renderer
    - slime chunks renderer
    - custom shape renderer
    - `B + C`
    </details>

  - Chat Heads
  - Chat Notify - ping sound when your name is mentioned
  - Longer Chat History - 100 ➔ 65000 messages - supports Server_Chat_Sync.mod
  - No Chat Reports - disables telemtry, chat, & player reporting - removes message indicator
  - Server Chat Sync - history while offline & rejoining
  - Chest Tracker - remembers/search for items in nearby inventories - `` ` `` for settings - search with `Y` - WARNING button position may overlap with other GUI elements
  - Clean Tooltips - extra tooltip for item colour info - enchants (with visual icons) are ordered by importance, max level, curses with colour - Clean_Tooltips_Patch.fork to format & order enchants, with in-built Visual_Enchantments.rp enchant icons - WARNING no Useful_Spyglass.mod support
  - EnhancedTooltips - tooltip info for durability, food status effects, extra armour / bucket of x / spawn egg preview - opinionated.fork
  - Colorize - `RMB` dyes on blocks - amethyst on glass - `+ CROUCH` vines for mossy variants
  - Condensed Creative - similar items are grouped in the creative menu
  - Connected Glass - adds glass types/recipes with connecting textures
  - Cut Through - attack foes behind blocks like tall grass
  - Death Finder - coordinates on death screen - distance from death - pet & named mobs support
  - Death Sorter - restores inventory layout after death
  - Dynamic Fire Overlay - no fire overlay if you have fire resistance
  - <details><summary>Easy Anvils</summary>

    - removed too expensive limit
    - `CROUCH + RMB` + name tag GUI
    - colours & text formatting in anvils & name tag GUI - style items & entity names
    - rename, repair, & enchant work changes - linear cost
    - free renames & doesn't damage anvil
    - `RMB` + iron block + anvil to repair one stage - automate with dispensers
    </details>

  - <details><summary>Easy Magic</summary>

    - custom reroll enchants with 1 lapis, 32 XP
    - full enchant outcome hint
    - tooltip for the hovered book in a chiseled bookshelf
    - non full blocks don't block enchanting power - water, carpets, etc.
    - semi automatic with hoppers
    - comparator lapis count support
    </details>

  - <details><summary>Enchanting Infuser</summary>

    - new upgradable enchant table
    - choose enchants
    - un-restricts some enchants (i.e. sharpness 5 on axe)
    </details>

  - <details><summary>Universal Enchants</summary>

    - feather falling prevents farmland trampling
    - infinity doesn't require arrows to use
    - looting & fortune grants more XP points
    - disabled projectile immunity frames
    - use enchants on more tools
    - Sword: Impaling
    - Axe: Sharpness, Smite, Bane of Arthropods, Knockback, Fire Aspect, Looting, Sweeping Edge, Impaling
    - Trident: Sharpness, Smite, Bane of Arthropods, Knockback, Fire Aspect, Looting, Sweeping Edge, Quick Charge, Piercing
    - Bow: Piercing, Multishot, Quick Charge, Looting
    - Crossbow: Flame, Punch, Power, Infinity, Looting
    - Horse Armor: Protection, Blast Protection, Fire Protection, Projectile Protection, Feather Falling, Respiration, Thorns, Depth Strider, Frost Walker, Curse of Binding, Soul Speed, Curse of Vanishing
    - Shield: Thorns, Knockback
    </details>

  - Enchantment Lore - open enchant books to read their description - even supports books with multiple enchants - Simple_Enchant_Descriptions.rp that supports Universal_Enchants.mod, Useful_Spyglass.mod changes
  - <details><summary>Easy Shulker Boxes</summary>

    - shulker works like a bundle
    - map tooltip - WARNING unexpected feature
    </details>

  - Elytra Physics - visual cape-like physics for elytra
  - Elytra Slot - Accessories.mod support for elytras - allowing you to wear armour with your elytra
  - GUI Clock - must be in inventory - day counter - WARNING hides behind turtle helmet status effect
  - GUI Compass - must be in inventory
  - <details><summary>Horse Buff</summary>

    - removes horseback mining fatigue
    - +0.1 blocks step height (i.e. path blocks)
    - horse swimming (disabled for camels & undead horses)
    - no random bucking/stopping
    - horse fade - transparent as you look down while mounted
    - horse head pitch offset - lower horse head for visibility
    - rainbow `jeb_` horses
    - toggle between player & horse inventory with `LEFT_ALT + INVENTORY`
    - rubberbanding fix on stairs
    </details>

  - Horse Expert - see stats of horse types with `LOOK + SHIFT + MONOCLE`
  - HorseInBoat - horse types sit in boats & hitbox change
  - <details><summary>Horseshoes</summary>

    - enchantable equippable horse gear to boost base mount speed & apply player-boot-items-like enchants
    - opinionated.fork
    - WARNING horseshoes don't appear enchantable in enchant table. only anvils & commands
    - WARNING thorns not working on horse armour/shoes
    - removed horse armour enchants that are more appropriate with horseshoes (Horseshoes.mod) counterpart (i.e. `Depth Strider`, `Feather Falling`, `Frost Walker`, `Soul Speed`)
    </details>

  - Immersive Armor HUD - armour info & durability above hotbar HUD - WARNING no Accessories.mod support
  - Inline - [inline text rendering support](https://modrinth.com/mod/inline#:~:text=for%20some%20examples%20!-,Player%20Facing%20Features,-Clientside) - i.e. items textures in text chat/signs/names & show off items you own in chat - WARNING player heads don't work properly in chat
  - Leave My Bars Alone - food & experience bars are visible when riding on a horse - fixes AppleSkin issue where saturation overlaps with mount HUD
  - <details><summary>Logical Efficient Tools</summary>

    - improved mining speed support for certain blocks - WARNING no Connected_Glass.mod glass support
    - <details><summary>Pickaxe</summary>

      - Glass
      - Glass panes
      - All stained glass colors
      - All stained glass pane colors
      - Tinted glass
      - Beacons
      - Glowstone
      - Sea lanterns
      - Redstone lamps
      - Levers
      - Frosted ice
      - Dragon eggs (if you can manage to mine it, at least...)
      - Turtle eggs
      - Sniffer eggs
      </details>

    - <details><summary>Axe</summary>

      - All bed colors
      - Skeleton skulls
      - Wither skeleton skulls
      - Player heads
      - Zombie heads
      - Creeper heads
      - Piglin heads
      - Dragon heads
      </details>

    - <details><summary>Shovel</summary>

      - Powder snow
      - Cakes
      - All candle cake colors
      </details>

    - <details><summary>Hoe</summary>

      - Cacti
      - Honeycomb blocks
      - Ochre froglights
      - Verdant froglights
      - Pearlescent froglights
      </details>

    - <details><summary>Shear</summary>

      - All carpet colors
      </details>

    </details>

  - Potion Icons - effect icons next to potion tooltips / overlayed over potion items - [typable by text](https://modrinth.com/mod/potionicons#:~:text=in%20the%20config.-,Typable%20in%20Text,-Effect%20icons%20can)
  - MinecraftCapes - custom capes (`J` by default)
  - Skin Restorer - enable player skins for when Minecraft authentication servers are down or for servers in offline/insecure mode
  - Skin Shuffle - in-game, real-time skin customization & management - WARNING no cape management support
  - Sodium Dynamic Lights - specific items/entities emit light dynamically
  - Multi Mine - mine the same block with other players, or mine other blocks with their own mining progress
  - Ping Wheel - communicate with pings using `MOUSE_5` - hold `LEFT_ALT` to also see player names
  - PlayerRevive - revive a player within 120 seconds after death - WARNING revive text is bugged
  - Raised - raises the hotbar so the selector is not cut off
  - RightClickHarvest - `RMB` replant crops automatically - hoe tiers increases radius
  - Simple Snowy Fix - snow generation on tree leaves
  - <details><summary>Snow! Real Magic!</summary>

    - snowy fence/wall/slab/stair/tallgrass
    - snow layers fall like sand
    - snow layers falling on water becomes ice
    - snow layers accumulate during snowstorms
    - snow layers have a thinner bounding box
    - snow reduces falled damage
    - blocks replace snow
    - `CROUCH + RMB` snow to make snowballs
    </details>

  - Snow Under Trees - snow under trees in snowy biomes
  - Smooth Scrolling - smoothly scroll chat, hotbar, menus, etc. - chat open/close animation
  - Spyglass Improvements - spyglass zoom scroll/keybind (`Z` by default) - Accessories.mod support - WARNING hiding zoom overlay, removes spyglass overlay
  - <details><summary>Useful Spyglass</summary>

    - Hwyla-like entity info (health, armour)
    - `marking` enchant glowing with `LMB`
    - `spotter` enchant marks nearby entities via eye of ender that detects invisible entities with `LMB`
    - `precision` enchant perfect accuracy & no gravity with `CROUCH + RANGE WEAPON`
    </details>

  - Stylish Effects - status effect display overhaul
  - Trade Cycling - cycle trades of villagers who haven't traded before
  - Toni's Immersive Lanterns - wear lanterns on your belt with Accessories.mod support - WARNING `CROUCH + RMB` to belt doesn't work
  - Wandering Pets - `CROUCH + RMB` to toggle pets' follow & wander states

- Additional Content

  - AmbientSounds - ambient sounds in the Minecraft world with mod support
  - <details><summary>Particular Reforged</summary>

    - 3D water splashes when breaking the surface of water
    - waterfalls spray ambient water particles
    - trees have falling leaves
    - cave dust
    - containers (like (ender) chests, barrels)
    - soul sand under (ender) chests randomly open them for air bubbles to escape
    - bubbles pop
    - rain/water drip ripples - WARNING doesn't work with shaders
    - cake eating particles
    - emissive lava drips - WARNING might not be working
    </details>

  - Sounds - adds sounds to block & UI interactions
  - Sound Physics Remastered - realistic sound attenuation, reverberation, & absorption through blocks - Simple_Voice_Chat.mod support
  - <details><summary>Subtle Effects</summary>

    - decaying/despawning leaves play sounds & particles
    - farmland trampled/dries out plays sounds & particles
    - experience bottle particles
    - sleeping Zs when entities are sleeping (includes beehives/nests)
    - mace attack will spawn a dust cloud
    - sparks float up from campfires, torches, candles, candle cakes, furnaces, lava (cauldrons), & fire
    - sparks using anvils, grindstones, & smithing tables
    - sparks minecarts landing on rails
    - reworked particles for smoke & replaces some with steam
    - puffs of dust come off glowstone/redstone blocks
    - poof of feathers when parrots are attacked
    - allays & vex have magic particles
    - amethyst blocks have sparkles
    - wool fluff when sheep are sheared
    - mushroom biome air dust
    - glowing dots spawn around command blocks when not in creative mode
    - coloured dots float up from powered beacons
    - compost textured particles appear when using a composter
    - stripping logs causes particles
    - carving pumpkins causes particles
    - bonemeal item particles when used
    - blue & green particles get pulled through the end portal
    - particles hover around end crystals
    - falling flowering azalea leaves
    - snow golems drop snow flakes when hit
    - snow balls have a snow flake trail when thrown
    - enderpearls & dragon fireballs have a trail of ender magic
    - fireflies spawn in swamps, mangrove swamps or around flowers at night
    - reworked particles for illagers casting spells
    - particles float around deep dark biome & sculk blocks
    - trapped souls escape from sculk catalysts & shriekers when broken
    - warden spawn 3 to 5 souls when they die
    - birch & flower forests have pollen in the air
    - respawn anchors spawn crying obsidian tears
    - dragon eggs spawn ender chest particles
    - torch flowers spawn flames & smoke like torches
    - burning entities spawn flames, smoke, & sparks
    - iron golems causes particles when they crack
    - ignited TNT causes sparks, smoke & flames
    - ignited creepers cause smoke & flames
    - spectral arrows cause glowstone dust
    - falling blocks (like sand, gravel, & concrete powder) have a trail of dust & play a sound when landing
    - cold biomes, with a light level below 10, humanoid entities will occasionally create a puff of steam from their mouth
    - air bubbles when humanoid entities are under water from their mouth, until they run out of air
    - flame particles & some sparks appear at the clicked location when using flint & steel to light a block (like candles, or campfires)
    - activated creaking hearts drip resin particles
    - slime block sounds make a sound when bouncing on them
    - slime block & oozing effect particles use slime block instead of slime item
    - particles when shearing beehives/nests
    - reworked particles for powder snow flakes
    - ender eyes placed in frames have rings & dot particles
    - ominous vaults are accordingly blue instead of orange
    - eggs have a splat particle if chickens don't spawn
    - snow flakes appear from entities when freezing
    - rain colour matching biome water colour
    - reworked particles when waxing off copper
    - increased item break particles
    </details>

  - <details><summary>Visuality Reforged</summary>

    - charged creepers have energy sparks
    - water circles on the surface of the water when raining
    - skeleton type entities scatter bones particles when hit
    - chickens scatter feather particles when hit
    - villagers scatter emeralds particles when hit
    - gold & diamond armour sparkle - WARNING not working
    - gold, diamond, & emerald ore sparkle
    - stepping on soul sand/soil causes soul particles
    - soul sand/soil causes ambient soul particles
    </details>

  - Camerapture - take/upload pictures - frame/album - `CROUCH + RMB` GUI - recipe_fix.fork
  - Carry On - carry blocks & non-hostile-entities around with `CROUCH + RMB` & empty hands
  - DiscCord - upload/custom music discs
  - ReForgedPlay - record, replay & edit gameplay
  - Simple Voice Chat - in-game voice chat
  - Simple Voice Chat Enhanced Groups - `/instantgroup` add nearby players to a VC group - `/persistentgroup` won't be deleted automatically
  - Voice Chat Interaction - SVC skulk sensor activation & warden detection

- Cosmetic
  - 3D Skin Layers
  - Fusion (Connected Textures)
  - Iris Shaders
  - Model Gap Fix
  - Simple Discord RPC - Discord status while playing
  - Tab Tweaks - custom player list HUD
  - What Are They Up To - player visuals for actions
- Resource Packs

  - 3D Mace
  - Animated Items
  - Better Fire - lower & transparent fire
  - Better HUD icons
  - Better Lanterns - 3D lanterns & chains - lanterns are held in your hand nicer
  - Bibliophilia - books look unique to their enchants - WARNING no Useful_Spyglass.mod support
  - Compact Font
  - Deep Origins Overlays - block transition textures
  - Distinct Dyes
  - Fresh Animations - entity animation overhaul - disabled by default
  - GUIdes - in-game wiki guides - GUIdes_Patch.fork to support Australian English
  - Gentler Weather Sounds
  - Improved Brewing Guide
  - Midnighttigger's Default Connected Textures - MDCT_patch.fork to remove connected glass to integrate with Connected_Glass.mod - WARNING no chiseled bookshelf support
  - Redstone Tweaks
  - Snowier Snow Layers! - snow layer overhangs on blocks below - WARNING snow layers on snow blocks looks bad
  - Unobtrusive Spawners
  - <details><summary>Vanilla Tweaks</summary>

    - <details><summary>Aesthetic</summary>

      - Desaturated Purpur
      - Desaturated Dark Oak
      - Brown Leather - Recolours leather realted items to use a similar palette to leather armour
      - Red Iron Golem Flowers
      - Rename 'Stem' to 'Log' - Renames "Crimson/Warped Stem/Hyphae" to "Crimson/Warped Log/Wood" - intuitive - WARNING no command support
      - Colorful Enchanting Table Particles
      - 1.21.2 Redstone Torch
      - HD Shield Banner Patterns
      - Splash Bottle o' Enchanting
      - Accurate Spyglass
      - Fencier Fences
      - Smoother Warped Planks
      - Horizontal World Border
      - Plain Leather Armor - removes brown stripes & overlays
      - Darker Dark Oak Leaves
      - Lush Grass (Mostly) All 'Round!
      - Circular Log Tops
      - Smoother Oak Log
      - Brighter Nether
      </details>

    - <details><summary>Utility</summary>

      - Unique Spawn Eggs
      - Unique Painting Items
      - Unique Axolotol Buckets
      - Visual Infested Stone (Items) - item texture only
      - Visual Waxed Copper (Items) - item texture only
      - Different Stems - differentiate melon & pumpkin
      - Age 25 Kelp - flowers on fully grown kelp
      - Music Disc Redstone Level Preview
      - Sticky Piston Sides
      - Directional Hoppers
      - Directional Dispensers & Droppers
      - Directional Observers
      - Compass Lodestone
      - Visual Honey Stages
      - Arabic Numerals - replaces roman with arabic numerals for enchants/potions
      </details>

    - <details><summary>Unobtrusive</summary>

      - Unobtrusive Rain
      - Unobtrusive Snow
      - Unobtrusive Scaffolding
      </details>

    - <details><summary>3D Models</summary>

      - Ladders
      - Rails
      - Iron Bars
      - Lily Pads
      - Doors & Trapdoors
      - Vines
      - Glow Lichen
      - Sculk Veins
      - Stonecutters
      </details>

    - <details><summary>Fun</summary>

      - Spinning Skull on Fire Painting
      </details>

    - <details><summary>Parity</summary>

      - Bedrock Piston Arms
      - Dungeons Mossy Skeleton
      </details>

    - <details><summary>Fixes & Consistency</summary>

      - Updated Observer Texture
      - Redstone Wire Fix
      - Big Dripleaf Stem Fix
      - Small Dripleaf Stem Fix
      - Consistent Blank Decorated Pot
      - Cactus Bottom Fix
      - Brighter Rib Armor Fix
      - Pixel Consistent Ghast
      - Pixel Consistent Guardian
      - Pixel Consistent Wither
      - Pixel Consistent Tripwire
      - Pixel Consistent Signs
      - Pixel Consistent Experience Orbs
      - Pixel Consistent Beacon Beam
      - Pixel Consistent Sonic Boom
      - Pixel Consistent Guardian Beam
      - Soul Soil Soul Campfire
      - Slime Particle Fix
      - Nicer Fast Leaves
      - Proper Break Particles
      - Don't Eat the Bowl!
      - Sandstone Wall Top Fix
      - Double Slab Fix
      - Corrected Item Holding
      - Hoe Fix
      </details>

    </details>

- Shader Packs
  - Complementary Shaders - Reimagined - on by default
- Performance
  - AI Improvements - disable look at goal (player or attack target) AI task - cause AIs to not face targets or walking directions - replaces default look controller with a more efficient version
  - Alternate Current - efficient & non-locational redstone dust fix
  - C2ME - performant chunk loading
  - Distant Horizons - further, but simpler render distance - pregenerating & multiplayer LOD sharing support
  - Sodium - optimised terrain, entities, GUIs, block entities, etc. renderer & improved categorised options menu
  - Embeddium Extra - visual bug fixes & more performance options
  - Entity Culling - hide Block-/Entities that aren't visible
  - GpuTape - fix VRAM leaks
  - More Culling - hide Block-/Entities that aren't visible
  - Fast IP Ping - ping/connect to servers faster
  - FerriteCore - memory optimisation
  - Let Me Despawn - despawns unintentional persistent mobs - drops their picked up or equipped items - configurable whitelist
  - ImmediatelyFast - speed up immediate mode rendering
  - Ksyxis - disabled spawn chunks being constantly loaded
  - Lithium - optimised game physics, mob AI, block ticking, etc.
  - Noisium - worldgen performance mod
  - Palladium - memory optimisation
  - Particle Core - particle culling & optimisation
  - Remove Reloading Screen - ignore reloading screens & resume gameplay
  - ScalableLux - performant light updates
  - ServerCore - dynamic server settings based on performance
- Monitoring & Management
  - Better ModList - hide mods/libraries & looks better
  - Configured Defaults - for game settings & resource packs for new installs
  - Death Backup - restore inventories after death (server management)
  - LuckPerms - permissions manager for servers
  - ModListMemory - mod list has memory of position
  - Reese's Sodium Options - alternative options menu for Sodium
  - Resource Pack Overrides - resource pack cleaner & manager
  - Resourcify - browse & update RP, DP, shaders in-game
  - RollingGate - technical game manager - instantly pickup experience orbs
  - SiliconeDolls - fake player spawning with `/player`
  - BetterTab - TPS & MSPT in tab list
  - ServerPlusPlus - `/here` to share coordinates in chat
  - SurvivalPlusPlus - calculator in chat with `=1+1*2/3^4` - creative no clip
  - Simple Discord Link - Discord & Minecraft whitelist integration
  - spark - client/server performance profiler
- Support Mods & Dependencies
  - Admiral - library for Brigadier - Simple_Voice_Chat_Enhanced_Groups.mod
  - Almanac - frikinjay's mods - Let_Me_Despawn.mod
  - Architectury API - abstraction layer for multiplatform mods - Death_Sorter.mod
  - Bookshelf - open source library - Enchantment_Descriptions.mod
  - Caelus API - elytra flight support - Elytra_Slot.mod
  - CIT Resewn - custom item texture support - Bibliophilia.rp
  - CITResewnNeoPatcher - CIT Resewn & Sinytra Connector support mod - CIT_Resewn.mod
  - Cloth Config API - config library - Better_ModList.mod
  - Collective - Serilum's mods - Death_Backup.mod
  - Continuity - efficient connected textures support - Deep_Origins_Overlays.rp
  - CoroUtil - Corosus's mods - What_Are_They_Up_To.mod
  - CraterLib - HypherionSA's mods - Simple_Discord_Link.mod & Simple Discord RPC
  - Entity Model Features - custom entity model support - Fresh_Animations.rp
  - Entity Texture Features - custom texture support for entities in resource packs - Fresh_Animations.rp
  - Forgified Fabric API - Fabric API implementation for NeoForge - Sinytra_Connector.mod
  - Fzzy Config - config API with GUI support - Subtle_Effects.mod
  - GroovyModLoader - Groovy programming language support - Eating_Animation.mod
  - JamLib - JamCoreModding's mods - RightClickHarvest.mod
  - Kotlin for Forge - Kotlin language loader - Resourcify.mod
  - LibJF - JFronny's mods - Respackopts.mod
  - MaFgLib - forge port of MaLiLib - masa's mods - BoccHUD.mod
  - MRU - IMB11's mods - Sounds.mod
  - owo-lib - GUI & config library - Accessories.mod
  - Prickle - JSON based configuration support - Enchantment_Descriptions.mod
  - Puzzles Lib - mod compatibility & porting library - Held_Item_Tooltip.mod
  - Respackopts - config menu support for resource packs - Redstone_Tweaks.rp
  - Searchables - searching & filtering library - Controlling.mod
  - Sinytra Connector - Fabric Compatibility Layer for NeoForge - Dynamic_Fire_Overlay.mod
  - Sodium Options API - config API for adding more Sodium option menus
  - SuperMartijn642's Config Lib - Durability_Tooltip.mod
  - SuperMartijn642's Core Lib - Connected_Glass.mod
  - TCDCommons API - TheCSDev's mods - Better_Statistics_Screen.mod
  - ToadLib - Mr.Toad's mods - Palladium.mod
  - TxniLib - Txni's mods - Toni's_Immersive_Lanterns.mod
  - YetAnotherConfigLib - config screen generator - Structurify.mod
- Server Only Mods
  - ServuxForged - extra support/features for client mods - BoccHUD.mod
