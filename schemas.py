from pydantic import BaseModel


class Calculate(BaseModel):
    id: int
    request: str
    response: str
    status: str

    class Config:
        orm_mode = True