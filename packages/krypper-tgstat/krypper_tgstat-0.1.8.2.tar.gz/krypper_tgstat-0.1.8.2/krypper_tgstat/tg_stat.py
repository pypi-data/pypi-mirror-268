from typing import Union
import json
from requests import Request, Session
from aiohttp import ClientSession

from .enums import *
from .classes import *
from .exceptions import * 


class TGStatSync:

    base_url = "https://api.tgstat.ru"
    
    def __init__(self, token, **kwargs):
        self.token = token
        self.session = Session()
        if not kwargs.get("tests", False):
            result = self.session.get(self.base_url + "/usage/stat", params={"token":token}).json()
            if result['status'] == "error":
                raise TGStatAuthError(result["error"])
            
        
    def _send_request(self, method: RequestsMethods, url: str, **kwargs):
        kwargs["token"] = self.token
        response = self.session.request(method=method.value, url=url, params=kwargs)
        return response.json()
    
    
    def _check_catgory(self, api_request):
        if not type(api_request) in [ChannelsRequests, PostsRequests, StoriesRequests, WordsRequests,
                                        CallbackRequests, UsageRequests, DatabaseRequests]:
            raise TGStatTypeError(type(api_request), [ChannelsRequests, PostsRequests, StoriesRequests, WordsRequests,
                                        CallbackRequests, UsageRequests, DatabaseRequests], api_request._name_)
        
        return True

    
    def _build_result(self, data, api_request: Union[
                    ChannelsRequests, PostsRequests, StoriesRequests, WordsRequests,
                    CallbackRequests, UsageRequests, DatabaseRequests
                ]):
        self._check_catgory(api_request)

        if isinstance(data, str):
            try:
                data = json.loads(data)
            except:
                raise TGStatException("Incorrect data value")

        if data['status'] == "error":
            raise TGStatAPIError(data["error"])
        
        class_parser = None
        kwargs = {}
        return_type = ReturnTypes.OBJECT
        if api_request in [ChannelsRequests.SEARCH, ChannelsRequests.POSTS, ChannelsRequests.STORIES,
                            ChannelsRequests.MENTIONS, ChannelsRequests.FORWARDS, PostsRequests.SEARCH,
                             WordsRequests.MENTIONS_BY_CHANNELS]:
            class_parser = MassiveResult
            
            key = "result_type"

            value_dict = {
                ChannelsRequests.SEARCH: ResultsType.CHANNELS,
                ChannelsRequests.POSTS: ResultsType.POST, 
                PostsRequests.SEARCH: ResultsType.POST,
                ChannelsRequests.STORIES: ResultsType.STORIES,
                ChannelsRequests.FORWARDS: ResultsType.FORWARDS,
                ChannelsRequests.MENTIONS:ResultsType.MENTIONS, 
                WordsRequests.MENTIONS_BY_CHANNELS:ResultsType.MENTIONS_CHANNEL
            }

            try:
                kwargs[key] = value_dict[api_request]
            except:
                raise TGStatException("Unsupported Enum")
            
            kwargs.update(data["response"])
        
        elif api_request in [
                                ChannelsRequests.SUBSCRIBERS, ChannelsRequests.VIEWS, ChannelsRequests.AVG_POSTS_REACH,
                                ChannelsRequests.ER, ChannelsRequests.ERR, ChannelsRequests.ERR24,
                                WordsRequests.MENTIONS_BY_PERIOD
                            ]:

            class_parser = DynamicData
            
            key = "dynamic_type"

            value_dict = {
                ChannelsRequests.SUBSCRIBERS: DynamicType.SUBSCRIBERS,
                ChannelsRequests.VIEWS: DynamicType.VIEWS,
                ChannelsRequests.AVG_POSTS_REACH: DynamicType.AVG_POSTS_REACH,
                ChannelsRequests.ER: DynamicType.ER,
                ChannelsRequests.ERR: DynamicType.ERR,
                ChannelsRequests.ERR24: DynamicType.ERR24,
                WordsRequests.MENTIONS_BY_PERIOD: DynamicType.MENTIONS_BY_PERIOD,
            }

            try:
                kwargs[key] = value_dict[api_request]
            except:
                raise TGStatException("Unsupported Enum")

            return_type = ReturnTypes.LIST 
        
        elif api_request in [ChannelsRequests.GET, PostsRequests.GET, StoriesRequests.GET,
            ChannelsRequests.STAT, PostsRequests.STAT, StoriesRequests.STAT, 
            PostsRequests.STAT_MULTI, StoriesRequests.STAT_MULTI]:
            
            objects_dict = {
                ChannelsRequests.GET: Channel,
                PostsRequests.GET: Post,
                StoriesRequests.GET: Story,
                ChannelsRequests.STAT: ChannelStatistic,
                PostsRequests.STAT: GroupStatistic,
                StoriesRequests.STAT: GroupStatistic,
                PostsRequests.STAT_MULTI: UnionStatistic,
                StoriesRequests.STAT_MULTI: UnionStatistic
            }

            try:
                class_parser = objects_dict[api_request]
            except:
                raise TGStatException("Unsupported Enum")
            
            if api_request not in [PostsRequests.STAT_MULTI, StoriesRequests.STAT_MULTI]:
                kwargs.update(data["response"])
            else:
                return_type = ReturnTypes.LIST
        
        elif isinstance(api_request, DatabaseRequests):
            class_parser = DatabaseEntity

            database_types = {
                DatabaseRequests.CATEGORIES: DatabaseTypes.CATEGORIES,
                DatabaseRequests.COUNTRIES: DatabaseTypes.COUNTRIES,
                DatabaseRequests.LANGUAGES: DatabaseTypes.LANGUAGES,
            }

            try:
                kwargs["database_type"] = database_types[api_request]
            except:
                raise TGStatException("Unsupported Enum")
            
            return_type = ReturnTypes.LIST

        
        if return_type == ReturnTypes.OBJECT:
            return class_parser(**kwargs)

        elif return_type == ReturnTypes.LIST:
            return_datas = []
            for temp_data in data["response"]:
                if not isinstance(temp_data, str):
                    return_datas.append(class_parser(**kwargs, **temp_data))
                else:
                    for temp_data_two in data["response"][temp_data]:
                        return_datas.append(class_parser(**kwargs, **temp_data_two))
            
            return return_datas


    def get_result(self, data, api_request: Union[
                    ChannelsRequests, PostsRequests, StoriesRequests, WordsRequests,
                    CallbackRequests, UsageRequests, DatabaseRequests
                ]):
                
        self._check_catgory(api_request)

        return self._build_result(data, api_request)


    def api(self, api_request: Union[
                    ChannelsRequests, PostsRequests, StoriesRequests, WordsRequests,
                    CallbackRequests, UsageRequests, DatabaseRequests
                ], 
            **kwargs):

        self._check_catgory(api_request)

        request_types = {
            ChannelsRequests: RequestsCategory.CHANNELS,
            PostsRequests: RequestsCategory.POSTS,
            StoriesRequests: RequestsCategory.STORIES,
            WordsRequests: RequestsCategory.WORDS,
            CallbackRequests: RequestsCategory.CALLBACK,
            UsageRequests: RequestsCategory.USAGE,
            DatabaseRequests: RequestsCategory.DATABASE
        }

        category = request_types.get(type(api_request), False)

        if not category:
            raise TGStatTypeError(type(api_request), [ChannelsRequests, PostsRequests, StoriesRequests, WordsRequests,
                    CallbackRequests, UsageRequests, DatabaseRequests], "api_request")

        first_postfix = category.value
        last_postfix, method = api_request.value
        sending_url = self.base_url + "/" + first_postfix + "/" + last_postfix
        response = self._send_request(method, sending_url, **kwargs)
        result = self._build_result(response, api_request)

        return result


