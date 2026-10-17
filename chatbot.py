import re
def parse_message(message):
    text = message.lower()
    bedrooms_match = re.search(
        r"(\d+)\s*[- ]?\s*bed(?:room)?s?",
        text
    )
    budget_match = re.search(
        r"(?:under|below|budget(?: of)?|maximum|max(?:imum)?(?: budget)?|less than)\s*₱?\s*([\d,]+)",
        text
    )
    location_match = re.search(
        r"\b(?:in|at|near)\s+(Cainta|Pasig|Quezon City)\b",
        message,
        re.IGNORECASE
    )
    bedrooms = (
        int(bedrooms_match.group(1))
        if bedrooms_match else None
    )
    max_rent = (
        int(budget_match.group(1).replace(",", ""))
        if budget_match else None
    )
    location = (
        location_match.group(1)
        if location_match else None
    )
    return {
        "bedrooms": bedrooms,
        "max_rent": max_rent,
        "location": location
    }
if __name__ == "__main__":
    message = "Find me a 2-bedroom property in Cainta under 12,000"
    print(parse_message(message))