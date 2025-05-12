import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse, quote, urljoin
from dataclasses import dataclass
import requests


LIMIT_OF_DEF = 3
LIMIT_OF_THE_SAME_WORDS = 3


@dataclass
class Card:

    word: str
    pos: str
    src_uk_mp3: str = None
    pron_uk: str = None
    src_us_mp3: str = None
    pron_us: str = None
    definitions: list = None
    examples: list = None
    ru: list = None
    src_images: list = None


class OxfordDict:
    """
    Grabber from Oxford Learners Dictionary.

    """
    dictionary = {'en': '/definition/english/',
                  'am-en': '/definition/american_english/'}
    url_parse = urlparse('https://www.oxfordlearnersdictionaries.com/')

    def __init__(self):
        self.soup = BeautifulSoup()
        self.cards = []

    def get_page_soup(self, word, driver, dictionary='am-en'):
        driver.get(self._make_url(word, dictionary))
        self.soup = BeautifulSoup(driver.page_source, "html.parser")

    def _make_url(self, word, dictionary):
        dict_url = urljoin(self.__class__.url_parse.geturl(),
                                        self.__class__.dictionary[dictionary])
        return urljoin(dict_url, quote(word))

    def make_cards(self):
        self._make_card()
        self._find_the_same_words()

    def _find_the_same_words(self):
        block_matches = self.soup.find('ul', attrs={'class': 'list-col'})

        items = block_matches.find_all('a')
        self.urls = []
        for item in items:
            if item.find('span', class_='arl1'):
                self.urls.append(item.get('href'))

        # print(self.urls)

    def _make_card(self):
        main_container = self.soup.find('div', {'class': 'main-container'})
        webtop = main_container.find('div', { 'class': 'top-container'})
        word = webtop.find(re.compile('^h')).get_text()
        pos = webtop.find('span', class_='pos').get_text()
        card = Card(word, pos)

        try:
            blok_uk = self.soup.find('div', title=re.compile("pronunciation English"))

            card.src_uk_mp3 = blok_uk.get('data-src-mp3')
            card.pron_uk = webtop.find('span', class_='phon').get_text(strip=True)
        except AttributeError:
            pass

        try:
            blok_us = self.soup.find('div', title=re.compile("pronunciation American"))
            card.src_us_mp3 = blok_us.get('data-src-mp3')
            card.pron_us = blok_us.parent.get_text(strip=True)
        except AttributeError:
            pass

        def has_li_and_id(tag):
            return tag.name == 'li' and tag.has_attr('id')

        blocks = main_container.find_all(has_li_and_id, limit=LIMIT_OF_DEF)
        card.definitions = []
        card.examples = []
        for block in blocks:

            definition = block.find('span', class_='def').get_text()

            card.definitions.append(definition)
            try:
                examples = [x.get_text() for x in block.find_all('span', class_='x')]
            except AttributeError:
                card.examples.append([])
            else:
                card.examples.append(examples)


        try:
            src_img = self.soup.find('img', class_='thumb').get('src')
            card.src_images = [src_img.replace('thumb', 'fullsize')]
        except AttributeError:
            pass

        self.cards.append(card)


