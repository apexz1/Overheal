"""Collection of spell names and coefficients to match spell ids."""

# fmt: off

# Spell id to spell names, including rank
SPELL_NAMES = {
    "25235": "Flash Heal (Rank 9)",
    "25233": "Flash Heal (Rank 8)",
    "10917": "Flash Heal (Rank 7)",
    "10916": "Flash Heal (Rank 6)",
    "10915": "Flash Heal (Rank 5)",
    "9474": "Flash Heal (Rank 4)",
    "9473": "Flash Heal (Rank 3)",
    "9472": "Flash Heal (Rank 2)",
    "2061": "Flash Heal (Rank 1)",

    "2053": "Lesser Heal (Rank 3)",

    "32546": "Binding Heal (Rank 1)",

    "25308": "Prayer of Healing (Rank 6)",
    "25316": "Prayer of Healing (Rank 5)",
    "10961": "Prayer of Healing (Rank 4)",
    "10960": "Prayer of Healing (Rank 3)",
    "996": "Prayer of Healing (Rank 2)",
    "596": "Prayer of Healing (Rank 1)",

    "25213": "Greater Heal (Rank 7)",
    "25210": "Greater Heal (Rank 6)",
    "25314": "Greater Heal (Rank 5)",
    "10965": "Greater Heal (Rank 4)",
    "10964": "Greater Heal (Rank 3)",
    "10963": "Greater Heal (Rank 2)",
    "2060": "Greater Heal (Rank 1)",

    "33110": "Prayer of Mending (Rank 1)",

    "6064": "Heal (Rank 4)",
    "6063": "Heal (Rank 3)",
    "2055": "Heal (Rank 2)",
    "2054": "Heal (Rank 1)",

    "27823": "Holy Nova (Rank 6)",
    "27805": "Holy Nova (Rank 6)",
    "27801": "Holy Nova (Rank 6)",
    "27804": "Holy Nova (Rank 5)",
    "23455": "Holy Nova (Rank 1)",

    "25222": "Renew (Rank 12)",
    "10929": "Renew (Rank 9)",
    "6078": "Renew (Rank 6)",
    "6077": "Renew (Rank 5)",
    "6075": "Renew (Rank 3)",
    "139": "Renew (Rank 1)",

    "22009": "Greater Heal Renew",
    "37563": "Renewal",

    "19243": "Desperate Prayer (Rank 7)",

    "25218": "Power Word: Shield (Rank 12)",
    "10901": "Power Word: Shield (Rank 10)",
    "10899": "Power Word: Shiled (Rank 8)",

    # Other misc spells
    "25429": "Fade (Rank 7)",
    "10942": "Fade (Rank 6)",
    "10890": "Psychic Scream (Rank 4)",

    # Damage spells
    "10947": "Mind Blast (Rank 9)",
    "10934": "Smite (Rank 8)",

    # Utility spells
    # Priest
    "32999": "Prayer of Spirit (Rank 2)",
    "25392": "Prayer of Fortitude (Rank 3)",

    "25312": "Divine Spirit (Rank 5)",
    "10958": "Shadow Protection (Rank 3)",
    "25389": "Power Word: Fortitude (Rank 7)",

    "20770": "Resurrection (Rank 5)",
    "10881": "Resurrection (Rank 4)",

    "527": "Dispel Magic (Rank 1)",
    "988": "Dispel Magic (Rank 2)",
    "552": "Abolish Disease",

    "10060": "Power Infusion",

    # Mage
    "23028": "Arcane Brilliance (Rank 1)",
    "10157": "Arcane Intellect (Rank 5)",

    "475": "Remove Lesser Curse",

    # Druid
    "9889": "Healing Touch (Rank 10)",
    "8903": "Healing Touch (Rank 7)",

    "9841": "Rejuvenation (Rank 10)",

    "9858": "Regrowth (Rank 9)",
    "9857": "Regrowth (Rank 8)",

    "17116": "Nature's Swiftness",
    "18562": "Swiftmend",
    "29166": "Innervate",

    "21850": "Gift of the Wild (Rank 2)",
    "9885": "Mark of the Wild (Rank 7)",

    "20748": "Rebirth (Rank 5)",

    "9907": "Faerie Fire (Rank 4)",

    "8946": "Cure Poison",
    "2893": "Abolish Poison",
    "2782": "Remove Curse",

    # Shaman
    "10623": "Chain Heal (Rank 3)",
    "10622": "Chain Heal (Rank 2)",
    "1064": "Chain Heal (Rank 1)",

    "10468": "Lesser Healing Wave (Rank 6)",
    "8008": "Lesser Healing Wave (Rank 2)",

    "10396": "Healing Wave (Rank 9)",
    "8005": "Healing Wave (Rank 7)",
    "959": "Healing Wave (Rank 6)",
    "939": "Healing Wave (Rank 5)",
    "331": "Healing Wave (Rank 1)",

    "20777": "Ancestral Spirit (Rank 5)",

    "2870": "Cure Disease",
    "526": "Cure Poison",

    # Paladin
    "20773": "Redemption (Rank 5)",

    "4987": "Cleanse",

    # Hunter
    "19801": "Tranquilizing Shot",

    # Gnome
    "20589": "Escape Artist",

    # Mobs
    "23859": "Dispel Magic",  # ZG bosses
    "17201": "Dispel Magic",  # ZG mobs
    "19492": "Antimagic Pulse",  # Garr

    # Generic
    "15701": "Night Dragon's Breath",
}

