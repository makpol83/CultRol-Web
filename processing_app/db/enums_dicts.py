from enum import Enum


# =====================
# RACES
# =====================
class Races(Enum):
    NO_RACE = 'sin_raza'
    HUMAN = 'humano'
    ASURA = 'asura'
    KITSUNE = 'kitsune'
    ONI = 'oni'
    PIGMAN = 'pigmeo'
    BESTIAL = 'bestial'
    OPTION8 = 'option8'
    OPTION9 = 'option9'
    OPTION10 = 'option10'


# =====================
# SEX
# =====================
class Sex(Enum):
    NO_SEX = 'sin_sexo'
    FEMALE = 'femenino'
    MALE = 'masculino'


# =====================
# EQUIPMENT SLOTS
# =====================
class Slot(Enum):
    NO_SLOT = 'sin_slot'
    HEAD = 'cabeza'
    CHEST = 'pecho'
    GLOVES = 'guantes'
    PANTS = 'pantalones'
    SHOES = 'zapatos'
    NECKLACE = 'colgante'
    RING = 'anillo'


# =====================
# CULTIVATION REALMS
# =====================
class CultivationRealm(Enum):
    NO_REALM = 'sin reino'
    QI_CONDENSATION = 'Condensación del Qi'
    FOUNDATION_ESTABLISHMENT = 'Establecimiento de la fundación'
    CORE_FORMATION = 'Formación del núcleo'
    NASCENT_SOUL = 'Alma naciente'
    SPIRIT_SEPARATION = 'Separación del espíritu'
    DAO_SEEKING = 'Búsqueda del Dao'


# =====================
# CULTIVATION RANGES
# =====================
class CultivationRange(Enum):
    MORTAL = 'mortal'
    CQ1 = 'CQ1'
    CQ2 = 'CQ2'
    CQ3 = 'CQ3'
    CQ4 = 'CQ4'
    CQ5 = 'CQ5'
    CQ6 = 'CQ6'
    CQ7 = 'CQ7'
    CQ8 = 'CQ8'
    CQ9 = 'CQ9'
    CQ10 = 'CQ10'
    CQ11 = 'CQ11'
    CQ12 = 'CQ12'
    CQ13 = 'CQ13'
    EF1P = 'EF1P'
    EF2P = 'EF2P'
    EF3P = 'EF3P'
    EF4P = 'EF4P'
    EF5P = 'EF5P'
    EF6P = 'EF6P'
    EF7P = 'EF7P'
    EF8P = 'EF8P'
    EF9P = 'EF9P'
    FNTEMP1 = 'FNTEMP1'
    FNTEMP2 = 'FNTEMP2'
    FNTEMP3 = 'FNTEMP3'
    FNMED1 = 'FNMED1'
    FNMED2 = 'FNMED2'
    FNMED3 = 'FNMED3'
    FNTARD1 = 'FNTARD1'
    FNTARD2 = 'FNTARD2'
    FNTARD3 = 'FNTARD3'
    ANTEMP1 = 'ANTEMP1'
    ANTEMP2 = 'ANTEMP2'
    ANTEMP3 = 'ANTEMP3'
    ANMED1 = 'ANMED1'
    ANMED2 = 'ANMED2'
    ANMED3 = 'ANMED3'
    ANTARD1 = 'ANTARD1'
    ANTARD2 = 'ANTARD2'
    ANTARD3 = 'ANTARD3'
    SEP1 = 'SEP1'
    SEP2 = 'SEP2'
    SEP3 = 'SEP3'
    BDTEMP = 'BDTEMP'
    BDMED = 'BDMED'
    BDTARD = 'BDTARD'
    BDSEMI = 'BDSEMI'

# =====================
# TALENT LEVEL
# =====================
class TalentLevel(Enum):
    X = 'X'
    E = 'E'
    C = 'C'
    B = 'B'
    A = 'A'
    S = 'S'

# Dictionary that relates a table with its Primary Keys

PRIMARY_KEYS = {
    'object_stats': ['id_os'],
    'object': ['id_o'],
    'clan': ['id_cl'],
    'don': ['id_d'],
    'talent': ['id_t'],
    'stats': ['id_s'],
    'character': ['id_c'],
    'statchar_relation': ['id_s', 'id_c'],
    'donchar_relation': ['id_d', 'id_c'],
    'inventory': ['id_c', 'id_o']
}

# Dictionary with the columns of each table
TABLES_COLUMNS = {
    "object_stats": ['id_os', 'strength', 'speed', 'agility', 'resistance', 'vitality',
                     'perception', 'intelligence', 'concentration', 'spiritual_energy',
                     'qi_control', 'qi_quality', 'spiritual_sense', 'qi_nucl'],
                     
    "object": ['id_o', 'slot_type', 'name', 'descr', 'added_stats'],

    "clan": ['id_cl', 'name'],

    "don": ['id_d', 'name', 'EE_use', 'description'],

    "talent": ['id_t', 'strength', 'speed', 'agility', 'resistance', 'vitality',
               'perception', 'intelligence', 'concentration', 'spiritual_energy',
               'qi_control', 'qi_quality', 'spiritual_sense', 'qi_nucl'],

    "stats": ['id_s', 'cult_range', 'talent_id', 'strength', 'speed', 'agility', 'resistance',
              'vitality', 'perception', 'intelligence', 'concentration', 'spiritual_energy',
              'qi_control', 'qi_quality', 'spiritual_sense', 'qi_nucl'],

    "character": ['id_c', 'name', 'age', 'lifespan', 'sex', 'race', 'martial_title',
                  'clan_born', 'clan_actual', 'cult_realm', 'cult_range', 'prestige', 'level',
                  'actual_xp', 'required_xp', 'actual_sp', 'actual_cp', 'appearance', 
                  'past', 'diseases', 'wounds'],

    "statchar_relation": ['id_s', 'id_c'],

    "donchar_relation": ['id_d', 'id_c'],

    "inventory": ['id_c', 'id_o', 'quantity']
}

PRIMARY_KEYS = {
    "object_stats": ['id_os'],
                     
    "object": ['id_o'],

    "clan": ['id_cl'],

    "don": ['id_d'],

    "talent": ['id_t'],

    "stats": ['id_s'],

    "character": ['id_c'],

    "statchar_relation": ['id_s', 'id_c'],

    "donchar_relation": ['id_d', 'id_c'],

    "inventory": ['id_c', 'id_o', 'quantity']
}