"""Module to define the database models for the app."""

from typing import Annotated

from sqlmodel import Field, Relationship, SQLModel


class HealthCategory(SQLModel, table=True):
    """Represents the categories of health claims.

    It's a table and not an enum since it can change over time.
    + one claim can have multiple categories.
    """

    __tablename__ = "HEALTH_CATEGORY"
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    health_claims: list["HealthClaim"] = Relationship(
        back_populates="health_categories"
    )


class HealthClaim(SQLModel, table=True):
    __tablename__ = "HEALTH_CLAIM"
    id: int | None = Field(default=None, primary_key=True)
    claim_text: str
    url_source: Annotated[
        str, "Social media url post, tweet, etc. where the claim was made"
    ]
    date: Annotated[str, "Date when the claim was made (publication of the post)"]

    health_influencer_id: int = Field(
        foreign_key="HEALTH_INFLUENCER.id", ondelete="CASCADE"
    )
    health_influencer: "HealthInfluencer" = Relationship(back_populates="health_claims")
    health_categories: list[HealthCategory] = Relationship(
        back_populates="health_claims"
    )


class ClaimHealthCategory(SQLModel, table=True):
    """Represents Association table between HealthClaim and HealthCategory.

    since it's a many-to-many relationship.
    """

    __tablename__ = "CLAIM_HEALTH_CATEGORY"
    claim_id: int | None = Field(
        default=None, foreign_key="HEALTH_CLAIM.id", primary_key=True
    )
    category_id: int | None = Field(
        default=None, foreign_key="HEALTH_CATEGORY.id", primary_key=True
    )


class HealthInfluencer(SQLModel, table=True):
    __tablename__ = "HEALTH_INFLUENCER"
    id: int | None = Field(default=None, primary_key=True)
    name: str | None
    twitter_url: str = Field(unique=True)
    twitter_nickname: str = Field(index=True, unique=True)
    followers: int
    trend: str  # "up" | "down" | "stable"]

    trust_score_avg: float
    number_verified_claims: int = 0
    estimated_annual_earnings: float
    primary_category_id: Annotated[
        int | None, "Category in which the influencer has made most claims"
    ] = Field(foreign_key="HEALTH_CATEGORY.id", default=None)

    health_claims: list["HealthClaim"] = Relationship(
        back_populates="health_influencer",
        cascade_delete=True,
    )
    primary_category: HealthCategory | None = Relationship()


# NOTE(@jfmonsa): it could exits a table for user social media accounts
# e.g. HealthInfluencerSocialMedia(id, health_influencer_id, social_media_id, url)
