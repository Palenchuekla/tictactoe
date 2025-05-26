# Requirementes

# 1. Web Service Implementation

## Application
- As recommended, I have used Python 3.12.6 and FastAPI for developing the web application. 
- Given the fact that it is a relatively simple/small application, I did not use the Routers constrcuts; however, this makes the implementation less maintainble.
- To delegate some of the validation of the parameters of the requests, I used Pydantic Models. However, I did not take advance of them when returning responses (`response_model` parameter of a function defined for an endpoint).

### /move endpoint
Given the fact that it is a POST operation, I guessed that the tip was to make this an endpoint whose funcitionality is registering a new row on a table. This would be a table called "moves", where every register contains an id, the id of the match it was made at, the player that did it (symbol, "X" or "O"), and the square ([x,y]) it moved to.

**Note**: Keeping track of the moves was not only motivated by this POST-hint. It is much more realist (think about harder games), it may open the door the allow to revert the last move, it can be use dto extrac analytics or even to train the definitive AI player.

- Database requirements: "moves" table.
    - id: Primary key. An integer that the DB automatically generates in increasing fasion. 
        - The client does not have to worry about giving an id. **THIS IS WHY IS NULLABLE IN THE PYDANTIC MODEL**.
        - It allows to order moves belonging to the same match. The smaller the id, the sooner the move was made.
    - match_id: Foreign Key. An integer that must appear as the id of a row in other table called "matches". It makes no sense storing a move that belongs to no match.
    - square: The position where the move was made. It was decomposed to two integer columns, x and y. They have to be bigger or equal than 1 and equal or less than 3. They cannot be null, it makes no sense.

- Logic of the endpoint:
    1. The endpoint recieves a request whose body specifies the niformation about the move. Thanks to the defined Pydantic models, defined in [models.py](../src/models.py), a good portion of the data from the request is validated:
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
    
### /status endpoint
Pretty self explainatory, the only thing left to the imagination was the type of the id (I choose the most basic, integer) and what to return. For this last one, I choose all the fileds that a match has in the proposed database: id, turn, board .

- Database requirements:
    - id: Primary key. An integer that the DB automatically generates in increasing fasion. 
        - The client does not have to worry about giving an id. **THIS IS WHY IS NULLABLE IN THE PYDANTIC MODEL**.
    winner: Null until winner. In that moment, only "X" or "O".
    - turn: Not nullable. "X" or "O". Checked from the Pydantic validation.
    - board: string. One character per cell, the (x,y) cell is accesed by board[3*x+y]. Choose this way because is really efficient to store/query (compared to a matrix).

- Logic of the Endpoint: 
    1. Again, the Pydantic models take good part of the validation.
    2. Simple query. 404 error if not existent.

### /create endpoint
Here, it was not defined the entry of the endpoint. I assumed that the body could be an already defined match or None.
1. Again, the Pydantic models take good part of the validation.
2. Before creating, it must be checked that it does exist (in case we input a match with all it's fields, including the id).
## Logging
- I did not add a logging feature. However, you'd only need to add a new module (for example, at main's level, `logging.py`) where the package [logging](https://docs.python.org/3/library/logging.html) is imported to configure way we want to keep track of thing. Then, wherever we want our server to log something, we just have to import the logging module and use it as if it was a "print". However, before hand, we have specified a pretty format and different levels to filter the messages (debug, information, warning, error or critical).

## Database

For the database I used the easiest: SQLite, I wored with both databases in memory and databses in disk. I also included a script to generate a test/dummy database (check [README.md](../README.md)).

The schema for every table ("matches" and "moves") can be checked at the module [schemas.py](../src/database/schemas.py).

# 2. User Management Service Design

# 3. Cloud Microservices Design
