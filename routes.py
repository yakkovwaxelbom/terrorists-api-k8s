from fastapi import routing, File, UploadFile, HTTPException, Depends
import csv
from io import StringIO
import pandas as pd

terrorist_route = routing.APIRouter()


@terrorist_route.post('/top-threats')
def create_terrorist(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed")

    try:
        contents = file.file.read().decode("utf-8")
        df = pd.read_csv(StringIO(contents))

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid CSV file: {str(e)}")


    return {
        "rows": len(df),
        "columns": list(df.columns)
    }
