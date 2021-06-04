#### TO DO ####

# Sufix Spacetime: Add cooldown somewhere (perhaps on the skills part)

################### Items ##########################


Weapon={
    'Weapon':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

### Daggers ###

    'Vesper Spite':{'Class': ['Hunter', 'Assassin', 'Saboteur', 'Soulweaver', 'Alchemist', 'Shinobi'],
    'Dmg': 325, 'HP': 0,'Mana': 0,'Atk': 65,'Mag': 0,'Defense': 35,'Resist': 35,'Speed': 9,'Spell_Haste': 0,'Lifesteal': 20,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 20, 'Threat': 0}, # Soulweaver can also use

    'Grimfell':{'Class': ['Hunter', 'Assassin', 'Saboteur', 'Alchemist', 'Shinobi'],
    'Dmg': 300, 'HP': 0,'Mana': 0,'Atk': 20,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 20,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 25, 'Threat': 0, 'Perc': {'Atk': 0.08}},

    'Bloodreign':{'Class': ['Hunter', 'Assassin', 'Saboteur', 'Soulweaver', 'Alchemist', 'Shinobi'],
    'Dmg': 420, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 15,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0}, # add crit damage

    'Indra':{'Class': ['Hunter', 'Assassin', 'Soulweaver', 'Alchemist', 'Shinobi'],
    'Dmg': 200, 'HP': 0,'Mana': 0,'Atk': 10,'Mag': 0,'Defense': 15,'Resist': 15,'Speed': 35,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 20,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 35,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0, 'Perc': {'Speed': 0.1}},

    'Moonsinger Sickle':{'Class': ['Hunter', 'Assassin', 'Saboteur', 'Soulweaver', 'Alchemist'],
    'Dmg': 110, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 50,'Defense': 0,'Resist': 0,'Speed': 50,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 20,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 16,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 12, 'Threat': 0},

    'Treants Spine':{'Class': ['Hunter', 'Assassin', 'Saboteur', 'Soulweaver', 'Alchemist', 'Shinobi'],
    'Dmg': 300, 'HP': 2000,'Mana': 0,'Atk': 35,'Mag': 35,'Defense': 15,'Resist': 15,'Speed': 35,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 20,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 40,'Light': 0,'Dark': 0, 'Threat': 0},

    'Switch Blade':{'Class': ['Hunter'],
    'Dmg': 260, 'HP': 0,'Mana': 0,'Atk': 35,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 35,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 20,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 50},

    'Crimson Agony':{'Class': ['Assassin'],
    'Dmg': 300, 'HP': 0,'Mana': 0,'Atk': 20,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 20,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 20,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 30, 'Threat': 0, 'Perc': {'Atk': 0.08}},

    'Kage':{'Class': ['Shinobi'],
    'Dmg': 325, 'HP': 0,'Mana': 0,'Atk': 40,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 35,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 20,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 40, 'Threat': 0},

    'Andariel Claw':{'Class': ['Hunter','Assassin','Shinobi'],
    'Dmg': 190, 'HP': 0,'Mana': 0,'Atk': 40,'Mag': 0,'Defense': 0,'Resist': 15,'Speed': 25,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 30, 'Threat': 0},

    'Andariel Oath':{'Class': ['Necromancer', 'Saboteur', 'Dreadknight'],
    'Dmg': 190, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 30,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 30, 'Threat': 0, 'Perc': {'Mag': 0.05}},

    'Jeweled Kris':{'Class': ['Assassin', 'Shinobi', 'Saboteur', 'Alchemist'],
    'Dmg': 335, 'HP': 0,'Mana': 0,'Atk': 45,'Mag': 45,'Defense': 0,'Resist': 0,'Speed': 25,'Spell_Haste': 8,'Lifesteal': 0,'Tenacity': 0,'Crit': 15,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 25,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

### Bows ###
    'The Matriarch':{'Class': ['Hunter', 'Sniper'],
    'Dmg': 350, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 15,'Resist': 15,'Speed': 50,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 50,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 5},

    'Crimson Arch':{'Class': ['Sniper'],
    'Dmg': 680, 'HP': 0,'Mana': 0,'Atk': 15,'Mag': 15,'Defense': 0,'Resist': 0,'Speed': 60,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 30,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Drowned Wench':{'Class': ['Sniper', 'Hunter'],
    'Dmg': 335, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 45,'Speed': 45,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 5,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 25,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

### Swords ###

    'Amethyst Challenger':{'Class': ['Soldier', 'Warlord', 'Vanguard', 'Paladin', 'Paladin Wrath', 'Paladin Mercy','Paladin Protector'],
    'Dmg': 260, 'HP': 0,'Mana': 0,'Atk': -200,'Mag': -200,'Defense': 50,'Resist': 200, 'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 20,'Light': 0,'Dark': 0, 'Threat': 0, 'Perc':{'Resist': 0.25, 'Speed': 0.2, 'Threat': 2.5}},
        
    'Excalibur':{'Class': ['Soldier', 'Warlord', 'Vanguard', 'Paladin', 'Paladin Wrath', 'Paladin Mercy','Paladin Protector'],
    'Dmg': 700, 'HP': 2500,'Mana': 1000,'Atk': 50,'Mag': 25,'Defense': 50,'Resist': 25,'Speed': 25,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 50,'Dark': 0, 'Threat': 0},

    'Earthen Defender':{'Class': ['Soldier', 'Warlord', 'Vanguard', 'Paladin', 'Paladin Wrath', 'Paladin Mercy','Paladin Protector'],
    'Dmg': 150, 'HP': 3000,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 75,'Resist': 75,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 20,'Light': 0,'Dark': 0, 'Threat': 0, 'Perc':{'Atk': -0.2, 'Mag': -0.2, 'Threat': 100}},

    'Crystal Phalanx':{'Class': ['Vanguard', 'Dreadknight', 'Paladin', 'Paladin Wrath', 'Paladin Mercy','Paladin Protector'],
    'Dmg': 300, 'HP': 1850,'Mana': 0,'Atk': 20,'Mag': 0,'Defense': 45,'Resist': 45,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0, 'Perc':{'Atk': 0.04}},

    'Pearlescense':{'Class': ['Soldier', 'Warlord', 'Vanguard', 'Paladin', 'Paladin Wrath', 'Paladin Mercy','Paladin Protector', 'Blademaster'],
    'Dmg': 1000, 'HP': 1850,'Mana': 0,'Atk': 20,'Mag': 0,'Defense': 45,'Resist': 45,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 25,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0, 'Perc':{'Atk': 0.04}},

    'Thor':{'Class': ['Soldier', 'Warlord', 'Vanguard', 'Paladin', 'Paladin Wrath', 'Paladin Mercy','Paladin Protector'],
    'Dmg': 550, 'HP': 0,'Mana': 0,'Atk': 45,'Mag': 0,'Defense': 15,'Resist': 15,'Speed': 45,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 50,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},    

    'Vespers Visage':{'Class': ['Soldier', 'Warlord', 'Vanguard', 'Paladin', 'Paladin Wrath', 'Paladin Mercy','Paladin Protector'],
    'Dmg': 600, 'HP': 1500,'Mana': 0,'Atk': 65,'Mag': 0,'Defense': 35,'Resist': 35,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 20,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 50, 'Threat': 0},

    'Executioner Axe':{'Class': ['Soldier'],
    'Dmg': 500, 'HP': 0,'Mana': 0,'Atk': 60,'Mag': 0,'Defense': 40,'Resist': 40,'Speed': 30,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Giant Blade':{'Class': ['Warlord', 'Paladin', 'Paladin Wrath', 'Paladin Mercy','Paladin Protector'],
    'Dmg': 1600, 'HP': 1500,'Mana': 0,'Atk': 50,'Mag': 0,'Defense': 50,'Resist': 50,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Crimson Glaive':{'Class': ['Aquamancer', 'Dragonslayer'],
    'Dmg': 400, 'HP': 0,'Mana': 0,'Atk': 50,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 50,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 40,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'The Royale':{'Class': ['Vanguard'],
    'Dmg': 100, 'HP': 1500,'Mana': 0,'Atk': 25,'Mag': 0,'Defense': 50,'Resist': 40,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 50},

    'Andariel Spine':{'Class': ['Vanguard', 'Paladin', 'Paladin Wrath', 'Paladin Mercy','Paladin Protector', 'Dreadknight'],
    'Dmg': 200, 'HP': 5000,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 35,'Resist': 35,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 15, 'Threat': 0, 'Perc':{'Speed': -0.1}},

    'Andariel Mutilator':{'Class': ['Warlord', 'Soldier'],
    'Dmg': 1200, 'HP': 0,'Mana': 0,'Atk': 45,'Mag': 0,'Defense': 15,'Resist': 15,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 30, 'Threat': 0},

    'Slayer of Andariel':{'Class': ['Dragonslayer'],
    'Dmg': 310, 'HP': 0,'Mana': 0,'Atk': 40,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 40, 'Threat': 0},
    
    'Voidmother':{'Class': ['All'],
    'Dmg': 1000, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0, 'Perc':{'HP': 0.15, 'Mana': 0.15, 'Atk': 0.2,'Mag': 0.2,'Defense': 0.2,'Resist': 0.2,
    'Speed': 0.2, 'Fire': 0.2,'Water': 0.2,'Wind': 0.2,'Earth': 0.2,'Light': 0.2,'Dark': 0.2 }},

    'Jeweled Vigilant':{'Class': ['Vanguard', 'Paladin'],
    'Dmg': 380, 'HP': 2500,'Mana': 250,'Atk': 0,'Mag': 0,'Defense': 45,'Resist': 45,'Speed': 0,'Spell_Haste': 15,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 10,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 1000},

    'Murderous Pike':{'Class': ['Dragonslayer'],
    'Dmg': 740, 'HP': 0,'Mana': 0,'Atk': 55,'Mag': 0,'Defense': 15,'Resist': 15,'Speed': 45,'Spell_Haste': 0,'Lifesteal': 16,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Fleshrender':{'Class': ['Warlord', 'Einherjar'],
    'Dmg': 875, 'HP': 0,'Mana': 0,'Atk': 65,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 45,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 100,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

### Katana ###

    'Sakura Petal':{'Class': ['Ronin'],
    'Dmg': 400, 'HP': 0,'Mana': 0,'Atk': 25,'Mag': 0,'Defense': 15,'Resist': 15,'Speed': 25,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 10,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 30,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Kage-Hi':{'Class': ['Ronin'],
    'Dmg': 300, 'HP': 0,'Mana': 0,'Atk': 50,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 5,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 30, 'Threat': 0},
    
    'Crimson-Tech Katana':{'Class': ['Ronin'],
    'Dmg': 450, 'HP': 0,'Mana': 0,'Atk': 40,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 40,'Spell_Haste': 0,'Lifesteal': 20,'Tenacity': 0,'Crit': 10,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 35, 'Threat': 110},

    'Cloudwalker':{'Class': ['Ronin', 'Shinobi'],
    'Dmg': 620, 'HP': 0,'Mana': 0,'Atk': 35,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 25,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 5,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 25,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Stolen Treasure':{'Class': ['Ronin', 'Blademaster'],
    'Dmg': 650, 'HP': 0,'Mana': 0,'Atk': 55,'Mag': 0,'Defense': 25,'Resist': 25,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 5,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0, 'Perc':{'HP': 0.20}},    

### Wands ###

    'Apocrypha':{'Class': ['Acolyte', 'Druid', 'Elementalist', 'Timeweaver', 'Aquamancer', 'Necromancer'],
    'Dmg': 25, 'HP': 0,'Mana': 1000,'Atk': 0,'Mag': 80,'Defense': 10,'Resist': 25,'Speed': 15,'Spell_Haste': 0,'Lifesteal': 25,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 20, 'Threat': 0},

    'Barksinger':{'Class': ['Acolyte', 'Druid', 'Elementalist', 'Timeweaver', 'Aquamancer', 'Necromancer'],
    'Dmg': 25, 'HP': 850,'Mana': 500,'Atk': 0,'Mag': 60,'Defense': 40,'Resist': 40,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 20,'Light': 0,'Dark': 0, 'Threat': 0},

    'Sunsayer':{'Class': ['Acolyte', 'Druid', 'Elementalist', 'Timeweaver', 'Aquamancer', 'Necromancer', 'Pyromancer'],
    'Dmg': 30, 'HP': 0,'Mana': 1200,'Atk': 0,'Mag': 60,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 30,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0, 'Perc':{'Mana': 0.05}},

    'Howling Gale':{'Class': ['Acolyte', 'Druid', 'Elementalist', 'Cleric', 'Necromancer'],
    'Dmg': 40, 'HP': 0,'Mana': 1500,'Atk': 0,'Mag': 45,'Defense': 0,'Resist': 0,'Speed': 45,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 30,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0, 'Perc':{'Mana': 0.05}},

    'Stoneblossom':{'Class': ['Acolyte', 'Druid', 'Elementalist', 'Cleric', 'Necromancer'],
    'Dmg': 40, 'HP': 0,'Mana': 1500,'Atk': 0,'Mag': 45,'Defense': 0,'Resist': 0,'Speed': 45,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 30,'Light': 0,'Dark': 0, 'Threat': 0, 'Perc':{'Mana': 0.05}},

    'Zeus':{'Class': ['Acolyte', 'Druid', 'Elementalist', 'Timeweaver', 'Necromancer', 'Pyromancer', 'Aquamancer'],
    'Dmg': 35, 'HP': 0,'Mana': 1000,'Atk': 0,'Mag': 65,'Defense': 0,'Resist': 0,'Speed': 35,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 5,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 20,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Heaven Banquet':{'Class': ['Cleric', 'Timeweaver'],
    'Dmg': 40, 'HP': 0,'Mana': 1500,'Atk': 0,'Mag': 45,'Defense': 0,'Resist': 0,'Speed': 45,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 30,'Dark': 0, 'Threat': 0, 'Perc':{'Mana': 0.05}},

    'Infinite Void':{'Class': ['Necromancer'],
    'Dmg': 50, 'HP': 0,'Mana': 1500,'Atk': 0,'Mag': 45,'Defense': 0,'Resist': 0,'Speed': 45,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 30, 'Threat': 0, 'Perc':{'Mana': 0.05}},

    'True Ice':{'Class': ['Elementalist', 'Aquamancer'],
    'Dmg': 30, 'HP': 0,'Mana': 1500,'Atk': 0,'Mag': 40,'Defense': 0,'Resist': 40,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 30,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0, 'Perc':{'Mana': 0.05}},

    'Poseidon Envy':{'Class': ['Aquamancer'],
    'Dmg': 200, 'HP': 0,'Mana': 0,'Atk': 50,'Mag': 50,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 15,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 40,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Manatear Rod':{'Class': ['Acolyte'],
    'Dmg': 100, 'HP': 0,'Mana': 2000,'Atk': 0,'Mag': 60,'Defense': 0,'Resist': 30,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 50, 'Perc':{'Mana': 0.1}},

    'Cursed Stave':{'Class': ['Necromancer'],
    'Dmg': 100, 'HP': 1200,'Mana': 800,'Atk': 0,'Mag': 35,'Defense': 25,'Resist': 25,'Speed': -20,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 40, 'Threat': 50},

    'Grovetender':{'Class': ['Druid'],
    'Dmg': 100, 'HP': 500,'Mana': 1500,'Atk': 0,'Mag': 35,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 40,'Light': 0,'Dark': 0, 'Threat': 50},

    'Archangel':{'Class': ['Cleric'],
    'Dmg': 140, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 50,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 40,'Dark': 0, 'Threat': 50},

    'Timekeeper Stave':{'Class': ['Timeweaver'],
    'Dmg': 170, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 40,'Defense': 0,'Resist': 0,'Speed': 40,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 35,'Dark': 35, 'Threat': 0},

    'Elementaris':{'Class': ['Elementalist'],
    'Dmg': 100, 'HP': 0,'Mana': 1000,'Atk': 0,'Mag': 50,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 25,'Water': 25,'Wind': 25,'Earth': 25,'Light': 0,'Dark': 0, 'Threat': 50, 'Perc':{'Fire': 0.04,'Water': 0.04,'Wind': 0.04,'Earth': 0.04}},

    'Andariel Wisdom':{'Class': ['Aquamancer','Necromancer','Pyromancer','Elementalist', 'Acolyte', 'Timeweaver'],
    'Dmg': 115, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 30,'Defense': 30,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 25,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 30, 'Threat': 0, 'Perc':{'Mag': 0.15}},

    'Molten Heart':{'Class': ['Elementalist','Pyromancer'],
    'Dmg': 250, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 55,'Defense': 0,'Resist': 15,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 25,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Holy Jewel':{'Class': ['Cleric', 'Druid', 'Paladin', 'Acolyte'],
    'Dmg': 100, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 45,'Defense': 0,'Resist': 45,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 35,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Corrupted Jewel':{'Class': ['Elementalist', 'Necromancer', 'Acolyte'],
    'Dmg': 100, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 60,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 25,'Water': 25,'Wind': 25,'Earth': 25,'Light': 25,'Dark': 25, 'Threat': 0},

    'Sacrificial Totem':{'Class': ['Necromancer', 'Timeweaver'],
    'Dmg': 150, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 55,'Defense': 0,'Resist': 25,'Speed': 15,'Spell_Haste': 0,'Lifesteal': 16,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

### Scythes ###

    'Jungle Bulwark':{'Class': ['Dreadknight'],
    'Dmg': 420, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 75,'Resist': 75,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 40,'Dark': 0, 'Threat': 0, 'Perc':{'Mag': -0.1, 'Threat': 100}},  

    'Kirin':{'Class': ['Dreadknight'],
    'Dmg': 400, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 50,'Resist': 40,'Speed': 40,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 45, 'Threat': 0},

    'Soulfire Scythe':{'Class': ['Dreadknight'],
    'Dmg': 250, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 15,'Defense': 40,'Resist': 40,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 30, 'Threat': 550, 'Perc':{'HP': 0.2, 'Mana': 0.1, 'Defense': 0.05, 'Resist': 0.05}},

    'Man Eater':{'Class': ['Dreadknight'],
    'Dmg': 465, 'HP': 3300,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 66,'Resist': 66,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 25, 'Threat': 1200, 'Perc':{'Defense': 0.06, 'Resist': 0.06}},

### Fist ###

    'Ki Manipulator (Ruby)':{'Class': ['Monk'],
    'Dmg': 500, 'HP': 750,'Mana': 750,'Atk': 25,'Mag': 0,'Defense': 0,'Resist': 25,'Speed': 25,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0, 'Fire': 25,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},  


}

Armor={
    'Armor':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Fiend Regalia':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 150,'Resist': 150,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 10,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Void Coil':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 140,'Resist': 140,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0, 'Perc':{'HP': 0.1, 'Mana':0.1}},

    'Demonic Robe':{'Class': ['Acolyte','Elementalist','Druid','Timeweaver','Alchemist','Cleric','Aquamancer','Pyromancer','Necromancer'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 100,'Resist': 200,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Demonic Mail':{'Class': ['Hunter','Assassin','Druid','Saboteur','Monk','Sniper','Shinobi'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 150,'Resist': 150,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Demonic Hauberk':{'Class': ['Soldier','Warlord','Vanguard','Paladin','Paladin Wrath','Paladin Mercy','Paladin Protector','Dreadknight','Dragonslayer'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 200,'Resist': 100,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Crimson Regalia':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 150,'Resist': 150,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Demon Regalia':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 150,'Mag': 150,'Defense': 0,'Resist': 0,'Speed': 150,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Shade Regalia':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 150,'Resist': 150,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Shaman Regalia':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 150,'Resist': 150,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0, 'Perc':{'Mana': 0.25}},

    'Giant Regalia':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 150,'Resist': 150,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0, 'Perc':{'HP': 0.5, 'Atk': -0.15,'Mag': -0.15,'Defense': -0.15,'Resist': -0.15,'Speed': -0.15,
    'Fire': -0.15,'Water': -0.15,'Wind': -0.15,'Earth': -0.15,'Light': -0.15,'Dark': -0.15}},

    'Leprechaun Regalia':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 150,'Resist': 150,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 15,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Serpent Regalia':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 150,'Resist': 150,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Stormbreaker':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 180,'Resist': 180,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0, 'Perc':{'Speed': 0.1, 'Wind': 0.1}}
}

Offhand={
    'Off-hand':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Guilded Quiver':{'Class': ['Hunter', 'Sniper'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 40,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Spellfire Focus':{'Class': ['Acolyte', 'Elementalist', 'Druid', 'Timeweaver', 'Alchemist', 'Cleric', 'Monk', 'Necromancer', 'Aquamancer', 'Pyromancer'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 35,'Water': 35,'Wind': 35,'Earth': 35,'Light': 35,'Dark': 35, 'Threat': 0},

    'Frozen Loom':{'Class': ['Aquamancer'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 40,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 30,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Stone of Haltazar':{'Class': ['Alchemist'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 40,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 30,'Light': 0,'Dark': 0, 'Threat': 0},

    'Godfall Quiver':{'Class': ['Hunter', 'Sniper'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 75,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 30,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Dragonhide Deflector':{'Class': ['Soldier', 'Warlord', 'Vanguard', 'Dragonslayer', 'Dreadknight'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 50,'Mag': 0,'Defense': 25,'Resist': 25,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 50,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Camelot':{'Class': ['Warlord', 'Vanguard', 'Dragonslayer', 'Dreadknight', 'Paladin','Paladin Wrath','Paladin Mercy','Paladin Protector'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 50,'Resist': 50,'Speed': 50,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 15,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 500},

    'Thundarius':{'Class': ['Warlord'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 75,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Immovable Object':{'Class': ['Vanguard'],
    'Dmg': 0, 'HP': 2000,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 45,'Resist': 45,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Righteous Shield':{'Class': ['Paladin','Paladin Wrath','Paladin Mercy','Paladin Protector'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 25,'Mag': 25,'Defense': 25,'Resist': 25,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 35,'Dark': 0, 'Threat': 0, 'Perc':{'HP': 0.15, 'Mana': 0.15}},

    'Crucifix':{'Class': ['Hunter', 'Assassin', 'Saboteur', 'Shinobi', 'Ronin'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 100,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Brewed Devilment':{'Class': ['Saboteur'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 40,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 30,'Light': 0,'Dark': 0, 'Threat': 0},

    'Seitsugan':{'Class': ['Ronin'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 75,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0}

}

Accessory={
    'Accessory':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Subterfuge Cloak':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 20,'Resist': 0,'Speed': 50,'Spell_Haste': 10,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0, 'Perc':{'Speed': 0.1}},

    'Rejuvination Ring':{'Class': ['All'],
    'Dmg': 0, 'HP': 1000,'Mana': 1000,'Atk': 15,'Mag': 15,'Defense': 15,'Resist': 15,'Speed': 15,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Universal Ring':{'Class': ['All'],
    'Dmg': 0, 'HP': 500,'Mana': 500,'Atk': 25,'Mag': 25,'Defense': 25,'Resist': 25,'Speed': 25,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 35,'Water': 35,'Wind': 35,'Earth': 35,'Light': 35,'Dark': 35, 'Threat': 0},

    'Pearl Shell':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 50,'Defense': 0,'Resist': 50,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 30,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Crimson Visage':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 40,'Mag': 40,'Defense': 0,'Resist': 0,'Speed': 40,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 30,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 30, 'Threat': 0},

    'Fox Spirit Mask':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 40,'Defense': 0,'Resist': 40,'Speed': 40,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 25,'Water': 0,'Wind': 25,'Earth': 0,'Light': 25,'Dark': 0, 'Threat': 0},

    'Fault Ring':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 35,'Mag': 35,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 35,'Light': 0,'Dark': 0, 'Threat': 0},

    'Heartfire Charm':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 100,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Entropy Ring':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 35,'Mag': 35,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 35, 'Threat': 0},

    'Fear Ring':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 35,'Mag': 35,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 35, 'Threat': 0},

    'Woodland Heart':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 35,'Mag': 35,'Defense': 35,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 30,'Light': 0,'Dark': 0, 'Threat': 0}


}

Soul={
    'Soul':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Soul of the Ancients':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 25,'Mag': 25,'Defense': 25,'Resist': 25,'Speed': 25,'Spell_Haste': 10,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Dragonfire Soul':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 50,'Mag': 50,'Defense': 0,'Resist': 0,'Speed': 50,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Treant Soul':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 35,'Resist': 35,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 25,'Light': 0,'Dark': 0, 'Threat': 0},

    'Andariel Soul':{'Class': ['All'],
    'Dmg': 0, 'HP': 500,'Mana': 250,'Atk': 0,'Mag': 0,'Defense': 10,'Resist': 10,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 18,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Voidfire Soul':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 25,'Mag': 25,'Defense': 25,'Resist': 25,'Speed': 25,'Spell_Haste': 0,'Lifesteal': 20,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 50, 'Threat': 0},

    'Navel Core':{'Class': ['All'],
    'Dmg': 0, 'HP': 2500,'Mana': 500,'Atk': 35,'Mag': 35,'Defense': 35,'Resist': 35,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 50,'Water': 0,'Wind': 0,'Earth': 50,'Light': 0,'Dark': 0, 'Threat': 0},

    'Unicorn Soul':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 40,'Dark': 0, 'Threat': 0},

    'Jackal Soul':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 30,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 30,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Soul of Atlantis':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 50,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 50,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0, 'Perc':{'Mana': 0.1}},

    'Stormfront Soul':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 50,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Soul of the Harvest':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0, 'Perc':{'Water': 0.1, 'Wind': 0.1, 'Earth': 0.1}},

    'Gnoglin Soul':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 40,'Mag': 40,'Defense': -25,'Resist': -25,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Soul of the Phoenix':{'Class': ['All'],
    'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 50,'Water': 0,'Wind': 50,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0}

}

#################### Class ##############

Base_Stats={
    'Class':{'Dmg': 0,'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,
    'Luck': 0,'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0,'Threat': 0},

    'Hunter':{'Dmg': 0,'HP': 17450,'Mana': 1200,'Atk': 112,'Mag': 44,'Defense': 49,'Resist': 44,'Speed': 84,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,
    'Luck': 0,'Dodge': 10,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0,'Threat': 0},

    'Assassin':{'Dmg': 0,'HP': 14450,'Mana': 1200,'Atk': 127,'Mag': 34,'Defense': 5,'Resist': 5,'Speed': 128,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,
    'Luck': 0,'Dodge': 10,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0,'Threat': 0},

    'Saboteur':{'Dmg': 0,'HP': 15990,'Mana': 1505,'Atk': 44,'Mag': 34,'Defense': 39,'Resist': 39,'Speed': 157,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,
    'Luck': 0,'Dodge': 10,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0,'Threat': 0},

    'Acolyte':{'Dmg': 0,'HP': 15700,'Mana': 2085,'Atk': 33,'Mag': 112,'Defense': 44,'Resist': 83,'Speed': 50,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,
    'Luck': 0,'Dodge': 2,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0,'Threat': 0},

    'Elementalist':{'Dmg': 0,'HP': 14630,'Mana': 2095,'Atk': 34,'Mag': 132,'Defense': 34,'Resist': 73,'Speed': 50,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,
    'Luck': 0,'Dodge': 2,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0,'Threat': 0},

    'Druid':{'Dmg': 0,'HP': 12780,'Mana': 2565,'Atk': 34,'Mag': 127,'Defense': 5,'Resist': 25,'Speed': 60,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,
    'Luck': 0,'Dodge': 2,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0,'Threat': 0},

    'Soldier':{'Dmg': 0,'HP': 21675,'Mana': 605,'Atk': 83,'Mag': 44,'Defense': 112,'Resist': 44,'Speed': 50,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,
    'Luck': 0,'Dodge': 4,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0,'Threat': 0},

    'Vanguard':{'Dmg': 0,'HP': 25250,'Mana': 0,'Atk': 44,'Mag': 5,'Defense': 83,'Resist': 78,'Speed': 79,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,
    'Luck': 0,'Dodge': 4,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0,'Threat': 0},

    'Warlord':{'Dmg': 0,'HP': 19650,'Mana': 0,'Atk': 122,'Mag': 34,'Defense': 78,'Resist': 34,'Speed': 60,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,
    'Luck': 0,'Dodge': 4,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0,'Threat': 0},

    'Cleric':{'Dmg': 0,'HP': 12930,'Mana': 2085,'Atk': 44,'Mag': 12,'Defense': 15,'Resist': 25,'Speed': 50,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,
    'Luck': 0,'Dodge': 2,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0,'Threat': 0},

    'Aquamancer':{'Dmg': 0,'HP': 13800,'Mana': 2665,'Atk': 44,'Mag': 112,'Defense': 44,'Resist': 83,'Speed': 50,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,
    'Luck': 0,'Dodge': 2,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0,'Threat': 0},

    'Alchemist':{'Dmg': 0,'HP': 14920,'Mana': 2085,'Atk': 44,'Mag': 112,'Defense': 44,'Resist': 54,'Speed': 50,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,
    'Luck': 0,'Dodge': 10,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0,'Threat': 0},

    'Dreadknight':{'Dmg': 0,'HP': 23800,'Mana': 1115,'Atk': 20,'Mag': 78,'Defense': 73,'Resist': 73,'Speed': 40,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,
    'Luck': 0,'Dodge': 4,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0,'Threat': 0},

    'Sniper':{'Dmg': 0,'HP': 13380,'Mana': 0,'Atk': 10,'Mag': 10,'Defense': 44,'Resist': 44,'Speed': 138,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,
    'Luck': 0,'Dodge': 10,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0,'Threat': 0},

    'Monk':{'Dmg': 0,'HP': 18965,'Mana': 1210,'Atk': 78,'Mag': 34,'Defense': 49,'Resist': 49,'Speed': 108,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,
    'Luck': 0,'Dodge': 6,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0,'Threat': 0},

    'Dragonslayer':{'Dmg': 0,'HP': 17350,'Mana': 2090,'Atk': 76,'Mag': 76,'Defense': 47,'Resist': 47,'Speed': 79,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,
    'Luck': 0,'Dodge': 6,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0,'Threat': 0},

    'Necromancer':{'Dmg': 0,'HP': 17260,'Mana': 2085,'Atk': 39,'Mag': 83,'Defense': 83,'Resist': 83,'Speed': 40,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,
    'Luck': 0,'Dodge': 2,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0,'Threat': 0},

    'Timeweaver':{'Dmg': 0,'HP': 15250,'Mana': 2085,'Atk': 44,'Mag': 112,'Defense': 44,'Resist': 44,'Speed': 123,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,
    'Luck': 0,'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0,'Threat': 0},

    'Shinobi':{'Dmg': 0,'HP': 14920,'Mana': 1200,'Atk': 137,'Mag': 5,'Defense': 29,'Resist': 29,'Speed': 157,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,
    'Luck': 0,'Dodge': 10,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0,'Threat': 0},

    'Ronin':{'Dmg': 0,'HP': 15850,'Mana': 0,'Atk': 122,'Mag': 34,'Defense': 44,'Resist': 44,'Speed': 118,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,
    'Luck': 0,'Dodge': 6,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0,'Threat': 0},

    'Paladin':{'Dmg': 0,'HP': 8750,'Mana': 1550,'Atk': 78,'Mag': 78,'Defense': 73,'Resist': 73,'Speed': 69,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,
    'Luck': 0,'Dodge': 4,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0,'Threat': 0},

    'Paladin Wrath':{'Dmg': 0,'HP': 16000,'Mana': 1550,'Atk': 90,'Mag': 78,'Defense': 73,'Resist': 73,'Speed': 69,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,
    'Luck': 0,'Dodge': 4,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0,'Threat': 0},

    'Paladin Mercy':{'Dmg': 0,'HP': 14050,'Mana': 1550,'Atk': 78,'Mag': 90,'Defense': 73,'Resist': 73,'Speed': 69,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,
    'Luck': 0,'Dodge': 4,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0,'Threat': 0},

    'Paladin Protector':{'Dmg': 0,'HP': 20900,'Mana': 1550,'Atk': 67,'Mag': 67,'Defense': 199,'Resist': 199,'Speed': 69,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,
    'Luck': 0,'Dodge': 4,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0,'Threat': 0},
    
    'Pyromancer':{'Dmg': 0,'HP': 10500,'Mana': 2665,'Atk': 15,'Mag': 170,'Defense': 15,'Resist': 15,'Speed': 50,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,
    'Luck': 0,'Dodge': 2,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0,'Threat': 0}
}

#############    Prefixes ###############

prefix ={
    'Prefix':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0, 'Perc':{'Atk': 0}},

    'Archangel':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 30,'Mag': 30,'Defense': 0,'Resist': 10,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 10,'Dark': 0, 'Threat': 0},

    'Hellsinger':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 25,'Defense': 25,'Resist': 25,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 6,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 25, 'Threat': 0},

    'Artemian':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 30,'Resist': 30,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 6,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 25,'Light': 0,'Dark': 0, 'Threat': 0},

    'Boreas':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 10,'Mag': 30,'Defense': 0,'Resist': 0,'Speed': 30,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 25,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Empyrean':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 20,'Mag': 20,'Defense': 0,'Resist': 35,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Ifrit':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 35,'Mag': 35,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 25,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Prismatic':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 15,'Mag': 15,'Defense': 15,'Resist': 15,'Speed': 15,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 12,'Water': 12,'Wind': 12,'Earth': 12,'Light': 12,'Dark': 12, 'Threat': 0},

    'Deathbringer':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 20,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Manaslayer':{'Dmg': 0, 'HP': 0,'Mana': 400,'Atk': 26,'Mag': 26,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 8,'Water': 8,'Wind': 8,'Earth': 8,'Light': 8,'Dark': 8, 'Threat': 0},

    'Glaring':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 40,'Water': 40,'Wind': 40,'Earth': 40,'Light': 40,'Dark': 40, 'Threat': 0, 'Perc':{'Atk': -0.25, 'Mag': -0.25}},

    'Shattering':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0, 'Perc':{'Atk': 0.1, 'Mag': 0.1,'Defense': -0.1,'Resist': -0.1,'Speed': -0.1}},

    'Mammoth':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0, 'Perc':{'HP': 0.15, 'Speed': -0.25}},

    'Destroyer':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 50,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},
    
    'Eldritch':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 60,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Dauntless':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 50,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Regal':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 50,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Hyperflux':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 50,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Molten':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 45,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},
    
    'Tsunami':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 45,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Surging':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 45,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Dryad':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 45,'Light': 0,'Dark': 0, 'Threat': 0},
    
    'Angelic':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 45,'Dark': 0, 'Threat': 0},
    
    'Gorging':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 45, 'Threat': 0}
    }

sufix ={
    'Suffix':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Bloodthirst':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 6,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Feasting':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 15,'Mag': 15,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 6,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Spacetime':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 10,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0, 'Perc':{'Atk': -0.1, 'Mag': -0.1,'Defense': -0.1,'Resist': -0.1, 'Speed': -0.1, 'Fire': -0.08,'Water': -0.08, 'Wind': -0.08,'Earth': -0.08,'Light': -0.08,'Dark': -0.08}},

    'Crystal':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 15,'Resist': 15,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0, 'Perc':{'HP': 0.06, 'Mana': 0.06}},

    'Juggernaut':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 12,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0, 'Perc':{'Speed': -0.08}},

    'Apocalypse':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 100,'Mag': 100,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 50,'Water': 50,'Wind': 50,'Earth': 50,'Light': 50,'Dark': 50, 'Threat': 0, 'Perc':{'HP': -0.33, 'Mana': -0.33}},

    'Gods':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0, 'Perc':{'Atk': 0.05,'Mag': 0.05,'Defense': 0.05,'Resist': 0.05,'Speed': 0.05,
    'Fire': 0.05,'Water': 0.05,'Wind': 0.05,'Earth': 0.05,'Light': 0.05,'Dark': 0.05}},

    'Ninja':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 8,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},

    'Hellfire':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 20,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 20, 'Threat': 0},

    'Purity':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 20,'Wind': 0,'Earth': 0,'Light': 20,'Dark': 0, 'Threat': 0},

    'Alta Nimbus':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 20,'Earth': 20,'Light': 0,'Dark': 0, 'Threat': 0},

    'Midas':{'Dmg': 0, 'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 5,
    'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0, 'Threat': 0},
}