class CambridgeDict:
    """
    Grabber from Cambridge Dictionary.

    """
    dictionary = {'en': '/dictionary/english/',
                  'en-ru': '/dictionary/english-russian/',}
    url_parse = urlparse('https://dictionary.cambridge.org/')

    def __init__(self):
        self.soup = BeautifulSoup()
        self.cards = []
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Cache-Control": "max-age=0"
        })

    def get_page_soup(self, word, dictionary='en'):
        response = self.fetch_with_redirects(self._make_url(word, dictionary))
        self.soup = BeautifulSoup(response.text, "html.parser")

    def _make_url(self, word, dictionary):
        dict_url = urljoin(self.__class__.url_parse.geturl(),
                                        self.__class__.dictionary[dictionary])
        return urljoin(dict_url, quote(word))

    def make_cards(self):

        first_dictionary = self.soup.find('div', {'class': 'pr dictionary'})
        if first_dictionary:
            # for a page of english dictionary
            body_elements = first_dictionary.find_all('div', {'class': "pr entry-body__el"},
                                               limit=LIMIT_OF_THE_SAME_WORDS)
        else:
            # for a page of english-russian dictionary
            body_elements = self.soup.find_all('div', { 'class': "pr entry-body__el"},
                                           limit=LIMIT_OF_THE_SAME_WORDS)

        self.cards = []

        if body_elements:
            # for general page
            for body_element in body_elements:
                self._make_card(body_element)
        else:
            # for a page with a phase verb
            body_element = self.soup.find('div', {'class': "pv-block"},)
            if body_element:
                self._make_card(body_element)

    def _make_card(self, element):
        """
        It creates a card from the element of the body.
        :param element: the element containing the coup with the header (word, part of speech, pronunciation)
        :return: it saves the card to the instance of class CambridgeDict
        """

        word = element.find('div', class_='di-title').get_text()
        pos = element.find('span', class_='pos dpos').get_text()
        card = Card(word, pos)

        try:
            blok_uk = element.find('span', string='uk').parent
            src_uk = blok_uk.find('source', type='audio/mpeg').get('src')
            card.src_uk_mp3 = CambridgeDict.url_parse._replace(path=src_uk).geturl()
            card.pron_uk = blok_uk.find('span', class_='pron dpron').get_text(strip=True)
        except AttributeError:
            pass

        try:
            blok_us = element.find('span', string='us').parent
            src_us = blok_us.find('source', type='audio/mpeg').get('src')
            card.src_us_mp3 = CambridgeDict.url_parse._replace(path=src_us).geturl()
            card.pron_us = blok_us.find('span', class_='pron dpron').get_text(strip=True)
        except AttributeError:
            pass

        if card.pron_us:
            card.pron_us = card.pron_uk

        # block contains the definition and the examples
        blocks = element.find_all('div', class_='def-block ddef_block', limit=LIMIT_OF_DEF)
        card.definitions = []
        card.examples = []
        card.ru = []
        for block in blocks:
            card.definitions.append(block.find('div', {'class': 'def ddef_d db'}).get_text())
            try:
                examps = block.find_all('div', class_='examp dexamp')
                examples = []
                for examp in examps:
                    examples.append(examp.get_text())
            except AttributeError:
                card.examples.append([])
            else:
                card.examples.append(examples)

            try:
                card.ru.append(block.find('span', {'lang': 'ru'}).get_text())
            except AttributeError:
                pass

        try:
            card.src_images = []
            parts = element.find_all('amp-img', class_='dimg_i hp')
            for part in parts:
                src = part.get('src')
                src_img = src.replace('thumb', 'full')
                card.src_images.append( CambridgeDict.url_parse._replace(path=src_img).geturl())
        except AttributeError:
            pass

        self.cards.append(card)

    def fetch_with_redirects(self, url: str, max_redirects: int = 10) -> requests.Response:
        """
        Fetch URL with manual redirect handling.

        """
        current_url = url

        for _ in range(max_redirects):
            response = self.session.get(current_url, allow_redirects=False)

            if response.status_code == 200:
                return response
            elif response.status_code in (301, 302, 303, 307, 308):
                location = response.headers.get('Location')
                if not location:
                    raise Exception("Redirect without Location header")

                if not urlparse(location).netloc:
                    current_url = urljoin(url, location)
                else:
                    current_url = location
                continue
            else:
                response.raise_for_status()

        raise Exception("Too many redirects")


class LanGeekDict:

    api_url = "https://api.langeek.co/v1/cs/en/word/"

    def __init__(self, word: str):

        self.cards = []
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Cache-Control": "max-age=0"
        })
        self.response_json = self.fetch_point(word)
        self.make_cards()

    def make_cards(self):
        """
        Create cards only with pictures
        :return: list of cards
        """
        for item in self.response_json:
            for pos in item["translations"].keys():
                for meaning in item["translations"][pos]:
                    try:
                        self.cards.append(Card(word=item["entry"],
                                               pos=pos,
                                               definitions=[meaning["translation"]],
                                               src_images=[meaning["wordPhoto"]["photoThumbnail"]]
                                               )
                                          )
                    except KeyError:
                        pass
                    except TypeError:
                        pass

    def fetch_point(self, word):
        response = self.session.get(self.__class__.api_url,
                                    params={"term": word,
                                            "filter": ",inCategory,photo"}
                                    )
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
