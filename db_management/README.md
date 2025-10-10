## Database structure

The database will use postgresql for data management. The table creation has been done on the init.sql and permission_init.sql

## Database workflow

Database name will be cultrol and it will hold character, object and user information.

## Database character management description

The following paragraphs will showcase how the database is intended to work.

The main table is called characters. characters has several columns with
static data and four references, two of them are the clan_born and 
clan_actual, both of them reference a clan.id register. Another important link
is the cum_stats which refers to the total stats of a character on this moment.

A don is related to a character via the chardon_relation table.

The next important set of tables relates the stats of a character. A character
has a predefined set of stats(strength, speed, agility...), the real value of
the stats that the character will use in combat is the actual_stats table. But
according to the quality of the cultivation and the breakthroughs a character
can develop different levels of power. That's why the stats table exists, this
table represents for a cultivation range the stats that the character has 
reached on that range. If a character for example is on QI3, he will have 3 
stats register: 1 for QI1, another for QI2 and another for QI3 (Actual range),
and actual_stats will represent the total sum relative to a set of functions
to scale properly through ranges. All the formulas will be described on 
scaling.txt.

Relative to the stats. When adding points to a stat, the talent takes action.
Each character has a talent associated to each stat via the talent table.
The multipliers for the talent will be managed by the processing program, so
the database just needs to know what talent levels exist and what talent level
has each stat for each character.

To address which stat is from which character, the statchar_relation table takes
effect, linking the stats id with the character id.

Inventory management is done through the inventory table. Each object is
stored in the object table, then, through the inventory table, an object
is linked to a character. This table has a column for quantity so you can have
multiple objects of the same type in an inventory.

An object is defined by its id, but it also has important columns. For example,
slot_type. If the object can be equipped by a player then this column will
reference the part where the player will be able to put it. The idea is the
following: if the object is equippable it will have a slot_type assigned,
distinct from no_slot and will reference a register on the object stats table,
which will hold the stats this object gives the wearer. If it is not equippable,
the object register will have slot_type as no_slot and the added_stats set to NULL

NOTE: An object has a name and a description. The effects related to the description
are designed to be managed by the master on the roleplay so the database doesn't 
control that effects.

## Database permission levels

The database will have three types of users:

- Admin: Can control everything in the database and the processing.
- Player: Can manage their characters and modify them if the admin gives them
   permission to do so
- Guest: Can't modify anything. Only will be able to view the data from characters.

This permission levels will be implemented by the following tables on
permission_init.sql
