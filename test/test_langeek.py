import requests

from parser import LanGeekDict, Card


json_langeek_brief = [
 {'id': 23570,
  'entry': 'brief',
  'inCategory': True,
  'pronunciation': '',
  'secondPronunciation': '',
  'translation': {'id': 23600,
                  'translation': 'to give someone essential information or '
                                 'instructions about a particular subject or '
                                 'task',
                  'wordPhoto': {'originalTitle': 'keep posted',
                                'otherTitles': [],
                                'updatedAt': '2024-06-08T11:41:40+0000',
                                'photoId': 44786,
                                'description': '',
                                'urlId': '',
                                'webTitle': 'گفتن و اطلاع دادن',
                                'photo': 'https://cdn.langeek.co/photo/44786/original/?type=jpeg',
                                'photoThumbnail': 'https://cdn.langeek.co/photo/44786/thumb?type=jpeg'},
                  'position': 0,
                  'partOfSpeech': {'partOfSpeechType': 'verb'}},
                       'translations': {'verb': [{'id': 23600,
                             'translation': 'to give someone essential '
                                            'information or instructions about '
                                            'a particular subject or task',
                             'wordPhoto': {'originalTitle': 'keep posted',
                                           'otherTitles': [],
                                           'updatedAt': '2024-06-08T11:41:40+0000',
                                           'photoId': 44786,
                                           'description': '',
                                           'urlId': '',
                                           'webTitle': 'گفتن و اطلاع دادن',
                                           'photo': 'https://cdn.langeek.co/photo/44786/original/?type=jpeg',
                                           'photoThumbnail': 'https://cdn.langeek.co/photo/44786/thumb?type=jpeg'},
                             'position': 0,
                             'partOfSpeech': {'partOfSpeechType': 'verb'}},
                            {'id': 237501,
                             'translation': 'to create a summarized version of '
                                            'something, condensing the main '
                                            'points or information into a '
                                            'shorter form',
                             'wordPhoto': None,
                             'position': 1,
                             'partOfSpeech': {'partOfSpeechType': 'verb'}}],
                   'adjective': [{'id': 23603,
                                  'translation': 'short in duration',
                                  'wordPhoto': {'originalTitle': 'brief',
                                                'otherTitles': [],
                                                'updatedAt': '2022-04-10T12:00:30+0000',
                                                'photoId': 23687,
                                                'description': '',
                                                'urlId': '',
                                                'webTitle': 'کوتاه',
                                                'photo': 'https://cdn.langeek.co/photo/23687/original/?type=jpeg',
                                                'photoThumbnail': 'https://cdn.langeek.co/photo/23687/thumb?type=jpeg'},
                                  'position': 3,
                                  'partOfSpeech': {'partOfSpeechType': 'adjective'}},
                                 {'id': 23602,
                                  'translation': '(of clothes) short and '
                                                 'revealing',
                                  'wordPhoto': {'originalTitle': 'little black '
                                                                 'dress',
                                                'otherTitles': [],
                                                'updatedAt': '2022-05-18T12:51:18+0000',
                                                'photoId': 24959,
                                                'description': '',
                                                'urlId': '',
                                                'webTitle': 'پیراهن مشکی کوتاه',
                                                'photo': 'https://cdn.langeek.co/photo/24959/original/?type=jpeg',
                                                'photoThumbnail': 'https://cdn.langeek.co/photo/24959/thumb?type=jpeg'},
                                  'position': 4,
                                  'partOfSpeech': {'partOfSpeechType': 'adjective'}},
                                 {'id': 23601,
                                  'translation': 'concise and to the point',
                                  'wordPhoto': None,
                                  'position': 2,
                                  'partOfSpeech': {'partOfSpeechType': 'adjective'}}],
                   'noun': [{'id': 23599,
                             'translation': 'a short document stating the '
                                            'facts provided by one side of a '
                                            'case to be presented to a court '
                                            'or judge',
                             'wordPhoto': None,
                             'position': 5,
                             'partOfSpeech': {'partOfSpeechType': 'noun'}},
                            {'id': 237498,
                             'translation': 'a legal case or assignment given '
                                            'to a lawyer to argue or handle in '
                                            'court',
                             'wordPhoto': None,
                             'position': 6,
                             'partOfSpeech': {'partOfSpeechType': 'noun'}},
                            {'id': 237497,
                             'translation': 'a defense attorney representing '
                                            'someone in legal matters',
                             'wordPhoto': None,
                             'position': 7,
                             'partOfSpeech': {'partOfSpeechType': 'noun'}},
                            {'id': 237499,
                             'translation': 'the instructions and information '
                                            'given to provide a clear '
                                            'understanding of what is expected '
                                            'from someone in their job or '
                                            'assignment',
                             'wordPhoto': None,
                             'position': 8,
                             'partOfSpeech': {'partOfSpeechType': 'noun'}},
                            {'id': 23598,
                             'translation': 'a short, written summary or '
                                            'outline that condenses key '
                                            'information into a simplified '
                                            'form',
                             'wordPhoto': None,
                             'position': 9,
                             'partOfSpeech': {'partOfSpeechType': 'noun'}}]},
                       'otherForms': []},
{'id': 23578,
  'entry': 'briefs',
  'inCategory': True,
  'pronunciation': '',
  'secondPronunciation': '',
  'translation': {'id': 23613,
                  'translation': 'legless underwear that fits tightly',
                  'wordPhoto': {'originalTitle': 'briefs',
                                'otherTitles': [],
                                'updatedAt': '2022-06-06T09:50:11+0000',
                                'photoId': 25413,
                                'description': '',
                                'urlId': '',
                                'webTitle': 'شورت اسلیپ',
                                'photo': 'https://cdn.langeek.co/photo/25413/original/?type=jpeg',
                                'photoThumbnail': 'https://cdn.langeek.co/photo/25413/thumb?type=jpeg'},
                  'position': 0,
                  'partOfSpeech': {'partOfSpeechType': 'noun'}},
  'translations': {'noun': [{'id': 23613,
                             'translation': 'legless underwear that fits '
                                            'tightly',
                             'wordPhoto': {'originalTitle': 'briefs',
                                           'otherTitles': [],
                                           'updatedAt': '2022-06-06T09:50:11+0000',
                                           'photoId': 25413,
                                           'description': '',
                                           'urlId': '',
                                           'webTitle': 'شورت اسلیپ',
                                           'photo': 'https://cdn.langeek.co/photo/25413/original/?type=jpeg',
                                           'photoThumbnail': 'https://cdn.langeek.co/photo/25413/thumb?type=jpeg'},
                             'position': 0,
                             'partOfSpeech': {'partOfSpeechType': 'noun'}}]},
  'otherForms': []},
{'id': 23576,
  'entry': 'briefly',
  'inCategory': True,
  'pronunciation': '',
  'secondPronunciation': '',
  'translation': {'id': 23609,
                  'translation': 'in a way that takes a short period of time',
                  'wordPhoto': {'originalTitle': 'Shortly',
                                'otherTitles': [],
                                'updatedAt': '2024-03-06T09:21:28+0000',
                                'photoId': 48905,
                                'description': '',
                                'urlId': '',
                                'webTitle': 'به زودی',
                                'photo': 'https://cdn.langeek.co/photo/48905/original/?type=jpeg',
                                'photoThumbnail': 'https://cdn.langeek.co/photo/48905/thumb?type=jpeg'},
                  'position': 0,
                  'partOfSpeech': {'partOfSpeechType': 'adverb'}},
  'translations': {'adverb': [{'id': 23609,
                               'translation': 'in a way that takes a short '
                                              'period of time',
                               'wordPhoto': {'originalTitle': 'Shortly',
                                             'otherTitles': [],
                                             'updatedAt': '2024-03-06T09:21:28+0000',
                                             'photoId': 48905,
                                             'description': '',
                                             'urlId': '',
                                             'webTitle': 'به زودی',
                                             'photo': 'https://cdn.langeek.co/photo/48905/original/?type=jpeg',
                                             'photoThumbnail': 'https://cdn.langeek.co/photo/48905/thumb?type=jpeg'},
                               'position': 0,
                               'partOfSpeech': {'partOfSpeechType': 'adverb'}},
                              {'id': 23610,
                               'translation': 'in a few words and without many '
                                              'details',
                               'wordPhoto': None,
                               'position': 1,
                               'partOfSpeech': {'partOfSpeechType': 'adverb'}}]},
  'otherForms': []},
                      {'id': 23571,
  'entry': 'briefcase',
  'inCategory': True,
  'pronunciation': '',
  'secondPronunciation': '',
  'translation': {'id': 23604,
                  'translation': 'a flat, leather or plastic case with a '
                                 'handle, used for carrying papers or '
                                 'documents',
                  'wordPhoto': {'originalTitle': 'briefcase',
                                'otherTitles': [],
                                'updatedAt': '2024-04-21T16:06:21+0000',
                                'photoId': 49926,
                                'description': '',
                                'urlId': 'briefcase',
                                'webTitle': 'کیف دستی',
                                'photo': 'https://cdn.langeek.co/photo/49926/original/briefcase?type=jpeg',
                                'photoThumbnail': 'https://cdn.langeek.co/photo/49926/thumb/briefcase?type=jpeg'},
                  'position': 0,
                  'partOfSpeech': {'partOfSpeechType': 'noun'}},
  'translations': {'noun': [{'id': 23604,
                             'translation': 'a flat, leather or plastic case '
                                            'with a handle, used for carrying '
                                            'papers or documents',
                             'wordPhoto': {'originalTitle': 'briefcase',
                                           'otherTitles': [],
                                           'updatedAt': '2024-04-21T16:06:21+0000',
                                           'photoId': 49926,
                                           'description': '',
                                           'urlId': 'briefcase',
                                           'webTitle': 'کیف دستی',
                                           'photo': 'https://cdn.langeek.co/photo/49926/original/briefcase?type=jpeg',
                                           'photoThumbnail': 'https://cdn.langeek.co/photo/49926/thumb/briefcase?type=jpeg'},
                             'position': 0,
                             'partOfSpeech': {'partOfSpeechType': 'noun'}}]},
  'otherForms': []}]

