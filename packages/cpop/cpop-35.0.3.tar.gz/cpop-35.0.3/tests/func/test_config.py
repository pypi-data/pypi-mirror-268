async def test_load_with_config_file(hub, tmp_path):
    # Test loading with a configuration file
    cli = "test_cli"
    cli_config = hub._dynamic.config.cli_config
    cli_config.update({"test_cli": {"option": {}}})
    config = {"test_cli": {"option": {"default": "default"}}}
    config_file = tmp_path / "config.yaml"
    config_file.write_text("test_cli:\n  option: file_value\n")
    OPT = await hub.pop.config.load(
        cli=cli,
        cli_config=cli_config,
        config=config,
        subcommands={},
        global_clis=["pop"],
        parser_args=[f"--config={config_file}"],
    )
    assert OPT[cli]["option"] == "file_value"


async def test_load_with_subcommands(hub):
    # Test loading with subcommands
    cli = "test_cli"
    cli_config = {"test_cli": {"option": {}}}
    subcommands = {
        "test_cli": {"subcommand": {"description": "Subcommand description"}}
    }
    OPT = await hub.pop.config.load(
        cli=cli,
        cli_config=cli_config,
        subcommands=subcommands,
        global_clis=[],
        parser_args=["subcommand"],
    )
    assert OPT["pop"]["subparser"] == "subcommand"


async def test_prioritize_with_env_vars(hub):
    # Test prioritizing with environment variables
    cli = "test_cli"
    cli_opts = {}
    config = {"test_cli": {"option": {"os": "TEST_OPTION", "default": "default"}}}
    hub.lib.os.environ["TEST_OPTION"] = "env_value"
    OPT = await hub.pop.config.prioritize(
        cli=cli, cli_opts=cli_opts, config=config, config_file_data={}, global_clis=[]
    )
    assert OPT["test_cli"]["option"] == "env_value"


async def test_load_basic(hub):
    # Test loading with minimal arguments
    OPT = await hub.pop.config.load()
    assert isinstance(OPT, hub.lib.cpop.data.ImmutableNamespaceDict)
    assert "pop" in OPT
    assert "subparser" in OPT["pop"]
    assert "global_clis" in OPT["pop"]
    assert "log" in OPT


async def test_load_with_cli(hub):
    # Test loading with a CLI
    cli = "test_cli"
    cli_config = {"test_cli": {"option": {}}}
    config = {"test_cli": {"option": {"default": "default", "os": "TEST_OPTION"}}}

    hub.lib.os.environ.pop("TEST_OPTION", None)
    # Test the default
    OPT = await hub.pop.config.load(
        cli=cli,
        cli_config=cli_config,
        config=config,
        subcommands={},
        global_clis=[],
        parser_args=[],
    )
    assert OPT[cli]["option"] == "default"

    # Test that os vars overrides default
    hub.lib.os.environ["TEST_OPTION"] = "os"
    OPT = await hub.pop.config.load(
        cli=cli,
        cli_config=cli_config,
        config=config,
        subcommands={},
        global_clis=[],
        parser_args=[],
    )
    assert OPT[cli]["option"] == "os"

    # Test that cli supersedes all
    OPT = await hub.pop.config.load(
        cli=cli,
        cli_config=cli_config,
        config=config,
        subcommands={},
        global_clis=[],
        parser_args=["--option=cli"],
    )
    assert OPT[cli]["option"] == "cli"


async def test_parse_cli(hub):
    # Test parsing CLI options
    cli = "test_cli"
    active_cli = {"option": {"subcommands": ["__global__"]}}
    subcommands = {"subcommand": {}}
    parser_args = ("--option", "cli_value", "subcommand", "--option", "sub_cli_value")
    cli_opts = await hub.pop.config.parse_cli(
        cli=cli, active_cli=active_cli, subcommands=subcommands, parser_args=parser_args
    )
    assert cli_opts["option"] == "sub_cli_value"
    assert cli_opts["SUBPARSER"] == "subcommand"


async def test_prioritize(hub):
    # Test prioritizing configuration options
    cli = "test_cli"
    cli_opts = {"option": "cli_value"}
    config = {"test_cli": {"option": {"default": "config_value"}}}
    config_file_data = {"test_cli": {"option": "file_value"}}
    OPT = await hub.pop.config.prioritize(
        cli=cli,
        cli_opts=cli_opts,
        config=config,
        config_file_data=config_file_data,
        global_clis=["pop", "log"],
    )
    # CLI options have the highest priority
    assert OPT["test_cli"]["option"] == "cli_value"
