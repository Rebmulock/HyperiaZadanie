from page_parser import PageParser
import json

def main():
    parser = PageParser("https://www.prospektmaschine.de/hypermarkte/")

    data = parser.extract_data()

    with open("brochures.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()