.. _conf_integrate_overview:

====================
The Integrate System
====================

.. note::

    This document was written before the pop-config system was introduced in
    pop 10, the conf system will be completly deprecated in favor of the
    pop-config system. The pop-config system takes the power of conf.integrate
    to new levels and seperates it from pop itself.

Now that you have a clear view of the available constructs in configuration dicts used by
the ``conf`` system we can talk about the `pop.config.load` module. By itself ``conf`` is a great
tool to load configs, but ``cpop`` is all about dynamically merging multiple plugin subsystems.
Dynamically merging applications presents a significant issue when it comes to configuration,
`conf` and the `pop.config.load` systems are designed to work together to solve this issue.

Using `pop.config.load` is made to be as easy as possible, but it also means that the
configuration system follows a clear model.

The Config Yaml
===============

The integrate system uses this *config.yaml* file to simply define CLI options, local config
options, and options that we assume other systems would share. These types of
configuration data are defined in configuration dicts in *config.yaml*.

Simply populate these dicts with configuration data and it can be easily
and dynamically loaded by other ``cpop`` projects.

CONFIG
------

The ``config`` seciton is where the configuration options used specifically by the subsystems
defined in this project.

CLI_CONFIG
----------

The ``cli_config`` section is used for configuration data data specific to the command line.
It is only used to set positional arguments, things that define the structure of how
the CLI should be processed.

When using ``cli_config`` the options should still be defined in the ``config`` section. The
top level key in the ``cli_config`` will override the ``config`` values but having them set
in the ``config`` section will allow for the values to be absorbed by plugin systems
that are using your application.

SUBS
----

The ``subcommands`` section compliments the ``cli_config`` section in specifying what subparsers should be
added to the cli when importing this config as the primary cli interface.

Usage
=====

Now, with the conf.py file in place loading the configuration data up is easier then ever!
Just add this one line to your project:

.. code-block:: python

   hub.pop.config.load("<The authoritative namespace>")

The conf system will get loaded for you and hub.OPT will be populated with namespaced configuration
data as defined in the configuration dicts.

Multiple Projects
-----------------

Every project will have its `config` section loaded from its *config.yaml*.
However, only the authoritative CLI will be have its `cli_config` section exposed on the cli.

.. code-block:: python

    hub.pop.config.load(cli="rem")


Using The Roots System
======================

In many applications directories need to be created and verified. Often the directories also
need to be set up for a specific user if not run with admin privileges. This is where the
`roots` system comes into place.

If you have set up any option(s) that ends in `_dir`, then you can have `pop.config.load` do
some work for you! By setting the ``roots`` option ``conf`` will create the directory if it does
not already exist and it will change the paths to those directories to be in a hidden directory
in the user's home directory if not running as the root user.