answers = [
    Card(word='brief', pos='verb', source='https://dictionary.langeek.co/en/word/23570?entry=brief',
         definitions=['to give someone essential information or instructions about a particular subject or task'],
         src_images=['https://cdn.langeek.co/photo/44786/thumb?type=jpeg']),
    Card(word='brief', pos='adjective', source='https://dictionary.langeek.co/en/word/23570?entry=brief',
         definitions=['short in duration'],
         src_images=['https://cdn.langeek.co/photo/23687/thumb?type=jpeg']),
    Card(word='brief', pos='adjective', source='https://dictionary.langeek.co/en/word/23570?entry=brief',
         definitions=['(of clothes) short and revealing'],
         src_images=['https://cdn.langeek.co/photo/24959/thumb?type=jpeg']),
    Card(word='briefs', pos='noun', source='https://dictionary.langeek.co/en/word/23578?entry=briefs',
         definitions=['legless underwear that fits tightly'],
         src_images=['https://cdn.langeek.co/photo/25413/thumb?type=jpeg']),
    Card(word='briefly', pos='adverb', source='https://dictionary.langeek.co/en/word/23576?entry=briefly',
         definitions=['in a way that takes a short period of time'],
         src_images=['https://cdn.langeek.co/photo/48905/thumb?type=jpeg']),
    Card(word='briefcase', pos='noun', source='https://dictionary.langeek.co/en/word/23571?entry=briefcase',
         definitions=['a flat, leather or plastic case with a handle, used for carrying papers or documents'],
         src_images=['https://cdn.langeek.co/photo/49926/thumb/briefcase?type=jpeg'])
]


def test_langeek_fetch(monkeypatch):

    class MockResponse:
        def __init__(self, json_data, status_code):
            self._json = json_data
            self.status_code = status_code
            self.url = 'http://example.com',

        def json(self):
            return self._json


    class MockSession:
        def __init__(self):
            self.headers = {}

        def get(self, *args, **kwargs):
            return MockResponse(json_data=json_langeek_brief, status_code=200)


    monkeypatch.setattr(requests, "Session", lambda: MockSession())

    obj = LanGeekDict('brief')
    assert len(obj.cards) == len(answers)
    for card in obj.cards:
        assert card in answers
