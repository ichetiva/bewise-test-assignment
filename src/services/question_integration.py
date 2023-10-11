import aiohttp


class QuestionIntegrationService:
    async def get_questions(self, count: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://jservice.io/api/random", params={"count": count}
            ) as resp:
                contents = await resp.json()
        return contents
