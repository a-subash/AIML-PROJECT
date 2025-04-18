
import pandas as pd
import random
import faker
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

# Generate synthetic dataset
fake = faker.Faker()
data = []

for i in range(200):
    name = fake.name()
    phone = fake.phone_number()
    ip = f"192.168.{random.randint(0, 3)}.{random.randint(1, 255)}"
    promo_used = random.randint(1, 10)
    name_pattern_score = 1 if any(char.isdigit() for char in name) else 0
    ip_count = random.randint(1, 6) if random.random() > 0.7 else 1
    data.append([name, phone, ip, promo_used, name_pattern_score, ip_count])

df = pd.DataFrame(data, columns=['name', 'phone', 'ip_address', 'promo_used', 'name_pattern_score', 'ip_count'])

# Save dataset
df.to_csv("promo_code_dataset.csv", index=False)

# Feature selection and scaling
features = df[['promo_used', 'name_pattern_score', 'ip_count']]
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Apply Isolation Forest
model = IsolationForest(contamination=0.1, random_state=42)
df['fraud_score'] = model.fit_predict(scaled_features)
df['is_fraud'] = df['fraud_score'].apply(lambda x: 'Yes' if x == -1 else 'No')

# Save final output
df.to_csv("promo_code_fraud_output.csv", index=False)
print("Fraud detection completed. Output saved as 'promo_code_fraud_output.csv'")
