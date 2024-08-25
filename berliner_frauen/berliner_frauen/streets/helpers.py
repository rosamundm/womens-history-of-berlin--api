def slugify_umlauts(slug: str) -> str:
    umlaut_map = {
            ord("ä"): "ae",
            ord("Ä"): "ae",
            ord("ö"): "oe",
            ord("Ö"): "oe",
            ord("ü"): "ue",
            ord("Ü"): "ue",
    }
    return slug.translate(umlaut_map).replace(" ", "-").casefold()
