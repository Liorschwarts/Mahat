from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from .current_season import CurrentSeason
from .area import Area

class Competition(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    area_id: int = Field(foreign_key="area.id")
    area: Area = Relationship()
    name: str
    code: str
    type: str 
    emblem: str 
    plan: str 
    currentSeason_id: int = Field(foreign_key="currentseason.id")
    currentSeason: CurrentSeason = Relationship()
    numberOfAvailableSeasons: str 
    lastUpdated: str
    
# from typing import Optional
# from sqlmodel import SQLModel, Field, Relationship
# from .current_season import CurrentSeason
# from .area import Area
# from sqlalchemy import Sequence, Column, Integer

# # Define the sequence
# competition_id_seq = Sequence('competition_id_seq')

# class Competition(SQLModel, table=True):
#     id: Optional[int] = Field(
#         sa_column=Column(
#             Integer, 
#             competition_id_seq, 
#             server_default=competition_id_seq.next_value(), 
#             primary_key=True
#         )
#     )
#     area_id: int = Field(foreign_key="area.id")
#     area: Area = Relationship()
#     name: str
#     code: str
#     type: str 
#     emblem: str 
#     plan: str 
#     currentSeason_id: int = Field(foreign_key="currentseason.id")
#     currentSeason: CurrentSeason = Relationship()
#     numberOfAvailableSeasons: str 
#     lastUpdated: str