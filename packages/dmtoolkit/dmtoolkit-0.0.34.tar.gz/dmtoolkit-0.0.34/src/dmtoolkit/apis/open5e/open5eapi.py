import requests
from slugify import slugify


class Open5e:
    base_url = "https://www.dnd5eapi.co"
    api_path = "api"
    endpoints = []

    @classmethod
    def get_resources(cls):
        endpoints = [
            f"{cls.base_url}/{cls.api_path}/{endpoint}" for endpoint in cls.endpoints
        ]
        resources = []
        for endpoint in endpoints:
            response = requests.get(endpoint)
            response.raise_for_status()
            resources += response.json().get("results")
        return resources

    @classmethod
    def all(cls):
        results = []
        for resource in cls.get_resources():
            if url := resource.get("url"):
                if not url.startswith(cls.base_url):
                    url = cls.base_url + url
                response = requests.get(url)
                response.raise_for_status()
                results.append(response.json())
        return results

    @classmethod
    def search(cls, term):
        results = []
        for obj in cls.get_resources():
            if slugify(term) in obj["url"].lower():
                results.append(cls.get(obj["url"]))
        return results

    @classmethod
    def get(cls, url):
        if not url.startswith(cls.base_url):
            url = cls.base_url + url
        print(url)
        result = requests.get(url).json()
        if "error" not in result:
            return result
        return []
