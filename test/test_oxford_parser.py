import os
import pytest
import requests

import parser

data = [
    (
        'oxford_en_handle.html',
        [
            parser.Card(word='handle',
                        pos='verb',
                        source='http://example.com',
                        src_uk_mp3='https://www.oxfordlearnersdictionaries.com/media/english/uk_pron/h/han/handl/handle__gb_1.mp3',
                        pron_uk='/ˈhændl/',
                        src_us_mp3='https://www.oxfordlearnersdictionaries.com/media/english/us_pron/h/han/handl/handle__us_2.mp3',
                        pron_us='/ˈhændl/',
                        definitions=['to deal with a situation, a person, an area of work or a strong emotion',
                                     'to touch, hold or move something with your hands',
                                     'to control a vehicle, an animal, a tool, etc.'],
                        examples=[['A new man was appointed to handle the crisis.', "She's very good at handling her patients.", 'to handle a situation/case', 'He decided to handle things himself.', 'This matter has been handled very badly.', 'The sale was handled by Adams Commercial.', 'We can handle up to 500 calls an hour at our new offices.', 'We all have to learn to handle stress.', "‘Any problems?’ ‘Nothing I can't handle.’", "I've got to go. I can't handle it any more (= deal with a difficult situation).", 'You have to know how to handle yourself in this business (= know the right way to behave).'],
                                  ['Our cat hates being handled.', 'The label on the box said: ‘Fragile. Handle with care.’'],
                                  ["I wasn't sure if I could handle such a powerful car.", "She's a difficult horse to handle."]], )

        ]
    ),
    (
        'oxford_am_en_handle.html',
        [
            parser.Card(word='handle',
                        pos='verb',
                        source='http://example.com',
                        src_uk_mp3=None,
                        pron_uk=None,
                        src_us_mp3='https://www.oxfordlearnersdictionaries.com/media/american_english/us_pron/h/han/handl/handle__us_1.mp3',
                        pron_us='NAmE//ˈhændl//',
                        definitions=['to deal with a situation, a person, an area of work, or a strong emotion',
                                     'to touch, hold, or move something with your hands',
                                     'to control a vehicle, an animal, a tool, etc.'],
                        examples=[['A new man was appointed to handle the crisis.', "She's very good at handling her patients.", 'The sale was handled by Adams Commercial.', 'We can handle up to 500 calls an hour at our new offices.', 'We all have to learn to handle stress.', 'This matter has been handled very badly.', "“Any problems?” “Nothing I can't handle.”", "I have to go. I can't handle it anymore (= deal with a difficult situation).", 'You have to know how to handle yourself in this business (= know the right way to behave).'],
                                  ['Our cat hates being handled.', 'The label on the box said: “Fragile. Handle with care.”'],
                                  ["I wasn't sure if I could handle such a powerful car.", "She's a difficult horse to handle."]],

                        )

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

    obj = parser.OxfordDict(word='test')
    # print('===========')
    for card in obj.cards:
        # print(card)
        assert card in answers