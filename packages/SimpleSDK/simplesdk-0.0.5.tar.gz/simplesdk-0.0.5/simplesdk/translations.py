import requests


def translation(json_url):
    file = requests.get(json_url).json()
    return file


def language(translation: dict, lang: str):
    d = dict(translation["translations"][lang])

    def get(key):
        return d.get(key, key + "***")

    return get
