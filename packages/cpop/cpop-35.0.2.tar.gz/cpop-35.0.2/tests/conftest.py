import sys
from unittest import mock

import aiopath
import cpop.hub
import pytest


@pytest.fixture()
async def hub():
    async with cpop.hub.Hub(
         # Let each test manually add their structure
        load_all_dynes=False,
        load_all_subdirs=False,
        recurse_subdirs=False,
        logs=False,
        load_config=False,
    ) as hub:
        yield hub


@pytest.fixture(autouse=True, scope="session")
async def tpath():
    code_dir = await aiopath.Path(__file__).parent.parent.absolute()
    assert await code_dir.exists()

    tpath_dir = code_dir / "tests" / "tpath"
    assert await tpath_dir.exists()

    NEW_PATH = [str(code_dir), str(tpath_dir)]

    for p in sys.path:
        if p not in NEW_PATH:
            NEW_PATH.append(p)

    with mock.patch("sys.path", NEW_PATH):
        yield
