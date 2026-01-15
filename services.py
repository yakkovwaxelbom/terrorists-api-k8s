from io import StringIO
from fastapi import UploadFile
import pandas as pd
from typing import List

from models import TerroristModel, Response


class TerroristService:
    def __init__(self):
        pass


    def _data_analysis(self, file: UploadFile) -> pd.DataFrame:

        contents = file.file.read().decode("utf-8")
        df = pd.read_csv(StringIO(contents))
        df.sort_values(by='danger_rate', ascending=False, inplace=True)

        return df.loc[:4, ['name', 'location', 'danger_rate']]
    

    def _convert_to_terrorist_model(self, df: pd.DataFrame) -> List[TerroristModel]:
        terrorists: List[TerroristModel] = []

        for _, row in df.iterrows():
            terrorist = TerroristModel(
                name=row["name"],
                location=row["location"],
                rate_danger=row["danger_rate"]
            )
            terrorists.append(terrorist)

        return terrorists
    

    def _send_to_db():
        pass
    

    def process(self, file: UploadFile) -> List[TerroristModel]:

        df = self._data_analysis(file)
        terrorist_arr = self._convert_to_terrorist_model(df)

        self._send_to_db(terrorist_arr)

        return Response(count=len(terrorist_arr), top=terrorist_arr)
