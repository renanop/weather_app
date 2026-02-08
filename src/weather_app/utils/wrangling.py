import pandas as pd

def join_column_text(col:pd.Series, sep:str=",") -> str:

    # Transform col to string type and then put it in a list
    col = col.astype(str).tolist()

    # Join list as a string separated by ","
    joint_lst = ",".join(col)

    return joint_lst
