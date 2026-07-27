import time

from starlette.middleware.base import BaseHTTPMiddleware

from app.core.logger import logger


class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        start = time.time()

        response = await call_next(request)

        duration = (time.time() - start) * 1000

        logger.info(
            "%s %s %s %.2f ms",
            request.method,
            request.url.path,
            response.status_code,
            duration
        )

        return response