# Spells that might turn up but we don't care for listing in spell casts
# These do not cost mana so will not trigger 5sr, or BD (presumably)
SPELL_IGNORE = [
    "24354",  # Blessed Prayer Beads
    "23477",  # 1440 Health Stone
    "23394",  # Shadow of Ebonroc
    "18610",  # First Aid (Heavy Runecloth)
    "17544",  # Greater Frost Protection Potion
    "17543",  # Greater Fire Protection Potion
    "17531",  # Major Mana Potion
    "17291",  # Stratholme Holy Water
    "16666",  # Demonic Rune
    "15701",  # Night Dragon's Breath
    "14751",  # Inner Focus
    "7744",  # Will of the Forsaken
    "5019",  # Shoot
]

SPELL_BUFFS = [
    # Priest
    "21564",  # Prayer of Fortitude R2
    "27681",  # Prayer of Spirit R1
    "10938",  # Power Word: Fortitude R6
    "27841",  # Divine Spirit R4
    "10958",  # Shadow Protection R3

    # Mage
    "23028",  # Arcane Brilliance R1
    "10157",  # Arcane Intellect R5

    # Druid
    "21850",  # Gift of the Wild R2
    "9885",  # Mark of the Wild R7
]

# Spell coefficients of each spell id, for determining weight of heal power
SPELL_COEFFICIENTS = {
    # Flash Heal
    "25235": 0.429,
    "25233": 0.429,
    "10917": 0.429,
    "10916": 0.429,
    "10915": 0.429,
    "9474": 0.429,
    "9473": 0.429,
    "9472": 0.429,
    "2061": 0.429,

    # Lesser Heal
    "2053": 0.446,

    # Binding Heal
    "32546": 0.429,

    # Prayer of Healing
    "25308": 0.429,
    "25316": 0.429,
    "10961": 0.398,
    "10960": 0.398,
    "996": 0.337,
    "596": 0.275,

    # Greater Heal
    "25213": 0.857,
    "25210": 0.857,
    "25314": 0.833,
    "10965": 0.796,
    "10964": 0.771,
    "10963": 0.698,
    "2060": 0.624,

    # Prayer of Mending
    "33110": 0.429,

    # Heal
    "6064": 0.857,
    "6063": 0.857,
    "2055": 0.857,
    "2054": 0.729,

    # Holy Nova
    "27823": 0.107,
    "27805": 0.107,
    "27801": 0.107,
    "27804": 0.107,
    "23455": 0.107,

    # Renew
    "25222": 1.0 / 5,
    "10929": 1.0 / 5,
    "6078": 1.0 / 5,
    "6077": 1.0 / 5,
    "6075": 1.0 / 5,
    "139": 0.55 / 5,

    # Greater Heal Renew, 8t2
    "22009": 1.0 / 5,

    # Renewal
    "37563": 1.0 / 5,

    # Desperate Prayer
    "19243": 0.429,

    # Power Word: Shield
    "25218": 0.3,

    # Dispel Magic
    "988": 0.0,

    # Generic
    "15701": 0.0,
}

# Raw healing of each spell
SPELL_HEALS = {
    # Flash Heal
    "25235": 1205.5,
    "25233": 1004.5,
    "10917": 906,
    "10916": 722.5,
    "10915": 583.5,
    "9474": 453.0,
    "9473": 372.5,
    "9472": 297.0,
    "2061": 224.5,

    # Lesser Heal
    "2053": 154.0,

    # Binding Heal
    "32546": 1201.5,

    # Prayer of Healing
    # "25316": 0.0,
    "25308": 1286.5,
    # "10960": 0.0,
    # "996": 0.0,
    "596": (333 + 312) / 2,

    # Greater Heal
    "25213": 2608.5,
    "25210": 2275.5,
    "25314": 2080.0,
    "10965": 1917.0,
    "10964": 1556.0,
    "10963": 1248.0,
    "2060": 981.5,

    # Prayer of Mending
    "33110": 800.0,

    # Heal
    "6064": 780.5,
    "6063": 624.0,
    "2055": 476.0,
    "2054": 330.0,

    # Holy Nova
    "27823": 326.0,
    "27805": 326.0,
    "27801": 326.0,
    "27804": 257.5,
    "23455": 58.5,

    # Renew
    "25222": 1110 / 5,
    "10929": 810 / 5,
    "6078": 400 / 5,
    "6077": 315 / 5,
    "6075": 175 / 5,
    "139": 45 / 5,

    # Greater Heal Renew, 8t2
    "22009": 315 / 5,

    # Renewal, 2t4
    "37563": 150 / 3,

    # Desperate Prayer
    "19243": 1459.5,

    # Generic
    "15701": 425.0,
}

