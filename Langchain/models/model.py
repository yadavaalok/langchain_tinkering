from enum import Enum
from pydantic import BaseModel, Field


class Details(BaseModel):
    model_name: str = Field(
        ...,
        description="This is the model name.",
        enum=["MX", "AX3", "AX5", "AX7", "AX7L"]
    )
    transmission_type: str = Field(
        ...,
        description="This is the transmission type.",
        enum=["Auto", "Manual"]
    )
    fuel_type: str = Field(
        ...,
        description="This is the fuel type ",
        enum=["Petrol", "Diesel"]
    )
    drive_type: str = Field(
        ...,
        description="This is the drive type",
        enum=["AWD", "FWD"]
    )
