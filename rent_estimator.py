import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
# Temporary fictional rental data
data = {
    "bedrooms": [1, 2, 3, 1, 2, 3, 1, 2, 3, 2, 1, 3],
    "area_sqm": [25, 45, 70, 30, 50, 80, 28, 48, 75, 55, 32, 85],
    "location": [
        "Cainta", "Cainta", "Cainta",
        "Pasig", "Pasig", "Pasig",
        "Quezon City", "Quezon City", "Quezon City",
        "Cainta", "Pasig", "Quezon City"
    ],
    "rent": [
        5000, 9000, 14000, 6000, 10000, 16000,
        5500, 9500, 15000, 11000, 6500, 17000
    ]
}
df = pd.DataFrame(data)
print(df)
# Select input features and target
X = df[["bedrooms", "area_sqm", "location"]]
y = df["rent"]
# Split data for testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
print("Training data rows:", len(X_train))
print("Testing data rows:", len(X_test))

# Converting location names into numbers
preprocessor = ColumnTransformer(
    transformers=[
        ("location", OneHotEncoder(handle_unknown="ignore"), ["location"])
    ],
    remainder="passthrough"
)
# Build AI model
model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(
        n_estimators=100, random_state=42
    ))
])
# Train the model
model.fit(X_train, y_train)
print("Rent estimation model trained successfully!")
# Evaluate the model
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
print("Mean Absolute Error:", round(mae, 2), "PHP")
# Estimating monthly rent using property details
def estimate_rent(bedrooms, area_sqm, location):
    property_data = pd.DataFrame([{
        "bedrooms": bedrooms,
        "area_sqm": area_sqm,
        "location": location
    }])
    estimated_rent = model.predict(property_data)[0]
    return round(float(estimated_rent), 2)
# sample test
if __name__ == "__main__":
    rent = estimate_rent(2, 50, "Cainta")
    print("\nAI Rent Estimator - Prototype")
    print("Bedrooms: 2")
    print("Floor area: 50 sqm")
    print("Location: Cainta")
    print(f"Estimated monthly rent: PHP {rent:,.2f}")
    print(f"Test MAE: PHP {mae:,.2f}")
    print("Note: Uses fictional sample data.")