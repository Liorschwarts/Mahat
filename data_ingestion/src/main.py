from football_api import FootballApi
from sqlmodel import Session, create_engine, SQLModel
import os
from sqlalchemy import exc

def ingest_data():
    # Create the engine
    engine = create_engine(f"mysql+mysqlconnector://{os.environ['MYSQL_USER']}:{os.environ['MYSQL_PASSWORD']}@mysql/{os.environ['MYSQL_DATABASE']}")

    football_api = FootballApi()
    
    SQLModel.metadata.create_all(engine)

    # Open a session, add the data, and commit
    with Session(engine) as session:
        for team in football_api.get_teams():
            try:
                with session.begin_nested():
                    session.add(team)
            except exc.IntegrityError:
                print(f"Skipped record {team} - row already exists")
                    
        for competition in football_api.get_competitions():
            try:
                with session.begin_nested():
                    session.add(competition)
            except exc.IntegrityError:
                print(f"Skipped record {competition} - row already exists")
            
        session.commit()

    print("Data ingestion completed successfully")

if __name__ == "__main__":
    # for _ in range(3):  # Retry 3 times to load more data
    ingest_data()