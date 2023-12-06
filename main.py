from fastapi import FastAPI
import api.v1.controllers.skill_extractor as v1_controllers
import uvicorn

app = FastAPI()

app.include_router(router=v1_controllers.router, prefix="/api/v1")



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)