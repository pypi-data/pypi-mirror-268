import requests


class Open5e:
    base_url = "https://www.dnd5eapi.co"
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
            if any(term in obj["name"].lower() for term in terms):
                resource = obj["url"].split("/")[1]
                results.append(cls.get(index=obj["index"], resource=resource))
        return results

    @classmethod
    def get(cls, index, resource=None):
        if resource is None:
            urls = [f"{endpoint}/{index}" for endpoint in cls.get_endpoints()]
        else:
            urls = [f"{cls.base_url}/{cls.api_path}/{resource}/{index}"]
        print(urls)
        for endpoint in urls:
            result = requests.get(endpoint).json()
            if "error" not in result:
                return result
        return []
