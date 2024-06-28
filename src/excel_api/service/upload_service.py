from fastapi import HTTPException, File, UploadFile, Form
import pandas as pd

from excel_api.schemas.response_schema import ResponseModel


class UploadService:

    @staticmethod
    async def upload_excel(*, file: UploadFile = File(...)):
        # 直接判断后缀是不是csv 或者xlsx或者xls
        if file.filename.split(".")[-1] not in ["csv", "xlsx", "xls"]:
            raise HTTPException(
                status_code=400,
                detail="wrong file type, only csv, xlsx, xls are allowed",
            )
        if file.filename.split(".")[-1] == "csv":
            df = pd.read_csv(file.file)
        else:
            df = pd.read_excel(file.file)
        return ResponseModel(code=200, msg="success", data=df.to_dict(orient="records"))
