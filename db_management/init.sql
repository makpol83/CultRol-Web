-- Enum: All types of races implemented
CREATE TYPE race_type AS ENUM ('sin_raza', 'humano', 'asura', 'kitsune', 'oni', 'pigmeo', 'bestial', 'option8', 'option9', 'option10');

-- Enum: All types of gender related to all species
CREATE TYPE sex_type AS ENUM ('sin_sexo', 'femenino', 'masculino');

-- Enum: All types of slots of equipment a piece can be
CREATE TYPE slot_type AS ENUM ('sin_slot', 'cabeza', 'pecho', 'guantes', 'pantalones', 'zapatos', 'colgante', 'anillo');

-- Enum: All types of realms of cultivation implemented
CREATE TYPE cultivation_realm AS ENUM ('sin reino', 'Condensación del Qi',
    'Establecimiento de la fundación', 'Formación del núcleo', 'Alma naciente',
    'Separación del espíritu', 'Búsqueda del Dao');

-- Enum: All ranges of cultivation implemented
CREATE TYPE cultivation_range AS ENUM ('mortal', 'CQ1', 'CQ2', 'CQ3', 'CQ4', 'CQ5',
    'CQ6', 'CQ7', 'CQ8', 'CQ9', 'CQ10', 'CQ11', 'CQ12', 'CQ13', 'EF1P', 'EF2P',
    'EF3P', 'EF4P', 'EF5P', 'EF6P', 'EF7P', 'EF8P', 'EF9P', 'FNTEMP1', 'FNTEMP2',
    'FNTEMP3', 'FNMED1', 'FNMED2', 'FNMED3', 'FNTARD1', 'FNTARD2', 'FNTARD3',
    'ANTEMP1', 'ANTEMP2', 'ANTEMP3', 'ANMED1', 'ANMED2', 'ANMED3', 'ANTARD1',
    'ANTARD2', 'ANTARD3', 'SEP1', 'SEP2', 'SEP3', 'BDTEMP', 'BDMED', 'BDTARD',
    'BDSEMI');

-- Enum: All talent level a stat cna have
CREATE TYPE talent_level AS ENUM ('X', 'E', 'C', 'B', 'A', 'S');

-- Saves the stats an object gives when equipped
CREATE TABLE object_stats(
    id_os SERIAL PRIMARY KEY,

    strength integer DEFAULT 0,
    speed integer DEFAULT 0,
    agility integer DEFAULT 0,
    resistance integer DEFAULT 0,
    vitality integer DEFAULT 0,
    
    perception integer DEFAULT 0,
    intelligence integer DEFAULT 0,
    concentration integer DEFAULT 0,

    spiritual_energy integer DEFAULT 0,
    qi_control integer DEFAULT 0,
    qi_quality integer DEFAULT 0,

    spiritual_sense integer DEFAULT 0,
    qi_nucl integer DEFAULT 0
);

-- Table with all the objects added
CREATE TABLE object(
    id_o SERIAL PRIMARY KEY,
    slot_type slot_type DEFAULT 'sin_slot',
    name text NOT NULL,
    descr text NOT NULL,
    added_stats integer REFERENCES object_stats(id_os) -- Can be null if not an equipment object
);

-- Saves all the clans added in the world
CREATE TABLE clan(
    id_c SERIAL PRIMARY KEY,
    name text NOT NULL
);

-- Saves all implemented don
CREATE TABLE don(
    id_d SERIAL PRIMARY KEY,
    name text NOT NULL DEFAULT 'sin_nombre',
    EE_use integer DEFAULT 0,
    description text NOT NULL DEFAULT 'sin_descripción'
);


-- Saves the talent level of every skill for a character
CREATE TABLE talent(
    id_t SERIAL PRIMARY KEY,

    strength talent_level DEFAULT 'C',
    speed talent_level DEFAULT 'C',
    agility talent_level DEFAULT 'C',
    resistance talent_level DEFAULT 'C',
    vitality talent_level DEFAULT 'C',
    
    perception talent_level DEFAULT 'C',
    intelligence talent_level DEFAULT 'C',
    concentration talent_level DEFAULT 'C',

    spiritual_energy talent_level DEFAULT 'C',
    qi_control talent_level DEFAULT 'C',
    qi_quality talent_level DEFAULT 'C',

    spiritual_sense talent_level DEFAULT 'C',
    qi_nucl talent_level DEFAULT 'C'
);

