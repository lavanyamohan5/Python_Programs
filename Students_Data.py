import pandas as pd 
Students = { "Name" : ["Lavanya","Kaviya","Manasa","Gunasree","Hamsavardhini","Chandru","Sanjay","Chaithanya","Ragul","Sriram","Jagan"],
             "Department" : ["CSE","IT","CSE","CSE","IT","CSE","CSE","IT","IT","IT","CSE"],
             "Reg_No" : [7,36,3,24,23,41,47,27,40,1,21],
             "CGPA" : [8.3,8.9,8.5,7.3,8.3,7.8,8.1,8.2,7.5,7.4,8.2]
             }
df = pd.DataFrame(Students)

excel_filename = "Student_database.xlsx"
df.to_excel(excel_filename, index = False)
print(f"Data saved successfully to {excel_filename}")

df_read = pd.read_excel(excel_filename)
print("Data retrieved from Excel: ")
print(df_read)


