import os
import sqlite3
from pprint import pprint
import argparse
from warnings import warn
from pathlib import Path

from . import core
from . import schemas

def create_disk_sqlite_db(path : Path):
    '''
    '''
    try:
        with sqlite3.connect(f"") as conn:
            print(f"Created SQLite database ({path}) with version {sqlite3.sqlite_version} successfully.")
    except sqlite3.OperationalError as e:
        raise("Failed to open database:", e)

def create_example_db(path : Path, populate : bool = True, verbose : bool = False):
    '''
    '''
    # Create SQLite local disk-stored database
    create_disk_sqlite_db(path=path)
    # Connecting to DataBase: craeting engine and session maker
    db = core.DataBase(url=f"sqlite+pysqlite:///{path}")
    # Creating table
    db.create_tables()
    # Popualting table with test examples
    if populate: 
        with db.get_session_to_db_NOFastAPI() as session:
            
            matches = []
            moves = []

            matches.append(schemas.MatchSchema(turn="O", board="___X_____"))
            moves.append(schemas.MoveSchema(matchId=1, playerId="X", x=1+1, y=0+1))

            matches.append(schemas.MatchSchema(turn="X", board="O____X___"))
            moves.append(schemas.MoveSchema(matchId=2, playerId="X", x=1+1, y=2+1))
            moves.append(schemas.MoveSchema(matchId=2, playerId="O", x=0+1, y=0+1))

            matches.append(schemas.MatchSchema(turn="O", board="_X__X__O_"))
            moves.append(schemas.MoveSchema(matchId=3, playerId="X", x=0+1, y=1+1))
            moves.append(schemas.MoveSchema(matchId=3, playerId="O", x=2+1, y=1+1))
            moves.append(schemas.MoveSchema(matchId=3, playerId="X", x=1+1, y=1+1))

            matches.append(schemas.MatchSchema(turn="X", board="__OO___X_"))
            moves.append(schemas.MoveSchema(matchId=4, playerId="X", x=0+1, y=2+1))
            moves.append(schemas.MoveSchema(matchId=4, playerId="O", x=1+1, y=0+1))
            moves.append(schemas.MoveSchema(matchId=4, playerId="X", x=2+1, y=1+1))

            matches.append(schemas.MatchSchema(turn="O", winner="X", board="XXX___OO_"))
            moves.append(schemas.MoveSchema(matchId=5, playerId="X", x=0+1, y=0+1))
            moves.append(schemas.MoveSchema(matchId=5, playerId="O", x=2+1, y=0+1))
            moves.append(schemas.MoveSchema(matchId=5, playerId="X", x=0+1, y=1+1))
            moves.append(schemas.MoveSchema(matchId=5, playerId="O", x=2+1, y=1+1))
            moves.append(schemas.MoveSchema(matchId=5, playerId="X", x=0+1, y=2+1))

            matches.append(schemas.MatchSchema(turn="O", board="XXOXO__OX"))
            moves.append(schemas.MoveSchema(matchId=6, playerId="X", x=0+1, y=0+1))
            moves.append(schemas.MoveSchema(matchId=6, playerId="O", x=1+1, y=1+1))
            moves.append(schemas.MoveSchema(matchId=6, playerId="X", x=0+1, y=1+1))
            moves.append(schemas.MoveSchema(matchId=6, playerId="O", x=0+1, y=2+1))
            moves.append(schemas.MoveSchema(matchId=6, playerId="X", x=1+1, y=0+1))
            moves.append(schemas.MoveSchema(matchId=6, playerId="O", x=2+1, y=1+1))
            moves.append(schemas.MoveSchema(matchId=6, playerId="X", x=0+1, y=2+1))
            
            session.add_all(matches)
            session.add_all(moves)
            
            session.commit()
    # Verbose
    if verbose and populate:
        print(" --- MATCHES TABLE ---")
        pprint(session.query(schemas.MatchSchema).all())
        print(" --- MOVES TABLE ---")
        pprint(session.query(schemas.MoveSchema).all())

def main():
    # Parse Argument
    parser = argparse.ArgumentParser( 
                    prog='create_example_db',
                    description='This program creates a local SQLite database at the path specified.',
                    )
    parser.add_argument("-i", "--db_path", type=str, help="Path where the database will be created", required=True,)
    parser.add_argument("-v", "--verbose", help="Output contens of the created DB in a human understandable way",  action="store_true",)
    parser.add_argument("-p", "--populate", help="Populate the database with test examples",  action="store_true",)
    args = parser.parse_args()

    # Validate arguments
    # 2) Does the directory containing directory of DUMMY_DATABASE_PATH exist?
    containig_dir = Path(args.db_path).parent
    if not containig_dir.exists():
        raise Exception(f"Directory that must contain the database \"{containig_dir}\" does not exist.")
    # 2) Create DB (and populate)
    if os.path.exists(f"{args.db_path}"):
        print(f"\"{os.path.abspath(args.db_path)}\" already exists!\nManually erase it and call this script again if you want to re-instantiate it.")
    else:
        create_example_db(f"{args.db_path}", verbose=args.verbose, populate=args.populate)


if __name__ == "__main__":
    main()