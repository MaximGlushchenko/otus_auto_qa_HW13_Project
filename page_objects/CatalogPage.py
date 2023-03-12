from random import choice
from UI_tests_data import catalog_section
from page_objects.MainPage import MainPage


class CatalogPage(MainPage):
	endpoint = f"/{choice(catalog_section)}"

