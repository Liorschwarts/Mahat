from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from .team import Team

class CurrentSeason(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    startDate: str
    endDate: str
    currentMatchday: int
    winner_id: Optional[int] = Field(default=None, foreign_key="team.id")
    winner: Optional[Team] = Relationship()
    
# from sqlmodel import SQLModel, Field, Relationship
# from typing import Optional
# from .team import Team
# from sqlalchemy import Sequence, Column, Integer

# # Define the sequence
# current_season_id_seq = Sequence('current_season_id_seq')

# class CurrentSeason(SQLModel, table=True):
#     id: Optional[int] = Field(
#         sa_column=Column(
#             Integer, 
#             current_season_id_seq, 
#             server_default=current_season_id_seq.next_value(), 
#             primary_key=True
#         )
#     )
#     startDate: str
#     endDate: str
#     currentMatchday: int
#     winner_id: Optional[int] = Field(default=None, foreign_key="team.id")
#     winner: Optional[Team] = Relationship()