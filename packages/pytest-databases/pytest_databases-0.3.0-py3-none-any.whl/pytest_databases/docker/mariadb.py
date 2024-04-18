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

import contextlib
import os
from pathlib import Path
from typing import TYPE_CHECKING

import asyncmy
import pytest

if TYPE_CHECKING:
    from pytest_databases.docker import DockerServiceRegistry


async def mariadb_responsive(host: str, port: int, user: str, password: str, database: str) -> bool:
    try:
        conn = await asyncmy.connect(
            host=host,
            port=port,
            user=user,
            database=database,
            password=password,
        )
    except Exception:  # noqa: BLE001
        return False

    try:
        async with conn.cursor() as cursor:
            await cursor.execute("select 1 as is_available")
            resp = await cursor.fetchone()
        return resp[0] == 1
    finally:
        with contextlib.suppress(Exception):
            await conn.close()


@pytest.fixture()
def mariadb_user() -> str:
    return "app"


@pytest.fixture()
def mariadb_password() -> str:
    return "super-secret"


@pytest.fixture()
def mariadb_root_password() -> str:
    return "super-secret"


@pytest.fixture()
def mariadb_database() -> str:
    return "db"


@pytest.fixture()
def mariadb113_port() -> int:
    return 3359


@pytest.fixture()
def default_mariadb_service_name() -> str:
    return "mariadb113"


@pytest.fixture()
def mariadb_port(mariadb113_port: int) -> int:
    return mariadb113_port


@pytest.fixture(scope="session")
def docker_compose_files() -> list[Path]:
    return [Path(Path(__file__).parent / "docker-compose.mariadb.yml")]


@pytest.fixture()
async def mariadb113_service(
    docker_services: DockerServiceRegistry,
    docker_compose_files: list[Path],
    mariadb113_port: int,
    mariadb_database: str,
    mariadb_user: str,
    mariadb_password: str,
    mariadb_root_password: str,
) -> None:
    os.environ["MARIADB_ROOT_PASSWORD"] = mariadb_root_password
    os.environ["MARIADB_PASSWORD"] = mariadb_password
    os.environ["MARIADB_USER"] = mariadb_user
    os.environ["MARIADB_DATABASE"] = mariadb_database
    os.environ["MARIADB113_PORT"] = str(mariadb113_port)
    await docker_services.start(
        "mariadb113",
        docker_compose_files=docker_compose_files,
        timeout=45,
        pause=1,
        check=mariadb_responsive,
        port=mariadb113_port,
        database=mariadb_database,
        user=mariadb_user,
        password=mariadb_password,
    )


@pytest.fixture()
async def mariadb_service(
    docker_services: DockerServiceRegistry,
    default_mariadb_service_name: str,
    docker_compose_files: list[Path],
    mariadb_port: int,
    mariadb_database: str,
    mariadb_user: str,
    mariadb_password: str,
    mariadb_root_password: str,
) -> None:
    os.environ["MARIADB_ROOT_PASSWORD"] = mariadb_root_password
    os.environ["MARIADB_PASSWORD"] = mariadb_password
    os.environ["MARIADB_USER"] = mariadb_user
    os.environ["MARIADB_DATABASE"] = mariadb_database
    os.environ[f"{default_mariadb_service_name.upper()}_PORT"] = str(mariadb_port)
    await docker_services.start(
        name=default_mariadb_service_name,
        docker_compose_files=docker_compose_files,
        timeout=45,
        pause=1,
        check=mariadb_responsive,
        port=mariadb_port,
        database=mariadb_database,
        user=mariadb_user,
        password=mariadb_password,
    )
