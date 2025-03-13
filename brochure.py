class Brochure:
    """ A class representing a brochure.

    Attributes:
        title (str): The title of the brochure.
        thumbnail (str): The link of the brochure thumbnail picture.
        shop_name (str): The name of the shop.
        valid_from (str): The date the brochure is valid from.
        valid_to (str): The date the brochure is valid until.
        parsed_time (str): The time the brochure was parsed.
    """

    def __init__(self, title, thumbnail, shop_name, valid_from, valid_to, parsed_time):
        """Constructor

        Args:
            title (str): The title of the brochure.
            thumbnail (str): The link of the brochure thumbnail picture.
            shop_name (str): The name of the shop.
            valid_from (str): The date the brochure is valid from.
            valid_to (str): The date the brochure is valid until.
            parsed_time (str): The time the brochure was parsed.

        """

        self.title = title
        self.thumbnail = thumbnail
        self.shop_name = shop_name
        self.valid_from = valid_from
        self.valid_to = valid_to
        self.parsed_time = parsed_time