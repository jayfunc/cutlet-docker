from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import cutlet
import unidic

app = FastAPI(title="Cutlet Romaji API (Full Dictionary)")

katsu = cutlet.Cutlet() 
katsu.use_foreign_spelling = False

class TextRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"status": "running", "type": "Full UniDic"}

@app.post("/convert")
def convert_to_romaji(request: TextRequest):
    try:
        romaji = ""
        lines = request.text.split("\n")
        for line in lines:
            romaji_line = katsu.romaji(line)
            romaji += romaji_line + "\n"
        return {
            "romaji": romaji
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    # Container port
    # 容器端口
    uvicorn.run(app, host="0.0.0.0", port=23333)