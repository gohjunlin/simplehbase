import base64
from tqdm import tqdm

def base64_to_string(x):
    return base64.b64decode(x).decode()

def string_to_base64(x):
    return base64.b64encode(x.encode('utf-8')).decode()

# def df_to_dict(df):
#     df = df.applymap(str, na_action='ignore') # Converting all values to string except for NaN
#     df = df.melt(id_vars="ID").dropna().sort_values(by="ID").reset_index(drop = True).rename(columns = {'variable':'column', 'value':'$'})
#     # df = df.applymap(lambda x: base64.b64encode(x.encode('utf-8')).decode())
#     df = df.applymap(lambda x: string_to_base64(x))
#     df = df.set_index('ID')
#     data = {'Row': []}
#     for key in tqdm(df.index.unique()):
#         Key = {'key': key, 'Cell':df.loc[[key]].to_dict('records')}
#         data['Row'].append(Key)
#     return data

# def df_to_dict(df):
#     n_col = len(df.columns) - 1
#     num_list = [(0 + i) * (n_col) for i in range(len(df))]
#
#     df = df.fillna('').applymap(str, na_action='ignore')  # Converting all values to string except for NaN
#     df = df.melt(id_vars="ID").dropna().sort_values(by="ID").reset_index(drop=True).rename(
#         columns={'variable': 'column', 'value': '$'})
#     # df = df.applymap(lambda x: base64.b64encode(x.encode('utf-8')).decode())
#     df = df.applymap(lambda x: string_to_base64(x))
#     df = df.set_index('ID')
#
#     #     data = {'Row': [{'key': key, 'Cell':df.loc[[key]].to_dict('records')} for key in tqdm(df.index.unique())]}
#     data = {'Row': []}
#     data = {'Row': [{'key': df.iloc[i: i + n_col].index[0], 'Cell': df.iloc[i: i + n_col].to_dict('records')} for i in
#                     tqdm(num_list)]}
#     return data

def df_to_dict(df):
    df = df.fillna('').applymap(str)  # Convert NaN to empty string & change all values to string

    n_col = len(df.columns) - 1
    num_list = [i * n_col for i in range(len(df))]

    df = df.melt(id_vars="ID").sort_values(by="ID").rename(columns={'variable': 'column', 'value': '$'}).applymap(
        lambda x: string_to_base64(x))
    df = df.set_index('ID')

    data = {'Row': []}
    for i in tqdm(num_list):
        df_temp = df.iloc[i: i + n_col]
        Key = {'key': df_temp.index[0], 'Cell': df_temp.to_dict('records')}
        data['Row'].append(Key)

    return data