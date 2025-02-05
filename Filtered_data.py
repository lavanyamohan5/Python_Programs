import pandas as pd

df = pd.read_excel(r"Student_database.xlsx")
filtered_df = df[df["CGPA"]>8]

new_excel_filename = "filtered_data.xlsx"
filtered_df.to_excel(new_excel_filename, index = False)
print(f"Filtered data saved to {new_excel_filename}")

print("Filtered Data: ")
print(filtered_df)

#Make the filtered Database as dataframe..
df = pd.read_excel(r"Filtered_data.xlsx")
print(df)
