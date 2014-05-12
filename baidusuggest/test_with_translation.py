# -*- coding: utf-8 -*-

## pip install translate
## pip install mstranslate
## pip install yandex.translate

def google_translate(text, langc="zh-CN", langc_f="en"):
    import translate
    from translate import Translator
    translator= Translator(to_lang=langc, from_lang=langc_f)
    return translator.translate(text)

def bing_translate(text, langc="zh-CN"):
    # Using the free Bing Translation APIs: http://www.microsoft.com/web/post/using-the-free-bing-translation-apis  https://datamarket.azure.com/account
    from mstranslate import MSTranslate
    translator = MSTranslate('client_id', 'client_secret')
    return kk.translate(text, langc)

def y_translate(text, langc="zh-CN"):
    # http://api.yandex.com/translate/
    from yandex_translate import YandexTranslate
    translate = YandexTranslate('Your API key here.')
    ##    print('Languages:', translate.langs)
    ##    print('Translate directions:', translate.directions)
    ##    print('Detect language:', translate.detect('Привет, мир!'))
    ##    print('Translate:', translate.translate('Привет, мир!', 'ru-en'))
    return translate.translate(text, langc)

import baidusuggest

import sys
def msg_list(lst):
    return repr([x.encode('utf8') for x in lst]).decode('string-escape')

def list_translated(lst):
    return [google_translate(x.encode('utf-8'), langc="en", langc_f="zh") for x in lst] 


query_en="Communist party should" #
query_input=google_translate(query_en) 
suggestions_list=[]

query_output, suggestions_list=baidusuggest.get(query_input)
query_output_en=google_translate(query_output.encode('utf-8'), langc="en", langc_f="zh")

print "Input\tInput(Chinese)\tOutput(Chinese)\tOutput"
print "%s\t%s\t%s\t%s" % (query_en, query_input, query_output,query_output_en)
print "Output suggestions"
print msg_list(suggestions_list)
print msg_list(list_translated(suggestions_list))


##Sample output
##Input	Input(Chinese)	Output(Chinese)	Output
##Communist Party	共产党	共产党	Communist party
##Output suggestions
##['共产党宣言', '共产党员网', '共产党员', '共产党员的信仰', '共产党员新闻网', '共产党员网首页', '共产党员人数', '共产党员必须履行的八项义务是什么', '共产党员的基本条件', '共产党员公开承诺书']
##['The Communist Manifesto', 'Communists Network', 'Communists', 'Communist beliefs', 'Communist News Network', 'Communists Home', 'Communists number', 'What eight Communists must fulfill the obligations', 'Communist basic conditions', 'Communists public undertaking']
##>>> ================================ RESTART ================================
##Input	Input(Chinese)	Output(Chinese)	Output
##USA	美国	美国	United States
##Output suggestions
##['美国队长', '美国队长2', '美国队长1电影', '美国队长2电影', '美国亚马逊', '美国队长1', '美国恐怖故事', '美国队长2百度影音', '美国派', '美国骗局']
##['Captain America', 'Captain America 2', '1 Captain America movie', 'Captain America 2 Movie', 'Amazon U.S.', 'Captain America 1', 'American Horror Story', 'Captain America 2 Baidu Video', 'American Pie', 'American scam']
##>>> ================================ RESTART ================================
##Input	Input(Chinese)	Output(Chinese)	Output
##Japan	日本	日本	Japan
##Output suggestions
##['日本乙级联赛', '日本乙级联赛积分榜', '日本j2联赛直播', '日本动漫', '日本动漫黄动画大全', '日本电影', '日本旅游', '日本亚马逊', '日本天皇']
##['Japan League', 'Japan League Standings', 'Japan j2 League Live', 'Japanese anime', 'Japanese anime animation Daquan Huang', 'Japanese Movie', 'Japan Travel', 'Amazon Japan', 'Japanese Emperor']
##>>> ================================ RESTART ================================
##Input	Input(Chinese)	Output(Chinese)	Output
##Korea	韩国	韩国	Korea
##Output suggestions
##['韩国电影', '韩国综艺', '韩国女主播', '韩国沉船事故', '韩国客轮沉没', '韩国电视剧', '韩国娱乐新闻', '韩国旅游', '韩国公认10大零整容美女', '韩国美女']
##['Korean Movie', 'Korea Arts', 'South Korean female anchor', 'Korea shipwreck', 'South Korean ferry sinking', 'Korean drama', 'Korean Entertainment News', 'Korea Tourism', 'South Korea accepted 10 zero cosmetic beauty', 'Korean girls']
##>>> ================================ RESTART ================================
##Input	Input(Chinese)	Output(Chinese)	Output
##Taiwan	台湾	台湾	Taiwan
##Output suggestions
##['台湾新闻', '台湾旅游', '台湾菲律宾最新消息', '台湾偶像剧', '台湾综艺', '台湾地图', '台湾大学', '台湾自由行', '台湾旅游攻略', '台湾自由行手续']
##['Taiwan news', 'Taiwan Tourism', 'Taiwan and Philippines News', 'Taiwan idol drama', 'Taiwan Arts', 'Taiwan map', 'National Taiwan University', 'Taiwan Visit', 'Taiwan Travel Guides', 'Taiwan Visit formalities']
##>>> ================================ RESTART ================================
##Input	Input(Chinese)	Output(Chinese)	Output
##Hong Kong	香港	香港	Hong Kong
##Output suggestions
##['香港天气', '香港天文台', '香港电影', '香港大学', '香港地铁', '香港游攻略', '香港地图', '香港中文大学', '香港金像奖2014', '香港电视剧']
##['Hong Kong Weather', 'The Hong Kong Observatory', 'Hong Kong Film', 'University of Hong Kong', 'Hong Kong MTR', 'Hong Kong Tour Guides', 'Hong Kong map', 'Chinese University of Hong Kong', 'Hong Kong Awards 2014', 'Hong Kong TV']

