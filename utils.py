import pandas as pd

# 데이터 로드 함수
def load_data(file_path: str):
    """JSON 파일을 읽어 pandas DataFrame으로 반환"""
    return pd.read_json(file_path)

# 상표 필터링 함수
def filter_trademarks(df, name=None, status=None):
    """주어진 조건에 맞는 상표들을 필터링"""
    if name:
        df = df[df['productName'].str.contains(name, na=False)]
    if status:
        df = df[df['registerStatus'] == status]
    return df
