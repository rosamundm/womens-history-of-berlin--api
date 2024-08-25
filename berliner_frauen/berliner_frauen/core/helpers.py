def slugify_umlauts(str: str) -> str:
    umlaut_map = {
            ord("ä"): "ae",
            ord("Ä"): "ae",
            ord("ö"): "oe",
            ord("Ö"): "oe",
            ord("ü"): "ue",
            ord("Ü"): "ue",
    }
    return str.translate(umlaut_map).replace(" ", "-").casefold()
