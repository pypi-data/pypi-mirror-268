# AsyncPOW - https://github.com/totaldebug/asyncpow
#
# Copyright (c) 2024 Steven Marks, Total Debug
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


from typing import Literal

from pydantic import BaseModel

SortOptions = Literal["added", "modified", "mediaAdded"]
MediaType = Literal["movie", "tv"]


class UserModel(BaseModel):
    """
    Data class representing a user model.
    """

    displayName: str
    id: int
    email: str
    username: str | None = None
    password: str | None = None
    resetPasswordGuid: str | None = None
    recoveryLinkExpirationDate: str | None = None
    userType: int
    plexId: int | None = None
    plexToken: str | None = None
    plexUsername: str | None = None
    permissions: int
    avatar: str
    createdAt: str
    updatedAt: str
    requestCount: int
    requests: list | None = None  # TODO: Requests
    movieQuotaLimit: int | None = None
    movieQuotaDays: int | None = None
    tvQuotaLimit: int | None = None
    tvQuotaDays: int | None = None
    settings: dict | None = None  # TODO: UserSettingsModel
    pushSubscriptions: list | None = None  # TODO: UserPushSubscriptionModel
    createdIssues: list | None = None  # TODO: IssueModel


class PageInfoModel(BaseModel):
    """
    Data class representing page information.

    As per code
    """

    page: int
    pages: int
    results: int
    pageSize: int


class PaginatedResponseModel(BaseModel):
    """
    Data class representing page information.

    As per code
    """

    pageInfo: PageInfoModel


class CastModel(BaseModel):
    """
    Data class representing a cast member.
    """

    id: int
    castId: int | None = None
    character: str
    creditId: str
    gender: int
    name: str
    order: int
    profilePath: str | None


class CrewModel(BaseModel):
    """
    Data class representing a crew member.
    """

    id: int
    creditId: str | None = None
    gender: int
    name: str
    job: str
    department: str
    profilePath: str | None


class CreditModel(BaseModel):
    """Data class representing Credits"""

    cast: list[CastModel]
    crew: list[CrewModel]


class GenreModel(BaseModel):
    """
    Data class representing a movie genre.
    """

    id: int
    name: str


class SpokenLanguagesModelTv(BaseModel):
    """
    Data class representing a spoken language.
    """

    englishName: str
    iso_639_1: str
    name: str


class SpokenLanguagesModelMovie(BaseModel):
    """
    Data class representing a spoken language.
    """

    english_name: str
    iso_639_1: str
    name: str


class ExternalIdsModel(BaseModel):
    """
    Data class representing external IDs.
    """

    facebookId: str | None = None
    freebaseId: str | None = None
    freebaseMid: str | None = None
    imdbId: str | None = None
    instagramId: str | None = None
    tvdbId: int | None = None
    tvrageId: int | None = None
    twitterId: str | None = None


class KeywordModel(BaseModel):
    """Data class representing a Keyword"""

    id: int
    name: str


class WatchProviderDetailsModel(BaseModel):
    """
    Data class representing a watch provider details.
    """

    displayPriority: int
    logoPath: str
    id: int
    name: str


class WatchProviderModel(BaseModel):
    """
    Data class representing a watch provider.
    """

    iso_3166_1: str
    link: str
    buy: list[WatchProviderDetailsModel]
    flatrate: list[dict]


class ProductionCompanyModel(BaseModel):
    """
    Data class representing a production company.
    """

    id: int
    logoPath: str | None
    originCountry: str
    name: str


class ProductionCountryModel(BaseModel):
    """
    Data class representing a production country.
    """

    iso_3166_1: str
    name: str


class SeasonModel(BaseModel):
    """
    Data class representing a Season.
    """

    airDate: str | None = None
    id: int
    episodeCount: int
    name: str
    overview: str
    posterPath: str | None = None
    seasonNumber: int
