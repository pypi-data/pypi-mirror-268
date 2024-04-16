# Lazy Mongo Log
Write to MongoDB as you print!

# Installation
```sh
pip install lazy-mongo-log
```

# How to Use
```py
from pymongo import MongoClient
from lazy_mongo_log import LazyMongoLog

mongo = MongoClient("mongodb://localhost:27017/")
database = mongo["my-database"]
collection = database["my-collection"]

const log = LazyMongoLog(
    collection=collection,
)

log("Hello World!") # Hello World!
```

### MongoDB

```json
{
    "type": "info",
    "keyword": null,
    "message": "Hello World!",
    "date_created": 2023-01-08T06:42:01.003+00:00
}
```

# Configuration
```py
from pymongo import MongoClient
from lazy_mongo_log import LazyMongoLog

mongo = MongoClient("mongodb://localhost:27017/")
database = mongo["my-database"]
collection = database["my-collection"]

log = LazyMongoLog(
    # The MongoDB collection.
    collection=collection,

    # The default type when using the `print(...)`.
    # Other stuff like `print.error(...)` are not affected.
    type="super cool info",

    # Keyword to be included in the log.
    keyword="my cool keyword",

    # If this should also print on the console.
    use_console=True,

    # Don't like the log document schema?
    # You can change it here!
    log_selector=lambda document : {
        "super_message": document["message"],
        "secret_type": document["type"],
        # I don't want your damn keywords!
        "hello": "world!",
    },
)
```

# Other Fun Stuff

### Changing Configurations
If you want to set the configurations later, you can do it like so:
```py
from pymongo import MongoClient
from lazy_mongo_log import LazyMongoLog

log = LazyMongoLog(
    # We can set the collection later.
    keyword="unicorns",
)

log("Hello World!") # Won't write to MongoDB...

mongo = MongoClient("mongodb://localhost:27017/")

database = mongo["my-database"]
collection = database["my-collection"]

log.set(
    collection=collection,
    keyword="dragons", # I want dragons instead.
)

log("Hello World!") # Now it does!
```

### Branching Configurations
Do you only want to change the configuration for one specific thing?
Here is how you do it:
```py
from pymongo import MongoClient
from lazy_mongo_log import LazyMongoLog

log = LazyMongoLog(
    # We can set the collection later.
    keyword="unicorns",
)

log.using(
    keyword="dragons",
)("This is a dragon") # keyword = "dragons"

log("This is a unicorn.") # keyword = "unicorns"

log.using(
    type="my lair",
)("Welcome!") # type = "my lair"

log("Welcome back!") # type = "info"

# You can also do this!
log.using(
    keyword="snakes",
    type="sneaky",
).using(
    keyword="bears",
).using(
    collection=mySuperCoolCollection,
    keyword="why are you doing this?!",
).warn("Because, why not?")
```

### Others
More tools to play with:
```py
# Print using `info` type.
log.info("Hello %s!", "World") # MongoDB: type = "info"

# Print using `warning` type. Uses `console.warn(...)`.
log.warn("Tread lightly...") # MongoDB: type = "warning"

# Print using `error` type. Uses `console.error(...)`.
log.error("Something bad happened!") # MongoDB: type = "error"
```