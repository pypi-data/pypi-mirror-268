import requests


class Open5e:
    base_url = "   https://api.open5e.com"
    api_path = "api"
    endpoints = []

    @classmethod
    def get_endpoints(cls):
        return [
            f"{cls.base_url}/{cls.api_path}/{endpoint}" for endpoint in cls.endpoints
        ]

    @classmethod
    def all(cls, endpoint=None):
        results = []
        for endpoint in cls.get_endpoints():
            response = requests.get(endpoint)
            response.raise_for_status()
            response = response.json()
            results += response["results"]
        return results

    @classmethod
    def search(cls, terms):
        # split into tokens if possible
        if isinstance(terms, str):
            terms = terms.split()
        # ensure the terms are a list
        if not isinstance(terms, list):
            terms = [terms]
        results = []
        for obj in cls.all():
            if any(term.lower() in obj["url"].lower() for term in terms):
                results.append(cls.get(obj["url"]))
        return results

    @classmethod
    def get(cls, url):
        result = requests.get(url).json()
        if "error" not in result:
            return result
        return []
