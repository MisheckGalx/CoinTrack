from flask import url_for

def safe_url(endpoint, **values):
    """
    Return the URL for an endpoint if it exists, otherwise return '#'.
    Useful for templates to avoid 500 errors for missing routes.
    """
    try:
        return url_for(endpoint, **values)
    except Exception:
        return "#"


def human_readable_format(value):
    """
    Format numbers in a human-readable way.
    Floats: two decimals, Integers: spaces for thousands.
    """
    if value is None:
        return value
    if isinstance(value, float):
        return f"{value:.2f}"
    if isinstance(value, int):
        return f"{value:,}".replace(",", " ")
    return value


def human_readable_money_format(value):
    """
    Format numbers as currency.
    Floats: two decimals with dollar sign, Integers: spaces for thousands.
    """
    if value is None:
        return value
    if isinstance(value, float):
        return f"${value:,.2f}".replace(",", " ")
    if isinstance(value, int):
        return f"${value:,}".replace(",", " ")
    return value


def human_readable_percentage_format(value):
    """
    Format numbers as percentages.
    Floats: two decimals + %, Integers: spaces for thousands + %.
    """
    if value is None:
        return value
    if isinstance(value, float):
        return f"{value:.2f}%"
    if isinstance(value, int):
        return f"{value:,}".replace(",", " ") + "%"
    return value
