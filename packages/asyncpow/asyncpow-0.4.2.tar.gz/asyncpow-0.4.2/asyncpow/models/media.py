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

from asyncpow.models.common import MediaType, PaginatedResponseModel, SeasonModel, UserModel

MediaFilterOptions = Literal["all", "available", "partial", "allavailable", "pending", "processing"]

MediaStatusOptions = Literal["available", "partial", "pending", "processing", "unknown"]


class MediaRequestModel(BaseModel):
    """
    Data class representing a media request model.

    As per code
    """

    id: int
    status: int  # 1 = PENDING APPROVAL, 2 = APPROVED, 3 = DECLINED
    media: "MediaInfoModel"
    requestedBy: UserModel
    modifiedBy: UserModel | None = None
    createdAt: str
    updatedAt: str
    type: MediaType
    is4k: bool
    serverId: int | None = None
    profileId: int | None = None
    rootFolder: str | None = None
    languageProfileId: int | None = None
    tags: list | None = None
    isAutoRequest: bool = False
    seasonCount: int | None = None
    seasons: list["SeasonRequestModel"] | None = None


class MediaInfoModel(BaseModel):
    """
    Data class representing media information model.
    """

    id: int
    mediaType: MediaType
    tmdbId: int
    status: int  # 1 = UNKNOWN, 2 = PENDING, 3 = PROCESSING, 4 = PARTIALLY_AVAILABLE, 5 = AVAILABLE
    status4k: int

    createdAt: str
    updatedAt: str
    lastSeasonChange: str
    issues: dict | None = None  # TODO: Add list of issues model
    mediaAddedAt: str | None = None
    serviceId: int | None = None
    serviceId4k: int | None = None
    externalServiceId: int | None = None
    externalServiceId4k: int | None = None
    externalServiceSlug: str | None = None
    externalServiceSlug4k: str | None = None
    ratingKey: str | None = None
    ratingKey4k: str | None = None
    requests: list[MediaRequestModel] | None = None
    plexUrl: str | None = None
    plexUrl4k: str | None = None
    iOSPlexUrl: str | None = None
    iOSPlexUrl4k: str | None = None
    tautulliUrl: str | None = None
    tautulliUrl4k: str | None = None
    serviceUrl: str | None = None
    serviceUrl4k: int | None = None
    tvdbId: int | None = None
    imdbId: int | None = None
    downloadStatus: list | None = None
    downloadStatus4k: list | None = None
    seasons: list[SeasonModel] | list | None = None


class SeasonRequestModel(BaseModel):
    """Model for TV Seasons"""

    id: int
    seasonNumber: int
    status: int = 1  # PENDING = 1, APPROVED = 2, DECLINED = 3, FAILED = 4
    request: MediaRequestModel | None = None
    createdAt: str
    updatedAt: str


class MediaModel(PaginatedResponseModel):
    """
    Data class representing a media model.
    """

    results: MediaInfoModel


class MediaModel2(BaseModel):
    """
    Data class representing a secondary media model.
    """

    id: int
    tmdbId: int
    tvdbId: int
    status: int
    requests: list[MediaInfoModel]
