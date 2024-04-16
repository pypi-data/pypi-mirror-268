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

from aiohttp import ClientSession, hdrs
from yarl import URL

from asyncpow.apis.movie import Movie
from asyncpow.apis.tv import Tv
from asyncpow.exceptions import POWException, POWMediaTypeException
from asyncpow.models.common import SortOptions
from asyncpow.models.media import MediaRequestModel
from asyncpow.models.request import RequestFilterOptions, RequestResultsResponseModel
from asyncpow.models.tv import TvDetailsModel
from asyncpow.utils.http import request


class Request:
    """
    Class to interact with request-related endpoints.

    Initialize the Request object with the base URL, API key, and session.
    """

    def __init__(
        self,
        base_url: URL,
        api_key: str,
        session: ClientSession,
        tv_instance: Tv,
        movie_instance: Movie,
    ) -> None:
        """Initialize the RequestAPI object with the base URL, API key, and session.

        Args:
            base_url (str): The base URL for the media API.
            api_key (str): The API key for authentication.
            session (ClientSession): HTTP Session
            tv_instance (Search): The Search class instance

        Returns:
            None
        """
        self.request_url = base_url.joinpath("request")
        self.api_key = api_key
        self.session = session
        self.tv = tv_instance
        self.movie = movie_instance

    async def async_get_requests(
        self,
        raw_response: bool = False,
        take: int = 20,
        skip: int = 0,
        filter: RequestFilterOptions = "all",
        sort: SortOptions = "added",
        requested_by: int = 1,
    ) -> dict | RequestResultsResponseModel:
        """Get a list of requests

        Args:
            raw_response (bool, optional): Return JSON response. Defaults to False.
            take (int, optional): Number if pages. Defaults to 20.
            skip (int, optional): Pages to skip. Defaults to 0.
            filter (RequestFilterOptions, optional): Filter requests. Defaults to "all".
            sort (SortOptions, optional): Sort Requests. Defaults to "added".
            requested_by (int, optional): Only requests by user. Defaults to 1.

        Returns:
            dict | RequestResultsResponseModel: Returns a request record
        """

        url = self.request_url.with_query(
            {
                "take": take,
                "skip": skip,
                "filter": filter,
                "sort": sort,
                "requestedBy": requested_by,
            }
        )
        headers = {"X-Api-Key": self.api_key}
        response = await request(self.session, url, headers=headers)
        return response if raw_response else RequestResultsResponseModel(**response)

    async def async_post_request(
        self,
        id: int,
        type: Literal["movie", "tv"],
        series: Literal["all", "latest", "first"] = "all",
        raw_response: bool = False,
    ) -> dict | MediaRequestModel:
        """Get a list of requests

        Args:
            id (int): Movie or TV ID.
            type (str): Type of request movie | tv.
            series (str, optional): What series to request - all | latest | first, only aplies to tv. Defautls to all
            raw_response (bool, optional): Return JSON response. Defaults to False.

        Returns:
            dict | MediaRequestModel: Returns a request record
        """

        if type == "movie":
            req_data = {
                "mediaType": "movie",
                "mediaId": id,
            }
        elif type == "tv":
            data = await self.tv.async_get_tv(id=id)
            if isinstance(data, TvDetailsModel):
                if series == "all":
                    seasons_array = [
                        season.seasonNumber for season in data.seasons if season.seasonNumber != 0
                    ]
                elif series == "first":
                    seasons_array = [1]

                elif series == "latest":
                    for season in data.seasons:
                        seasons_array = [season.seasonNumber]
                req_data = {
                    "mediaType": "tv",
                    "mediaId": id,
                    "tvdbId": data.externalIds.tvdbId,
                    "seasons": seasons_array,
                }
            else:
                raise POWException(f"Expecting TvDetailsModel, got {type(data)}")
        else:
            raise POWMediaTypeException("Unknown media type, use either movie or tv")

        headers = {"X-Api-Key": self.api_key, "Content-Type": "application/json"}
        response = await request(
            self.session,
            self.request_url,
            method=hdrs.METH_POST,
            json_data=req_data,
            headers=headers,
        )
        return response if raw_response else MediaRequestModel(**response)
