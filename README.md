# TicTacToe
Tic-Tac-Toe basic backend implementation. Answers to the questions from the original document on [doc](./doc).
# Repository
The repository is strcutured in the following manner:
- [scripts](./script): Once the installation is done, they allow to set the server running ([run_server.sh](./scripts/run_server.sh)), build (and even populate) a local SQLite database ([create_db.sh](./scripts/create_db.sh) and [create_db.py](./src/database/create_db.py)) and execute some tests. Tests are database dependent and `/post` operations affect the state of the databse (and consecuently the response of the data), so they are
- [src](./src): Source code of the application. It is build as a Python package. Database specific code (stablish connection, entity schemas, session generators ...) has been isolated into its own subpackage [database](./src/database).
- [test](./test): Some python scripts to test the implemented endpoints with `pytest`.
# Installation
1. Clone the repository.
```bash
git clone https://github.com/Palenchuekla/tictactoe
```
2. Create and activate a virtual enviroment. You can check [FastAPI guide](https://fastapi.tiangolo.com/virtual-environments/) on this matter, but there is a lot of alternatives like [Conda](https://anaconda.org/anaconda/conda). Here is a simple way when using bash.
```bash
python -m venv .venv
source .venv/Scripts/activate
```
3. Install the requirements using `python` and `pip`.
```bash
pip install -r requirements.txt
```

# Execution

> [!WARNING]  
> DO NOT forget to activate your virtual environment before exeuting any of the following. You can omit this step if you opted for an alternative.

## Create Database
For simplicity, during development a disk SQLite database was used. However, the code should be Database independent, as long as is compatible with [SQLAlchemy](https://www.sqlalchemy.org/). 

To create said database, activate the virtual environment and execute the following commands.
```bash
source scripts/create_db.sh -v -p -n tictactoe
```
Check the script `-h|--help` to see how to specifiy the database name and to create this databse empty or populated with some examples.

The database will always be created at a local temporal directory called `./tmp` on the root directory of the repository. It will be created if not existent. This way we do not have to deal with privilege and removing sensible information problems.

The creation will not happen if a database with the same path already exists. User will be kindly asked to manuallly remove it to avoid not so lucky miss-commands.

I highly recommend using [SQLite Browser](https://sqlitebrowser.org/) to check and manipulate the database interactively with an intuituve GUI.

## Run the Server
To set the server running, activate the virtual environment and execute the following commands.
```bash
source scripts/run_server.sh --url sqlite+pysqlite:///./tmp/tictactoe.db
```
Check the script `-h|--help` to see how to set the database URL of the server's databse.

Now, the server should be up and running waiting for our requests.

# Testing
Testing in this context means comparing the response of the server with the expected responses. Even though the web application is stateless, information accessed is not. Responses are dependant of the state of the database and this state depends on the previously executed requests. To make testing with a tool like `pytest` less cumbersome for endpoints that alter the database like `/create` or `/move`, database is re-instantiated before testing every endpoint, as well as the server is re-launched. It is not ideal, the main of having database and web app isolated is for them to be independent, an error/change on the database side should not break the applicaiton.
### /status
- To test the `/status` endpoint.
1. Create a populated database using the [create_db.sh](./scripts/create_db.sh) script with the `-p|--populated` argument (check `-h|--help`).
```bash
source ./scripts/create_db.sh -v -p -n tictactoe
```
2. Run the server using the [run_server.sh](./scripts/run_server.sh) script with the `-u|--url` set to the created database.
```bash
source ./scripts/run_server.sh --url sqlite+pysqlite:///./tmp/tictactoe.db 
```
3. Execute the following command.
```bash
source scripts/test_status.sh 
```
### /create
- To test the `/create` endpoint.
1. Create an empty database using the [create_db.sh](./scripts/create_db.sh) script without the `-p|--populated` argument (check `-h|--help`).
2. Run the server using the [run_server.sh](./scripts/run_server.sh) script with the `-u|--url` set to the created database (check `-h|--help`).
3. Execute the following command.
```bash
 source scripts/test_create.sh 
```
### /move
- To test the `/move` endpoint.
1. Create a populated database using the [create_db.sh](./scripts/create_db.sh) script with the `-p|--populated` argument (check `-h|--help`).
```bash
source ./scripts/create_db.sh -v -p -n tictactoe
```
2. Run the server using the [run_server.sh](./scripts/run_server.sh) script with the `-u|--url` set to the created database (check `-h|--help`).
```bash
source ./scripts/run_server.sh --url sqlite+pysqlite:///./tmp/tictactoe.db 
```
3. Execute the following command.
```bash
 bash scripts/test_move.sh 
```
