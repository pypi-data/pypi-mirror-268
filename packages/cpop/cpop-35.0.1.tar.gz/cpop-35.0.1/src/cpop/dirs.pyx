"""
Find directories
"""

import importlib.resources
import os
import aiopath
import sys
from collections import defaultdict
from collections.abc import Iterable

import cpop.data
import msgpack
import yaml


async def dir_list(pypath: list[str] = None, static: list[str] = None) -> list[aiopath.Path]:
    """
    Return the directories to look for modules in, pypath specifies files
    relative to an installed python package, static is for static dirs
    :param pypath: One or many python paths which will be imported
    :param static: Directories that can be explicitly passed
    """
    ret = set()
    if pypath:
        for path in pypath:
            mod = importlib.import_module(path)
            for m_path in mod.__path__:
                # If we are inside of an executable the path will be different
                ret.add(aiopath.Path(m_path))
    if static:
        ret.update(aiopath.Path(dir_) for dir_ in static)
    return sorted(ret)


async def inline_dirs(dirs: Iterable[str], subdir: str) -> list[aiopath.Path]:
    """
    Look for the named subdir in the list of dirs
    :param dirs: The names of configured dynamic dirs
    :param subdir: The name of the subdir to check for in the list of dynamic dirs
    :return An extended list of dirs that includes the found subdirs
    """
    ret = set()
    for dir_ in dirs:
        check = aiopath.Path(dir_) / subdir
        if await check.is_dir():
            ret.add(check)
    return sorted(ret)


async def dynamic_dirs():
    """
    Iterate over the available python package imports and look for configured
    dynamic dirs in pyproject.toml
    """
    dirs = set()
    for dir_ in sys.path:
        if not dir_:
            continue
        path = aiopath.Path(dir_)
        if not await path.is_dir():
            continue
        async for sub in path.iterdir():
            full = path / sub
            if str(sub).endswith(".egg-link"):
                async with full.open() as rfh:
                    dirs.add(aiopath.Path((await rfh.read()).strip()))
            elif await full.is_dir():
                dirs.add(full)

    # Set up the _dynamic return
    ret = cpop.data.NamespaceDict(
        dyne=cpop.data.NamespaceDict(),
        config=cpop.data.NamespaceDict(),
        imports=cpop.data.NamespaceDict(),
    )

    # Iterate over namespaces in sys.path
    for dir_ in dirs:
        # Prefer msgpack configuration if available
        config_msgpack = dir_ / "config.msgpack"
        config_yaml = dir_ / "config.yaml"

        config_file = config_msgpack if await config_msgpack.is_file() else None
        if not config_file and await config_yaml.is_file():
            config_file = config_yaml

        if not config_file:
            # No configuration found, continue with the next directory
            continue

        dynes, configs, imports = await parse_config(config_file)
        if dynes:
            cpop.data.update(ret.dyne, dynes, merge_lists=True)
        if configs:
            cpop.data.update(ret.config, configs, merge_lists=True)
        if imports:
            cpop.data.update(ret.imports, imports)

    return ret


async def parse_config(config_file: aiopath.Path) -> tuple[dict[str, object], dict[str, object], set[str]]:
    dyne = defaultdict(lambda: cpop.data.NamespaceDict(paths=set()))
    config = cpop.data.NamespaceDict(
        config=cpop.data.NamespaceDict(),
        cli_config=cpop.data.NamespaceDict(),
        subcommands=cpop.data.NamespaceDict(),
    )
    imports = cpop.data.NamespaceDict()

    if not await config_file.is_file():
        return dyne, config, imports

    async with config_file.open("rb") as f:
        file_contents = await f.read()
        if config_file.suffix == ".yaml" or config_file.suffix == ".yml":
            pop_config = yaml.safe_load(file_contents) or {}
        elif config_file.suffix == ".msgpack":
            pop_config = msgpack.unpackb(file_contents) or {}
        else:
            raise ValueError("Unsupported file format")

    # Gather dynamic namespace paths for this import
    for name, paths in pop_config.get("dyne", {}).items():
        for path in paths:
            ref = config_file.parent / path.replace(".", os.sep)
            dyne[name]["paths"].add(ref)

    # Get config sections
    for section in ["config", "cli_config", "subcommands"]:
        section_data = pop_config.get(section)
        if not isinstance(section_data, dict):
            continue
        for namespace, data in section_data.items():
            if data is None:
                continue
            config[section].setdefault(namespace, cpop.data.NamespaceDict()).update(data)

    # Handle python imports
    for imp in pop_config.get("import", []):
        base = imp.split(".", 1)[0]
        if base not in imports:
            imports[base] = importlib.import_module(base)
        if "." in imp:
            importlib.import_module(imp)

    for name in dyne:
        dyne[name]["paths"] = sorted(dyne[name]["paths"])

    return dyne, config, imports
