from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from .routes import competitions_route, teams_route
import logging

logger = logging.getLogger("uvicorn")

# description = """
# ChimichangApp API helps you do awesome stuff. 🚀

# ## Items

# You can **read items**.

# ## Users

# You will be able to:

# * **Create users** (_not implemented_).
# * **Read users** (_not implemented_).
# """

app = FastAPI(
    # title="ChimichangApp",
    # description=description,
    # summary="Deadpool's favorite app. Nuff said.",
    # version="0.0.1",
    # terms_of_service="http://example.com/terms/",
    # contact={
    #     "name": "Deadpoolio the Amazing",
    #     "url": "http://x-force.example.com/contact/",
    #     "email": "dp@x-force.example.com",
    # },
    # license_info={
    #     "name": "Apache 2.0",
    #     "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    # },
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ExceptionHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            logger.info(f"Received request: {request.method} {request.url}")
            response = await call_next(request)
            return response
        except Exception as e:
            logger.exception(f"Unhandled exception: {e}")
            return JSONResponse(
                status_code=500,
                content={"error": e.__class__.__name__, "message": str(e)}
            )

app.add_middleware(ExceptionHandlerMiddleware)

app.include_router(competitions_route, prefix="/competitions", tags=["competitions"])
app.include_router(teams_route, prefix="/teams", tags=["teams"])
