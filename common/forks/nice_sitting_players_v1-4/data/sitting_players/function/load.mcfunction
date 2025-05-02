##additional Scoreboards
scoreboard objectives add sit trigger {"text": "Sit"}
scoreboard objectives add sitting_players.technical dummy

##init schedules
schedule function sitting_players:run 5t