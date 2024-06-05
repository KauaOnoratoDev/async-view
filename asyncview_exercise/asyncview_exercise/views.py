import asyncio
import httpx
from django.http import HttpResponse

async def http_call():
    for num in range(1, 7):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org")
        print(r)
        
        
async def async_view(request):
    loop = asyncio.get_running_loop()
    loop.create_task(http_call())
    return HttpResponse("Non-blocking HTTP request")