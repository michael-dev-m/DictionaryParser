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
                examples=[],
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


def test_add_img():
    for main_card in main_cards:
        for donor_card in donor_cards:
            main_card.add_images_equal_pos(donor_card)
            main_card.fill_out_pron_us(donor_card)
    print('answer')
    for card in main_cards:
        print(card)

