class Config:
    def __init__(self, seq_len, pred_len, enc_in, individual):
        """
        seq_len = 유량 예측시 참조할 과거 데이터 길이
        pred_len = 유량 예측을 시행할 범위 (미래 시점)
        euc_in = 학습에 사용된 특성의 갯수
        individual = Bool type. 단일 값 예측 or not
        """
        self.seq_len = seq_len
        self.pred_len = pred_len
        self.enc_in = enc_in
        self.individual = individual