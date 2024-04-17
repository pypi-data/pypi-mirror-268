from .NLinear import NLinear_Model
from .GAILinear import GAILinear_model

from .create_seq import create_seq

import os

import torch
import torch.nn.functional as F
import torch.optim as optim
from datetime import datetime, timedelta

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 학습데이터, 장소, config, 학습특성개수, 추가학습여부
def model_train(data, place, configs, feature_num, latest_date):
    version = 0 # 첫버전은 0
    filtered_data = data

    if feature_num < 2:
        # 시간 + 유량 모델
        directory = "./example/trainedModels/"+place+"/"
        loaded_model = GAILinear_model(configs).cuda()
        file_name = place
    else:
        # 추가 데이터 학습 모델
        directory = "./example/trainedModels/"+place+"_cli/"
        loaded_model = NLinear_Model(configs).cuda()
        file_name = place+"_cli"

        # 모델 로드
    model_list = os.listdir(directory)
    model_list_pt = [file for file in model_list if file.endswith(".pt")]
    final_model = directory+model_list_pt[-1]
    loaded_model.load_state_dict(torch.load(final_model))
        
    with open(directory+'latest_train_date.txt', 'r' ) as f:
        lines = f.readlines()  # 파일의 모든 줄을 읽어옵니다.

        # 첫 번째 행의 날짜와 두 번째 행의 버전 값을 분리
        saved_date = lines[0].strip()
        version = float(lines[1].strip()[1:])
        
        date_obj = datetime.strptime(lines[0].strip(), "%Y%m%d%H%M").strftime('%Y-%m-%d %H:%M')

    X,y =  create_seq(filtered_data, configs.seq_len, configs.pred_len)
    
    # 학습을 위한 설정
    n_epochs = 300
    batch_size = 100
    split_ratio = 0.9
    learning_rate = 0.00001

    optimizer = optim.Adam(loaded_model.parameters(), lr=learning_rate)

    # 총 개수 train / val 데이터 분할을 위함.
    n_samples = X.shape[0]
    train_samples = int(n_samples * split_ratio)

    X_train, y_train = X[:train_samples], y[:train_samples]
    X_val, y_val = X[train_samples:], y[train_samples:]

    X_train, X_val = torch.tensor(X_train).float().to(device), torch.tensor(X_val).float().to(device)
    y_train, y_val = torch.tensor(y_train).float().to(device), torch.tensor(y_val).float().to(device)
    
    for epoch in range(n_epochs):
        # 모델 학습
        loaded_model.train()
        for i in range(0, X_train.shape[0], batch_size):
            optimizer.zero_grad()
            X_batch = X_train[i:i + batch_size]
            y_batch = y_train[i:i + batch_size]
            
            output = loaded_model(X_batch)
            loss = F.mse_loss(output, y_batch)
            loss.backward()
            optimizer.step()

        # 모델 평가
        loaded_model.eval()
        val_output = loaded_model(X_val)
        val_loss = F.mse_loss(val_output, y_val)
        print(f"Epoch {epoch + 1}, Loss: {loss.item()}, Validation Loss: {val_loss.item()}")
    
    # 폴더가 없을시 생성
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")

    if version > 0:
        version += 0.1
    else:
        version = 0.1

    file_name = file_name+"_updated_model_"+str(version).replace(".","")+".pt"

    if feature_num < 2:
        torch.save(loaded_model.state_dict(), "./example/trainedModels/"+place+"/"+file_name)
    else:
        torch.save(loaded_model.state_dict(), "./example/trainedModels/"+place+"_cli/"+file_name)
    # 업데이트된 날짜와 버전 값을 파일에 기록합니다.
    with open(directory+'latest_train_date.txt', 'w' ) as f:
        f.write(str(latest_date) + '\n') 
        f.write(f'v{version:.1f}')
    