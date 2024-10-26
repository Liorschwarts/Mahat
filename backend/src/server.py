from controller import app
import logging
import sys

logger = logging.getLogger("uvicorn")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)