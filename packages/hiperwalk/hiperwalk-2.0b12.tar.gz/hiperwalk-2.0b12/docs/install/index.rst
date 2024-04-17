=======
Install
=======

You can install Hiperwalk locally or its docker distribution.
We recommend to use Hiperwalk's docker distribution.

-------------------
Docker Installation
-------------------

Using Hiperwalk on its Docker distribution offers
numerous benefits to users.
Docker provides a lightweight, portable, and scalable environment,
ensuring seamless deployment across
different operating systems and environments.
With Docker, users can easily manage dependencies,
streamline updates, and replicate configurations,
leading to improved consistency and reliability.
Additionally, Docker enables efficient resource utilization,
facilitating faster development cycles and easier collaboration
among team members.
Overall, opting for Hiperwalk on its Docker distribution
empowers users with enhanced flexibility, efficiency,
and agility in their development and deployment processes.

.. todo::

   Add installation guidelines

------------------
Local Installation
------------------

Hiperwalk relies on a number of Python libraries.
However, installing these Python libraries alone does not enable
Hiperwalk to leverage High-Performance Computing (HPC).
If you desire to install Hiperwalk with HPC support, please refer
to :ref:`docs_install_hpc_prerequisites` before proceeding
with the Hiperwalk installation.

On this page, we outline the process for installing Hiperwalk on
a newly installed Ubuntu 20.04 operating system. The steps will
cover identifying the GPU, installing the GPU drivers,
hiperblas-core, hiperblas-opencl-bridge, pyhiperblas, and
all necessary Python libraries.

.. _docs_install_hiperwalk:

Hiperwalk
=========

Hiperwalk can be conveniently installed using pip.
To begin, ensure that pip is installed on your system.

.. code-block:: shell

   sudo apt install python3-pip

The following command will install Hiperwalk as well as all its
Python dependencies, which include
`numpy <https://numpy.org/>`_,
`scipy <https://scipy.org/>`_,
`networkx <https://networkx.org/>`_, and
`matplotlib <https://matplotlib.org/>`_.

.. warning::

    If you have older versions of these packages, they will likely be
    updated. If you prefer not to have them updated, we recommend
    `creating a virtual environment
    <https://docs.python.org/3/library/venv.html>`_.

.. code-block:: shell

   pip3 install hiperwalk

To verify the success of the installation,
you can execute any code found in the
`examples directory of the repository
<https://github.com/hiperwalk/hiperwalk/tree/master/examples>`_
or proceed to the :ref:`docs_tutorial`.

To update an older version of the hiperwalk package:

.. code-block:: shell

   pip3 install hiperwalk --upgrade

.. _docs_install_hpc_prerequisites:

HPC Prerequisites
=================

Before proceeding, it's advisable to update and upgrade your
Ubuntu packages. Execute the following commands:

.. code-block:: shell

   sudo apt update
   sudo apt upgrade


Next, run the following commands to install the prerequisites:

.. code-block:: shell

   sudo apt install git
   sudo apt install g++
   sudo apt install cmake
   sudo apt install libgtest-dev
   sudo apt install python3-distutils
   sudo apt install python3-pip
   pip3 install pytest


These newly installed programs serve the following purposes:

* git: used to download hiperblas-core, hiperblas-opencl-bridge,
  pyhiperblas, and hiperwalk;
* g++: used for compiling hiperblas-core, and hiperblas-opencl-bridge;
* cmake: essential for compiling hiperblas-core, hiperblas-opencl-bridge;
* libgtest-dev: verifies the successful installation of
  hiperblas-core, and hiperblas-opencl-bridge;
* python3-distutils: aids in the installation of pyhiperblas;
* python3-pip: necessary for installing Python libraries;
* pytest: helps test pyhiperblas.

Although it's not essential, we **recommend** installing FFmpeg,
which is used for generating animations.

.. code-block:: shell

   sudo apt install ffmpeg

GPU Driver
----------

To install the GPU driver, you can follow this
`tutorial for installing NVIDIA drivers <https://www.linuxcapable.com/install-nvidia-drivers-on-ubuntu-linux/>`_
Below, we have outlined the essential steps.

First, you'll need to identify your GPU by running the following command:

.. code-block:: shell

   lspci | grep -e VGA

You can then verify if the outputted
`GPU is CUDA compatible <https://developer.nvidia.com/cuda-gpus>`_.
If it is, execute the following command:

.. code-block:: shell

   ubuntu-drivers devices