##>>> ================================ RESTART ================================
##Input	Input(Chinese)	Output(Chinese)	Output
##Communist party should	共产党应该	共产党应该	The Communist Party should
##Output suggestions
##[]
##[]
##>>> ================================ RESTART ================================
## "USA should"
##Input	Input(Chinese)	Output(Chinese)	Output
##USA should	美国应	美国应	The United States should
##Output suggestions
##['美国应用材料公司', '美国应用生物系统公司', '美国应召女郎', '美国应对恐怖袭击幸存指南', '美国应用材料', '美国应用数学专业排名', '美国应对恐怖袭击幸存指南 逃不了再战', '美国应用数学排名', '美国应用材料公司 西安', '美国应急管理']
##['Applied Materials, Inc.', 'Applied Biosystems', 'American call girl', 'U.S. response to the terrorist attacks survived Guide', 'Applied Materials', 'Applied Mathematics Rankings', 'U.S. response to the terrorist attacks on the surviving guide run away to fight another day', 'Applied Mathematics ranking', "Applied Materials Xi'an", 'American Emergency Management']
##>>> ================================ RESTART ================================
## "Japan should"
##Input	Input(Chinese)	Output(Chinese)	Output
##Japan should	日本应	日本应	Japan should
##Output suggestions
##['日本应庆大学', '日本应召女郎', '日本应试教育', '日本应用', '日本应援团']
##['Keio University, Japan', 'Japanese call girl', "Japan's exam-oriented education", 'Japanese Application', 'Japanese Ouendan']
##>>> ================================ RESTART ================================
##Input	Input(Chinese)	Output(Chinese)	Output
##Korea should	韩国应	韩国应	Korea should
##Output suggestions
##['韩国应援', '韩国应援文化', '韩国应用', '韩国应该买什么']
##['Korea should aid', 'Korean culture should aid', 'Korea Application', 'Korea should buy what']
##>>> ================================ RESTART ================================
##Input	Input(Chinese)	Output(Chinese)	Output
##Taiwan should	台湾应	台湾应	Taiwan should
##Output suggestions
##['台湾应召站']
##['Taiwan summoned station']
##>>> ================================ RESTART ================================
##Input	Input(Chinese)	Output(Chinese)	Output
##Hong Kong should	香港应	香港应	Hong Kong should
##Output suggestions
##['香港应用科技研究院', '香港应科院', '香港应用科技研究院有限公司', '香港应聘', '香港应该买什么', '香港应届生招聘', '香港应对占领中环', '香港应急电话', '香港应召女郎']
##['Hong Kong Science and Technology Research Institute', 'ASTRI', 'Hong Kong Science and Technology Research Institute Company Limited', 'Hong Kong candidates', 'Hong Kong should buy what', 'Graduates Jobs in Hong Kong', 'Occupy Central Hong Kong to deal with', 'Hong Kong Emergency Phone', 'Hong Kong call girl']
##

