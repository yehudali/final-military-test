from pydantic import BaseModel, Field


class IntelMesege(BaseModel):
    timestamp : str
    signal_id : str
    entity_id : str
    reported_lat : float
    reported_lon : float
    signal_type:str
    priority_level:int = Field(default=99)

