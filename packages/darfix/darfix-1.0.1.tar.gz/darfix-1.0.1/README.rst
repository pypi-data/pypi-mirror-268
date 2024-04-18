darfix
======

*darfix* is a Python library for the analysis of dark-field microscopy data. It provides a series of computer vision techniques,
together with a graphical user interface and an `Orange3 <https://github.com/biolab/orange3>`_ add-on to define the workflow.

Installation
++++++++++++

Installing *darfix* involves creating a python environment, installing dependencies and potentially
Windows enabling long paths.

Environment
-----------

It is recommended to create a `virtual environment <https://docs.python.org/3/library/venv.html>`_ to
avoid conflicts between dependencies.

On Linux or Mac

.. code-block:: bash

    python3 -m venv /path/to/new/virtual/environment

    source /path/to/new/virtual/environment/bin/activate

On Windows

.. code-block:: bash

    python3 -m venv C:\path\to\new\virtual\environment

    C:\path\to\new\virtual\environment\Scripts\activate.bat

*Note: To deactivate the environment call:* :code:`deactivate`

Installation
------------

Installation from pypi
^^^^^^^^^^^^^^^^^^^^^^

Install *darfix* with all its dependencies

.. code-block:: bash

    pip install darfix[full]

To install *darfix* with a minimal set of dependencies run instead

.. code-block:: bash

    pip install darfix

Troubleshooting
^^^^^^^^^^^^^^^

On Windows you may get this intallation error

.. code-block:: bash

    Building wheels for collected packages: ewoksorange
    Building wheel for ewoksorange (pyproject.toml) ... error
    error: subprocess-exited-with-error

    × Building wheel for ewoksorange (pyproject.toml) did not run successfully.
    │ exit code: 1
    ╰─> [154 lines of output]
        ...
        error: could not create 'build\lib\ewoksorange\tests\examples\ewoks_example_1_addon\orangecontrib\ewoks_example_supercategory\ewoks_example_subcategory\tutorials\sumtask_tutorial3.ows': No such file or directory
        [end of output]

    note: This error originates from a subprocess, and is likely not a problem with pip.
    ERROR: Failed building wheel for ewoksorange
    Failed to build ewoksorange
    ERROR: Could not build wheels for ewoksorange, which is required to install pyproject.toml-based projects

Instructions on how to enable long paths in Windows 10 or later can be found `here <https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=registry>`_.

Getting started
+++++++++++++++

Start the graphical interface

.. code-block:: bash

    orange-canvas

Drag widgets from the left pane to the canvas to start making your workflow.

Documentation
+++++++++++++

The documentation of the latest release is available at https://darfix.readthedocs.io

User guide
++++++++++

A user guide can be downloaded at https://darfix.readthedocs.io/en/latest/user_guide.html
