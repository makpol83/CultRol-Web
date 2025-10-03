-- Enum with access levels
CREATE TYPE access_levels AS ENUM ('guest', 'player', 'admin');


CREATE TABLE users (
    id_user SERIAL PRIMARY KEY,
    username text NOT NULL,
    password text NOT NULL,
    access_level access_levels DEFAULT 'guest'
);