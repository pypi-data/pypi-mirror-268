import fnmatch

from finter import BaseAlpha
from finter.api.content_api import ContentApi
from finter.data.content_model.catalog_sheet import get_data
from finter.settings import logger


class ContentFactory:
    """
    A class representing a content model (CM) factory that generates and manages content models
    based on a specified universe name and a time range.

    Attributes:
        start (int): Start date for the content in YYYYMMDD format.
        end (int): End date for the content in YYYYMMDD format.
        universe_name (str): Name of the universe to base content models on.
        match_list (list[str]): Patterns used to match content models based on the universe name.
        cm_dict (dict[str, list[str]]): Dictionary mapping content match patterns to lists of corresponding content model names.

    Methods:
        get_df(item_name: str) -> pd.DataFrame:
            Retrieves the DataFrame associated with a specified item name.
        get_full_cm_name(item_name: str) -> str:
            Retrieves the full content model name for a specified item name.
        determine_base() -> list[str]:
            Determines the base match patterns for content models based on the universe name.
        get_cm_dict() -> dict:
            Generates the content model dictionary based on the universe's match list.
        show():
            Displays an interactive widget for exploring content model information in a scrollable list format.

    Property:
        item_list (list[str]): Provides a sorted list of unique item names from the content model dictionary.
    """

    def __init__(self, universe_name: str, start: int, end: int):
        """
        Initializes the ContentFactory with the specified universe name, start date, and end date.

        Args:
            universe_name (str): The name of the universe which the content models are based on.
                Example: 'raw', 'kr_stock'.
            start (int): The start date for the content in YYYYMMDD format.
                Example: 20210101.
            end (int): The end date for the content in YYYYMMDD format.
                Example: 20211231.

        Raises:
            ValueError: If the universe name is not supported.
        """
        self.start = start
        self.end = end
        self.universe_name = universe_name

        self.match_list = self.determine_base()
        self.cm_dict = self.get_cm_dict()

    # Todo: check generate dependency when submit alpha
    def get_df(self, item_name):
        cm_name = self.get_full_cm_name(item_name)
        return BaseAlpha.get_cm(cm_name).get_df(self.start, self.end)

    # Todo: Dealing duplicated item name later
    def get_full_cm_name(self, item_name):
        if self.universe_name == "raw":
            return item_name

        try:
            return next(
                key.replace("*", item_name)
                for key, items in self.cm_dict.items()
                if item_name in items
            )
        except StopIteration:
            raise ValueError(f"Unknown item_name: {item_name}")

    # Todo: Migrate universe with db or gs sheet or ...
    def determine_base(self):
        if self.universe_name == "raw":
            return []
        elif self.universe_name == "kr_stock":
            df = get_data()
            l = list(df[df["Universe"] == "KR STOCK"]["Object Path"])
            return l
        else:
            raise ValueError(f"Unknown universe: {self.universe_name}")

    def get_cm_dict(self):
        if self.universe_name == "raw":
            return {}

        api_instance = ContentApi()
        cm_dict = {}
        for match in self.match_list:
            category = match.split(".")[3]
            try:
                cm_list = api_instance.content_identities_retrieve(
                    category=category
                ).cm_identity_name_list
                net_cm_list = [
                    item.split(".")[4]
                    for item in cm_list
                    if fnmatch.fnmatchcase(item, match)
                ]
                cm_dict[match] = net_cm_list
            except Exception as e:
                logger.error(f"API call failed: {e}")
        return cm_dict

    def show(self):
        from IPython.display import HTML, display
        from ipywidgets import interact

        key_mapping = {key.split(".")[3]: key for key in self.cm_dict.keys()}

        def show_key_info(category):
            original_key = key_mapping[category]
            value = self.cm_dict[original_key]
            scrollable_list = (
                '<div style="height:200px;width:600px;border:1px solid #ccc;overflow:auto;">'
                + "<ul>"
                + "".join(f"<li>{item}</li>" for item in value)
                + "</ul></div>"
            )
            display(HTML(f"<h3>{category}</h3>" + scrollable_list))

        simplified_keys = list(key_mapping.keys())

        interact(show_key_info, category=simplified_keys)

    @property
    def item_list(self):
        return sorted(
            set(item for sublist in self.cm_dict.values() for item in sublist)
        )
