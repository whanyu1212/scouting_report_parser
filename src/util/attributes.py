from pydantic import BaseModel, Field


class ScoutingFeatures(BaseModel):
    name: str = Field(
        ...,
        description="Player's name",
    )
    height: str = Field(
        ...,
        description="Player's height",
    )
    weight: str = Field(
        ...,
        description="Player's weight in lbs",
    )
    dob: str = Field(
        ...,
        description="Player's date of birth",
    )
    college: str = Field(
        ...,
        description="Player's college/university name",
    )
    offense: int = Field(
        ...,
        description="How good is the player at offense? Give a rating of 1 to 10",
        enum=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    )
    defense: int = Field(
        ...,
        description="How good is the player at defense? Give a rating of 1 to 10",
        enum=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    )
    athleticism: int = Field(
        ...,
        description="How athletic is the player? Give a rating of 1 to 10",
        enum=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    )
    basketball_iq: int = Field(
        ...,
        description="How good is the player's basketball IQ? Give a rating of 1 to 10",
        enum=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    )
    mentality: int = Field(
        ...,
        description="How good is the player's mentality, e.g. confidence, work ethic? Give a rating of 1 to 10",
        enum=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    )
    ceiling: int = Field(
        ...,
        description="Does the player have a high ceiling? How good is/was his NBA comparison? Give a rating of 1 to 10",
        enum=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    )
