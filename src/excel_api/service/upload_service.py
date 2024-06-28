from fastapi import HTTPException, File, UploadFile, Form
import pandas as pd
import io

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
        contents = await file.read()
        file_object = io.BytesIO(contents)
        if file.filename.split(".")[-1] == "csv":
            df = pd.read_csv(file_object)
        else:
            df = pd.read_excel(file_object)
        return ResponseModel(code=200, msg="success", data=df.to_dict(orient="records"))
