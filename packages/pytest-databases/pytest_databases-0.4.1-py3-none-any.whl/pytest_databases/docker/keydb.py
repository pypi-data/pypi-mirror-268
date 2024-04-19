# MIT License

# Copyright (c) 2024 Litestar

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from __future__ import annotations

import os
from pathlib import Path
from typing import TYPE_CHECKING

import pytest
from redis.asyncio import Redis as AsyncRedis
from redis.exceptions import ConnectionError as RedisConnectionError

if TYPE_CHECKING:
    from pytest_databases.docker import DockerServiceRegistry


async def keydb_responsive(host: str, port: int) -> bool:
    client: AsyncRedis = AsyncRedis(host=host, port=port)
    try:
        return await client.ping()
    except (ConnectionError, RedisConnectionError):
        return False
    finally:
        await client.aclose()  # type: ignore[attr-defined]


@pytest.fixture()
def keydb_port() -> int:
    return 6396


@pytest.fixture(scope="session")
def docker_compose_files() -> list[Path]:
    return [Path(Path(__file__).parent / "docker-compose.keydb.yml")]


@pytest.fixture(scope="session")
def default_keydb_service_name() -> str:
    return "keydb"


@pytest.fixture(autouse=False)
async def keydb_service(
    docker_services: DockerServiceRegistry,
    default_keydb_service_name: str,
    docker_compose_files: list[Path],
    keydb_port: int,
) -> None:
    os.environ["KEYDB_PORT"] = str(keydb_port)
    await docker_services.start(
        name=default_keydb_service_name,
        docker_compose_files=docker_compose_files,
        check=keydb_responsive,
        port=keydb_port,
    )