#### Skill buffs ####

    #### Only buff skills
Skills_b={
        'Class':{
            'Base1':{'type': 'buff', 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Duration': 0 , 'Cooldown': 0,'Stat': 0},
        },

        'Hunter':{
            'Hunter\'s Gaze':{'type': 'buff' , 'img':'.\image\skill\Hgaze.png', 'Skilltext': 'You enter a state of singular focus on your prey', 'Duration': 8 , 'Cooldown': 60,'Atk': 0.5, 'Speed': 0.5},
        },

        'Assassin':{
        },

        'Saboteur':{'Base1':{'type': 'dmg' , 'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Acolyte':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Elementalist':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            
        },

        'Soldier':{
            'Morale Boost':{'type': 'buff' , 'img':'.\image\skill\Smoral.png', 'Skilltext': 'Boost your morale buffing yourself and regenerating 2% MaxHP and 1% MaxMP each second for the duration.', 'Duration': 10 , 'Cooldown': 120,'Defense': 0.5, 'Atk': 0.5, 'Speed': 0.5},
        },

        'Vanguard':{
            'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Warlord':{
            'Enrage':{'type': 'buff' , 'img':'.\image\skill\Wdec.png', 'Skilltext': 'Become fueled by rage! Increase Attack by 50%  while reducing defense by 50%','Duration': 20 , 'Cooldown': 0.25,'Defense': -0.5, 'Atk': 0.5},
        },

        'Cleric':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Aquamancer':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Alchemist':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Dreadknight':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Sniper':{ 
            'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Monk':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Dragonslayer':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Necromancer':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Timeweaver':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Shinobi':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Ronin':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Paladin':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Paladin Wrath':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Paladin Mercy':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Paladin Protector':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Pyromancer':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },
    }


