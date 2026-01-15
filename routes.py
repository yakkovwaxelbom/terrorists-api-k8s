from fastapi import routing, File, UploadFile, HTTPException, Depends

from services import TerroristService
from models import Response

terrorist_route = routing.APIRouter()


@terrorist_route.post('/top-threats', response_model=Response, status_code=201)
def create_terrorist(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed")

    try:
        return TerroristService().process(file)


    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid CSV file: {str(e)}")


