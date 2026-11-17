from fastapi import FastAPI, HTTPException

app = FastAPI(title="CI Comparison Demo")


@app.get("/")
def health():
    return {"status": "ok"}


@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"result": a + b}


@app.get("/divide/{a}/{b}")
def divide(a: int, b: int):
    if b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"result": a / b}
