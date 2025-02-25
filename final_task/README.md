I have chosen to use PokeAPI which returns information about the Pokemon games as JSON. There are different endpoints for different kinds of information. The /pokemon endpoint includes lots of information such as game sprites, moves a Pokemon has/can learn and at what level, etc. Those moves can be looked at in more detail using the /move endpoint and so on and so forth.

For this exercise I have used the /pokemon endpoint to fetch details about specified Pokemon.
 - Pokedex Number **Integer** *(used here as an ID, however this is a number referenced in the in-game universe)*
 - Name **String**
 - Height **Integer**
 - Weight **Integer**
 - Types (a Pokemon may have more than 1 type) **String**

I realise now, too late, that I should have used 2 tables to store the data. One table for the Pokemon, and another for types I could have then used the Pokedex Number (pokemon table ID) as a foreign key. Then when accessing a pokemon I could have looked up their types in the type table using the Pokedex Number (more than 1 row may be returned from the type table). So instead, a Pokemon's types are stored as a string in pokemon table.