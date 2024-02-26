#2880. Select Data

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
   return students[students['student_id']==101][['name','age']]


#2881 Create a new column

import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus']=2*employees['salary']
    return employees
    
