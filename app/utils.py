from fastapi import HTTPException

async def riot_get(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            return await response.json()

        if response.status == 401:
            raise HTTPException(status_code=401, detail="Not authorized, verify API key")
        if response.status == 403:
            raise HTTPException(status_code=403, detail="API Key expired or no permission")
        if response.status == 404:
            raise HTTPException(status_code=404, detail="Info not found")
        if response.status == 429:
            raise HTTPException(status_code=429, detail="Rate limited: Too many requests")
        
        raise HTTPException(status_code=response.status, detail="Unexpected error")


