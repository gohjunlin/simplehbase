import base64
from tqdm import tqdm

def base64_to_string(x):
    return base64.b64decode(x).decode()

def string_to_base64(x):
    return base64.b64encode(x.encode('utf-8')).decode()

def df_to_dict(df):
    df = df.applymap(str, na_action='ignore') # Converting all values to string except for NaN
    df = df.melt(id_vars="ID").dropna().sort_values(by="ID").reset_index(drop = True).rename(columns = {'variable':'column', 'value':'$'})
    df = df.set_index('ID')
    data = {'Row': []}
    for key in tqdm(df.index.unique()):
        Key = {'key': string_to_base64(key), 'Cell':df.loc[[key]].applymap(lambda x: string_to_base64(x)).to_dict('records')}
        data['Row'].append(Key)
    return data