#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fastapi import APIRouter, Depends, BackgroundTasks
from fastapi import HTTPException, File, UploadFile, Form

from excel_api.service.upload_service import UploadService

router = APIRouter()

service = UploadService


@router.post("/upload_excel")
async def upload_excel(*, file: UploadFile = File(...)):
    """
    Upload excel file
    """
    return await service.upload_excel(file=file)
