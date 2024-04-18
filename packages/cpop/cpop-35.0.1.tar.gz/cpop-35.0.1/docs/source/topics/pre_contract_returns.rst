Pre-Contract Return Handling
============================

- **Pre-Contract Failure Handling:**
  - If a ``pre``contract returns ``False``, or a tuple ``(False, "custom message")``, POP can be configured to raise a ``cpop.exc.PreContractFailed`` exception.
  - Returning ``False`` indicates a failure condition, preventing the associated function from being called.
  - A custom message can be provided for more detailed feedback on the failure.

Usage Example
-------------
Here's an example of a ``pre`` contract for a function named "func" that returns False:

.. code-block:: python

    # project_root/contracts/plugin.py
    async def pre_func(hub, ctx):
        if condition_not_met:
            return False


    # project_root/plugin.py
    async def func(hub): ...

Here's an example of a pre-contract for a function named "func" that returns a custom message:

.. code-block:: python

    # project_root/contracts/plugin.py
    async def pre_function(hub, ctx):
        if condition_not_met:
            return False, "Condition for execution not met"


    # project_root/plugin.py
    async def function(hub): ...

Here is a function that calls "func" and catches the exception:

.. code-block:: python


    async def main(hub):
        try:
            hub.plugin.func()
        except hub.lib.cpop.exc.PreContractFailed as e:
            # Handle the error as needed
            ...
