# Requirementes

# 1. Web Service Implementation

## Application
- As recommended, I have used Python 3.12.6 and FastAPI for developing the web application. 
- Given the fact that it is a relatively simple/small application, I did not use the Routers constrcuts; however, this makes the implementation less maintainble.
- To delegate some of the validation of the parameters of the requests, I used Pydantic Models. However, I did not take advance of them when returning responses (`response_model` parameter of a function defined for an endpoint).

### /move
Given the fact that it is a POST operation, I guessed that the tip was to make this an endpoint whose funcitionality is registering a new row on a table. This would be a table called "moves", where every register contains an id, the id of the match it was made at, the player that did it (symbol, "X" or "O"), and the square ([x,y]) it moved to.

**Note**: Keeping track of the moves was not only motivated by this POST-hint. It is much more realist (think about harder games), it may open the door the allow to revert the last move, it can be use dto extrac analytics or even to train the definitive AI player.

- Database requirements: `MoveSchema` in [schemas.py](../src/database/schemas.py).
    - id: Primary key. An integer that the DB automatically generates in increasing fasion. 
        - The client does not have to worry about giving an unique id. **THIS IS WHY IS NULLABLE IN THE PYDANTIC MODEL**.
        - It allows to order moves belonging to the same match. The smaller the id, the sooner the move was made.
    - match_id: Foreign Key. An integer that must appear as the id of a row in other table called "matches". It makes no sense storing a move that belongs to no match.
    - square: The position where the move was made. It was decomposed to two integer columns, x and y. They have to be bigger or equal than 1 and equal or less than 3. They cannot be null, it makes no sense.

- Logic of the endpoint:
    1. The endpoint recieves a request whose body specifies the niformation about the move. Thanks to the defined Pydantic models, a good portion of the data from the request is validated. Check `MoveModel` in [models.py](../src/models.py).
        - The id of the match (matchId) must be an integer not null.
        - The player that moves (playerId) must be a string equal to "X" or "O" and not null.
        - The defined square must be within the limits of the board and cannot be null.
    2. The `post_move(...)` function is invoked. Check [crud_operations.py](../src/crud_operations.py).
        - First, we check if the move is valid, can be registered (`check_move(...)`):
            - Check if the match it belongs to exist.
            - Check if that match is not over.
            - Check if it is the turn of the specified player in the move.
            - Check if the square is occupied.
            - In case of an error, the endpoint returns a 400 response giving some details about the reason f the fail.
        - Secondly, if everything went fine, the move is stored in the dabase.
        - Thirdly, the corresponding match has to be modified.
            - Actualize the turn.
            - Actualize the board.
            - Actualize the winner. 
        - Finally, the returned response. I opted for adding both, the stored move and the match to the client. Maybe was enough providing the id in the database of both, so then they can be checked at other endpoints.
    
### /status
The only thing left to the imagination was the type of the id and what to return, what the "overall" state of the game is. For the response, I chose returning all the fileds that the match has in database (id, turn, winner and board), if it does exist. If not, HTTP 4040 error.

- Database requirements: `MatchSchema` in [schemas.py](../src/database/schemas.py).
    - id: Primary key. An integer that the DB automatically generates in increasing fasion. 
        - The client does not have to worry about giving an unique id. **THIS IS WHY IS NULLABLE IN THE PYDANTIC MODEL**.
    winner: Null until winner. In that moment, only "X" or "O".
    - turn: Not nullable. "X" or "O". Checked from the Pydantic validation of the requests.
    - board: string. Checked from the Pydantic validation of the requests.
        - One character per cell, the (x,y) cell is accesed by board[3*x+y].
        - Can be "X", "O" or "_", representing both players and empty.
        - Choose this way because is really efficient to store/query (compared to a matrix).

- Logic of the Endpoint: `staus(...)` in [main.py](../src/main.py) and `get_match_by_id(...)` in [crud_operations.py](../src/crud_operations.py).
    1. The input must be an integer representing the game id.
    2. Simple query to the `matches` table at the database by primary key. 
        - If it does not exist, return a 404 HTTP error. 

### /create
Here, it was not defined the entry of the endpoint. I assumed that the body could be an already partially defined match or None.
- Logic of the Enpoint: `create(...)` in [main.py](../src/main.py) and `post_match_by_id(...)` in [crud_operations.py](../src/crud_operations.py).
    1. Again, the Pydantic models take good part of the input validation. Check `MatchModel` in [models.py](../src/models.py).
        - You can input nothing (this is also dealed with within the function's code).
        - You can input a whole match: id, board, turn and winner.
        - You can input just the id, and must be an integer.
        - You can input just the turn, and must be as single char equal to "X" or "O".
        - You can input just the board, and it must be an string of 9 characters result of a combination of X, O and _ (empty).
    2. If the id was specified, it must be checked that the match does NOT exist.
        - Return HTTP 404 error response if it does.
    3. After inserting it in the database, read the automatically asigned id to return it.
    4. Return the id.

## Logging
I did not add a logging feature. However, keeping in mind that `uvicorn` and `fastapi` use the `logging` package from `python`, the configuration should not be too cumbersome (if you have previously configured a python logger, which is not the case). 

## Database

For the database I used the easiest: SQLite, I wored with both databases in memory and databses in disk. I also included a script to generate a test/dummy database (check [README.md](../README.md)).

The schema for every table ("matches" and "moves") can be checked at the module [schemas.py](../src/database/schemas.py).

The relationship between the entities is many-to-one: one match can have many moves. One move, only one match.

This is the SQL commands to generate the tables (DDL):
```sql
CREATE TABLE matches (
	id INTEGER NOT NULL, 
	turn CHAR(1) NOT NULL, 
	winner CHAR(1), 
	board CHAR(9) NOT NULL, 
	PRIMARY KEY (id)
)
```

```sql
CREATE TABLE moves (
	id INTEGER NOT NULL, 
	"matchId" INTEGER, 
	"playerId" CHAR(1) NOT NULL, 
	x INTEGER NOT NULL, 
	y INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("matchId") REFERENCES matches (id)
)
```

**NOTE**: In the case of `moves`, `matchId` was declared a 

## Testing

To test the endpints I did lean on the `pytest` and `request` packages from `python`. Testing the server formally has revealed to be quite challenging as, even though the app is stateless, the database is not. This makes responses dependent of the previosly executed requests, which makes testing specially cumbersome when dealing with `/post` request. That is why, before testing every endpoint, the database should be re-instantiated and the server re-run too.

# 2. User Management Service Design

## High Level

Tipically, when talking about users in the context of web applications, users are presented by a set of credentials (user + password), a set of data information and operations that they may can do or not depending on who they are 

## API Changes
## Database Structure
## Architectural Changes

# 3. Cloud Microservices Design
