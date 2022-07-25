import uvicorn
from fastapi import FastAPI

import src.app.routes as rts

app = FastAPI()

app.include_router(rts.main_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8004)
