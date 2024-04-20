.. _conf_overview:

=====================
Configuration Reading
=====================

.. note::

    This document was written before the pop-config system was introduced in
    pop 10, the conf system will be completely deprecated in favor of the
    pop-config system

.. note::

    This document was written before the conf.integrate system was introduced.
    While the information in this document is relevant, it is recommended to
    use the conf.integrate system that extends the raw functionality shown here.

One of the classic issues with systems software development is adding
configuration and options to CLI programs. The problem is that configuration
data needs to come from multiple sources. Defaults need to be set, CLI options
need to be accepted, config file(s) need to exist. Config file settings need to
override defaults, while CLI options need to override both, but the CLI needs
to be able to define the location of the config file(s). Finally there ends up
being multiple sources of truth. Config options are documented in one place
while config file options are documented elsewhere.

This little issue can get confusing, and turns into a manual process for many
applications. Pop's ``conf`` subsystem aims to solve this problem! Instead of
having to maintain multiple sources of documentation, it is in one place. Instead
of having to build the system that takes care of these deps, it is in one place.
Instead of defining all of the loading of config files ``conf`` supports multiple
file formats.

All in all, ``conf`` should make your life much easier!

Getting Started
===============

Pop's ``conf`` system is loaded onto the hub by default.

So first, create a python dict with your configuration data, we will start with something simple:

.. code-block:: yaml

    config:
      poppy:
        cache_dir:
          default: /var/cache/


Following ``pop`` conventions it would make sense to save your configuration
values on the hub so they are available to your application.

.. note::
    Typically loading configuration is done at the beginning of an application. A good place therefore
    to load up configs could be as early as in the primary init.new function in your first subsystem.

Adding Extra CLI Options
========================

The CLI option is determined by the top level dict key, but often it is preferred
to add an alternative or a shortcut option to the CLI, this can be easily added:

.. code-block:: yaml

    config:
      poppy:
        cache_dir:
          default /var/cache/

    cli_config:
      poppy:
        options:
          - -C
          - --cacheland
        help: the place to cache stuff

Actions
=======

The ``conf`` system supports setting actions. This allows for a flag to set an action
within the parser. All of the flags for action that are supported by Argparser are
supported here: https://docs.python.org/3/library/argparse.html#action

.. code-block:: yaml

    config:
      poppy:
        cheese:
          default: False

    cli_config:
      poppy:
        cheese:
          action: store_true
          help: Say yes to cheese!

Grouping CLI Options
====================

Sometimes it is helpful for multiple CLI arguments to appear as a group. Just
adding the ``group`` key is all you need:

.. code-block:: yaml

    config;
      poppy:
        cache_dir:
          default: /var/cache
        cheese:
          default: False

    cli_config;
      poppy:
        cache_dir:
          options:
            - -C
            - --cacheland
          group: global
          help: The place to cache stuff!
        cheese:
          action: store_true
          group: app
          help: Say yes to cheese!


Using Config Files
==================
POP automatically adds a ``config`` and logging options to the cli to make things easier.

When you call `pop.config.load` it will also look for a toml file in the
location that is defined for config. TOML is the default but you can specify
yaml or json.

Using Nargs
===========

Using ``nargs`` allows you to set up how many space delimited arguments are
accepted by the option. This value is sent down to the Argparser nargs
options. To see what can be passed in for nargs take a look at the python docs:
https://docs.python.org/3/library/argparse.html#nargs

Using Positional args
=====================

It often makes sense to use positional arguments for your CLI options. This
can be easily added to `conf`:

.. code-block:: yaml

    config:
      poppy:
        name:
        stuff:

    cli_config:
      poppy:
        name:
          positional: True
          nargs: 1
          help: The name of the thing
        stuff:
          positional: True
          nargs: "*"
          help: The stuff you need and want


By using ``positional``, you can determine the order of
positional arguments. Keep in mind that if you set nargs to '*' that will need
to be the last argument.


Enable OS Variables (Environment Vars and Registry)
===================================================

Enabling OS variables as configuration sources for a given value can be easily done.
An OS source is defined as an environment variable on Unix style systems and as an
entry in the registry on Windows

Just add the ``os`` option to the values passed to the key in the configuration dict:

.. code-block:: yaml

    config:
      poppy:
        output_color:
          default: red
          os: OUTPUT_COLOR
        test_extra_options:
          default: reactive
          os: TESTEXTRAOPTS

    cli_config:
      poppy:
        output_color:
          help: the color to print out
        test_extra_options:
          help: Test mod for the extra options


The ``os`` option can be set to a string which will be used to read the option.
In the case os unix style systems the environment variable  will be all uppercase
to follow the standard convention.

Using Subcommands
=================

Subcommands allow for the cli application to accept a second command, like the
`git` command has `git clone` and `git commit`. To use subcommands just add
another dict to define the subcommnds:

.. code-block:: yaml

    subcommands:
      poppy:
        sub:
          description: a subparser!

    config:
      poppy:
        foo:
          subcommands:
            - sub
          help: Set some foo!

So now you have a subcommand called ``sub`` and then under the subcommand the option `foo`
resides.

Config options can be applied to multiple subcommands:

.. code-block:: yaml

    cli_config:
      poppy:
        foo:
          action: store_true
          subcommands:
            - create
            - remove
            - edit

    config:
      poppy:
        foo:
          default: False

    subcommands:
      poppy:
        create:
          description: Create some things
        remove:
          description: Remove some things
        edit:
          description: Edit some things
