# Import necessary libraries
from drawranflow.models import Message, Identifiers
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Function to train, save, and load the Isolation Forest model
def train_save_load_model():
    try:
        queryset = Message.objects.values()
        t_df = pd.DataFrame.from_records(queryset)
        X_train, X_test = train_test_split(t_df, test_size=0.2, random_state=42)
        features_to_use = ['identifiers_id','uploaded_file_id']  

        # Train Isolation Forest model
        model = IsolationForest(n_estimators=100, max_samples='auto', contamination=float(.1),
                        max_features=1.0, bootstrap=False, n_jobs=-1, random_state=42, verbose=0)
        model.fit(t_df[features_to_use])
        joblib.dump(model, 'trained_model.joblib')
        print("Model trained and saved.")

        loaded_model = joblib.load('trained_model.joblib')
        pred = loaded_model.predict(t_df[features_to_use])
        t_df['anomaly'] = pred
        outliers = t_df.loc[t_df['anomaly'] < -0.7]

       # Save anomalies into the 'Identifiers' table
        for idx, row in outliers.iterrows():
           print(row)
           call_id = row['identifiers_id']
           file = row['uploaded_file_id']
           identifier_instance = Identifiers.objects.get(id=call_id,uploaded_file=file)
           # Update 'Identifiers' fields for anomalies
           identifier_instance.anomaly = True
           identifier_instance.save()
        print("Anomalies saved in the Identifiers table.")

    except Exception as e:
        print(e)


#
