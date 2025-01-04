"""Module to define the database models for the app."""

from sqlmodel import SQLModel, Field, Relationship

class HealthInfluencer(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    twitter_url: str
    twitter_nickname: str
    followers: int
    trend: str # up, down
    number_verified_claims: int
    stimated_annual_earnings: float

    #claims: list["Claim"] = Relationship(back_populates="health_influencer")

class HealthClaim(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    claim: str
    source: str
    date: str
    health_influencer_id: int

    #health_influencer: HealthInfluencer = Relationship(back_populates="claims")


# also i could have a table for user social media accounts
# class HealthInfluencerSocialMedia(SQLModel, table=True):
#    id: int = None
#    health_influencer_id: int
#    social_media_id: int
#    url: str
