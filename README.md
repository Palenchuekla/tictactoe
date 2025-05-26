# TicTacToe
Tic-Tac-Toe basic backend implementation.
# Repository
The repository is strcutured in the following manner:
- [.config/.env](./config): Contains configuration parameters of the project. It is a violation of the 12-Factor-App, but it was included for simplicity. Configuraiton is built on top of environment variables.
- [scripts](./script): Once the installation is done, they allow to set the server running ([run_server.sh](./scripts/run_server.sh)), build a local SQLite database for it ([create_db.sh](./scripts/create_db.sh)) and execute some tests ([run_test.sh](./scripts/run_tests.sh)).
- [scr](./src): Source code of the application. It is build as a Python package. Database specific code (stablish connection, entity schemas, session generators ...) has been isolated into its own subpackage [database](./src/database).
- [test](./test): Some Python scripts to test the implemented endpoints.
# Installation
1. Clone the repository.
```bash
git clone https://github.com/Palenchuekla/tictactoe
```
2. Create and activate a virtual enviroment. You can check [FastAPI guide](https://fastapi.tiangolo.com/virtual-environments/) on this matter, but there is a lot of alternatives like [Conda](https://anaconda.org/anaconda/conda). Here is a simple way when using bash.
```bash
python -m venv .venv
source .venv/Scripts/activate
````
3. Install the requirements using `python` and `pip`.
```bash
pip install -r requirements.txt
```

# Execution

> [!WARNING]  
> DO NOT forget to activate your virtual environment before exeuting any of the following. You can omit this step if you opted for an alternative.

### Create Database
For simplicity, during development a disk SQLite database was used. However, the code should be Database independent, as long as is compatible with [SQLAlchemy](https://www.sqlalchemy.org/). 

To create said database, on a terminal window, navigate to the [root directory](.) of the repository, activate the virtual environment and execute the following command. You can execute the script from anywhere too.
```bash
 bash scripts/create_db.sh 
```
### Run the Server
To set the server running, on a terminal window, navigate to the [root directory](.) of the repository, activate the virtual environment and execute the following command. You can execute the script from anywhere too.
```bash
 bash scripts/run_server.sh 
```
Now, the server should be up and running waiting for our requests.

### Run the Tests
To run the tests, with the server running, on a terminal window, navigate to the [root directory](.) of the repository, activate the virtual environment and execute the following command. You can execute the script from anywhere too.
```bash
 bash scripts/run_server.sh 
```