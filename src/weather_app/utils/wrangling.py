import pandas as pd

def join_column_text(col:pd.Series, sep:str=",") -> str:
    """ Transforms a pandas Series to a string of values separated by a separator.

    Args:
        col (pd.Series): The column to be joined.
        sep (str, optional): The separator to use. Defaults to ",".

    Returns:
        str: A string with all values from the series separated by 'sep'.
    """

    # Transform col to string type and then put it in a list
    col = col.astype(str).tolist()

    # Join list as a string separated by ","
    joint_lst = sep.join(col)

    return joint_lst
