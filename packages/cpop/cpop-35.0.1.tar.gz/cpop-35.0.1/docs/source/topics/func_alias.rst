.. _func_alias:

================
Function Aliases
================

Earlier versions of POP have allowed a dictionary called ``__func_alias__`` to be defined in
a plugin. This dictionary would map the names of functions in the plugin to
aliases on the hub.  The intention of this feature was to allow functions to
exist on the hub that mirrored the names of builtin keywords.  (Such as "list",
"id", or "async")

For example:

.. code-block:: python

    # This mapping makes it so that the function called "list_" shows up on
    # the hub as hub.*.list instead of hub.*.list_

    __func_alias__ = {
        "list_": "list",
    }


    async def list_(hub): ...

It is important to note that in the above example, while ``list`` will now be
registered on the hub, you wouldn't be able to call ``list`` directly in your
plugin. This is because of the way ``__func_alias__`` works. It is simply
registering ``list`` as being a function available to those *outside* your plugin
who are accessing these methods via the hub. It doesn't do any python magic to
make ``list`` available inside your plugin.

New Alias Functionality
=======================

POP 16 introduces two powerful new extensions to `__func_alias__`.
`__func_alias__` can now be a function which *returns* the dictionary of mappings
used. For example:

.. code-block:: python

   async def __func_alias__(hub):
       return {"list_": "list"}

``__func_alias__`` is called and evaluated when the plugin is loaded on to the
hub.

The second way that ``__func_alias__`` has been augmented is useful for wrapping
other non-POP APIs. The values of the mapping dictionary are now allowed to be
functions themselves, which are then called directly.

For example:

.. code-block:: python

    import os


    async def __func_alias__(hub):
        return {"os_mkdir": os.mkdir}


    __func_alias__ = {"os_mkdir": os.mkdir}

In the above example, now other POP code can call `hub.foo.bar.os_mkdir()` and
the underlying `os.mkdir()` function will be called. Simple, elegant -- and
have you noticed something a bit odd about the example above?

If you are a seasoned POP developer, the above example may actually look
horribly wrong, even though it does in fact work. Aren't all POP functions
supposed to accept a ``hub`` as the first argument? Since `os.mkdir` has the
function call signature of `os.mkdir(dirname)` and not `os.mkdir(hub,
dirname)`, how can we map `os.mkdir(dirname)` into our plugin and still have it
able to be called from other POP code via the hub? All of our other POP
functions in the plugin must accept a ``hub`` as their first argument to be
called from outside it. What makes this mapped function acceptable when
it should not be?

Unlike other functions in your plugin, POP uses a slightly different contract
for any functions passed as ``__func_alias__`` dictionary values.  This special
contract does *not* pass a ``hub`` as a first argument, but your mapped function
is *still* callable from the hub.

This makes it really easy to map non-POP-aware code into your plugin. There is
maybe only one downside, which is the special circumstances where your mapped
function is POP-aware and you *do* want to be able to reference the hub from
within it. Our final two examples will demonstrate why in some cases you may
want to do this and how to make it work.

But first, let's look at another example. Here, we'll wrap a method of an object:

.. code-block:: python

    from external_module.api import OtherService


    # This will be put on the hub at hub._.SERVICE and will only be called once when the mod is loaded
    SERVICE = OtherService()


    async def __func_alias__(hub):
        return {"start": SERVICE.start}

Behind the scenes, our plugin is now interfacing with an object, but to users
of our plugin we provide standard POP functions.

Like our previous example, a special POP contract is used for the mapped
`start` method, so it does not have to accept a ``hub`` as a first argument.

But there are potential scenarios where we want to map to a function that
*does* need access to the hub. We can handle this scenario with the following
pattern:

.. code-block:: python

   async def __init__(hub):
       hub.SPECIAL_STRING = "fancy"


   async def return_a_wrapper(hub):
       def wrapper(arg1, arg2):
           print(f"{arg1} {arg2} {hub.SPECIAL_STRING}")

       return wrapper


   async def __func_alias__(hub):
       return {"wrapped": return_a_wrapper(hub)}

We've already shown how mapped functions have a special contract that does
not inject a hub. But by using the wrapper pattern above, our `wrapper`
function does have access to the hub via the parent context of
`return_a_wrapper`. Also note that in our ``__func_alias__`` mapping, we
are actually *calling* `return_a_wrapper`, which returns `wrapper`, a
function, as a return value. In previous examples, we were not performing
a call here but instead just passing a reference to a function without
calling it.

Our final example will show how this pattern can be used in a more
sophisticated way. We will dynamically create a bunch of plugin functions
using a loop. We will use a wrapper so that our mapped methods can access
the hub.

I recommend reading this code from bottom-to-top. Start with the
`do_things_with_our_example` function. Thanks to the special POP contract
used, the functions would be callable from outside our plugin as
`hub.foo.bar.get_job_id("super-task")`, etc.:

.. code-block:: python

    from external_module.api import OtherService

    # This will be put on the hub at hub._.SERVICE and will only be called once when the mod is loaded
    SERVICE = OtherService()


    async def _wrap_service_get_method(hub, target):
        """
        ``target`` is used to find a method name of OtherService called `get_{target}`.

        Return the alias we should use in this plugin, as well as function that
        calls this method of OtherService.
        """
        method_name = f"get_{target}"

        def wrapper(arg1):
            method = getattr(hub._.SERVICE, target)
            return method(arg1)

        return method_name, wrapper


    async def __func_alias__(hub):
        out = {"start": SERVICE.start}

        for target in "job_id", "process_id", "user_id", "parent_id":
            func_name, func = _wrap_service_get_method(hub, target)
            out[func_name] = func

        return out


    async def do_things_with_our_example(hub):

        # This function call will not work:

        try:
            job_id = get_job_id("super-task")
        except NameError:
            print("I couldn't find get_job_id.")

        # We *could* call it like this, assuming this plugin is at this path
        # on the hub:

        job_id = hub.foo.bar.get_job_id("super-task")

        # This approach would work because we are referencing the function from
        # the hub. All our __func_alias__ does is augment look-up tables when we
        # are finding functions via the hub. It doesn't do any python magic to
        # inject aliases into the current namespace. So we need to reference our
        # aliases 'from the outside' so that these look-up tables are searched.

        job_id = hub.foo.bar.get_job_id("super-task")
        process_id = hub.foo.bar.get_process_id("super-task")
        user_id = hub.foo.bar.get_user_id("super-task")


This example, while complex, begins to demonstrate the power of using
`__func_alias__` to wrap third-party APIs and modules. Since `__func_alias__`
can be a function, there are many approaches that can be used to create these
mappings, and they can dynamically respond to changes in third-party libraries.

For example, you could dynamically introspect the methods of a third-party
object and use what you find to create functions in your plugin 'on the fly'.
Not only is this powerful, it can also reduce the number of boilerplate wrapper
functions you might otherwise have to write by hand to wrap third-party APIs.
You can simply write a small amount of code to automate this wrapping
for you. This accelerates integration of code into the POP ecosystem and makes
these wrappers more compact and maintainable.
