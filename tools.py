from ddgs import DDGS


# TOOL 1 — General Web Search
def web_search(query):

    results = []

    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=5):
            title = r.get("title", "")
            body = r.get("body", "")

            results.append(f"{title} - {body}")

    return "\n".join(results)


# TOOL 2 — Hotel Search
def hotel_search(destination):

    query = f"best hotels in {destination} with price per night"

    results = []

    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=5):
            title = r.get("title", "")
            body = r.get("body", "")

            results.append(f"{title} - {body}")

    return "\n".join(results)


# TOOL 3 — Tourist Activity Search
def activity_search(destination):

    query = f"top tourist attractions in {destination}"

    results = []

    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=5):
            title = r.get("title", "")
            body = r.get("body", "")

            results.append(f"{title} - {body}")

    return "\n".join(results)


# TOOL 4 — Safe Calculator
def calculator(expression):

    allowed_chars = "0123456789+-*/(). "

    if not all(c in allowed_chars for c in expression):
        return "Invalid expression"

    try:
        result = eval(expression)
        return str(result)

    except:
        return "Calculation error"