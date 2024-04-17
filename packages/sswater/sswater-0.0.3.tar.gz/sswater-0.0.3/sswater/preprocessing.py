import pymysql
import pandas as pd
from datetime import datetime, timedelta
from sklearn.preprocessing import StandardScaler


def preprocess(data) :
    data.dropna(inplace=True)
    data.set_index('data_time',inplace=True)
    data.index = pd.to_datetime(data.index)
    data.info()

    columns_to_scale = ['ma_q']
    scaler = StandardScaler()
    scaler2 = StandardScaler()
    data_scaled = scaler.fit_transform(data[columns_to_scale])
    target_scaled = scaler2.fit_transform(data['ma_q'].values.reshape(-1, 1))
    
    # 스케일링된 열을 포함한 DataFrame 생성
    data_scaled_df = pd.DataFrame(data_scaled, columns=columns_to_scale)
    data_scaled_df = data_scaled_df.set_index(data.index)
    data_scaled_df.rename(columns={'ma_q':'learningma_q'},inplace=True)
    
    # 'ma_Q' 열을 추가하여 원본 DataFrame과 병합
    data_scaled_df['ma_q'] = data_scaled_df['learningma_q'] # ma_Q/의 경우 scaling 하지 않고 target으로 사용해봄. <=== 해당 부분 문제 가능성이 있어 주석처리
    data_scaled_df.drop('learningma_q',axis=1, inplace=True)

    features = data_scaled_df.values
    
    return features, scaler2

def correction(data):
    # 최종학습날짜 확인
    directory = "./example/trainedModels/js/"
    with open(directory+'latest_train_date.txt', 'r' ) as f:
        lines = f.readlines() 
        saved_date = lines[0].strip()
        
    df = pd.DataFrame(data)

    cor_df = df[df['data_time'] > str(saved_date)]
    isna = cor_df.isna().sum()
    cols = cor_df.columns

    for i in range(len(isna)):
        if isna[i] > 0:
            df[cols[i]].fillna(0, inplace=True)
    
    zeroInd = cor_df[cor_df['ma_q'] == 0]['data_time']
    cor_df['correction'] = 0
    cor_df['ma_pcode'] = '210601'
    if(len(zeroInd) > 0):
        for i in range(len(zeroInd)):
            dt = zeroInd.iloc[i]
            cor_df.loc[cor_df['data_time'] == dt,'ma_q'] = df.loc[(df.ma_q != 0) & (df.data_time%10000 == zeroInd.iloc[0]%10000)]['ma_q'].mean()
            cor_df.loc[cor_df['data_time'] == dt, 'correction'] = 1
    
    insertDB(cor_df)
    
    cor_df.drop("correction",axis=1, inplace=True)
    cor_df.drop("ma_pcode",axis=1, inplace=True)

    result = cor_df.to_dict('records')

    return result

def calStrDate(date):
    list_date = list(date)
    str_month = int(list_date[5])-1
    if str_month < 1:
        str_month = 12
        list_date[3] = str(int(list_date[3])-1)
    list_date[5] = str(str_month)

    start_date = datetime.strptime(''.join(list_date), "%Y%m%d%H%M")

    return start_date
    
def calEndDate(date, monthVal):
    list_date = list(date)
    end_month = int(list_date[5])+monthVal
    if end_month > 12:
        end_month -= 12
        list_date[3] = str(int(list_date[3])+1)
        
    list_date[5] = str(end_month)
    end_date = datetime.strptime(''.join(list_date), "%Y%m%d%H%M")

    return end_date

def insertDB(df):
    con = pymysql.connect(host='127.0.0.1', user='root', password='manhattancafe', db='scmsdb011', charset='utf8')
    cursor = con.cursor()
    
    sql = "insert into flowdata (data_time, ma_q, temp, humodity, atmo, floor, hr, correction, ma_pcode) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = df.values.tolist()
    
    cursor.excute(sql, val)

    con.commit()

    cursor.close()
    con.close()
