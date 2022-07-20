from fastapi import FastAPI

app = FastAPI()


@app.get("/calc_vlp")
async def calc_vlp():
    return {"message": "Hello World"}
