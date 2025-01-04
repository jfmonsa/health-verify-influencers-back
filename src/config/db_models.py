"""Module to define the database models for the app."""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated, Literal

from src.utils.to_snake_case import to_snake_case

if TYPE_CHECKING:
    from pydantic import HttpUrl

from sqlalchemy.orm import declared_attr
from sqlmodel import Field, Relationship
from sqlmodel import SQLModel as _SQLModel


class SQLModel(_SQLModel):
    @declared_attr
    def __tablename__(self) -> str:
        """Set the snake case of the class name of the model as the table name."""
        return to_snake_case(self.__class__.__name__)


class HealthInfluencer(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str | None
    twitter_url: HttpUrl = Field(unique=True)
    twitter_nickname: str = Field(index=True, unique=True)
    followers: int
    trend: Literal["up", "down", "stable"]
    trust_score_avg: float
    number_verified_claims: int = 0
    estimated_annual_earnings: float
    primary_category_id: Annotated[
        int | None, "Category in which the influencer has made most claims"
    ] = Field(foreign_key="health_category.id", default=None)

    health_claims: list[HealthClaim] = Relationship(
        back_populates="health_influencer", cascade_delete=True
    )
    primary_category: HealthCategory = Relationship()


class HealthClaim(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    claim_text: str
    url_source: Annotated[
        HttpUrl, "Social media url post, tweet, etc. where the claim was made"
    ]
    date: Annotated[str, "Date when the claim was made (publication of the post)"]

    health_influencer_id: int = Field(
        foreign_key="health_influencer.id", ondelete="CASCADE"
    )
    health_influencer: HealthInfluencer = Relationship(back_populates="health_claims")
    health_categories: list[HealthCategory] = Relationship(
        back_populates="health_claims"
    )


class HealthCategory(SQLModel, table=True):
    """Represents the categories of health claims.

    It's a table and not an enum since it can change over time.
    + one claim can have multiple categories.
    """

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    health_claims: list[HealthClaim] = Relationship(back_populates="health_categories")


class ClaimHealthCategory(SQLModel, table=True):
    """Represents Association table between HealthClaim and HealthCategory.

    since it's a many-to-many relationship.
    """

    claim_id: int | None = Field(
        default=None, foreign_key="health_claim.id", primary_key=True
    )
    category_id: int | None = Field(
        default=None, foreign_key="health_category.id", primary_key=True
    )


# NOTE(@jfmonsa): it could exits a table for user social media accounts
# e.g. HealthInfluencerSocialMedia(id, health_influencer_id, social_media_id, url)
