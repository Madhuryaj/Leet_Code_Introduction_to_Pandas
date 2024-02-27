#2882. Drop Duplicate Rows
import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=['email'],keep='first')
  
####### ---------------------- ###########  

#2883. Drop Missing Data
import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset="name")

####### ---------------------- ###########     

#2884. Modify Columns
import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary']=employees['salary']*2
    return employees

####### ---------------------- ###########     

#2885. Rename Columns
import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students.rename(columns={'id':'student_id',"first":"first_name","last":"last_name","age":"age_in_years"},inplace=True)
    return students

####### ---------------------- ###########     

#886. Change Data Type
import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade']=students['grade'].astype(int)
    return students

####### ---------------------- ###########    

#2887. Fill Missing Data
import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity']=products['quantity'].fillna(0)
    return products
    

    
