# Packages required
import pandas as pd

# Create data frame from csv and print column names
read_csv = pd.read_csv('../csv/US Monthly Air Passengers.csv')
csv_df = pd.DataFrame(read_csv)
print(csv_df.columns)


# Create list of Origin Airports
origin = []
for x in csv_df['ORIGIN']:
    origin.append(x)
# Clear duplicate value from list
Origin = [*set(origin)]
