from pydantic import BaseModel,Field
from typing import Annotated,Literal


class input_validation(BaseModel):
    Hours_Studied : Annotated[int,Field(...,gt=0,lt=10,description="Enter Study Hour")]
    Previous_Scores : Annotated[int,Field(...,gt=0,lt=100,description="Enter Previous Scores")]
    Extracurricular_Activities : Annotated[str,Field(...,description="Enter Extracurricular Activities")]
    Sleep_Hours : Annotated[int,Field(...,gt=3,lt=10,description="Enter Sleep Hour")]
    Sample_Question_Papers_Practiced : Annotated[int,Field(...,gt=0,lt=10,description="Enter Sample Question Papers Practiced")]
