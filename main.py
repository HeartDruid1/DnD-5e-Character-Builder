###

import random

def rolld6():
    return random.randint(3,18)

def standardArray():
    stdArrayNums = [15, 14, 13, 12, 10, 8]
    stdStrength = random.choice(stdArrayNums)
    stdArrayNums.remove(stdStrength)
    stdDexterity = random.choice(stdArrayNums)
    stdArrayNums.remove(stdDexterity)
    stdConstitution = random.choice(stdArrayNums)
    stdArrayNums.remove(stdConstitution)
    stdIntelligence = random.choice(stdArrayNums)
    stdArrayNums.remove(stdIntelligence)
    stdWisdom = random.choice(stdArrayNums)
    stdArrayNums.remove(stdWisdom)
    stdCharisma = random.choice(stdArrayNums)

    return [stdStrength, stdDexterity, stdConstitution, stdIntelligence, stdWisdom, stdCharisma]

def rollForStats():
    rollStrength = rolld6()
    rollDexterity = rolld6()
    rollConstitution = rolld6()
    rollIntelligence = rolld6()
    rollWisdom = rolld6()
    rollCharisma = rolld6()

    return [rollStrength, rollDexterity, rollConstitution, rollIntelligence, rollWisdom, rollCharisma]

def displayStats(pcName, stats):
    print('Name: ' + pcName)
    print('**********************')
    print('Strength: ' + str(stats[0]))
    print('Dexterity: ' + str(stats[1]))
    print('Constitution: ' + str(stats[2]))
    print('Intelligence: ' + str(stats[3]))
    print('Wisdom: ' + str(stats[4]))
    print('Charisma: ' + str(stats[5]))


print('*********************************************')
print("Nick Ferguson's Easy Character Builder For 5e")
print('*********************************************\r\n')
print('Please enter your character name to begin')
characterName = input('>>> ')

print('Would you like to roll for stats, or use the standard array?')
print('1) Roll For Stats')
print('2) Standard Array')
print('*Please select the standard array choice for Adventurers League PCs')
menuSelect = int(input('>>> '))
if menuSelect == 1:
    stats = rollForStats()
    displayStats(characterName, stats)
elif menuSelect == 2:
    stats = standardArray()
    displayStats(characterName, stats)
else:
    print('That is not a valid option')


