==========
Quickstart
==========

Using pop to create a plugin oriented project is easy. This tutorial will help you
learn how ``cpop`` works and how to make a project.

.. note::

    A repo with the full working example can be found `here <https://gitlab.com/saltlc/poppy>`_.

Getting Started
===============

Start by installing pop and making a new directory for your project:

.. code-block:: bash

    $ pip3 install cpop[cli]
    $ mkdir poppy

Now outside of the newly created directory, create a simple python script called *run.py*
to create the ``hub`` and start the plugin system.

.. note::

    Normally a python project uses ``setuptools`` and a setup.py file. Because this tutorial
    is about ``cpop`` we skip this part and use the *run.py* script. This can make development
    easier because you can run your application directly from your checkout.

The ``hub`` is the root of the namespace that ``cpop`` operates on. Don't worry, it is not
that complicated! Think of the hub like a big ``self`` variable that is shared across
your entire application. The hub allows you to save data that is relative to your plugins
while still allowing that data to be shared safely across the application.

.. code-block:: python

    # run.py

    import asyncio
    import cpop.hub


    async def main():
        # Create the hub
        hub = await cpop.hub.AsyncHub()
        # Load up your first plugin subsystem called "plugins"
        await hub.pop.sub.add(dyne_name="poppy")
        # Call the cli function that initializes the app
        await hub.poppy.init.cli()


    asyncio.run(main())


This script has created your ``hub`` and loaded up your first subsystem, or ``sub``. The
``dyne_name`` option tells ``pop`` where to load up the python package that contains the plugins.
Adding the sub is redundant, by default, ``cpop`` will load all the plugins it can find in the PYTHONPATH.
``src/config.yaml`` has a key called ``dynes`` that maps the source code files for plugin
subsystems to directories that contain the subs.

.. note::

    To learn more about the ``hub`` take a look at our doc on the hub and how to use it:
    :ref:`hub_overview`

Now lets create the python package and make it start to work! Make a new directory
called poppy as the base python package and then another for your plugins.

.. code-block:: bash

    $ mkdir -p src/poppy

Now that you are in the new poppy directory create the new plugin subsystem's initializer.
Create a file called *poppy/poppy/init.py* and give it an ``__init__`` function. Like a
class you can initialize a new plugin subsystem, or a new module in that function.

.. code-block:: python

    # poppy/poppy/init.py


    async def cli(hub):
        print("Hello World!!")

.. note::

    Your first ``sub`` has been created! To learn more about making subs check the doc here:
    :ref:`subs_overview`

Now that you have a plugin with an initializer you can run it! Go back to the same directory
as the *run.py* file and execute it.

.. code-block:: bash

    $ python3 run.py

With a project up and running you can now add more plugins, more code and more subsystems!

.. note::

    When you make a new sub, that sub follows a `pattern`. Patterns are an important part of
    Plugin Oriented Programming. Get to know the basics first! But then spend a few minutes
    learning about ``patterns`` here: :ref:`sub_patterns`. Just so you know, the pattern you
    just started is called the **spine** pattern.

Adding Configuration Data
=========================

Now that you have the basic structure of your application you can easily add configuration
data to your project.

Loading configuration data into a project looks easy at first but quickly becomes difficult.
To solve this issue ``cpop`` comes with a system to make configuration loading easy.

When loading configuration data, the data can come from many sources, the command line,
environment variables, windows registry, configuration files, etc. But certain sources
should overwrite other sources; config files overwrite defaults, environment variables overwrite
config files and cli overwrites all. Also, you end up defining default configuration values
and parameters in multiple places to enable supporting multiple mediums for configuration input.
Finally, you only want to have to document your configuration options in one place.

The ``config`` system in ``pop`` solves this issue by making a single location where you can
define your configuration data. You can also merge the configuration data from multiple `pop`
projects, just like you can add other ``pop`` projects' plugin subsystems to your project's `hub`!

.. note::

    That's right! I just said that you can merge entire applications together onto one hub and
    bring in all the configuration data too! To learn more about this, take a look at the doc
    on merging applications: :ref:`app_merging`

Using the ``config`` system, is easy! Create a file called `poppy/config.yaml` and populate it with
your configuration data.

.. code-block:: yaml

    # poppy/config.yaml

    cli_config:
      poppy:
        addr:
          options:
            - -a
          help: the address to present the rpc server on
        port:
          options:
            - -p
          help: The port to bind to

    config:
      poppy:
        addr:
          default: 127.0.0.1
        port:
          default: 8888


