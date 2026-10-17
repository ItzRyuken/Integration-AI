from chatbot import parse_message
# Fictional data btw
properties = [
    {
        "property_id": 1,
        "title": "Cainta Apartment A",
        "location": "Cainta",
        "bedrooms": 2,
        "monthly_rent": 9500,
        "status": "approved"
    },
    {
        "property_id": 2,
        "title": "Cainta Family Home",
        "location": "Cainta",
        "bedrooms": 3,
        "monthly_rent": 15000,
        "status": "pending"
    },
    {
        "property_id": 3,
        "title": "Pasig Apartment B",
        "location": "Pasig",
        "bedrooms": 2,
        "monthly_rent": 12000,
        "status": "approved"
    },
    {
        "property_id": 4,
        "title": "Quezon City Studio",
        "location": "Quezon City",
        "bedrooms": 1,
        "monthly_rent": 6500,
        "status": "approved"
    }
]
def search_properties(message):
    criteria = parse_message(message)
    results = []
    for property in properties:
        if property["status"] != "approved":
            continue
        if (
            criteria["bedrooms"] is not None
            and property["bedrooms"] != criteria["bedrooms"]
        ):
            continue
        if (
            criteria["max_rent"] is not None
            and property["monthly_rent"] > criteria["max_rent"]
        ):
            continue
        if (
            criteria["location"] is not None
            and property["location"].lower()
            != criteria["location"].lower()
        ):
            continue
        results.append(property)
    return results
if __name__ == "__main__":
    message = "Find me a 3-bedroom property in Cainta under 10,000"
    print("Tenant message:", message)
    print("\nMatching approved properties:")
    results = search_properties(message)
    if results:
        for property in results:
            print(
                f'{property["title"]} | '
                f'{property["location"]} | '
                f'{property["bedrooms"]} bedrooms | '
                f'PHP {property["monthly_rent"]:,}/month'
            )
    else:
        print("No matching approved properties found.")