import numpy as np
from PIL import Image
from fastapi import FastAPI, UploadFile, File
from starlette.responses import JSONResponse

import predictor

app = FastAPI()

@app.post("/classify-card")
async def verify_video(image: UploadFile = File()):
    try:
        arr_img = np.array(Image.open(image.file))
        result = predictor.predict(arr_img)
        return JSONResponse(status_code=200, content={"success": True, "message":"", "data": result})
    except Exception as e:
        return JSONResponse(status_code=200, content={"success": False, "message": "Field image harap diisi", "data": None})