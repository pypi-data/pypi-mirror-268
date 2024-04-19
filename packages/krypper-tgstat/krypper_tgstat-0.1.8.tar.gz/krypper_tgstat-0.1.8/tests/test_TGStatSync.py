from os import environ
import unittest

from dotenv import load_dotenv
from krypper_tgstat import classes, enums, exceptions, tg_stat

load_dotenv()

class TGStatSyncTest(unittest.TestCase):

    def test_exeptions(self):
        self.assertRaises(exceptions.TGStatAuthError, tg_stat.TGStatSync, "")
        self.assertRaises(exceptions.TGStatAuthError, tg_stat.TGStatSync, "000")
        tgs = tg_stat.TGStatSync("f", tests=True)
        self.assertRaises(exceptions.TGStatTypeError, tgs.api, category=enums.RequestsCategory.CALLBACK, sub_category=enums.DatabaseRequests.CATEGORIES)

        
    def test_get_databases(self):
        pass
        # tgs = tg_stat.TGStatSync(environ.get("TOKEN"))
        # categories = tgs.api(enums.RequestsCategory.DATABASE, enums.DatabaseRequests.CATEGORIES)
        # countries = tgs.api(enums.RequestsCategory.DATABASE, enums.DatabaseRequests.COUNTRIES)
        # languages = tgs.api(enums.RequestsCategory.DATABASE, enums.DatabaseRequests.LANGUAGES)
        # self.assertIsInstance(categories[0], classes.DatabaseEntity, "Database not return DatabaseEntity in categories")
        # self.assertIsInstance(countries[0], classes.DatabaseEntity, "Database not return DatabaseEntity in countries")
        # self.assertIsInstance(languages[0], classes.DatabaseEntity, "Database not return DatabaseEntity in languages")

        # self.assertEqual(categories[0].database_type, enums.DatabaseTypes.CATEGORIES, f"Not correct db type in category : {categories[0].database_type}")
        # self.assertEqual(countries[0].database_type, enums.DatabaseTypes.COUNTRIES, f"Not correct db type in countries : {countries[0].database_type}")
        # self.assertEqual(languages[0].database_type, enums.DatabaseTypes.LANGUAGES, f"Not correct db type in languages : {languages[0].database_type}")

    
    def test_get_channel_info(self):
        tgs = tg_stat.TGStatSync(environ.get("0000"), tests=True)
        null = None
        data = {
            "status": "ok",
            "response": {
                "id": 321,
                "link": "t.me/varlamov",
                "peer_type": "channel",
                "username": "@varlamov",
                "active_usernames": [
                    "@varlamov"
                ],
                "title": "Varlamov.ru",
                "about": "Илья Варламов. Make Russia warm again! ...",
                "category": "Блоги",
                "country": "Россия",
                "language": "Русский",
                "image100": "//static.tgstat.ru/public/images/channels/_100/ca/caf1a3dfb505ffed0d024130f58c5cfa.jpg",
                "image640": "//static.tgstat.ru/public/images/channels/_0/ca/caf1a3dfb505ffed0d024130f58c5cfa.jpg",
                "participants_count": 154800,
                "tgstat_restrictions": {      # ограничения, наложенные на канал (если ограничений нет - будет возвращен пустой массив)
                    "red_label": True,        # канал помечен красной меткой (за накрутку) на TGStat.ru
                    "black_label": True,      # канал помечен черной меткой (за мошенничество) на TGStat.ru
                }
            }
        }

        result = tgs.get_result(data, enums.ChannelsRequests.GET)
        self.assertIsInstance(result, classes.Channel, "Channel result not a Channel type")

        data = {
            "status": "ok",
            "response": {
                "count": 3,
                "items": [
                    {
                        "id": 53248,
                        "link": "t.me/tg_analytics",
                        "peer_type": "channel",
                        "username": "@tg_analytics",
                        "title": "Telegram Analytics",
                        "about": "Канал проекта Telegram Analytics. \nЗдесь будут появляться последние новости проекта https://tgstat.ru \n\nЧат: @tg_analytics_chat - вопросы, предложения, замечания - всё сюда.\nСтраница проекта в ВК: https://vk.com/tg_analytics",
                        "image100": "//static10.tgstat.ru/channels/_100/1b/1ba75ef1c643f82ac4a09c7aa43bd3ff.jpg",
                        "image640": "//static10.tgstat.ru/channels/_0/1b/1ba75ef1c643f82ac4a09c7aa43bd3ff.jpg",
                        "participants_count": 21905
                    },
                    {
                        "id": 123357,
                        "link": "t.me/AnalyticsFree",
                        "peer_type": "chat",
                        "username": "@AnalyticsFree",
                        "title": "Бесплатные разборы каналов Telegram",
                        "about": "Я делаю разборы Telegram-каналов.\n\nЕсли вы хотите, чтоб я сделал разбор вашего канала напишите мне @LoikoR ссылку на ваш канал с меткой «на разбор».\n\nРазбираю все по пунктам и бесплатно.",
                        "image100": "//static10.tgstat.ru/channels/_100/b6/b6a1d5de6e0101f3886464727fc6fb22.jpg",
                        "image640": "//static10.tgstat.ru/channels/_0/b6/b6a1d5de6e0101f3886464727fc6fb22.jpg",
                        "participants_count": 21
                    },
                    {
                        "id": 798202,
                        "link": "t.me/telega_analytics",
                        "peer_type": "channel",
                        "username": "@telega_analytics",
                        "title": "Telegram Analytics",
                        "about": "Привет, мы поможем тебе прокачать свой канал, разместим его на всех популярных сайтах рекламы телеграмм бесплатно, слишком много интересных идей которые никто не видит!",
                        "image100": "//static10.tgstat.ru/channels/_100/32/322f3e36cdffba89c2168fd1244ca1ff.jpg",
                        "image640": "//static10.tgstat.ru/channels/_0/32/322f3e36cdffba89c2168fd1244ca1ff.jpg",
                        "participants_count": 3
                    }
                ]
            }
        }
        result = tgs.get_result(data, enums.ChannelsRequests.SEARCH)
        self.assertIsInstance(result, classes.MassiveResult, "Channel result not a Channel type")

        data = {
            "status": "ok",
            "response": {
                "id": 118,                           # Внутренний ID канала в TGStat
                "title": "РИА Новости",              # Название канала
                "username": "@rian_ru",              # Username канала
                "peer_type": "channel",              # Тип (канал/чат)
                "participants_count": 2048184,       # Количество подписчиков канала на момент запроса
                "avg_post_reach": 541540,            # Средний охват публикации
                "adv_post_reach_12h": 475712,        # Средний рекламный охват публикации за 12 часов
                "adv_post_reach_24h": 554476,        # Средний рекламный охват публикации за 24 часа
                "adv_post_reach_48h": 580952,        # Средний рекламный охват публикации за 48 часов
                "err_percent": 26.4,                 # Процент вовлеченности подписчиков (ERR %)
                "err24_percent": 25.2,               # Процент вовлеченности подписчиков в просмотр поста за первые 24 часа (ERR24 %)
                "er_percent": 11.11,                 # Коэффициент вовлеченности подписчиков во взаимодействия с постом (реакция, пересылка, комментарий)        
                "daily_reach": 35496444,             # Cуммарный дневной охват
                "ci_index": 8737.68,                 # Индекс цитирования (ИЦ)
                "mentions_count": 171477,            # Количество упоминаний канала в других каналах
                "forwards_count": 472536,            # Количество репостов в другие каналы
                "mentioning_channels_count": 18740,  # Количество каналов, упоминающих данный канал
                "posts_count": 53500,                # Общее количество неудаленных публикаций в канале
            }
        }

        result = tgs.get_result(data, enums.ChannelsRequests.STAT)
        self.assertIsInstance(result, classes.ChannelStatistic)


        data = {
            "status": "ok",
            "response": {
                "count": 50,
                "total_count": 8007,
                "channel": {
                    "id": 7377,
                    "link": "t.me/breakingmash",
                    "username": "@breakingmash",
                    "title": "Mash",
                    "about": "Помахаться и обсудить новости - @mash_chat ...",
                    "image100": "//static2.tgstat.com/public/images/channels/_100/a7/a76c0abe2b7b1b79e70f0073f43c3b44.jpg",
                    "image640": "//static2.tgstat.com/public/images/channels/_0/a7/a76c0abe2b7b1b79e70f0073f43c3b44.jpg",
                    "participants_count": 431868
                },
                "items": [
                    {
                        "id": 3598980241,
                        "date": 1540123429,
                        "views": 148382,
                        "link": "t.me/breakingmash/8419",
                        "channel_id": 7377,
                        "forwarded_from": None,
                        "is_deleted": 0,
                        "text": "В Твери заправщик принял лишнего и решил, ...",
                        "media": {
                            "media_type": "mediaDocument",
                            "mime_type": "video/mp4",
                            "size": 5085138
                        }
                    },
                ]
            }
        }

        result = tgs.get_result(data, enums.ChannelsRequests.POSTS)
        self.assertIsInstance(result, classes.MassiveResult)

        
        data = {
            "status": "ok",
            "response": {
                "count": 8,
                "total_count": 10,        
                "channel": {
                    "id": 7377,
                    "tg_id": 1036240821,
                    "link": "t.me/meduzalive",
                    "peer_type": "channel",
                    "username": "@meduzalive",
                    "active_usernames": [
                        "@meduzalive"
                    ],
                    "title": "Медуза — LIVE",
                    "about": "Главный телеграм-канал «Медузы». Для связи: @meduzalovesyou\n\nПриложение для iOS https://mdza.io/JtSJ9t50Ww4\nИ для Android https://mdza.io/IQkzDh0RHw4\n\nРассылка Signal в телеграме: @meduzasignal",
                    "category": "Новости и СМИ",
                    "country": "Россия",
                    "language": "Русский",
                    "image100": "//static10.tgstat.ru/channels/_100/ad/ad61ab143223efbc24c7d2583be69251.jpg",
                    "image640": "//static1.tgstat.ru/channels/_0/ad/ad61ab143223efbc24c7d2583be69251.jpg",
                    "participants_count": 1211062,
                    "tgstat_restrictions": []
                },
                "items": [
                    {
                        "id": 2,
                        "date": 1696843128,
                        "views": 23483,
                        "link": "t.me/meduzalive/s/18",
                        "channel_id": 74,
                        "is_expired": 1,
                        "expire_at": 1697015928,
                        "caption": "Мой первый день преподавателя)",
                        "media": {
                            "file_size": 9184495,
                            "file_url": "https://static23.tgcnt.ru/stories/_0/32/321b22809d2f98d3c7d7cd08154aaeda.mp4",
                            "file_thumbnail_url": "https://static20.tgcnt.ru/stories/_720/d7/d726d7f5e89acf67d01e4a98afcd9f1e.jpg"
                        }
                    },
                ]
            }
        }


        result = tgs.get_result(data, enums.ChannelsRequests.STORIES)
        self.assertIsInstance(result, classes.MassiveResult)


        data = {
            "status": "ok",
            "response": {
                "items": [
                    {
                        "mentionId": 48258272,
                        "mentionType": "channel",
                        "postId": 4375814870,
                        "postLink": "https://t.me/Heath_Ledger_media/51932",
                        "postDate": 1543487975,
                        "channelId": 197080
                    },
                    {
                        "mentionId": 48254456,
                        "mentionType": "channel",
                        "postId": 4375344988,
                        "postLink": "https://t.me/zradaperemoga/2865",
                        "postDate": 1543487209,
                        "channelId": 79853
                    }
                ],
                "channels": [
                    {
                        "id": 79853,
                        "link": "t.me/zradaperemoga",
                        "username": "@zradaperemoga",
                        "title": "Зрада чи Перемога",
                        "about": "Реальные новости из украинского зазеркалья. Телеграмируем из матери городов русских (Киев - не без ватников).\nДля связи: zperemoga78@mail.ru",
                        "image100": "//static2.tgstat.com/public/images/channels/_100/ac/ac2c1fd09bc875e9e64d78c947c38128.jpg",
                        "image640": "//static2.tgstat.com/public/images/channels/_0/ac/ac2c1fd09bc875e9e64d78c947c38128.jpg",
                        "participants_count": 12921
                    },
                    {
                        "id": 197080,
                        "link": "t.me/Heath_Ledger_media",
                        "username": "@Heath_Ledger_media",
                        "title": "Хит Леджер",
                        "about": "Новости, которые мы заслужили.\nВсе самое свежее про вільну і незалежну тут!\nДля связи - @nika_toy",
                        "image100": "//static2.tgstat.com/public/images/channels/_100/97/97f0a0d896218504dc12fc312a433fe0.jpg",
                        "image640": "//static2.tgstat.com/public/images/channels/_0/97/97f0a0d896218504dc12fc312a433fe0.jpg",
                        "participants_count": 3306
                    },
                    
                ]
            }
        }


        result = tgs.get_result(data, enums.ChannelsRequests.MENTIONS)
        self.assertIsInstance(result, classes.MassiveResult)

        data = {
            "status": "ok",
            "response": {
                "items": [
                    {
                        "forwardId": 29244863,
                        "sourcePostId": 29470001798,
                        "postId": 4221534307,
                        "postLink": "https://t.me/telebrend/429",
                        "postDate": 1542823702,
                        "channelId": 217945
                    },
                    {
                        "forwardId": 28132523,
                        "sourcePostId": 29464481491,
                        "postId": 4128289212,
                        "postLink": "https://t.me/telepulse/289",
                        "postDate": 1542451613,
                        "channelId": 194251
                    }
                ],
                "channels": [
                    {
                        "id": 194251,
                        "link": "t.me/telepulse",
                        "username": "@telepulse",
                        "title": "Пульс Telegram",
                        "about": "Самые интересные события, происходящие в Telegram. \n\n▫️Каналы, стремительно набирающие популярность;\n▫️Сводки по самым популярным и цитируемым публикациям за день;\n▫️Тренды недели - все здесь!\n\nДержи руку на пульсе!",
                        "image100": "//static.tgstat.ru/public/images/channels/_100/76/764b7b71a9162b27d30a1750e17230c4.jpg",
                        "image640": "//static.tgstat.ru/public/images/channels/_0/76/764b7b71a9162b27d30a1750e17230c4.jpg",
                        "participants_count": 498
                    },
                    {
                        "id": 217945,
                        "link": "t.me/telebrend",
                        "username": "@telebrend",
                        "title": "Телеграм БРЕНД 🔝",
                        "about": "Продвижение и заработок в Telegram\n😊 Новичкам 😎 Средним 😜 Профи\n\n📌 Запись на консультацию https://t.me/telebrend/241\n\n✅ По вопросам сотрудничества \nи рекламе @reklama_dengi\n\nБот-автоответчик 🤖 @telebrend_bot",
                        "image100": "//static.tgstat.ru/public/images/channels/_100/e8/e8acde5aeadc76bab05dc26544259d2a.jpg",
                        "image640": "//static.tgstat.ru/public/images/channels/_0/e8/e8acde5aeadc76bab05dc26544259d2a.jpg",
                        "participants_count": 172
                    }
                ]
            }
        }


        result = tgs.get_result(data, enums.ChannelsRequests.FORWARDS)
        self.assertIsInstance(result, classes.MassiveResult)

    
    def test_dynamic_info(self):
        tgs = tg_stat.TGStatSync(environ.get("0000"), tests=True)
        data = {
            "status": "ok",
            "response": [
                {
                    "period": "2020-03-11 10:00",           # 11 марта 2020, 10:00
                    "participants_count": 1518              # кол-во подписчиков по состоянию на 10:00 11 марта 2020
                },
                {
                    "period": "2020-03-11 09:00",
                    "participants_count": 1407
                },
                {
                    "period": "2020-03-11 08:00",
                    "participants_count": 1391
                },
                {
                    "period": "2020-03-11 07:00",
                    "participants_count": 1370
                },
                {
                    "period": "2020-03-11 06:00",
                    "participants_count": 1338
                },
            ]
        }
        dynamic_data = tgs.get_result(data, enums.ChannelsRequests.SUBSCRIBERS)
        self.assertIsInstance(dynamic_data[-1], classes.DynamicData, "Channels SUBSCRIBERS not DynamicData class")

        data = {
            "status": "ok",
            "response": [
                {
                    "period": "2018-11-04",             # 4 ноября 2018
                    "views_count": 3985                 # суммарное кол-во просмотров, совершенных 4 ноября 2018 до 23:59
                },
                {
                    "period": "2018-11-03",
                    "views_count": 4010
                },
                {
                    "period": "2018-11-02",
                    "views_count": 2381
                },
            ]
        }
        dynamic_data = tgs.get_result(data, enums.ChannelsRequests.VIEWS)
        self.assertIsInstance(dynamic_data[-1], classes.DynamicData, "Channels VIEWS not DynamicData class")

        data={
            "status": "ok",
            "response": [
                {
                    "period": "2021-11-26",
                    "avg_posts_reach": 6017
                },
                {
                    "period": "2021-11-25",
                    "avg_posts_reach": 5875
                },
                {
                    "period": "2021-11-24",
                    "avg_posts_reach": 5738
                },
            ]
        }
        dynamic_data = tgs.get_result(data, enums.ChannelsRequests.AVG_POSTS_REACH)
        self.assertIsInstance(dynamic_data[-1], classes.DynamicData, "Channels AVG_POSTS_REACH not DynamicData class")

        data={
            "status": "ok",
            "response": [
                {
                    "period": "2021-11-26",
                    "er": 41
                },
                {
                    "period": "2021-11-25",
                    "er": 41.4
                },
                {
                    "period": "2021-11-24",
                    "er": 40.9
                },
            ]
        }
        dynamic_data = tgs.get_result(data, enums.ChannelsRequests.ER)
        self.assertIsInstance(dynamic_data[-1], classes.DynamicData, "Channels ER not DynamicData class")

        data = {
            "status": "ok",
            "response": [
                {
                    "period": "2021-11-26",
                    "err": 41
                },
                {
                    "period": "2021-11-25",
                    "err": 41.4
                },
                {
                    "period": "2021-11-24",
                    "err": 40.9
                },
            ]
        }
        dynamic_data = tgs.get_result(data, enums.ChannelsRequests.ERR)
        self.assertIsInstance(dynamic_data[-1], classes.DynamicData, "Channels ERR not DynamicData class")

        data = {
            "status": "ok",
            "response": [
                {
                    "period": "2021-11-26",
                    "err24": 41
                },
                {
                    "period": "2021-11-25",
                    "err24": 41.4
                },
                {
                    "period": "2021-11-24",
                    "err24": 40.9
                },
            ]
        }
        dynamic_data = tgs.get_result(data, enums.ChannelsRequests.ERR24)
        self.assertIsInstance(dynamic_data[-1], classes.DynamicData, "Channels ERR24 not DynamicData class")
        
        
    def test_posts(self):
        null = None
        tgs = tg_stat.TGStatSync(environ.get("0000"), tests=True)

        data = {
            "status": "ok",
            "response": {
                "id": 1002665528,
                "date": 1523019187,
                "views": 9736,
                "link": "t.me/tg_analytics/130",
                "channel_id": 53248,
                "forwarded_from": null,
                "is_deleted": 0,
                "text": "Хотите узнать кто репостнул или поделился ссылкой на публикацию и при этом не выходить из любимого Телеграмчика — просто перешлите публикацию нашему боту @TGStat_Bot",
                "media": {
                    "media_type": "mediaPhoto",
                    "caption": ""
                }
            }
        }
        result = tgs.get_result(data, sub_category=enums.PostsRequests.GET)
        self.assertIsInstance(result, classes.Post)

        data = {
            "status": "ok",
            "response": {
                "viewsCount": 157210,
                "sharesCount": 723,
                "commentsCount": 1,
                "reactionsCount": 7452,
                "forwardsCount": 3,
                "mentionsCount": 0,
                "forwards": [
                    {
                        "postId": "26784773903",
                        "postLink": "t.me/LEGION_URAL/726365",
                        "postDate": 1659673815,
                        "channelId": 12337001,
                        "peerType": "chat"
                    },
                    {
                        "postId": "26778706543",
                        "postLink": "t.me/moyvictortsoy/983",
                        "postDate": 1659645896,
                        "channelId": 11015249,
                        "peerType": "channel"
                    },
                    {
                        "postId": "26776890651",
                        "postLink": "t.me/p0pizdelki/453004",
                        "postDate": 1659645701,
                        "channelId": 4186970,
                        "peerType": "chat"
                    }
                ],
                "mentions": [],
                "views": [
                    {
                        "date": "2022-08-05 00:41",
                        "viewsGrowth": 32367
                    },
                    {
                        "date": "2022-08-05 01:41",
                        "viewsGrowth": 7566
                    }, 
                    {
                        "date": "2022-08-08 07:41",
                        "viewsGrowth": 313
                    },
                    {
                        "date": "2022-08-08 08:41",
                        "viewsGrowth": 384
                    },
                    {
                        "date": "2022-08-08 09:41",
                        "viewsGrowth": 250
                    },
                ]
            }
        }
        result = tgs.get_result(data, sub_category=enums.PostsRequests.STAT)
        self.assertIsInstance(result, classes.GroupStatistic)

        data = {
            "status": "ok",
            "response": [
                {
                    "postId": 33322446607,
                    "viewsCount": 10355,
                    "sharesCount": 97,
                    "commentsCount": 55,
                    "reactionsCount": 130
                },
                {
                    "postId": 32755689682,
                    "viewsCount": 24846,
                    "sharesCount": 263,
                    "commentsCount": 95,
                    "reactionsCount": 148
                },
                {
                    "postId": 32302735720,
                    "viewsCount": 39015,
                    "sharesCount": 91,
                    "commentsCount": 52,
                    "reactionsCount": 112
                },
                {
                    "postId": 32061730638,
                    "viewsCount": 37303,
                    "sharesCount": 95,
                    "commentsCount": 24,
                    "reactionsCount": 113
                }
            ]
        }
        result = tgs.get_result(data, sub_category=enums.PostsRequests.STAT_MULTI)
        self.assertIsInstance(result[0], classes.UnionStatistic)

        data = {
            "status": "ok",
            "response": {
                "count": 50, 
                "total_count": 27518, 
                "items": [ 
                    {
                        "id": 3584651917, 
                        "date": 1540057519, 
                        "views": 3139, 
                        "shares_count": 12,
                        "comments_count": 0,
                        "reactions_count": 42,
                        "link": "t.me/orfosvinstvo/6325", 
                        "channel_id": 14069, 
                        "forwarded_from": null,  
                        "is_deleted": 0, 
                        "text": "Друзья! Я уверен, что вы ведёте свои телеграм-каналы ...",
                        "snippet": "Друзья! Я уверен, что вы ведёте свои телеграм-каналы ...", 
                        "media": {
                            "media_type": "mediaDocument",
                            "mime_type": "video/mp4",
                            "size": 5085138
                        }
                    },
                ],
                "channels": [ 
                    {
                        "id": 14069, 
                        "link": "t.me/orfosvinstvo", 
                        "username": "@orfosvinstvo", 
                        "title": "Орфосвинство и идиомаркетинг", 
                        "about": "Исправляем ошибки ...", 
                        "image100": "//static.tgstat.ru/...", 
                        "image640": "//static.tgstat.ru/...", 
                        "participants_count": 9097
                    },
                ]
            }
        }
        result = tgs.get_result(data, sub_category=enums.PostsRequests.SEARCH)
        self.assertIsInstance(result, classes.MassiveResult)


    def test_stories(self):
        null = None
        tgs = tg_stat.TGStatSync(environ.get("0000"), tests=True)

        data = {
            "status": "ok",
            "response": {
                "id": 7939137,
                "date": 1701281859,
                "views": 218410,
                "link": "t.me/breakingmash/s/35",
                "channel_id": 7377,
                "is_expired": 1,
                "expire_at": 1701368259,
                "caption": "Капелька новых поправок к законам в нашей сторис. Бусты как всегда по ссылке: https://t.me/breakingmash?boost",
                "media": {
                    "file_size": 24708968,
                    "file_url": null,
                    "file_thumbnail_url": "https://static25.tgcnt.ru/stories/_180/9d/9d2c28eda69a445965639cd2b1f9e4fd.jpg"
                }
            }
        }
        result = tgs.get_result(data, sub_category=enums.StoriesRequests.GET)
        self.assertIsInstance(result, classes.Story)


        data = {
            "status": "ok",
            "response": {
                "viewsCount": 218410,
                "forwardsCount": 130,        
                "reactionsCount": 9953,       
                "views": [
                    {
                        "date": "2023-11-29 22:17",
                        "viewsGrowth": 28272
                    },
                    {
                        "date": "2023-11-29 23:17",
                        "viewsGrowth": 20169
                    },
                    {
                        "date": "2023-11-30 00:17",
                        "viewsGrowth": 12194
                    },
                    {
                        "date": "2023-11-30 21:17",
                        "viewsGrowth": 9099
                    }
                ]
            }
        }
        result = tgs.get_result(data, sub_category=enums.StoriesRequests.STAT)
        self.assertIsInstance(result, classes.GroupStatistic)

        data = {
            "status": "ok",
            "response": [
                {
                    "storyId": 21176184921,
                    "viewsCount": 1281,
                    "sharesCount": 83,          
                    "reactionsCount": 105
                },
                {
                    "storyId": 28776184920,
                    "viewsCount": 2729,
                    "sharesCount": 192,            
                    "reactionsCount": 123
                },
                {
                    "storyId": 22776184919,
                    "viewsCount": 3007,
                    "sharesCount": 62,            
                    "reactionsCount": 98
                },
                {
                    "storyId": 26476184918,
                    "viewsCount": 3201,
                    "sharesCount": 74,            
                    "reactionsCount": 85
                }
            ]
        }
        result = tgs.get_result(data, sub_category=enums.StoriesRequests.STAT_MULTI)
        self.assertIsInstance(result[0], classes.UnionStatistic)


    def test_mentions(self):
        null = None
        tgs = tg_stat.TGStatSync(environ.get("0000"), tests=True)
        data = {
            "status": "ok",
            "response": {
                "items": [
                    {
                        "period": "2018-11-04",
                        "mentions_count": 11,
                        "views_count": 6781
                    },
                    {
                        "period": "2018-11-03",
                        "mentions_count": 27,
                        "views_count": 13097
                    },
                    {
                        "period": "2018-11-02",
                        "mentions_count": 38,
                        "views_count": 19091
                    },
                ]
            }
        }
        result = tgs.get_result(data, sub_category=enums.WordsRequests.MENTIONS_BY_PERIOD)
        self.assertIsInstance(result[0], classes.DynamicData)

        data = {
            "status": "ok",
            "response": {
                "items": [
                    {
                        "channel_id": 74647,
                        "mentions_count": 4544,
                        "views_count": 78710,
                        "last_mention_date": 1572539401
                    },
                    {
                        "channel_id": 55422,
                        "mentions_count": 1,
                        "views_count": 900,
                        "last_mention_date": 1572204557
                    },
                    {
                        "channel_id": 63694,
                        "mentions_count": 1,
                        "views_count": 1053,
                        "last_mention_date": 1570826223
                    },
                ],
                "channels": [
                    {
                        "id": 74647,
                        "link": "t.me/newchans",
                        "username": "@newchans",
                        "title": "Новые каналы",
                        "about": "Здесь автоматически публикуются новые каналы, зарегистрированные в Telegram и попавшие в индекс TGStat.",
                        "image100": "//static10.tgstat.ru/channels/_100/a8/a82c47f8c5d7d1259ee13ed84a4be346.jpg",
                        "image640": "//static10.tgstat.ru/channels/_0/a8/a82c47f8c5d7d1259ee13ed84a4be346.jpg",
                        "participants_count": 259
                    },
                    {
                        "id": 55422,
                        "link": "t.me/raskruti",
                        "username": "@raskruti",
                        "title": "Раскрути канал",
                        "about": "Если вам нехрен делать - пишите сюда @neznayca \nА лучше не пишите, а то я добрый, добрый, а могу и на хер послать",
                        "image100": "//static10.tgstat.ru/channels/_100/2e/2e72ed76b7b3b9ce2f15fce64178dfaf.jpg",
                        "image640": "//static10.tgstat.ru/channels/_0/2e/2e72ed76b7b3b9ce2f15fce64178dfaf.jpg",
                        "participants_count": 6521
                    },
                    {
                        "id": 63694,
                        "link": "t.me/pltrk",
                        "username": "@pltrk",
                        "title": "Политрук 2.0",
                        "about": "Подкрепление? Ты и есть подкрепление.\n\nПоддержать: 4432 7300 1577 4617",
                        "image100": "//static10.tgstat.ru/channels/_100/0c/0c3f40425314745073e174541ba5e6ad.jpg",
                        "image640": "//static10.tgstat.ru/channels/_0/0c/0c3f40425314745073e174541ba5e6ad.jpg",
                        "participants_count": 2823
                    },
                ]
            }
        }
        result = tgs.get_result(data, sub_category=enums.WordsRequests.MENTIONS_BY_CHANNELS)
        self.assertIsInstance(result, classes.MassiveResult)

if __name__ == '__main__':
    unittest.main()