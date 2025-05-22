import os
import pytest
import requests

import parser


data = [
    ('cambridge_en_ru_handle.html',
     [
         parser.Card(word='handle',
                     pos='verb',
                     source='http://example.com',
                     src_uk_mp3='https://dictionary.cambridge.org/media/english-russian/uk_pron/u/ukh/ukhan/ukhandb022.mp3',
                     pron_uk='/ˈhændl/',
                     src_us_mp3='https://dictionary.cambridge.org/media/english-russian/us_pron/h/han/handl/handle.mp3',
                     pron_us='/ˈhændl/',
                     data=[{'definition': 'to deal with something',
                            'examples': ['He handled the situation very well.',
                                         ' This office handles thousands of enquiries every '
                                         'day.'],
                            'translate': 'иметь дело с чем-либо, справляться '},
                           {'definition': 'to touch, hold, or pick up something',
                            'examples': ['You must wash your hands before handling food.'],
                            'translate': 'трогать, прикасаться '},
                           {'definition': 'to buy and sell goods',
                            'examples': ["He's been charged with handling stolen goods."],
                            'translate': 'торговать '}],
                     src_images=[]),
         parser.Card(word='handle',
                     pos='noun',
                     source='http://example.com',
                     src_uk_mp3='https://dictionary.cambridge.org/media/english-russian/uk_pron/u/ukh/ukhan/ukhandb022.mp3',
                     pron_uk='/ˈhændl/',
                     src_us_mp3='https://dictionary.cambridge.org/media/english-russian/us_pron/h/han/handl/handle.mp3',
                     pron_us='/ˈhændl/',
                     data=[{'definition': 'the part of something that you use to hold it or '
                                          'open it',
                            'examples': ['a door handle ', 'the handle on a suitcase'],
                            'translate': 'ручка, рукоятка '}],
                     src_images=[])

     ]
     ),

    ('cambridge_en_ru_pick_sth_sb_up.html',

     [
         parser.Card(word='pick sth/sb up',
                     pos='phrasal verb',
                     source='http://example.com',
                     src_uk_mp3='https://dictionary.cambridge.org/media/english-russian/uk_pron/u/ukp/ukpia/ukpiano004.mp3',
                     pron_uk='/pɪk/',
                     src_us_mp3='https://dictionary.cambridge.org/media/english-russian/us_pron/p/pic/pick_/pick.mp3',
                     pron_us='/pɪk/',
                     data=[{'definition': 'to lift something or someone by using your hands',
                            'examples': ['He picked his coat up off the floor.',
                                         ' Just pick up the phone and call him.'],
                            'translate': 'поднимать, подбирать '},
                           {'definition': 'to collect someone who is waiting for you, or to '
                                          'collect something that you have left somewhere',
                            'examples': ['Can you pick me up from the airport?',
                                         " I've got to pick up those books I ordered."],
                            'translate': 'заезжать за кем-либо, забирать что-либо '}],
                     src_images=[])

     ]
     ),
    (
        'cambridge_en_handle.html',
        [
            parser.Card(word='handle',
                        pos='noun',
                        source='http://example.com',
                        src_uk_mp3='https://dictionary.cambridge.org/media/english/uk_pron/u/ukh/ukhan/ukhandb022.mp3',
                        pron_uk='/ˈhæn.dəl/',
                        src_us_mp3='https://dictionary.cambridge.org/media/english/us_pron/h/han/handl/handle.mp3',
                        pron_us='/ˈhæn.dəl/',
                        data=[{'definition': 'a part of an object designed for holding, moving, '
                                             'or carrying the object easily: ',
                               'examples': ['a door handle',
                                            ' the handle on a suitcase',
                                            " I can't pick the kettle up - the handle's too hot.",
                                            'turn a handle She turned the handle and slowly '
                                            'opened the door.'],
                               'translate': ''},
                              {'definition': 'a name of a person or place, especially a strange '
                                             'one: ',
                               'examples': ["That's some handle to go through life with!"],
                               'translate': ''},
                              {'definition': 'a name that someone is known by on some social '
                                             'media websites: ',
                               'examples': ['On this site, handles start with an @ sign.',
                                            ' You can follow the team under the handle '
                                            '@ManUtd.'],
                               'translate': ''}],
                        src_images=[
                            'https://dictionary.cambridge.org/images/full/handle_noun_002_17134.jpg?version=6.0.50']),
            parser.Card(word='handle',
                        pos='verb',
                        source='http://example.com',
                        src_uk_mp3='https://dictionary.cambridge.org/media/english/uk_pron/u/ukh/ukhan/ukhandb022.mp3',
                        pron_uk='/ˈhæn.dəl/',
                        src_us_mp3='https://dictionary.cambridge.org/media/english/us_pron/h/han/handl/handle.mp3',
                        pron_us='/ˈhæn.dəl/',
                        data=[{'definition': 'to deal with, have responsibility for, or be in '
                                             'charge of: ',
                               'examples': ['I thought he handled the situation very well.',
                                            ' Some people are brilliant with computers, but have '
                                            'no idea how to handle (= behave with) other people.',
                                            " If you can't handle the job I'll get someone else "
                                            'to do it.',
                                            ' Who handles the marketing in your company?'],
                               'translate': ''},
                              {'definition': 'to pick something up and touch, hold, or move it '
                                             'with your hands: ',
                               'examples': ['Always wash your hands before handling food.',
                                            " Please don't handle the vases - they're very "
                                            'fragile.'],
                               'translate': ''},
                              {'definition': 'to operate or control something that could be '
                                             'difficult or dangerous: ',
                               'examples': ['Have you ever handled a gun before?'],
                               'translate': ''}],
                        src_images=[])
        ]
    )
]


@pytest.mark.parametrize('filename, answers', data)
def test_cambridge(monkeypatch, filename, answers):

    path = os.path.join(os.path.dirname(__file__), 'sample_pages', filename)
    with open(path, 'r') as f:
        page = f.read()


    class MockResponse:
        def __init__(self, text, status_code):
            self.text = text
            self.status_code = status_code
            self.url = 'http://example.com'


    class MockSession:
        def __init__(self):
            self.headers = {}

        def get(self, *args, **kwargs):
            return MockResponse(text=page, status_code=200)


    monkeypatch.setattr(requests, "Session", lambda: MockSession())

    obj = parser.CambridgeDict(word='test')

    assert len(obj.cards) == len(answers)

    for card in obj.cards:
        assert card in answers