This will list the available drivers for your GPU. We recommend
installing the driver tagged with ``recommended`` at the end.
The driver's name typically follows the format ``nvidia-driver-XXX``
where ``XXX`` is a specific number.
For the subsequent steps in the installation process, substitute ``XXX``
as required. To install the GPU driver, execute the following command:

.. code-block:: shell

   sudo apt install nvidia-driver-XXX

Finally, **reboot you computer**.
After rebooting, if the installation was successful,
running the following command:

.. code-block::

   nvidia-smi

should display GPU information such as the name, driver version,
CUDA version, and so on. Alternatively, you can verify the
availability of the **NVIDIA Settings** application by
pressing the ``Super`` key on your keyboard and
typing ``nvidia settings``.

NVIDIA Toolkit
--------------

Once the GPU drivers have been successfully installed, it's
necessary to install the NVIDIA Toolkit, allowing hiperblas-core
to use CUDA. To do this, execute the following command:

.. code-block:: shell

   sudo apt install nvidia-cuda-toolkit

To verify the correct installation of the NVIDIA Toolkit,
you can check if the ``nvcc`` compiler has been installed.
This can be simply done by running the following command:

.. code-block:: shell

   nvcc --version


Installing hiperblas-core hiperblas-opencl-bridge and pyhiperblas
=================================================================

For HPC support,
Hiperwalk uses
`hiperblas-core <https://github.com/hiperblas/hiperblas-core>`_,
`hiperblas-opencl-bridge
<https://github.com/hiperblas/hiperblas-opencl-bridge>`_,
and `pyhiperblas <https://github.com/hiperblas/pyhiperblas>`_.
Note that a computer with a **GPU compatible with CUDA** is required
for this.

The information in this guide is compiled from
`Paulo Motta's blog
<https://paulomotta.pro.br/wp/2021/05/01/pyhiperblas-and-hiperblas-core/>`_,
`hiperblas-core github <https://github.com/hiperblas/hiperblas-core>`_,
and `pyhiperblas github <https://github.com/hiperblas/pyhiperblas>`_.

It is **strongly recommended** that hiperblas-core,
hiperblas-opencl-bridge, and pyhiperblas
are installed (i.e. cloned) in the same directory.
In this guide, we will install both projects into the home directory.
In Linux, the tilde (``~``) serves as an alias for the home directory.

hiperblas-core
--------------

Firstly, clone the repository in the home directory.

.. code-block:: shell

   cd ~
   git clone https://github.com/hiperblas/hiperblas-core.git

Next, navigate to the hiperblas-core directory to compile and
install the code.

.. code-block:: shell

   cd hiperblas-core
   cmake .
   make
   sudo make install
   sudo ldconfig

The ``ldconfig`` command creates a link for the newly installed hiperblas-core,
making it accessible for use by pyhiperblas.
Before moving forward, **reboot** your computer to
ensure that the ``ldconfig`` command takes effect.

After rebboting,
run the following ``ln`` command to create
a symbolic link to another directory.

.. code-block:: shell

   sudo ln -s /usr/local/lib /usr/local/lib64

To verify the successful installation of hiperblas-core,
execute the ``vector_test`` and ``matrix_test`` tests.

.. code-block:: shell

   ./vector_test
   ./matrix_test

hiperblas-opencl-bridge
-----------------------

The installation of the hiperblas-opencl-bridge is very similar to
the installation of hiperblas-core.
To install hiperblas-opencl-bridge,
first clone the repository into
**the same directory hiperblas-core was cloned**.
In this guide, we cloned hiperblas-core into the home directory.

.. code-block:: shell

   cd ~
   git clone https://github.com/hiperblas/hiperblas-opencl-bridge.git

Now, enter the new ``hiperblas-opencl-bridge`` directory to compile and
install the code.

.. code-block:: shell

   cd hiperblas-opencl-bridge
   cmake .
   make
   sudo make install

To verify the succesful installation of hiperblas-opencl-bridge,
execute the tests

.. code-block:: shell

   ./vector_test
   ./matrix_test

pyhiperblas
-----------

To install pyhiperblas, first clone the repository into
**the same directory hiperblas-core was cloned**.
In this guide, we cloned hiperblas-core into the home directory.
Thus, execute:

.. code-block:: shell

   cd ~
   git clone https://github.com/hiperblas/pyhiperblas.git

Next, navigate to the newly created ``pyhiperblas`` directory to install it.

.. code-block:: shell

   cd pyhiperblas
   sudo python3 setup.py install

To verify whether the installation was successful, run the following test:

.. code-block:: shell

   python3 test.py
