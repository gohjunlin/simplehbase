import base64

def df_to_dict(df):
    df = df.melt(id_vars="ID").dropna().sort_values(by="ID").reset_index(drop = True).rename(columns = {'variable':'column', 'value':'$'})
    df = df.applymap(lambda x: base64.b64encode(x.encode('utf-8')).decode())
    data = {'Row': []}
    for key in df["ID"].unique():
        Key = {'key': key, 'Cell':df.set_index("ID").loc[[key]].to_dict('records')}
        data['Row'].append(Key)
    return data

def base64_to_string(x):
    return base64.b64decode(x).decode()