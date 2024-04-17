import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
import pandas as pd
import numpy as np
from tensorflow import keras
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical

class FeatureMerger(BaseEstimator, TransformerMixin):
  def fit(self, X, y=None):
    return self
  
  def transform(self, X):
    df = pd.DataFrame()
    df['result'] = X.apply(lambda row: ' '.join(row.values.astype(str)), axis=1)
    return df['result']


numerical_transformer = Pipeline(steps=[
  ('imputer', SimpleImputer(strategy='median')),
  ('scaler', StandardScaler())
]) 

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

vectorized_transformer = Pipeline(steps=[
  ('merge', FeatureMerger()),
  ('vectorize', TfidfVectorizer(max_features=2000))
])

class PreprocessingModel:
  def __init__(self, model, pipeline, label_encoder):
    self.model = model
    self.pipeline = pipeline
    self.label_encoder = label_encoder
    
  def preprocess(self, X):
    return self.pipeline.transform(X)
    
  def decode_target(self, encoded_target):
    encoded_label_target = np.argmax(encoded_target, axis=1)
    return self.label_encoder.inverse_transform(encoded_label_target)
  
  def predict(self, X):
    X_prep = self.preprocess(X)
    y_pred = self.model.predict(X_prep)
    return self.decode_target(y_pred)

def process_data(df, target_column):
  if type(df) == str:
    df = pd.read_csv(df)
  df_train = df.sample(frac=0.7)
  df_valid = df.drop(df_train.index)
  le = LabelEncoder()
  y_train = to_categorical(le.fit_transform(df_train[target_column]))
  y_valid = to_categorical(le.transform(df_valid[target_column]))
  X_train = df_train.drop([target_column], axis=1)
  X_valid = df_valid.drop([target_column], axis=1)
  categorical_cols = [cname for cname in X_train.columns if X_train[cname].nunique() < 10 and  X_train[cname].dtype == "object"]
  vectorized_cols = [cname for cname in X_train.columns if X_train[cname].nunique() >= 10 and  X_train[cname].dtype == "object"]
  numerical_cols = [cname for cname in X_train.columns if X_train[cname].dtype in ['int64', 'float64']]
  preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols),
        ('vect', vectorized_transformer, vectorized_cols)
    ])
  pipeline = Pipeline(steps=[('preprocessor', preprocessor)])
  X_prep_train = pipeline.fit_transform(X_train)
  input_shape = [X_prep_train.shape[1]]
  X_prep_valid = pipeline.transform(X_valid)
  model = keras.Sequential([
    keras.layers.Input(input_shape),
    keras.layers.Dense(units=256, activation='relu'),
    keras.layers.BatchNormalization(),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(units=128, activation='relu'),
    keras.layers.BatchNormalization(),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(units=y_train.shape[1], activation='sigmoid'),
  ])
  model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
  early_stopping = keras.callbacks.EarlyStopping(
    patience=10,
    min_delta=0.001,
    restore_best_weights=True,
  )
  history = model.fit(
    X_prep_train, y_train, 
    validation_data=(X_prep_valid, y_valid), 
    batch_size=32, 
    epochs=100, 
    callbacks=[early_stopping],
  )
  history_df = pd.DataFrame(history.history)
  print(("Best Validation Loss: {:0.4f}" +\
      "\nBest Validation Accuracy: {:0.4f}")\
      .format(history_df['loss'].min(), 
              history_df['accuracy'].max()))
  return PreprocessingModel(model, pipeline, le)
