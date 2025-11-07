from sqlmodel import Field, SQLModel, Column
from sqlalchemy import Text, JSON, func
from datetime import datetime


class post(SQLModel, table= True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(max_length=255, nullable=False)
    content: str = Field(sa_column=Column(Text, nullable=False))
    category: str = Field(max_length=100, nullable=False)
    tags: list[str] | None = Field(default=None, sa_column=Column(JSON))
    created_at: datetime = Field(
        sa_column=Column(
            # usa la hora del servidor o la actual
            default=func.now(),  
            nullable=False
        )
    )
    updated_at: datetime = Field(
        sa_column=Column(
            default=func.now(),
            onupdate=func.now(),
            nullable=False
        )
    )
