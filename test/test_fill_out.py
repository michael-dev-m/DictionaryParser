import parser

main_cards = [
    parser.Card(word='handle',
                pos='verb',
                source='http://test.com',
                src_uk_mp3='https://dictionary.cambridge.org/media/english-russian/uk_pron/u/ukh/ukhan/ukhandb022.mp3',
                pron_uk='/ˈhændl/',
                src_us_mp3='https://dictionary.cambridge.org/media/english-russian/us_pron/h/han/handl/handle.mp3',
                pron_us=None,
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
                src_images=[]
                ),
    parser.Card(word='handle',
                pos='noun',
source='http://test.com',
                src_uk_mp3='https://dictionary.cambridge.org/media/english-russian/uk_pron/u/ukh/ukhan/ukhandb022.mp3',
                pron_uk='/ˈhændl/',
                src_us_mp3='https://dictionary.cambridge.org/media/english-russian/us_pron/h/han/handl/handle.mp3',
                pron_us=None,
                definitions=['the part of something that you use to hold it or open it'],
                examples=[['a door handle ', 'the handle on a suitcase']],
                ru=['ручка, рукоятка '],
                src_images=[]
                )
]

donor_cards = [
    parser.Card(word='handle',
                pos='noun',
                source='http://test.com',
                src_uk_mp3='https://dictionary.cambridge.org/media/english/uk_pron/u/ukh/ukhan/ukhandb022.mp3',
                pron_uk='/ˈhæn.dəl/',
                src_us_mp3='https://dictionary.cambridge.org/media/english/us_pron/h/han/handl/handle.mp3',
                pron_us='/ˈhæn.dəl/',
                definitions=[],
                examples=[],
                ru=[],
                src_images=['https://dictionary.cambridge.org/images/full/handle_noun_002_17134.jpg?version=6.0.50']),
    parser.Card(word='handle',
                pos='verb',
                source='http://test.com',
                src_uk_mp3='https://dictionary.cambridge.org/media/english/uk_pron/u/ukh/ukhan/ukhandb022.mp3',
                pron_uk='/ˈhæn.dəl/',
                src_us_mp3='https://dictionary.cambridge.org/media/english/us_pron/h/han/handl/handle.mp3',
                pron_us='/ˈhæn.dəl/',
                definitions=[],
                examples=[],
                ru=[],
                src_images=[])
]

modify_cards = [
    parser.Card(word='handle', pos='verb', source='http://test.com',
                src_uk_mp3='https://dictionary.cambridge.org/media/english-russian/uk_pron/u/ukh/ukhan/ukhandb022.mp3',
                pron_uk='/ˈhændl/',
                src_us_mp3='https://dictionary.cambridge.org/media/english-russian/us_pron/h/han/handl/handle.mp3',
                pron_us='/ˈhæn.dəl/',
                definitions=['{{c1::handle::verb}} - to deal with something',
                             '{{c1::handle::verb}} - to touch, hold, or pick up something',
                             '{{c1::handle::verb}} - to buy and sell goods'],
                examples=[
                    ['He {{c1::handled}} the situation very well.',
                     ' This office {{c1::handles}} thousands of enquiries every day.'],
                    ['You must wash your hands before {{c1::handling}} food.'],
                    ["He's been charged with {{c1::handling}} stolen goods."]],
                ru=['иметь дело с чем-либо, справляться ', 'трогать, прикасаться ', 'торговать '], src_images=[]),
    parser.Card(word='handle', pos='noun', source='http://test.com',
                src_uk_mp3='https://dictionary.cambridge.org/media/english-russian/uk_pron/u/ukh/ukhan/ukhandb022.mp3',
                pron_uk='/ˈhændl/',
                src_us_mp3='https://dictionary.cambridge.org/media/english-russian/us_pron/h/han/handl/handle.mp3',
                pron_us='/ˈhæn.dəl/',
                definitions=['{{c1::handle::noun}} - the part of something that you use to hold it or open it'],
                examples=[['a door {{c1::handle}} ', 'the {{c1::handle}} on a suitcase']], ru=['ручка, рукоятка '],
                src_images=['https://dictionary.cambridge.org/images/full/handle_noun_002_17134.jpg?version=6.0.50'])

]

def test_add_img():
    for main_card in main_cards:
        main_card.cloze_anki()
        for donor_card in donor_cards:
            main_card.add_images_equal_pos(donor_card)
            main_card.fill_out_pron_us(donor_card)
    for card in main_cards:
        assert card in main_cards
