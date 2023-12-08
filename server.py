import os

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=str("0.0.0.0"),
        port=int(os.environ.get('PORT',8888)),
        reload=False,
        log_level="info",
        workers=1
    )