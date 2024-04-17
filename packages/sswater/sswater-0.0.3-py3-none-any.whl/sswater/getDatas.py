import pyodbc

class Tibero:
    def __init__(self):
        """
        뷰테이블 정보 
        ip : 172.28.201.81 / port : 8629 / sid = tibero / id : IS_AI / pw : IS_AI
        """
        self.con = pyodbc.connect('DSN=Tibero6;UID=sys;PWD=kkk123')
        self.con.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
        self.con.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
        self.con.setdecoding(pyodbc.SQL_WMETADATA, encoding='euc-kr')
        self.con.setencoding(encoding='utf-8')
        self.cursor = self.con.cursor()

    def getTrainData(self, pcode, ex_factor):
        sql = ""
        if ex_factor == "cli":
            dic_key = ['ma_pcode', 'data_time', 'ma_q', 'temp', 'humodity', 'atmo', 'floor', 'hr']
            sql = "select ma_pcode, concat(day, hhmm) as data_time, ma_q, temp, humodity, atmo, floor, hr from flowdata where ma_pcode='"+str(pcode)+"' order by data_time asc"
        else:
            dic_key = ['ma_pcode', 'data_time', 'ma_q']
            sql = "select ma_pcode, concat(day, hhmm) as data_time, ma_q from flowdata where ma_pcode='"+str(pcode)+"' order by data_time asc"

        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        
        result = []
        for d in list(data):
            result.append(dict(zip(dic_key, d)))
        
        return result
        