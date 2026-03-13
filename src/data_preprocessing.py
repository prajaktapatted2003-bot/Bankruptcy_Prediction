import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.impute import SimpleImputer


def load_data(path):
    df = pd.read_csv(path)
    return df


def clean_data(df):

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Fill missing values
    for col in df.columns:
        if df[col].dtype in ['float64', 'int64']:
            df[col].fillna(df[col].mean(), inplace=True)
        else:
            df[col].fillna(df[col].mode()[0], inplace=True)

    return df


def encode_categorical(df):

    label_enc = LabelEncoder()

    for col in df.select_dtypes(include=['object']).columns:
        df[col] = label_enc.fit_transform(df[col])

    return df


def scale_features(df, target_col='class'):

    X = df.drop(columns=[target_col])
    y = df[target_col]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_scaled = pd.DataFrame(X_scaled, columns=X.columns)

    return X_scaled, y


def feature_selection(X, y, k=4):

    selector = SelectKBest(score_func=f_classif, k=k)
    X_selected = selector.fit_transform(X, y)

    selected_features = X.columns[selector.get_support()]

    X_selected = pd.DataFrame(X_selected, columns=selected_features)

    return X_selected, y