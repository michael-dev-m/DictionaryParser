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
                     definitions=['to deal with something',
                                  'to touch, hold, or pick up something',
                                  'to buy and sell goods'],
                     examples=[
                         ['He handled the situation very well.',
                          ' This office handles thousands of enquiries every day.'],
                         ['You must wash your hands before handling food.'],
                         ["He's been charged with handling stolen goods."]
                     ],
                     ru=['иметь дело с чем-либо, справляться ',
                         'трогать, прикасаться ',
                         'торговать '],
                     src_images=[]),
         parser.Card(word='handle',
                     pos='noun',
                     source='http://example.com',
                     src_uk_mp3='https://dictionary.cambridge.org/media/english-russian/uk_pron/u/ukh/ukhan/ukhandb022.mp3',
                     pron_uk='/ˈhændl/',
                     src_us_mp3='https://dictionary.cambridge.org/media/english-russian/us_pron/h/han/handl/handle.mp3',
                     pron_us='/ˈhændl/',
                     definitions=['the part of something that you use to hold it or open it'],
                     examples=[['a door handle ', 'the handle on a suitcase']],
                     ru=['ручка, рукоятка '],
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
                     definitions=['to lift something or someone by using your hands',
                                  'to collect someone who is waiting for you, or to collect something that you have left somewhere'],
                     examples=[['He picked his coat up off the floor.', ' Just pick up the phone and call him.'],
                               ['Can you pick me up from the airport?', " I've got to pick up those books I ordered."]],
                     ru=['поднимать, подбирать ', 'заезжать за кем-либо, забирать что-либо '],
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
                        definitions=['a part of an object designed for holding, moving, or '
                                     'carrying the object easily: ',
                                     'a name of a person or place, especially a strange one: ',
                                     'a name that someone is known by on some social media '
                                     'websites: '],
                        examples=[['a door handle',
                                   ' the handle on a suitcase',
                                   " I can't pick the kettle up - the handle's too hot.",
                                   'turn a handle She turned the handle and slowly opened the '
                                   'door.'],
                                  ["That's some handle to go through life with!"],
                                  ['On this site, handles start with an @ sign.',
                                   ' You can follow the team under the handle @ManUtd.']],
                        ru=[],
                        src_images=[
                            'https://dictionary.cambridge.org/images/full/handle_noun_002_17134.jpg?version=6.0.50']),
            parser.Card(word='handle',
                        pos='verb',
                        source='http://example.com',
                        src_uk_mp3='https://dictionary.cambridge.org/media/english/uk_pron/u/ukh/ukhan/ukhandb022.mp3',
                        pron_uk='/ˈhæn.dəl/',
                        src_us_mp3='https://dictionary.cambridge.org/media/english/us_pron/h/han/handl/handle.mp3',
                        pron_us='/ˈhæn.dəl/',
                        definitions=['to deal with, have responsibility for, or be in charge of: ',
                                     'to pick something up and touch, hold, or move it with your '
                                     'hands: ',
                                     'to operate or control something that could be difficult or '
                                     'dangerous: '],
                        examples=[['I thought he handled the situation very well.',
                                   ' Some people are brilliant with computers, but have no idea '
                                   'how to handle (= behave with) other people.',
                                   " If you can't handle the job I'll get someone else to do it.",
                                   ' Who handles the marketing in your company?'],
                                  ['Always wash your hands before handling food.',
                                   " Please don't handle the vases - they're very fragile."],
                                  ['Have you ever handled a gun before?']],
                        ru=[],
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
