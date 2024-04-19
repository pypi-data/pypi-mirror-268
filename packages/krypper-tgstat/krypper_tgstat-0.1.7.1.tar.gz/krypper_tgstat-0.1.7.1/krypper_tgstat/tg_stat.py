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
    
    
    def _check_catgory(self, category, sub_category):
        if category and not isinstance(category, RequestsCategory):
            raise TGStatTypeError(type(category), type(RequestsCategory), category._name_)
        
        if not type(sub_category) in [ChannelsRequests, PostsRequests, StoriesRequests, WordsRequests,
                                        CallbackRequests, UsageRequests, DatabaseRequests]:
            raise TGStatTypeError(type(category), [ChannelsRequests, PostsRequests, StoriesRequests, WordsRequests,
                                        CallbackRequests, UsageRequests, DatabaseRequests], sub_category._name_)
        
        return True

    
    def _build_result(self, data, sub_category: Union[
                    ChannelsRequests, PostsRequests, StoriesRequests, WordsRequests,
                    CallbackRequests, UsageRequests, DatabaseRequests
                ]):
        self._check_catgory(None, sub_category)

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
        if sub_category in [ChannelsRequests.SEARCH, ChannelsRequests.POSTS, ChannelsRequests.STORIES,
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
                kwargs[key] = value_dict[sub_category]
            except:
                raise TGStatException("Unsupported Enum")
            
            kwargs.update(data["response"])
        
        elif sub_category in [
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
                kwargs[key] = value_dict[sub_category]
            except:
                raise TGStatException("Unsupported Enum")

            return_type = ReturnTypes.LIST 
        
        elif sub_category in [ChannelsRequests.GET, PostsRequests.GET, StoriesRequests.GET,
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
                class_parser = objects_dict[sub_category]
            except:
                raise TGStatException("Unsupported Enum")
            
            if sub_category not in [PostsRequests.STAT_MULTI, StoriesRequests.STAT_MULTI]:
                kwargs.update(data["response"])
            else:
                return_type = ReturnTypes.LIST
        
        elif isinstance(sub_category, DatabaseRequests):
            class_parser = DatabaseEntity

            database_types = {
                DatabaseRequests.CATEGORIES: DatabaseTypes.CATEGORIES,
                DatabaseRequests.COUNTRIES: DatabaseTypes.COUNTRIES,
                DatabaseRequests.LANGUAGES: DatabaseTypes.LANGUAGES,
            }

            try:
                kwargs["database_type"] = database_types[sub_category]
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


    def get_result(self, data, sub_category: Union[
                    ChannelsRequests, PostsRequests, StoriesRequests, WordsRequests,
                    CallbackRequests, UsageRequests, DatabaseRequests
                ]):
                
        self._check_catgory(None, sub_category)

        return self._build_result(data, sub_category)


    def api(self, category: RequestsCategory, 
            sub_category: Union[
                    ChannelsRequests, PostsRequests, StoriesRequests, WordsRequests,
                    CallbackRequests, UsageRequests, DatabaseRequests
                ], 
            **kwargs):

        self._check_catgory(category, sub_category)

        check_sub_category = {
            RequestsCategory.CHANNELS: ChannelsRequests,
            RequestsCategory.POSTS: PostsRequests,
            RequestsCategory.STORIES: StoriesRequests,
            RequestsCategory.WORDS: WordsRequests,
            RequestsCategory.CALLBACK: CallbackRequests,
            RequestsCategory.USAGE: UsageRequests,
            RequestsCategory.DATABASE: DatabaseRequests,
        }

        if not isinstance(sub_category, check_sub_category[category]):
            raise TGStatTypeError(type(sub_category), type(check_sub_category[category]), "sub_category")

        first_postfix = category.value
        last_postfix, method = sub_category.value
        sending_url = self.base_url + "/" + first_postfix + "/" + last_postfix
        response = self._send_request(method, sending_url, **kwargs)
        result = self._build_result(response, sub_category)

        return result