-- Saves the stat level on a cultivation range for a character
CREATE TABLE stats(
    id_s SERIAL PRIMARY KEY,
    cult_range cultivation_range DEFAULT 'mortal',      -- Rango de cultivo de estas stats

    strength integer DEFAULT 0,
    speed integer DEFAULT 0,
    agility integer DEFAULT 0,
    resistance integer DEFAULT 0,
    vitality integer DEFAULT 0,
    
    perception integer DEFAULT 0,
    intelligence integer DEFAULT 0,
    concentration integer DEFAULT 0,

    spiritual_energy integer DEFAULT 0,
    qi_control integer DEFAULT 0,
    qi_quality integer DEFAULT 0,

    spiritual_sense integer DEFAULT 0,
    qi_nucl integer DEFAULT 0,

    range_quality REAL GENERATED ALWAYS AS              
    ((strength + speed + agility + resistance + vitality + perception + intelligence
    + concentration + spiritual_energy + qi_control + qi_quality)/11.0) STORED 
    -- Calidad del rango
);

-- Saves the total level of the stats for a character (throughout the cultivation ranges)
CREATE TABLE actual_stats(
    id_as SERIAL PRIMARY KEY,
    talent_id integer REFERENCES talent(id_t),            -- ID de los talentos del personaje

    strength integer DEFAULT 0,
    speed integer DEFAULT 0,
    agility integer DEFAULT 0,
    resistance integer DEFAULT 0,
    vitality integer DEFAULT 0,
    
    perception integer DEFAULT 0,
    intelligence integer DEFAULT 0,
    concentration integer DEFAULT 0,

    spiritual_energy integer DEFAULT 0,
    qi_control integer DEFAULT 0,
    qi_quality integer DEFAULT 0,

    spiritual_sense integer DEFAULT 0,
    qi_nucl integer DEFAULT 0
);

-- Saves all the information related to a character
CREATE TABLE character (
    id_c SERIAL PRIMARY KEY,                             -- clave primaria
    name text NOT NULL,                                 -- nombre completo
    age integer DEFAULT 0,                              -- edad actual
    lifespan integer DEFAULT 0,                         -- tiempo de vida restante

    sex sex_type NOT NULL DEFAULT 'sin_sexo',           -- tipo de sexo 
    race race_type NOT NULL DEFAULT 'sin_raza',         -- tipo de raza
    martial_title text NOT NULL,                        -- titulo marcial 
    clan_born integer REFERENCES clan(id_c),              -- clan en el que nació el personaje
    clan_actual integer REFERENCES clan(id_c),            -- clan al que pertenece el personaje

    cult_realm cultivation_realm DEFAULT 'sin reino',   -- reino de cultivo
    cult_range cultivation_range DEFAULT 'mortal',      -- rango de cultivo
    prestige integer DEFAULT 0,                         -- puntos de prestigio
    level integer DEFAULT 0,                            -- valor del nivel
    actual_xp integer DEFAULT 0,                        -- experiencia actual
    required_xp integer DEFAULT 0,                      -- experiencia requerida para subir de nivel
    actual_sp integer DEFAULT 0,                        -- Skill Points
    actual_cp integer DEFAULT 0,                        -- puntos de campeón

    appearance text,                                    -- apariencia
    past text,                                          -- pasado
    diseases text,                                      -- enfermedades
    wounds text,                                        -- heridas
);

-- Relational table where a character is linked to their stats through cultivation ranges
CREATE TABLE statchar_relation(
    id_s integer REFERENCES stats(id_s),                -- id de las stats del personaje
    id_c integer REFERENCES character(id_c),                -- id del personaje

    PRIMARY KEY(id_s, id_c)
);

-- Relational table where a character is linked to their Don
CREATE TABLE donchar_relation(
    id_d integer REFERENCES don(id_d),
    id_c integer REFERENCES character(id_c),

    PRIMARY KEY(id_d, id_c)
)

-- Relational table that links an inventory with its item
CREATE TABLE inventory (
    id_c integer REFERENCES character(id_c) ON DELETE CASCADE, -- id del personaje al que pertenece el inventario
    id_o integer REFERENCES object(id_o) ON DELETE CASCADE,  -- id del objeto que pertenece al personaje
    quantity integer DEFAULT 1,                         -- cantidad de ese objeto en el inventario

    PRIMARY KEY(id_c, id_o)
);

