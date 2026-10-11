import re
def parse_property_request(message):
    text = message.lower()
    bedrooms_match = re.search(r"(\d+)\s*(?:bedrooms?|br|bed)", text)
    budget_match = re.search(
        r"(?:below|under|less than|budget of|maximum|max)\s*₱?\s*([\d,]+)",
        text
    )
    location_match = re.search(
        r"\bin\s+([a-zA-Z ]+?)(?=\s+(?:below|under|less|with|and)\b|$)",
        text
    )
    return {
        "bedrooms": int(bedrooms_match.group(1)) if bedrooms_match else None,
        "max_rent": (
            int(budget_match.group(1).replace(",", ""))
            if budget_match else None
        ),
        "location": location_match.group(1).strip() if location_match else None
    }
if __name__ == "__main__":
    query = input("Describe the property you want: ")
    result = parse_property_request(query)
    print("Interpreted search:")
    print(result)