execute as @e[type=minecraft:block_display,tag=sit_display] at @s unless entity @a[distance=..5,sort=nearest] run tag @s add remove_sit
execute as @e[type=minecraft:block_display,tag=sit_display] at @s if block ~ ~-1 ~ #eden:non_solid_blocks run tag @s add remove_sit
kill @e[type=minecraft:block_display,tag=remove_sit]