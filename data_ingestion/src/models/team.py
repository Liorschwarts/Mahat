from typing import Optional
from sqlmodel import SQLModel, Field

class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    shortName: str
    tla: str
    crest: str
    address: str
    website: str
    founded: int
    clubColors: str
    venue: str
    lastUpdated: str
    
# from typing import Optional
# from sqlmodel import SQLModel, Field
# from sqlalchemy import Sequence, Column, Integer

# # Define the sequence
# team_id_seq = Sequence('team_id_seq')

# class Team(SQLModel, table=True):
#     id: Optional[int] = Field(
#         sa_column=Column(
#             Integer, 
#             team_id_seq, 
#             server_default=team_id_seq.next_value(), 
#             primary_key=True
#         )
#     )
#     name: str
#     shortName: str
#     tla: str
#     crest: str
#     address: str
#     website: str
#     founded: int
#     clubColors: str
#     venue: str
#     lastUpdated: str