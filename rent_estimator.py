import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
# Temporary sample rental data testing
data = {
    "bedrooms": [1, 2, 3, 1, 2, 3, 1, 2, 3, 2, 1, 3],
    "area_sqm": [25, 45, 70, 30, 50, 80, 28, 48, 75, 55, 32, 85],
    "rent": [5000, 9000, 14000, 6000, 10000, 16000,
             5500, 9500, 15000, 11000, 6500, 17000]
}
df = pd.DataFrame(data)
print(df)
# Features and target rent
X = df[["bedrooms", "area_sqm"]]
y = df["rent"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
print("Training data rows:", len(X_train))
print("Testing data rows:", len(X_test))
# Rent estimation model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print("Rent estimation model trained successfully!")
# Evaluating predictions
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
print("Mean Absolute Error:", round(mae, 2), "PHP")
# Monthly estimated rate
def estimate_rent(bedrooms, area_sqm):
    property_data = pd.DataFrame([{
        "bedrooms": bedrooms,
        "area_sqm": area_sqm
    }])

    estimated_rent = model.predict(property_data)[0]
    return round(estimated_rent, 2)
# Run a sample estimate when this file is executed directly
if __name__ == "__main__":
    rent = estimate_rent(2, 50)

    print("\nAI Rent Estimator — Prototype")
    print("Bedrooms: 2")
    print("Floor area: 50 sqm")
    print(f"Estimated monthly rent: PHP {rent:,.2f}")
    print(f"Test MAE: PHP {mae:,.2f}")
    print("Note: Uses fictional sample data.")