Now lets change the ``__init__`` function in *poppy/poppy/init.py* to load up the project's config!

.. code-block:: python

    # src/poppy/init.py


    async def cli(hub):
        await hub.pop.config.load(["poppy"], cli="poppy")
        print(hub.OPT.poppy.addr)
        print(hub.OPT.poppy.port)

Now the configuration data has been loaded, if you run *run.py* with `--help` you will see
all of your configuration options available. The configuration options will now be made
available on the ``hub`` under the ``OPT`` dict and under the name of the imported project.

This allows for configuration data to be loaded from multiple projects and still cleanly
namespaced. So the values of our configurations will be available on the `hub`:

.. code-block:: python

    hub.OPT.poppy.addr
    hub.OPT.poppy.port


Now you can use the default IP address and port, or you can pass in different
values when you start up the (to be developed) server.

.. code-block:: bash

    $ python3 ./run.py
    127.0.0.1
    8888

    $ python3 ./run.py --addr 0.0.0.0 --port 8080
    0.0.0.0
    8080

.. note::

    The ``config`` system is very powerful and expansive, take a look at the docs on the conf
    system to get to know more of the available options and features. It is made to solve
    many problems that occur when loading configuration data:
    :ref:`conf_overview`
    :ref:`conf_integrate_overview`

Adding More Plugin Subsystems
=============================

Next lets create a new plugin subsystem. This makes a new namespace on the hub and allows us
to create a pattern in ``cpop`` So there are a few more new terms to learn!

A plugin subsystem is typically referred to as a `sub`. This is a namespace on the ``hub`` that
defines the new set of plugins. Using these namespaces on the ``hub`` allows you to set variables
on the ``hub`` that are defined as to how they should be used based on where they exist. Data
on the hub should only be written by relative plugins, but can be read globally.

.. note::

    Remember how I mentioned patterns before? If you are curious, the sub we are making now
    follows the ``router`` pattern. :ref:`sub_patterns`

When you create a new ``sub`` it should follow a `pattern`. These patterns define how the `sub`
interacts with your application. We will start by making a simple ``pattern`` called the
`library pattern`. This pattern means that modules have functions that are generally available.

When the ``hub`` is created it comes with a ``sub`` called `pop`. The ``pop`` ``sub`` comes with
the functions we need to add our own `hub`. Now you can execute `hub.pop.sub.add` to add a new
plugin subsystem. Remove the previous print statements, and add the subsystem:

.. code-block:: python

    # poppy/poppy/init.py


    async def cli(hub):
        await hub.pop.config.load(["poppy"], cli="poppy")
        await hub.pop.sub.add(dyne_name="rpc")

We will also need to update the ``dyne`` dictionary in our `config.yaml` so that pop is aware of where the "rpc" code exists:

.. code-block:: yaml

    # poppy/config.yaml
    dyne:
      poppy:
        - poppy
      rpc:
        - rpc

All imports will be added under ``hub.lib`` if they are defined in the `config.yaml`.
This way, you can see all imports your app uses in one place!

.. code-block:: yaml

    # poppy/config.yaml
    imports:
      - asyncio
      - aiohttp.web


Now that we are able to load up a new subsystem we need to define it in our code! Start by making
a new directory inside of `poppy/` called `rpc`. When we added the new ``sub`` we specified the path
to find the ``rpc`` ``sub`` to be in the ``rpc`` dyne.

Now create the *src/rpc/init.py* file and make an rpc server. This rpc server will expose
all of the functions in the ``rpc`` plugin subsystem over a simple http server.

.. code-block:: python

    # poppy/rpc/init.py


    async def __init__(hub):
        hub.rpc.APP = hub.lib.aiohttp.web.Application()
        hub.rpc.RUNNER = hub.lib.aiohttp.web.AppRunner(hub.rpc.APP)
        hub.rpc.ROUTES = [
            hub.lib.aiohttp.web.get("/", hub.rpc.init.router),
        ]
        hub.rpc.APP.add_routes(hub.rpc.ROUTES)


    async def run(hub, addr: str = None, port: int = None, **kwargs):
        await hub.rpc.RUNNER.setup()
        site = aiohttp.web.TCPSite(hub.rpc.RUNNER, host=addr, port=port)
        await site.start()
        while True:
            await hub.lib.asyncio.sleep(0.1)


    async def router(hub, request):
        try:
            data = await request.json()
        except:
            data = {}
        if "ref" in data:
            result = {}
            result["ref"] = await getattr(hub.rpc, data["ref"])(**data.get("kwargs"))
            return aiohttp.web.json_response(result)
        default_text = """example: curl -X GET http://{0}:{1} -d '{{"ref": "math.fib", "kwargs": {{"num": "11"}}}}'\n""".format(
            hub.OPT["poppy"]["addr"], hub.OPT["poppy"]["port"]
        )
        return hub.lib.aiohttp.web.Response(text=default_text)

