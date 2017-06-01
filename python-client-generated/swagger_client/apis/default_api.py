# coding: utf-8

"""
    Environmental Exposures API

    API for environmental exposure models for NIH Data Translator program

    OpenAPI spec version: 1.0.0
    Contact: stealey@renci.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class DefaultApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def exposures_exposure_type_coordinates_get(self, exposure_type, **kwargs):
        """
        Get exposure location(s) as latitude, longitude coordinates
        Returns paginated list of available latitude, longitude coordinates for given exposure_type. Optionally the user can provide a latitude, longitude coordinate with a radius in meters to discover if an exposure location is within the requested range.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.exposures_exposure_type_coordinates_get(exposure_type, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str exposure_type: The name of the exposure type (currently limited to pm25, o3, haz_waste, crime, res_den, poverty, ses). (required)
        :param str latitude: Search coordinates that match or are like 'latitude'
        :param str longitude: Search coordinates that match or are like 'longitude'
        :param str radius: radius in meters to search within for exposure point when a coordinate is provided. Range from 0 to 500
        :param str page: Page number. Return up to 100 items per page
        :return: list[Coordinate]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.exposures_exposure_type_coordinates_get_with_http_info(exposure_type, **kwargs)
        else:
            (data) = self.exposures_exposure_type_coordinates_get_with_http_info(exposure_type, **kwargs)
            return data

    def exposures_exposure_type_coordinates_get_with_http_info(self, exposure_type, **kwargs):
        """
        Get exposure location(s) as latitude, longitude coordinates
        Returns paginated list of available latitude, longitude coordinates for given exposure_type. Optionally the user can provide a latitude, longitude coordinate with a radius in meters to discover if an exposure location is within the requested range.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.exposures_exposure_type_coordinates_get_with_http_info(exposure_type, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str exposure_type: The name of the exposure type (currently limited to pm25, o3, haz_waste, crime, res_den, poverty, ses). (required)
        :param str latitude: Search coordinates that match or are like 'latitude'
        :param str longitude: Search coordinates that match or are like 'longitude'
        :param str radius: radius in meters to search within for exposure point when a coordinate is provided. Range from 0 to 500
        :param str page: Page number. Return up to 100 items per page
        :return: list[Coordinate]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['exposure_type', 'latitude', 'longitude', 'radius', 'page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method exposures_exposure_type_coordinates_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'exposure_type' is set
        if ('exposure_type' not in params) or (params['exposure_type'] is None):
            raise ValueError("Missing the required parameter `exposure_type` when calling `exposures_exposure_type_coordinates_get`")


        collection_formats = {}

        resource_path = '/exposures/{exposure_type}/coordinates'.replace('{format}', 'json')
        path_params = {}
        if 'exposure_type' in params:
            path_params['exposure_type'] = params['exposure_type']

        query_params = {}
        if 'latitude' in params:
            query_params['latitude'] = params['latitude']
        if 'longitude' in params:
            query_params['longitude'] = params['longitude']
        if 'radius' in params:
            query_params['radius'] = params['radius']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[Coordinate]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)

    def exposures_exposure_type_dates_get(self, exposure_type, **kwargs):
        """
        Get exposure start date and end date range for exposure type
        Returns exposure start date and end date range for given exposure type

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.exposures_exposure_type_dates_get(exposure_type, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str exposure_type: The name of the exposure type (currently limited to pm25, o3, haz_waste, crime, res_den, poverty, ses). (required)
        :return: DateRange
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.exposures_exposure_type_dates_get_with_http_info(exposure_type, **kwargs)
        else:
            (data) = self.exposures_exposure_type_dates_get_with_http_info(exposure_type, **kwargs)
            return data

    def exposures_exposure_type_dates_get_with_http_info(self, exposure_type, **kwargs):
        """
        Get exposure start date and end date range for exposure type
        Returns exposure start date and end date range for given exposure type

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.exposures_exposure_type_dates_get_with_http_info(exposure_type, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str exposure_type: The name of the exposure type (currently limited to pm25, o3, haz_waste, crime, res_den, poverty, ses). (required)
        :return: DateRange
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['exposure_type']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method exposures_exposure_type_dates_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'exposure_type' is set
        if ('exposure_type' not in params) or (params['exposure_type'] is None):
            raise ValueError("Missing the required parameter `exposure_type` when calling `exposures_exposure_type_dates_get`")


        collection_formats = {}

        resource_path = '/exposures/{exposure_type}/dates'.replace('{format}', 'json')
        path_params = {}
        if 'exposure_type' in params:
            path_params['exposure_type'] = params['exposure_type']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='DateRange',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)

    def exposures_exposure_type_scores_get(self, exposure_type, start_date, end_date, exposure_point, **kwargs):
        """
        Get exposure score for a given environmental factor at exposure location(s)
        Retrieve the computed exposure score(s) for a given environmental exposure factor, time period, and location(s).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.exposures_exposure_type_scores_get(exposure_type, start_date, end_date, exposure_point, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str exposure_type: The name of the exposure type (currently limited to pm25, o3, haz_waste, crime, res_den, poverty, ses). (required)
        :param date start_date: The starting date to obtain exposures for (example 2010-01-06 is January 6th 2010). (required)
        :param date end_date: The ending date to obtain exposures for (example 2010-01-15 is January 15th 2010). (required)
        :param str exposure_point: A description of the location(s) to retrieve the exposure for. Locaton may be a single geocoordinate (example '35.9131996,-79.0558445') or a semicomma separated list of geocoord:dayhours giving the start and ending hours on specific days of the week at that location (example '35.9131996,-79.0558445,Sa0813;35.7795897,-78.6381787,other') indicates Saturdays from 8am to 1pm is at one location and all other times are at another location. Hours should be in 24 hours time using 2 digits, days of the week should be the first two characters of the day.If the day of the week does not appear then the time periods apply to all days (example '35.9131996,-79.0558445,0614,35.7795897,-78.6381787,1424') gives two time periods for all days. If hours do not appear then the time period applies to all hours of the day (example '35.9131996,-79.0558445,Sa,35.7795897,-78.6381787,Su'). (required)
        :param str temporal_resolution: The temporal resolution to use for results, should be one of 'hour' or 'day'. Default is 'day'
        :param str score_type: The exposure score type to return. The accepted values vary by exposure type. For pm25 values are '7dayrisk', '14dayrisk'. Default is '7dayrisk' (NOT COMPLETE).
        :param str radius: radius in meters to search within for exposure point when a coordinate is provided. Range from 0 to 500
        :param str page: Page number. Return up to 100 items per page
        :return: list[Exposure]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.exposures_exposure_type_scores_get_with_http_info(exposure_type, start_date, end_date, exposure_point, **kwargs)
        else:
            (data) = self.exposures_exposure_type_scores_get_with_http_info(exposure_type, start_date, end_date, exposure_point, **kwargs)
            return data

    def exposures_exposure_type_scores_get_with_http_info(self, exposure_type, start_date, end_date, exposure_point, **kwargs):
        """
        Get exposure score for a given environmental factor at exposure location(s)
        Retrieve the computed exposure score(s) for a given environmental exposure factor, time period, and location(s).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.exposures_exposure_type_scores_get_with_http_info(exposure_type, start_date, end_date, exposure_point, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str exposure_type: The name of the exposure type (currently limited to pm25, o3, haz_waste, crime, res_den, poverty, ses). (required)
        :param date start_date: The starting date to obtain exposures for (example 2010-01-06 is January 6th 2010). (required)
        :param date end_date: The ending date to obtain exposures for (example 2010-01-15 is January 15th 2010). (required)
        :param str exposure_point: A description of the location(s) to retrieve the exposure for. Locaton may be a single geocoordinate (example '35.9131996,-79.0558445') or a semicomma separated list of geocoord:dayhours giving the start and ending hours on specific days of the week at that location (example '35.9131996,-79.0558445,Sa0813;35.7795897,-78.6381787,other') indicates Saturdays from 8am to 1pm is at one location and all other times are at another location. Hours should be in 24 hours time using 2 digits, days of the week should be the first two characters of the day.If the day of the week does not appear then the time periods apply to all days (example '35.9131996,-79.0558445,0614,35.7795897,-78.6381787,1424') gives two time periods for all days. If hours do not appear then the time period applies to all hours of the day (example '35.9131996,-79.0558445,Sa,35.7795897,-78.6381787,Su'). (required)
        :param str temporal_resolution: The temporal resolution to use for results, should be one of 'hour' or 'day'. Default is 'day'
        :param str score_type: The exposure score type to return. The accepted values vary by exposure type. For pm25 values are '7dayrisk', '14dayrisk'. Default is '7dayrisk' (NOT COMPLETE).
        :param str radius: radius in meters to search within for exposure point when a coordinate is provided. Range from 0 to 500
        :param str page: Page number. Return up to 100 items per page
        :return: list[Exposure]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['exposure_type', 'start_date', 'end_date', 'exposure_point', 'temporal_resolution', 'score_type', 'radius', 'page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method exposures_exposure_type_scores_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'exposure_type' is set
        if ('exposure_type' not in params) or (params['exposure_type'] is None):
            raise ValueError("Missing the required parameter `exposure_type` when calling `exposures_exposure_type_scores_get`")
        # verify the required parameter 'start_date' is set
        if ('start_date' not in params) or (params['start_date'] is None):
            raise ValueError("Missing the required parameter `start_date` when calling `exposures_exposure_type_scores_get`")
        # verify the required parameter 'end_date' is set
        if ('end_date' not in params) or (params['end_date'] is None):
            raise ValueError("Missing the required parameter `end_date` when calling `exposures_exposure_type_scores_get`")
        # verify the required parameter 'exposure_point' is set
        if ('exposure_point' not in params) or (params['exposure_point'] is None):
            raise ValueError("Missing the required parameter `exposure_point` when calling `exposures_exposure_type_scores_get`")


        collection_formats = {}

        resource_path = '/exposures/{exposure_type}/scores'.replace('{format}', 'json')
        path_params = {}
        if 'exposure_type' in params:
            path_params['exposure_type'] = params['exposure_type']

        query_params = {}
        if 'start_date' in params:
            query_params['start_date'] = params['start_date']
        if 'end_date' in params:
            query_params['end_date'] = params['end_date']
        if 'exposure_point' in params:
            query_params['exposure_point'] = params['exposure_point']
        if 'temporal_resolution' in params:
            query_params['temporal_resolution'] = params['temporal_resolution']
        if 'score_type' in params:
            query_params['score_type'] = params['score_type']
        if 'radius' in params:
            query_params['radius'] = params['radius']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[Exposure]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)

    def exposures_exposure_type_values_get(self, exposure_type, start_date, end_date, exposure_point, **kwargs):
        """
        Get exposure value for a given environmental factor at exposure location(s)
        Retrieve the computed exposure value(s) for a given environmental exposure factor, time period, and location(s).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.exposures_exposure_type_values_get(exposure_type, start_date, end_date, exposure_point, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str exposure_type: The name of the exposure type (currently limited to pm25, o3, haz_waste, crime, res_den, poverty, ses). (required)
        :param date start_date: The starting date to obtain exposures for (example 2010-01-06 is January 6th 2010). (required)
        :param date end_date: The ending date to obtain exposures for (example 2010-01-15 is January 15th 2010). (required)
        :param str exposure_point: A description of the location(s) to retrieve the exposure for. Locaton may be a single geocoordinate (example '35.9131996,-79.0558445') or a semicomma separated list of geocoord:dayhours giving the start and ending hours on specific days of the week at that location (example '35.9131996,-79.0558445,Sa0813;35.7795897,-78.6381787,other') indicates Saturdays from 8am to 1pm is at one location and all other times are at another location. Hours should be in 24 hours time using 2 digits, days of the week should be the first two characters of the day.If the day of the week does not appear then the time periods apply to all days (example '35.9131996,-79.0558445,0614,35.7795897,-78.6381787,1424') gives two time periods for all days. If hours do not appear then the time period applies to all hours of the day (example '35.9131996,-79.0558445,Sa,35.7795897,-78.6381787,Su'). (required)
        :param str temporal_resolution: The temporal resolution to use for results, should be one of 'hour' or 'day'. Default is 'day'
        :param str statistical_type: The statistic to use for results, should be one of 'max', 'mean', or 'median'. Default is 'max'
        :param str radius: radius in meters to search within for exposure point when a coordinate is provided. Range from 0 to 500
        :param str page: Page number. Return up to 100 items per page
        :return: list[Exposure]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.exposures_exposure_type_values_get_with_http_info(exposure_type, start_date, end_date, exposure_point, **kwargs)
        else:
            (data) = self.exposures_exposure_type_values_get_with_http_info(exposure_type, start_date, end_date, exposure_point, **kwargs)
            return data

    def exposures_exposure_type_values_get_with_http_info(self, exposure_type, start_date, end_date, exposure_point, **kwargs):
        """
        Get exposure value for a given environmental factor at exposure location(s)
        Retrieve the computed exposure value(s) for a given environmental exposure factor, time period, and location(s).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.exposures_exposure_type_values_get_with_http_info(exposure_type, start_date, end_date, exposure_point, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str exposure_type: The name of the exposure type (currently limited to pm25, o3, haz_waste, crime, res_den, poverty, ses). (required)
        :param date start_date: The starting date to obtain exposures for (example 2010-01-06 is January 6th 2010). (required)
        :param date end_date: The ending date to obtain exposures for (example 2010-01-15 is January 15th 2010). (required)
        :param str exposure_point: A description of the location(s) to retrieve the exposure for. Locaton may be a single geocoordinate (example '35.9131996,-79.0558445') or a semicomma separated list of geocoord:dayhours giving the start and ending hours on specific days of the week at that location (example '35.9131996,-79.0558445,Sa0813;35.7795897,-78.6381787,other') indicates Saturdays from 8am to 1pm is at one location and all other times are at another location. Hours should be in 24 hours time using 2 digits, days of the week should be the first two characters of the day.If the day of the week does not appear then the time periods apply to all days (example '35.9131996,-79.0558445,0614,35.7795897,-78.6381787,1424') gives two time periods for all days. If hours do not appear then the time period applies to all hours of the day (example '35.9131996,-79.0558445,Sa,35.7795897,-78.6381787,Su'). (required)
        :param str temporal_resolution: The temporal resolution to use for results, should be one of 'hour' or 'day'. Default is 'day'
        :param str statistical_type: The statistic to use for results, should be one of 'max', 'mean', or 'median'. Default is 'max'
        :param str radius: radius in meters to search within for exposure point when a coordinate is provided. Range from 0 to 500
        :param str page: Page number. Return up to 100 items per page
        :return: list[Exposure]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['exposure_type', 'start_date', 'end_date', 'exposure_point', 'temporal_resolution', 'statistical_type', 'radius', 'page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method exposures_exposure_type_values_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'exposure_type' is set
        if ('exposure_type' not in params) or (params['exposure_type'] is None):
            raise ValueError("Missing the required parameter `exposure_type` when calling `exposures_exposure_type_values_get`")
        # verify the required parameter 'start_date' is set
        if ('start_date' not in params) or (params['start_date'] is None):
            raise ValueError("Missing the required parameter `start_date` when calling `exposures_exposure_type_values_get`")
        # verify the required parameter 'end_date' is set
        if ('end_date' not in params) or (params['end_date'] is None):
            raise ValueError("Missing the required parameter `end_date` when calling `exposures_exposure_type_values_get`")
        # verify the required parameter 'exposure_point' is set
        if ('exposure_point' not in params) or (params['exposure_point'] is None):
            raise ValueError("Missing the required parameter `exposure_point` when calling `exposures_exposure_type_values_get`")


        collection_formats = {}

        resource_path = '/exposures/{exposure_type}/values'.replace('{format}', 'json')
        path_params = {}
        if 'exposure_type' in params:
            path_params['exposure_type'] = params['exposure_type']

        query_params = {}
        if 'start_date' in params:
            query_params['start_date'] = params['start_date']
        if 'end_date' in params:
            query_params['end_date'] = params['end_date']
        if 'exposure_point' in params:
            query_params['exposure_point'] = params['exposure_point']
        if 'temporal_resolution' in params:
            query_params['temporal_resolution'] = params['temporal_resolution']
        if 'statistical_type' in params:
            query_params['statistical_type'] = params['statistical_type']
        if 'radius' in params:
            query_params['radius'] = params['radius']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[Exposure]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)

    def exposures_get(self, **kwargs):
        """
        Get list of exposure types
        Returns a list of all available exposure types

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.exposures_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[ExposureType]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.exposures_get_with_http_info(**kwargs)
        else:
            (data) = self.exposures_get_with_http_info(**kwargs)
            return data

    def exposures_get_with_http_info(self, **kwargs):
        """
        Get list of exposure types
        Returns a list of all available exposure types

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.exposures_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[ExposureType]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method exposures_get" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/exposures'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[ExposureType]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)
