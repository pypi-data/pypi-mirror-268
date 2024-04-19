import aiohttp
import asyncio
from aiolimiter import AsyncLimiter
from typing import List, Dict, Any
import logging

# Setting up the logger for this module
logger = logging.getLogger(__name__)


class AIOEase:

    async def _call(self, session: aiohttp.ClientSession, request: Dict[str, Any]) -> Any:
        """
        Asynchronously make a HTTP request using the given session and request details.

        :param session: The aiohttp session to use for the request.
        :param request: The request details.
        :return: The response from the request.
        """
        methods = {
            "get": session.get,
            "post": session.post,
            "put": session.put,
            "delete": session.delete,
        }
        method = methods.get(request["method"].lower(), session.get)
        url = request["url"]
        id = request.get("id", None)
        # Debug-level log of the request details
        logger.debug(f"Sending {request['method'].upper()} request to {url}")
        del request["method"]
        if id:
            del request["id"]

        async with self.limiter:
            try:
                async with method(**request) as resp:
                    response = await resp.text()
                    # Debug-level log of the response details
                    logger.debug(f"Received response {resp.status} from {url}")
                    if id:
                        return {"status": resp.status, "response": response, "id": id}
                    else:
                        return {"status": resp.status, "response": response}
            except Exception as e:
                # Error-level log if an exception occurs
                logger.error(f"Error making request to {url}: {e}")
                return {"status": "error", "response": str(e)}

    async def _main(self, requests: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Main method to process multiple requests asynchronously.

        :param requests: A list of request details.
        :return: A list of response details.
        """
        async with aiohttp.ClientSession() as session:
            tasks = [self._call(session, request) for request in requests]
            return await asyncio.gather(*tasks)

    def execute(self, requests: List[Dict[str, Any]], requests_per_second_max: int = 1) -> List[Dict[str, Any]]:
        """
        Execute multiple HTTP requests asynchronously.

        :param requests: A list of request details.
        :param requests_per_second_max: Maximum number of requests per second.
        :return: A list of responses.
        """
        logger.info(
            f"AsyncRequest instance created with a rate limit of {requests_per_second_max} requests per second.")
        self.limiter = AsyncLimiter(requests_per_second_max, 1)
        logger.info(f"Executing {len(requests)} request(s) asynchronously.")
        return asyncio.run(self._main(requests))

def execute_async_requests(requests: List[Dict[str, Any]], requests_per_second_max: int = 1) -> List[Dict[str, Any]]:
    """
    Execute_async_requests multiple HTTP requests asynchronously.

    :param requests: A list of request details.
    :param requests_per_second_max: Maximum number of requests per second.
    :return: A list of responses.
    """
    return AIOEase().execute(requests, requests_per_second_max)