As you can see, this uses the ``aiohttp`` library, and will need to be installed (and added to your pyproject.toml dependencies):

.. code-block:: bash

    $ pip3 install aiohttp

Now let's have `src.poppy.init.cli()` call `rpc.init`'s run() function:

.. code-block:: python

    async def __init__(hub):
        print("Hello World!")
        await hub.pop.sub.add(dyne_name="rpc")


    async def cli(hub):
        await hub.pop.config.load(["poppy"], cli="poppy")
        print(hub.OPT.poppy.addr)
        print(hub.OPT.poppy.port)

        kwargs = dict(hub.OPT.poppy)

        await hub.poppy.init.run(**kwargs)


    async def run(hub, **kwargs):
        await hub.rpc.init.run(**kwargs)


Congratulations! You now have a working rpc server that takes json requests and routes to
plugins in the ``rpc`` sub. Now we just need to make a module in the ``rpc`` sub to route the
requests to, lets call this file *poppy/rpc/math.py*:

.. code-block:: python

    async def fib(hub, num=10):
        num = int(num)
        if num < 2:
            return num
        prev = 0
        curr = 1
        i = 1
        while i < num:
            prev, curr = curr, prev + curr
            i += 1
        return curr


    async def triple(hub, num=10):
        num = int(num)
        return num * 3


Now your rpc server can compute the Fibonacci sequence. So lets start up the server with the
*run.py* script and then hit it with a curl command:

.. code-block:: bash

    $ python3 ./run.py
    ======== Running on http://127.0.0.1:8888 ========
    (Press CTRL+C to quit)


.. code-block:: bash

    # Get a Fibonacci sequence using the generic router function

    $ curl -X GET http://127.0.0.1:8888 -d '{"ref": "math.fib", "kwargs": {"num": "11"}}'
    {"ref": 89}

.. code-block:: bash

    # Call the Math Triple function using the generic router function

    $ curl -X GET http://127.0.0.1:8888 -d '{"ref": "math.triple", "kwargs": {"num": "33"}}'
    {"ref": 99}

.. code-block:: bash

    # Request the root url. If you don't pass in any data it will respond with
    # an example command you can run.

    $ curl -X GET http://127.0.0.1:8888
    example: curl -X GET http://127.0.0.1:8888 -d '{"ref": "math.fib", "kwargs": {"num": "11"}}'


Now that you have a project up and running you can play around with extending what ``cpop`` can
do and get familiar with it.


Docs Review
===========

In this doc we introduced a lot of concepts, this is a whole new programming paradigm!
To become more familiar with Plugin Oriented Programming and ``cpop`` we already introduced these
docs:

What is a hub and how to use it:
    :ref:`hub_overview`

What a sub is and how to use it:
    :ref:`subs_overview`

What patters are and some examples of patterns that can help you start thinking in `pop`
    :ref:`sub_patterns`

How the built in configuration loading system ``config.yaml`` works:
    :ref:`conf_overview` and
    :ref:`conf_integrate_overview`

How the concept of app merging works:
    :ref:`app_merging`

Next Steps
==========

Now that you have the tools you need to make ``cpop`` work you will be able to start understanding
how to think in and really use the power behind Plugin Oriented Programming! Take a look at these
docs to get a better overview of Plugin Oriented programming:

Learning Plugin Oriented Programming
====================================

Learning and thinking in Plugin Oriented Programming starts here, it is a short doc trying to outline
how to think about your applications so they can all be truly Plugin Oriented:
:ref:`learning_POP`

The Story Behind Plugin Oriented Programming
============================================

Plugin Oriented Programming deviates from many of the norms in software development while working
to evolve to the modern way of developing. Learn about Thomas Hatch and how he came up with
the Plugin Oriented Programming paradigm:
:ref:`story_of_pop`
