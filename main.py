# ==========================================
# Used Car Price Prediction - Regression
# ==========================================

# Import Libraries
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score


# ==========================================
# Load Dataset
# ==========================================

def load_data():
    data = pd.read_csv("cars_sampled.csv")
    print("Dataset Loaded:", data.shape)
    return data


# ==========================================
# Data Cleaning
# ==========================================

def clean_data(data):
    # Remove unrealistic years
    data = data[(data['yearOfRegistration'] >= 1950) &
                (data['yearOfRegistration'] <= 2018)]

    # Remove extreme values
    data = data[(data['price'] >= 100) & (data['price'] <= 150000)]
    data = data[(data['powerPS'] >= 10) & (data['powerPS'] <= 500)]

    print("After Cleaning:", data.shape)
    return data


# ==========================================
# Feature Engineering
# ==========================================

def feature_engineering(data):
    # Convert month to fraction
    data['monthOfRegistration'] = data['monthOfRegistration'] / 12

    # Create Age
    data['Age'] = (2018 - data['yearOfRegistration']) + data['monthOfRegistration']

    # Drop original columns
    data = data.drop(['yearOfRegistration', 'monthOfRegistration'], axis=1)

    print("Feature Engineering Done")
    return data


# ==========================================
# Drop Irrelevant Columns
# ==========================================

def drop_columns(data):
    data = data.drop(['seller', 'offerType', 'abtest', 'name'], axis=1)
    print("Dropped unnecessary columns")
    return data


# ==========================================
# Encoding
# ==========================================

def encode_data(data):
    data = pd.get_dummies(data, drop_first=True)
    print("Encoding Done")
    return data


# ==========================================
# Train Models
# ==========================================

def train_models(data):
    X = data.drop('price', axis=1)
    y = np.log1p(data['price'])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # Linear Regression
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    y_pred_lr = lr.predict(X_test)

    # Random Forest
    rf = RandomForestRegressor(n_estimators=200, random_state=42)
    rf.fit(X_train, y_train)
    y_pred_rf = rf.predict(X_test)

    return y_test, y_pred_lr, y_pred_rf


# ==========================================
# Evaluation
# ==========================================

def evaluate_model(y_test, y_pred, model_name):
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    print(f"\n{model_name} Performance:")
    print("MSE:", round(mse, 4))
    print("RMSE:", round(rmse, 4))
    print("R2 Score:", round(r2, 4))


# ==========================================
# Main Function
# ==========================================

def main():
    data = load_data()
    data = clean_data(data)
    data = feature_engineering(data)
    data = drop_columns(data)
    data = encode_data(data)

    y_test, y_pred_lr, y_pred_rf = train_models(data)

    evaluate_model(y_test, y_pred_lr, "Linear Regression")
    evaluate_model(y_test, y_pred_rf, "Random Forest")


# ==========================================
# Run Script
# ==========================================

if __name__ == "__main__":
    main()