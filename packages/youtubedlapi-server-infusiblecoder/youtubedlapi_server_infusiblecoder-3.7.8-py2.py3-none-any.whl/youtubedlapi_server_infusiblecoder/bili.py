import asyncio
from bilix.sites.bilibili import api
from httpx import AsyncClient


async def main():

    client = AsyncClient(**api.dft_client_settings)
    data = await api.get_video_info(client, 'https://www.bilibili.com/video/BV1Dm4y1g7AZ/?spm_id_from=333.788.recommend_more_video.1')
    print(data)


asyncio.run(main())