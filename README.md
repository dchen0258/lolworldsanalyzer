# League of Legends Worlds Analysis

Currently, Riot Games is hosting its League of Legends World Championship. I want to use the Riot API to get information about teams and players’ champion pools and solo queue (playing the game by themselves outside of the game) answer some statistics about the current champions and win rates in these games compared to the games they are playing on stage (at the tournament) and creating a model to predict the win rate for a team vs another team based on these performances, along with their champion picks. I also hope to gather so broader statistics about the best champion pairings per team (ones with the highest win rates)

Week 4: Get API connection set up and basic player and team information set up. (After some playing around, the API is not as kind as I would have hoped and does not cotain match data for the tournamnet since it is a LAN event so I will use CSVs).
Week 5: Get basic statistics, given a player or team (win rates per champion, overall win rate).
Week 6: Play around with models to see the what model is best to predict game performance based on past performance and champion picks.
Week 7: Finalize model and start assessing predictions.
Week 8: Calculate more advanced statistics, like best champion pairings for teams.
Week 9: Clean up codebase and write documentation explaning how to run models.

What is League of Legends?

League of legends is a 5v5 MOBA (multiplayer online battle arena) that can be likened to a war game simulation. You recruit a champion for Runeterra alongside 4 other players in order to take down and destroy the enemy nexus (the goal of the game). Each champion comes with their unique spells, passives, and playstyles, and can sometimes even have special abilities depending on the allied champions or enemy champions.

The main objective
As a team, you must move forward towards the enemy land, destroy their defensive towers (think of outposts), slay their minions (think of troops) to acquire gold, and kill the enemies to make a path towards their nexus.

Resources
Each team is provided with a shop in their base, and a fountain that heals them upon standing on it. The fountain is the location you start every game at. If you die, you will respawn here. You can only access the shop from the fountain. The shop's currency is gold and that is the second main resource you will need in order to grow stronger. Using gold, you can buy completed items, or if you can't afford it, you can buy the pieces to the item until you have enough to combine the individual pieces to create the full item (think of buying ingredients to a potion). To get gold, you need to kill things. Enemy minions, neutral monsters that lurk in the jungle, enemy champions, enemy towers, heck even the nexus gives gold!

The first main resource is experience. Every champion has specific stats. How much base health, mana, attack damage, attack speed, armor, etc is different for each champion, but these stats automatically increase as you level up. This isn't the only thing you get from leveling up though. You also get ability points. You can use these ability points to unlock new abilities, or to upgrade your current abilities. This makes experience a highly prized resource. You get experience from being near enemies when they die (or killing them yourself).