from typing import Optional
from sqlmodel import SQLModel, Field

class Area(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    code: str
    flag: str
    
# from typing import Optional
# from sqlmodel import SQLModel, Field
# from sqlalchemy import Sequence, Column, Integer

# # Define the sequence
# area_id_seq = Sequence('area_id_seq')

# class Area(SQLModel, table=True):
#     id: Optional[int] = Field(
#         sa_column=Column(
#             Integer, 
#             area_id_seq, 
#             server_default=area_id_seq.next_value(), 
#             primary_key=True
#         )
#     )
#     name: str
#     code: str
#     flag: str