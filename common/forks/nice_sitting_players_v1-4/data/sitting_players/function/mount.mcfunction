tag @s[nbt={OnGround:1b}] add sits_down
execute as @a[tag=sits_down] at @s run summon block_display ~ ~ ~ {Tags:[sit_display]}
execute as @a[tag=sits_down] at @s run ride @s mount @n[type=block_display,tag=sit_display,distance=..1]

scoreboard players set @s sit 0
tag @s remove sits_down