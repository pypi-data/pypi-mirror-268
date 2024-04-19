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

import psycopg
import pytest

if TYPE_CHECKING:
    from pytest_databases.docker import DockerServiceRegistry


async def cockroachdb_responsive(host: str, port: int, database: str, driver_opts: dict[str, str]) -> bool:
    opts = "&".join(f"{k}={v}" for k, v in driver_opts.items()) if driver_opts else ""
    try:
        with psycopg.connect(f"postgresql://root@{host}:{port}/{database}?{opts}") as conn, conn.cursor() as cursor:
            cursor.execute("select 1 as is_available")
            resp = cursor.fetchone()
            return resp[0] if resp is not None else 0 == 1  # noqa: PLR0133
    except Exception:  # noqa: BLE001
        return False


@pytest.fixture()
def cockroachdb_port() -> int:
    return 26257


@pytest.fixture()
def cockroachdb_database() -> str:
    return "defaultdb"


@pytest.fixture()
def cockroachdb_driver_opts() -> dict[str, str]:
    return {"sslmode": "disable"}


@pytest.fixture(scope="session")
def docker_compose_files() -> list[Path]:
    return [Path(Path(__file__).parent / "docker-compose.cockroachdb.yml")]


@pytest.fixture(scope="session")
def default_cockroachdb_service_name() -> str:
    return "cockroachdb"


@pytest.fixture(autouse=False)
async def cockroachdb_service(
    docker_services: DockerServiceRegistry,
    default_cockroachdb_service_name: str,
    docker_compose_files: list[Path],
    cockroachdb_port: int,
    cockroachdb_database: str,
    cockroachdb_driver_opts: dict[str, str],
) -> None:
    os.environ["COCKROACHDB_DATABASE"] = cockroachdb_database
    os.environ["COCKROACHDB_PORT"] = str(cockroachdb_port)
    await docker_services.start(
        name=default_cockroachdb_service_name,
        docker_compose_files=docker_compose_files,
        timeout=60,
        pause=1,
        check=cockroachdb_responsive,
        port=cockroachdb_port,
        database=cockroachdb_database,
        driver_opts=cockroachdb_driver_opts,
    )
