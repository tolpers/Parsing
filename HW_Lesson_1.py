import json
from parse_5ka import Parse5ka

class CategoriesParser(Parse5ka):
    def __init__(self, cat_url, *args, **kwargs):
        self.cat_url = cat_url
        super.cat_url = cat_url

    def _get_cat(self):
        response = self._get_response(self.cat_url)
        data = response.json()
        return data

    def run(self):
        for cat in self._get_cat():
            cat["products"] = []
            params = f"?categories={cat['parent_group_cpde']}"
            url = f"{self.start_url}{params}"
            cat["products"].extend(list(self._parse(url)))
            file_name = f"{car['parent_group_cpde']}.json"
            cat_path = self.save_path.joinpath(file_name)
            self._save(cat, cat_path)

def get_save_path(dir_name):
    save_path = path(__file__).parent.joinpath(dir_name)
    if not save_path.exists():
        save_path.mkdir()
        return save_path

if __name__ == "__main__":
    url = "https://5ka.ru/api/v2/special_offers/"
    cat_url = "https://5ka.ru/api/v2/categories/"