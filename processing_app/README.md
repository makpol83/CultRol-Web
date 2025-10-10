## What processing language will we use

We will need a program that is able to manage API calls from the web. For example, to manage login, database data extraction and modifying the characters.
This can be done with many languages but python was selected due to its useful packages and simplicity.

## What is expected from the python program to manage

Here is a list with all the functionality that has to be implemented in order for the web to function properly:

Database queries:
    - Raw data extraction: the program will manage the queries to the database to obtain raw data, for example stats.
    - Modifying data on the database: the program will manage the queries that insert data or remove it from the db to keep it functional.
    - Processing special data: the program will make it possible to get statistical data and keep a log of all the movements in the db and API calls.

Permission management:
    - For each database interaction that the web API needs, the program will check user permissions from the database 
    - Will be able to create/delete users and change their permissions

## Source use

--> connection

    Connection is the module responsible for creating a connection with the db and closing it. The user has to manage the aperture and the closure.

--> data_insertion.py

    Data insertion regulates the insertion on the db. To determine where data is inserted the functions will follow these parameters:
        table_name - Name of the table where the register is to be inserted.
        data_1, data_2, data_3... - Follows the order of the table. For example:
            If our table is: id, name, descr, quantity
            The function will receive table_name, name, descr, quantity. There cannot be empty camps. 