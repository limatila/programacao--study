//First creation and insertion

//! IMPORTANT: need to use it in MongoShell.
// example in mongosh: load( "connect-and-insert.js" )

//* Connecting to local mongo for shell.
db = connect("mongodb://localhost/")

// in a simples resume, documents(registrys) are composed by JS Object Notation, so they are declared and inserted as such.
// in a JSON, all of its data is contained in key: value pairs, where values can be from any type, and can by Objects or Arrays of purely data.
use("Receitas")

//Using a recipes site as a reference, we'll build it like it has Users, Recipes(published by users), Comments...

//Collections: groups of Documents. While Documents contain data, Collections contain and organize Documents (like Relacional tables)
//* Creating a Collection
db.createCollection("users");

//* Inserting a object of data (Document) inside the Collection
db.users.insertOne(
    {
        name: "Átila",
        age: 19,
        profession: "Developer",
        locality: "Fortaleza/CE, Brasil",
        activeUser: true,
        skills: {  //By Year
            py: 2,
            js: 1,
        },
    },
)
//? notice IDs for Documents are NOT NECESSARY to be created in mongodb, as a random one is always created automatically.

//* Find ('Select') all Documents in the Collection
db.users.find();