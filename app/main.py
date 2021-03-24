from typing import Optional

import debugpy
from fastapi import FastAPI
from uvicorn.config import logger

app = FastAPI()


@app.on_event("startup")
async def start_remote_debug():
    logger.info('...: START UP :...')

    # if 'debug' in sys.argv:
    try:
        debugpy.listen(("0.0.0.0", 3004))
        logger.info(f"Waiting for debugger attach on port {3004}")
        debugpy.wait_for_client()
        logger.info('VSCODE attached with success. Happy debugging!')
    except Exception as ex:
        logger.error(f"DEBUG NOT WORKING: {ex}")


@app.get("/")
def read_root():
    return {
        "Hello": "World"
    }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {
        "item_id": item_id,
        "q": q
    }
