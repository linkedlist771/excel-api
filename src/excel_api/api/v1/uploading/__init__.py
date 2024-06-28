#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import APIRouter

from excel_api.api.v1.uploading.router import router as uploading_router

router = APIRouter(prefix="/uploading")

router.include_router(uploading_router, prefix="/uploading")
