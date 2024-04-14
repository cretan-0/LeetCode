import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    z = pd.DataFrame(employees)
    return z.loc[[0,1,2]]
