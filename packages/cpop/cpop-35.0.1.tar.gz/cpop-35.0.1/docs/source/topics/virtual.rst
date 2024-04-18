Virtual Functions
=================

Virtual functions make it so that plugins can be dynamically loaded based on arbitrary conditions.
Any plugin on the hub can define a virtual function.

.. code-block:: python

    async def __virtual__(hub):
        return True | False, "Reason for failure"


One common use for this feature is to only load a plugin if certain libraries are available.
I.E.

.. code-block:: python

    try:
        import some_library

        # If the module loaded successfully then we don't need to specify a reason, but HAS_LIBS needs to be a tuple
        HAS_LIBS = (True,)
    except ImportError as e:
        # If the library failed to load then let the reason be the text of the ImportError
        HAS_LIBS = False, str(e)


    async def __virtual__(hub):
        return HAS_LIBS

Another common usage of virtuals is to define multiple versions of a plugin, but only load the one that works on the host OS.

.. code-block:: python

    import os


    async def __virtual__(hub):
        return os.name == "nt", "This plugin only works on Windows"
