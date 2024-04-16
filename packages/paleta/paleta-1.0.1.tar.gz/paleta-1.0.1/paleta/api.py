import requests


class LospecAPI:
    """
    Lospec API (https://lospec.com/palettes/api)
    """

    URL_STRUCTURE = "https://Lospec.com/{api}/{palette}.{fmt}"
    PALETTE_API = "palette-list"

    @staticmethod
    def get_palette(name: str, fmt: str = "json") -> dict:
        return requests.get(
            LospecAPI.URL_STRUCTURE.format(
                api=LospecAPI.PALETTE_API,
                palette=name,
                fmt=fmt
            )
        ).json()

    @staticmethod
    def is_error_message(resp: dict):
        return 'error' in resp

