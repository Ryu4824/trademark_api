from fastapi import FastAPI, Request, Form, Query
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from utils import load_data,filter_trademarks
app = FastAPI()

templates = Jinja2Templates(directory="templates")

df = load_data("trademark_sample.json")

# 메인 페이지 - 검색폼과 상품 목록 10개씩 표시
@app.get("/")
def main_page(request: Request, page: int = 1):
    status_options = df['registerStatus'].unique()
    per_page = 10
    start = (page - 1) * per_page
    end = start + per_page
    sliced_df = df.iloc[start:end]
    return templates.TemplateResponse("main.html", {
        "request": request,
        "item": sliced_df,
        "status_options": status_options,
        "current_page": page,
        "has_next": end < len(df),
        "has_prev": start > 0
    })

# 자동완성 - 입력한 문자열로 시작하는 productName 10개 반환
@app.get("/autocomplete")
async def autocomplete(query: str):
    query = query.strip()
    productName = df["productName"].dropna().unique().tolist()
    matches = [name for name in productName if name.startswith(query)]
    return JSONResponse(content=matches[:10])

# 검색 요청 처리 - productName과 registerStatus로 필터링 후 결과 반환
@app.post("/search")
def search(request: Request, productName: str = Form(...), registerStatus: str = Form(...)):
    result_df = filter_trademarks(df, productName,registerStatus)
    results = result_df.to_dict(orient="records")
    return templates.TemplateResponse("result.html", {"request": request, "results": results, "query": productName})
    
# 동적 상태 옵션 제공 - 입력한 productName에 해당하는 registerStatus 옵션 반환
@app.get("/status_options")
def get_status_options(productName: str = Query(...)):
    filtered = df[df['productName'].str.contains(productName, case=False, na=False)]
    options = filtered['registerStatus'].dropna().unique().tolist()
    return options