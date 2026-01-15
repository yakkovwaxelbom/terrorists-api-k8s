from fastapi import FastAPI, Request
import uvicorn
from fastapi.responses import JSONResponse
from pymongo.errors import PyMongoError


from routes import terrorist_route


app = FastAPI()


app.include_router(terrorist_route)



if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)