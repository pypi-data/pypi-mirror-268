from enum import Enum


class RequestsMethods(Enum):
    GET = "GET"
    POST = "POST"


class RequestsCategory(Enum):
    CHANNELS = "channels"
    POSTS = "posts"
    STORIES = "stories"
    WORDS = "words"
    CALLBACK = "callback"
    USAGE = "usage"
    DATABASE = "database"


class ChannelsRequests(Enum):
    GET = ("get", RequestsMethods.GET)
    SEARCH = ("search", RequestsMethods.GET)
    STAT = ("stat", RequestsMethods.GET)
    POSTS = ("posts", RequestsMethods.GET)
    STORIES = ("stories", RequestsMethods.GET)
    MENTIONS = ("mentions", RequestsMethods.GET)
    FORWARDS = ("forwards", RequestsMethods.GET)
    SUBSCRIBERS = ("subscribers", RequestsMethods.GET)
    VIEWS = ("views", RequestsMethods.GET)
    AVG_POSTS_REACH = ("avg-posts-reach", RequestsMethods.GET)
    ER = ("er", RequestsMethods.GET)
    ERR = ("err", RequestsMethods.GET)
    ERR24 = ("err24", RequestsMethods.GET)
    ADD = ("add", RequestsMethods.POST)


class PostsRequests(Enum):
    GET = ("get", RequestsMethods.GET)
    STAT = ("stat", RequestsMethods.GET)
    STAT_MULTI = ("stat-multi", RequestsMethods.GET)
    SEARCH = ("search", RequestsMethods.GET)


class StoriesRequests(Enum):
    GET = ("get", RequestsMethods.GET)
    STAT = ("stat", RequestsMethods.GET)
    STAT_MULTI = ("stat-multi", RequestsMethods.GET)


class WordsRequests(Enum):
    MENTIONS_BY_PERIOD = ("mentions-by-period", RequestsMethods.GET)
    MENTIONS_BY_CHANNELS = ("mentions-by-channels", RequestsMethods.GET)


class CallbackRequests(Enum):
    SET_CALLBACK_URL = ("set-callback-url", RequestsMethods.POST)
    GET_CALLBACK_INFO = ("get-callback-info", RequestsMethods.GET)
    SUBSCRIBE_CHANNEL = ("subscribe-channel", RequestsMethods.POST)
    SUBSCRIBE_WORD = ("subscribe-word", RequestsMethods.POST)
    SUBSCRIPTIONS_LIST = ("subscriptions-list", RequestsMethods.GET)
    UNSUBSCRIBE = ("unsubscribe", RequestsMethods.POST)


class UsageRequests(Enum):
    STAT = ("stat", RequestsMethods.GET)


class DatabaseRequests(Enum):
    CATEGORIES = ("categories", RequestsMethods.GET)
    COUNTRIES = ("countries", RequestsMethods.GET)
    LANGUAGES = ("languages", RequestsMethods.GET)


class MediaTypes(Enum):
    MEDIA_PHOTO = "mediaPhoto"
    MEDIA_DOCUMENT = "mediaDocument"
    MEDIA_GEO = "mediaGeo"
    MEDIA_GEO_LIVE = "mediaGeoLive"
    MEDIA_VENUE = "mediaVenue"
    MEDIA_CONTACT = "mediaContact"
    MEDIA_GAME = "mediaGame"
    MEDIA_INVOICE = "mediaInvoice"


class DatabaseTypes(Enum):
    CATEGORIES = "categories"
    COUNTRIES = "countries"
    LANGUAGES = "languages"


class DynamicType(Enum):
    SUBSCRIBERS = 1
    VIEWS = 2
    AVG_POSTS_REACH = 3
    ER = 4
    ERR = 5
    ERR24 = 6
    MENTIONS_BY_PERIOD = 7


class ResultsType(Enum):
    POST = 1
    STORIES = 2
    MENTIONS = 3
    MENTIONS_CHANNEL = 6
    FORWARDS = 4
    CHANNELS = 5

class ReturnTypes(Enum):
    OBJECT = 1
    LIST = 2
    