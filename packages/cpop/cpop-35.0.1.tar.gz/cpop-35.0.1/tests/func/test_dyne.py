async def test_get(hub):
    assert await hub.pop.dyne.get() == hub._dynamic.dyne
