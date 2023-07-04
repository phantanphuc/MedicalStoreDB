import openpyxl

# Create a workbook object
workbook = openpyxl.Workbook()

# Select the active worksheet
worksheet = workbook.active

# Write some data into the worksheet
worksheet['A1'] = 'Hello'
worksheet['B1'] = 'World!'

# Save the workbook
workbook.save('example.xlsx')



