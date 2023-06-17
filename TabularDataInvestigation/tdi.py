import pandas as pd
import numpy as np


def find_index_for_null_values(df, return_type = 'dataframe'):
    response = pd.DataFrame()
    for col in df.columns:
        if df[df[col].isnull()].shape[0] > 0:
            response[col] = [df[df[col].isnull()].index.tolist()]
    if return_type == 'json': 
        return response.to_json(orient="records")
    if return_type == 'dataframe':
        return response
    else:
        return 'invalid return type'
    
def check_error_data_types(df, return_type = 'dataframe'):
    #make the response dataframe
    response = pd.DataFrame(columns = ['columns', 'error_data','error_index'])
    #make a list of categorical column name
    category_col_list = df.select_dtypes(exclude='number').columns


    for col in category_col_list:
        #take the selected categorical column values
        select_one_col_values = df[col].copy()
        #make a dataframe with that values and transpose them column name will be 0 to n
        temp_df = pd.DataFrame(select_one_col_values).T.reset_index(drop=True)
        #try to convert them in numeric each transposed columns
        temp_df_changed_type = temp_df.apply(pd.to_numeric, errors='ignore')
        #check if there is any category in numeric column
        if len(temp_df_changed_type.select_dtypes(include='number').columns) > 0:
            indexes_of_errors = temp_df_changed_type.select_dtypes(exclude='number').columns

            if len(np.unique(temp_df[indexes_of_errors].values)) <= (select_one_col_values.nunique() / 3):
                error_data = np.unique(temp_df[indexes_of_errors].values)
                response.loc[col] = [col, error_data, indexes_of_errors.values]



    if return_type == 'json':
        return response.to_json(orient="records")
    if return_type == 'dataframe':
        response.reset_index(drop=True, inplace=True)
        return response
    else:
        return 'invalid return type'

def check_num_of_min_category(df, minimum_threshold=3, return_type = 'dataframe'):
    response = pd.DataFrame(columns = ['columns', 'category','index'])
    category_col_list = df.select_dtypes(exclude='number').columns

    for col in category_col_list:
        temp_df = pd.DataFrame(df[col].value_counts()).reset_index()
        temp_df = temp_df[temp_df[col]<=minimum_threshold]
        if temp_df.shape[0] != 0:
            category = list(temp_df['index'].values)
            indexes = df.index[df[col].isin(category)].tolist()
            response.loc[col] = [col, category, indexes]

    if return_type == 'json':
        return response.to_json(orient="records")
    if return_type == 'dataframe':
        response.reset_index(drop=True, inplace=True)
        return response
    else:
        return 'invalid return type'
    
def check_col_with_one_category(df, return_type = 'dataframe'):
    response = pd.DataFrame(columns = ['columns', 'category_name'])
    category_col_list = df.select_dtypes(exclude='number').columns

    for col in category_col_list:
        if df[col].nunique() == 1:
            category = df[col].unique()
            response.loc[col] = [col, category]

    if return_type == 'json':
        return response.to_json(orient="records")
    if return_type == 'dataframe':
        response.reset_index(drop=True, inplace=True)
        return response
    else:
        return 'invalid return type'
    
def find_special_char_index(df, return_type = 'dataframe'):
    # define a regular expression pattern that matches any special character
    pattern = r'[^a-zA-Z0-9\s.]'
    response = pd.DataFrame(columns = ['columns', 'has_special_char_at'])

    for col in df.columns:
        # apply the regular expression to each cell in the dataframe
        matches = df[col].astype(str).str.contains(pattern).reset_index()
        indexes_spacial_char = matches[matches[col] == True]['index'].values.tolist()
        response.loc[col] = [col, indexes_spacial_char]

    if return_type == 'json':
        return response.to_json(orient="records")
    if return_type == 'dataframe':
        response.reset_index(drop=True, inplace=True)
        return response
    else:
        return 'invalid return type'
    
def duplicate_columns(df):
    #transpose the df
    temp = df.T
    temp.duplicated()
    #if the row have same value then both of them will return True
    dublicate_checked_df = pd.DataFrame(temp.duplicated(keep=False)).reset_index()
    #return a list of column name which are duplicate
    return list(dublicate_checked_df[dublicate_checked_df[0]==True]['index'])

def correlated_columns(df, return_type='dataframe'):
    risk_variable_df = pd.DataFrame()
    correalated_df = df.corr(numeric_only=True)
    correalated_df.reset_index(inplace=True)
    lst_leakage_cols = []
    lst_leakage_value = []
    for col in correalated_df.columns[1:]:
        
        j = np.where((correalated_df[col] > 0.9) & (col != correalated_df['index']), correalated_df['index'] , 0)
        j = j[np.where(j!=0)]
        k = np.where((correalated_df[col] > 0.9) & (col != correalated_df['index']), correalated_df[col] , 0)
        k = k[np.where(k!=0)]
        lst_leakage_cols.append(list(j))
        lst_leakage_value.append(k.astype(float))
    risk_variable_df['columns'] = correalated_df.columns[1:]
    risk_variable_df['correlated_columns'] = lst_leakage_cols
    risk_variable_df['correlation'] = lst_leakage_value
    if return_type == 'json': 
        return risk_variable_df.to_json(orient="records")
    if return_type == 'dataframe':
        risk_variable_df.reset_index(drop=True, inplace=True)
        return risk_variable_df
    else:
        return 'invalid return type'
    