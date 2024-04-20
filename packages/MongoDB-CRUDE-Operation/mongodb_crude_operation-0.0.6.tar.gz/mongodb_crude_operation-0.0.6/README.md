# `Description:`

mongo-operation is a Python library for simplifying MongoDB operations by providing an easy-to-use interface. This library allows users to perform common MongoDB tasks such as creating a client, database, or collection, as well as inserting records into collections and bulk inserting data from CSV or Excel files.

# `Features:`

MongoClient Creation: Easily create a MongoDB client with a given URL.
Database and Collection Management: Create databases and collections with ease, and automatically handle re-creating them if they already exist.
Insertion Operations: Insert records into MongoDB collections, whether it's a single record or bulk data from CSV or Excel files.


# `Example Usage:`

`python code`

from MongoDB_CRUDE_Operation.mongodb_connect.mongo_crud import  mongo_operation

Initialize MongoDB connection
client_url = "mongodb://localhost:27017/"
database_name = "mydatabase"
collection_name = "mycollection"

mongo_op = mongo_operation(client_url, database_name, collection_name)

Insert a single record
record = {"name": "John", "age": 30}
mongo_op.insert_record(record, collection_name)

Bulk insert data from CSV or Excel file
datafile = "data.csv"
mongo_op.bulk_insert(datafile, collection_name)

## `Requirements:`

Python 3.x
pandas
pymongo
ensure






### requirements_dev.txt we use for the testing
It makes it easier to install and manage dependencies for development and testing, separate from the dependencies required for production.

### difference between requirements_dev.txt and requirements.txt

requirements.txt is used to specify the dependencies required to run the production code of a Python project, while requirements_dev.txt is used to specify the dependencies required for development and testing purposes.

### tox.ini
We use if for the testing in the python package testing against different version of the python 

### how tox works tox enviornment creation
1. Install depedencies and packages 
2. Run commands
3. Its a combination of the (virtualenvwrapper and makefile)
4. It creates a .tox


### pyproject.toml
it is being used for configuration the python project it is a alternative of the setup.cfg file. its containts configuration related to the build system
such as the build tool used package name version author license and dependencies

### setup.cfg
In summary, setup.cfg is used by setuptools to configure the packaging and installation of a Python projec

### Testing python application
*types of testing*
1. Automated testing 
2. Manual testing

*Mode of testing*
1. Unit testing
2. Integration tests

*Testing frameworks*

1. pytest
2. unittest
3. robotframework
4. selenium
5. behave
6. doctest

### check with the code style formatting and syntax(coding standard)

1. pylint
2. flake8(it is best because it containt 3 library pylint pycodestyle mccabe)
3. pycodestyle

