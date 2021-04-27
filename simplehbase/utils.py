import base64
from tqdm import tqdm

def base64_to_string(x):
    return base64.b64decode(x).decode()

def string_to_base64(x):
    return base64.b64encode(x.encode('utf-8')).decode()

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