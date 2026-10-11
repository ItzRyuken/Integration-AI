from chatbot import parse_property_request
properties = [
    {
        "id": 1,
        "title": "Apartment in Cainta",
        "location": "Cainta",
        "bedrooms": 2,
        "rent": 9500,
        "status": "approved"
    },
    {
        "id": 2,
        "title": "House in Cainta",
        "location": "Cainta",
        "bedrooms": 3,
        "rent": 15000,
        "status": "pending"
    },
    {
        "id": 3,
        "title": "Condo in Pasig",
        "location": "Pasig",
        "bedrooms": 2,
        "rent": 12000,
        "status": "approved"
    }
]
def search_properties(message):
    filters = parse_property_request(message)
    results = [
        p for p in properties
        if p["status"] == "approved"
        and (
            filters["bedrooms"] is None
            or p["bedrooms"] == filters["bedrooms"]
        )
        and (
            filters["max_rent"] is None
            or p["rent"] <= filters["max_rent"]
        )
        and (
            filters["location"] is None
            or filters["location"].lower() in p["location"].lower()
        )
    ]
    return results
if __name__ == "__main__":
    query = input("What property are you looking for? ")
    results = search_properties(query)
    if results:
        for p in results:
            print(
                f'{p["title"]} | {p["bedrooms"]} bedrooms | '
                f'PHP {p["rent"]:,}/month'
            )
    else:
        print("No approved properties match your search.")