from fastapi import FastAPI
app = FastAPI()
import uvicorn

@app.get("/")
def read_root():
    return dict(name = "Ashutosh", Location = "Deheradun")

@app.get("/{data}")
def read_root(data):
    return dict(hi = data, Location = "Deheradun")

if name == "main":
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)
