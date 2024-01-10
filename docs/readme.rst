.. README

hmd-tf-pdf-generation
==================================

This project is an example of containerizing a Python script for use as an NeuronSphere Image Transform.
It is complete with unit tests and RobotFramework integration tests.
The project can be built and run using free NeuronSphere command line tools.

Building and Running Tests
---------------------------------------------

Prerequisites:
+++++++++++++++++++++++

* NeuronSphere Build CLIs installed via ``pip install neuronsphere``
* Configured NeuronSphere ``HMD_HOME`` directory, run ``hmd configure`` and follow the prompts
* Docker >= 21
* Python 3.9

Building
+++++++++++++++++++++++

Run the command ``hmd build`` from the project root directory.
This will build both a Python library, and run PyTest unit tests for it, and a Docker image that uses the Python library.
Once complete, the resulting Docker image will be tagged ``ghcr.io/neuronsphere/hmd-tf-pdf-generation:0.1``.

Running Tests
+++++++++++++++++++++++

The NeuronSphere ClIs include a tool for running RobotFramework tests called Bender.
From the project root, you can run ``hmd bender`` to run the included RobotFramework tests located in ``./test/``.
The test results will be found in ``./bender/`` directory.


Anatomy of the Transform
--------------------------------------

The Transform consists of two parts, a Python package that performs the actual work, and a Docker image that setups up the enviroment and calls an entrypoint function in the Python package.
The Python package must include a ``do_transform`` function located in the ``hmd_tf_pdf_generation.hmd_tf_pdf_generation`` module.
The function must accept the following parameters, a path to a mounted input directory, a path to a mounted output directory, a TransformInstance Identifier, and a TransformInstance Context.
The path parameters are mounted into the running container as /hmd_transform/input and /hmd_transform/output.
The TransformInstance Identifier and Context are provided by the NeuronSphere Transform Service at runtime, or in the case of the tests through the RobotFramework library, as enviroment variables.
The Docker container entrypoint is responsible for reading the enviroment variables and passing them to the ``do_transform`` function.
The TransformInstance Context is parsed as a JSON dictionary and passed as a Python ``dict``.

Within the Python ``do_transform`` function, we read values from the Context to get the PDF title and output filename.
Then we use the ReportLab library to generate and save a basic PDF with fake data.
More information about ReportLab can be found at `https://docs.reportlab.com/`.