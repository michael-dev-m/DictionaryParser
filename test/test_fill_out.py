import parser

main_cards =      [
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

donor_cards =         [
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

modify_cards = [
    parser.Card(word='handle',
                pos='verb',
                source='http://example.com',
                src_uk_mp3='https://dictionary.cambridge.org/media/english-russian/uk_pron/u/ukh/ukhan/ukhandb022.mp3',
                pron_uk='/ˈhændl/',
                src_us_mp3='https://dictionary.cambridge.org/media/english-russian/us_pron/h/han/handl/handle.mp3',
                pron_us='/ˈhændl/',
                data=[{'definition': '{{c1::handle::verb}} - to deal with something',
                       'examples': ['He {{c1::handled}} the situation very well.',
                                    ' This office {{c1::handles}} thousands of enquiries '
                                    'every day.'],
                       'translate': 'иметь дело с чем-либо, справляться '},
                      {'definition': '{{c1::handle::verb}} - to touch, hold, or pick up '
                                     'something',
                       'examples': ['You must wash your hands before {{c1::handling}} '
                                    'food.'],
                       'translate': 'трогать, прикасаться '},
                      {'definition': '{{c1::handle::verb}} - to buy and sell goods',
                       'examples': ["He's been charged with {{c1::handling}} stolen "
                                    'goods.'],
                       'translate': 'торговать '}],
                src_images=[]),
    parser.Card(word='handle',
                pos='noun',
                source='http://example.com',
                src_uk_mp3='https://dictionary.cambridge.org/media/english-russian/uk_pron/u/ukh/ukhan/ukhandb022.mp3',
                pron_uk='/ˈhændl/',
                src_us_mp3='https://dictionary.cambridge.org/media/english-russian/us_pron/h/han/handl/handle.mp3',
                pron_us='/ˈhændl/',
                data=[{'definition': '{{c1::handle::noun}} - the part of something that '
                                     'you use to hold it or open it',
                       'examples': ['a door {{c1::handle}} ',
                                    'the {{c1::handle}} on a suitcase'],
                       'translate': 'ручка, рукоятка '}],
                src_images=['https://dictionary.cambridge.org/images/full/handle_noun_002_17134.jpg?version=6.0.50'])

]

def test_add_img():
    for main_card in main_cards:
        main_card.cloze_anki()
        for donor_card in donor_cards:
            main_card.add_images_equal_pos(donor_card)
    for card in main_cards:
        assert card in modify_cards
