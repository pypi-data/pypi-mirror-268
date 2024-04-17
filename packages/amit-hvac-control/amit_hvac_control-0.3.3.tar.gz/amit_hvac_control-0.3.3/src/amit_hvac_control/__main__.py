import asyncio
import argparse

from amit_hvac_control.client import AmitHvacControlClient
from amit_hvac_control.models import Config


async def main(**kwargs):
    host, username, password = kwargs.values()
    config = Config(host, username, password)

    async with AmitHvacControlClient(config) as api:
        print(f"Fetching data for {host}...")

        status = await api.status_api.async_get_overview()
        print(status)

        temperature_data = await api.temperature_api.async_get_data()
        print(temperature_data)

        ventilation_data = await api.ventilation_api.async_get_data()
        print(ventilation_data)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--host", required=True)
    p.add_argument("--username", required=True)
    p.add_argument("--password", required=True)
    args = p.parse_args()
    asyncio.run(main(**vars(args)))
