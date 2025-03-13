import requests

from brochure import Brochure
from datetime import datetime
from bs4 import BeautifulSoup, Tag


class PageParser:
    def __init__(self, url):
        self.url = url

    def _parse_html(self):
        try:
            response = requests.get(self.url)

            response.raise_for_status()

            return response.text

        except requests.exceptions.HTTPError as err:
            print(err)

    def extract_data(self):
        res = self._parse_html()
        parse_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        soup = BeautifulSoup(res, "html.parser")
        page_wrapper = soup.find("div", class_="row row-flex")
        brochure_thumbs = page_wrapper.find_all("div", class_="brochure-thumb")

        brochures = []

        for brochure in brochure_thumbs:
            picture = brochure.find("picture")
            img = picture.find("img")
            content = brochure.find_all("p", class_="grid-item-content")

            title = None
            valid_from = None
            valid_to = None

            for tag in content:
                for child in tag.children:
                    if isinstance(child, Tag) and not child.get("class"):
                        title = child.text

                    else:
                        if isinstance(child, Tag) and child.get("class")[0] != "visible-sm":
                            if " - " in child.text:
                                date_str = child.text.split(" - ")

                                first_date = datetime.strptime(date_str[0], "%d.%m.%Y")
                                valid_from = first_date.strftime("%Y-%m-%d")

                                second_date = datetime.strptime(date_str[1], "%d.%m.%Y")
                                valid_to = second_date.strftime("%Y-%m-%d")
                            else:
                                valid_from = child.text

            # Niektore brozury pouzivaju lazy loading, niektore nie
            thumbnail = img.get("src") or img.get("data-src")

            #Nazov obchodu nie je explicitne pouzity
            #Kod predpoklada ze alt text obrazku bude vzdy popisovat nazov obchodu
            shop_name = brochure.find("img", alt=lambda x: x and "Logo" in x).get("alt").split(" ")[1]

            brochures.append(Brochure(title, thumbnail, shop_name, valid_from, valid_to, parse_time).__dict__)

        return brochures