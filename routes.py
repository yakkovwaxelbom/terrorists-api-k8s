from fastapi import routing, File, UploadFile, HTTPException
from pymongo.errors import PyMongoError
from bson.errors import InvalidDocument

from services import TerroristService
from models import Response
from db import get_mongo_db

terrorist_route = routing.APIRouter()


@terrorist_route.post('/top-threats', response_model=Response, status_code=201)
def create_terrorist(file: UploadFile = File(...)):
    
    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed")
    
    try:
        with get_mongo_db() as db:
                return TerroristService(db).process(file)
        
    except PyMongoError as e:
        raise HTTPException(status_code=503, detail=f"Unable to connect to MongoDB: {str(e)}")

    except TypeError as e:
         raise HTTPException(status_code=503, detail=f"Invalid type in MongoDB: {str(e)}")

    except Exception as e:
            raise HTTPException(status_code=400, detail=f"Invalid CSV file: {str(e)}")