# Mana cost of each spell
SPELL_MANA = {
    "25235": 470.0,
    "25233": 400.0,
    "10917": 380.0,
    "10916": 315.0,
    "10915": 265.0,
    "9474": 215.0,
    "9473": 185.0,
    "9472": 155.0,
    "2061": 125.0,

    "2053": 75.0,

    "32546": 705.0,

    "25308": 1255.0,
    "25316": 1070.0,
    "10961": 1030.0,
    "10960": 770.0,
    "996": 560.0,
    "596": 410.0,

    "25213": 701.0,
    "25210": 638.0,
    "25314": 710.0,
    "10965": 655.0,
    "10964": 545.0,
    "10963": 445.0,
    "2060": 370.0,

    "33110": 390.0,

    "6064": 305.0,
    "6063": 255.0,
    "2055": 205.0,
    "2054": 155.0,

    # Holy Novas
    "27823": 750.0,
    "27805": 750.0,
    "27801": 750.0,
    # "27804": "Holy Nova (Rank 5)",
    # "23455": "Holy Nova (Rank 1)",

    # Renews
    "25222": 405.0,
    "10929": 365.0,
    "6078": 205.0,
    "6077": 170.0,
    "6075": 105.0,
    "139": 30.0,

    # Greater Heal Renew
    "22009": 0.0,

    # "19243": "Desperate Prayer (Rank 7)",

    "10901": 500.0,

    # # Other misc spells
    # "10942": "Fade (Rank 6)",
    # "10890": "Psychic Scream (Rank 4)",
    #
    # # Damage spells
    # "10947": "Mind Blast (Rank 9)",
    # "10934": "Smite (Rank 8)",
    #
    # # Utility spells
    # # Priest
    # "27681": "Prayer of Spirit (Rank 1)",
    # "21564": "Prayer of Fortitude (Rank 2)",
    #
    # "27841": "Divine Spirit (Rank 4)",
    # "10958": "Shadow Protection (Rank 3)",
    # "10938": "Power Word: Fortitude (Rank 6)",
    #
    # "20770": "Resurrection (Rank 5)",
    # "10881": "Resurrection (Rank 4)",

    "988": 223.0,

    # "552": "Abolish Disease",

    # Generic
    "15701": 0.0,

}

# fmt: on
warning_list = dict(name=[], coef=[], heal=[], mana=[])


def spell_name(spell_id, warn_on_not_found=True):
    if spell_id in SPELL_NAMES:
        return SPELL_NAMES[spell_id]

    if warn_on_not_found and spell_id not in warning_list["name"]:
        print(f"Unknown name for spell {spell_id}, https://tbc.wowhead.com/spell={spell_id}")
        warning_list["name"].append(spell_id)

    return f"[Spell {spell_id}]"


def spell_coefficient(spell_id, warn_on_not_found=True):
    if spell_id in SPELL_COEFFICIENTS:
        return SPELL_COEFFICIENTS[spell_id]

    if warn_on_not_found and spell_id not in warning_list["coef"]:
        print(f"Unknown coefficient for spell {spell_id}, https://tbc.wowhead.com/spell={spell_id}")
        warning_list["coef"].append(spell_id)

    return 0.0


def spell_heal(spell_id, warn_on_not_found=True):
    if spell_id in SPELL_HEALS:
        return SPELL_HEALS[spell_id]

    if warn_on_not_found and spell_id not in warning_list["heal"]:
        print(f"Unknown base heal for spell {spell_id}, https://tbc.wowhead.com/spell={spell_id}")
        warning_list["heal"].append(spell_id)

    return 0.0


def spell_mana(spell_id, talents=None, warn_on_not_found=True):
    if talents is None:
        talents = {}

    if spell_id not in SPELL_MANA:
        if warn_on_not_found and spell_id not in warning_list["mana"]:
            print(f"Unknown mana cost for spell {spell_id}, https://tbc.wowhead.com/spell={spell_id}")
            warning_list["mana"].append(spell_id)

        return 0.0

    mana = SPELL_MANA[spell_id]
    name = spell_name(spell_id)
    name_without_rank = name.split("(")[0].strip()

    if "Improved Healing" in talents:
        if name_without_rank in ("Heal", "Greater Heal", "Lesser Heal"):
            # LH, H and GH reduced by 5% per talent
            mana -= mana * 0.05 * talents["Improved Healing"]

    if "Mental Agility" in talents:
        # all instant casts
        if name_without_rank in ("Power Word: Shield", "Dispel Magic", "Renew", "Power Infusion"):
            mana -= mana * 0.02 * talents["Mental Agility"]

    if "Improved Prayer of Healing" in talents:
        if name_without_rank == "Prayer of Healing":
            mana -= mana * 0.10 * talents["Improved Prayer of Healing"]

    return mana
