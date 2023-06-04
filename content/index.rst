Multiwavelet tutorial
=====================

In this tutorial you will learn how to use the multiresolution analysis tools of
the MRChem suite.

.. figure:: img/vampyr-logo.png
   :scale: 40%
   :alt: VAMPyR logo
   :align: center

Using the `VAMPyR <https://github.com/MRChemSoft/vampyr/>`_ Python package you will learn:

- What a multiwavelet basis is and what it looks like.
- How to use multiresolution analysis to represent functions and operators in
  1D, 2D and 3D real space.

.. prereq::

   Before attending this workshop, please make sure that you have the
   prerequisite software and hardware available.

       We will work within `Jupyter notebooks <https://jupyter.org/>`_. We have
       set up this lesson such that it can be run entirely within your browser,
       using cloud infrastructure. You can also use your own computer, provided
       that it has the necessary tools installed. If that is not the case, please
       follow these :ref:`detailed instructions <setup>`.

.. toctree::
   :hidden:
   :maxdepth: 1

   setup


.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Exercises
   
   notebooks/Ex-1_vampyr_intro
   notebooks/Ex-2_Ex-3_display_MW_scaling_wavelet
   notebooks/Ex-4_MW-filters
   notebooks/Ex-6_function_proejction_1d
   notebooks/Ex-7_3d-grid
   notebooks/Ex-8_separated_representation
   notebooks/Ex-9_Poisson_Helmholtz
   notebooks/Ex-10_derivatives
   notebooks/Ex-12_misc_math


.. csv-table::
   :widths: auto
   :delim: ;

   [15 min] ; :doc:`notebooks/Ex-1_vampyr_intro`
   [15 min] ; :doc:`notebooks/Ex-2_Ex-3_display_MW_scaling_wavelet`
   [15 min] ; :doc:`notebooks/Ex-4_MW-filters`
   [15 min] ; :doc:`notebooks/Ex-6_function_proejction_1d`
   [15 min] ; :doc:`notebooks/Ex-7_3d-grid`
   [15 min] ; :doc:`notebooks/Ex-8_separated_representation`
   [15 min] ; :doc:`notebooks/Ex-9_Poisson_Helmholtz`
   [15 min] ; :doc:`notebooks/Ex-10_derivatives`
   [15 min] ; :doc:`notebooks/Ex-12_misc_math`

.. toctree::
   :maxdepth: 1
   :caption: Reference

   zbibliography


.. _learner-personas:

Who is the course for?
----------------------

This lesson is for researchers and students that want to learn more about:

- What are multiresolution analysis (MRA) and multiwavelets?
- Which kind of operations can be performed with functions and
  operators using a Multiwalvelet representation?
- What are the advantages and disadvantages of a Multiwavelet representation.

We assume that participants have knowledge of

- calculus in one and several dimension 
- vector calculus
- linear algebra
- the Python programming language


About the course
----------------


This lesson material is developed by the MRChem group at the `Hylleraas Center for Quantum
Molecular Sciences <https://www.mn.uio.no/hylleraas/english/>`_, in
collaboration with Robert J. Harrison, Eduard Valeev and Florian Bischoff

Each lesson episode has clearly defined learning objectives and includes
exercises and solutions, and is therefore also useful for self-learning.
The lesson material is licensed under `CC-BY-4.0
<https://creativecommons.org/licenses/by/4.0/>`_ and can be reused in any form
(with appropriate credit) in other courses and workshops.

Interacting with the notebooks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`MyBinder <https://mybinder.org/>`_ offers a free, customizable cloud
computing environment and powers some of the contents of this lesson.
You can run the entirety of Exercise 1 and most of Exercise 2 of this
tutorial in the cloud.

The MyBinder web interface
~~~~~~~~~~~~~~~~~~~~~~~~~~

You can access the JupyterLab instance for this workshop by clicking the "launch
binder" button at the top of the ``README`` file displayed at
https://github.com/MRChemSoft/multiwavelet-tutorial

.. figure:: img/launch_binder_button.png
   :scale: 70%
   :alt: Launching the binder
   :align: center

This will bring you to the loading page for the binder, which might
take a few minutes to start up. Once loaded you will end up in a
Jupyter-Lab environment with all necessary software packages installed.
Bevare that the cloud instance runs on limited computational resources,
so don't expect awesome performance. Also, launching full-fledged MRChem
calculations on molecules containing more than a few atoms is probably a
bad idea.

Accessing a terminal
++++++++++++++++++++

From the "Launcher" tab, you can access terminal, Python interpreter, and notebook launchers:

.. figure:: img/launcher_menu.png
   :scale: 50%
   :alt: Launcher menu on Jupyter Lab
   :align: center

You can open a text editor (for input files etc) by clicking "New" and
select Text File. If you prefer a terminal editor, you can use ``nano`` or
``vim`` or ``emacs``.

Starting the notebook from an episode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can run the notebook directly from an episode in the lesson. Click on the
rocket icon on the top right of the page and select which launcher to use:

.. figure:: img/launchers.png
   :scale: 50%
   :alt: Launcher menu on Jupyter Lab
   :align: center

"Binder" will redirect you the binder instance. With "Live code", you can run
and modify the code cells within the webpage.
The "Live code" option is powered by `sphinx-thebe <https://github.com/executablebooks/sphinx-thebe>`_ and, behind the scenes,
MyBinder. Be aware that you will not be able to add new code cells in a live
session.

.. _see-also:

See also
--------

There are many free resources online regarding Python and Jupyter:

- The `MolSSI <http://molssi.org/>`_  introductory course on `Python scripting
  for computational molecular science
  <https://education.molssi.org/python_scripting_cms/>`_.
- The `Aalto Scientific Computing <https://scicomp.aalto.fi/>`_ course on `Python for scientific
  computing <https://aaltoscicomp.github.io/python-for-scicomp/>`_.
- The `CodeRefinery <https://coderefinery.org/>`_ course `Introduction to
  Jupyter and JupyterLab <https://coderefinery.github.io/jupyter/>`_


Credits
-------

The lesson file structure and layout is heavily inspired by
the `VeloxChem workshop <https://enccs.github.io/veloxchem-workshop/>`_ developed by
`EuroCC National Competence Center Sweden (ENCCS) <https://enccs.se/>`_ and the
`PDC Center for High Performance Computing <https://www.pdc.kth.se/>`_, which in turn
is derived from `work <https://github.com/coderefinery/sphinx-lesson>`_ by `CodeRefinery
<https://coderefinery.org/>`_ licensed under the `MIT license
<http://opensource.org/licenses/mit-license.html>`_. We have copied and adapted
most of their license text.

Instructional Material
^^^^^^^^^^^^^^^^^^^^^^

This instructional material is made available under the `Creative Commons
Attribution license (CC-BY-4.0)
<https://creativecommons.org/licenses/by/4.0/>`_. The following is a
human-readable summary of (and not a substitute for) the `full legal text of the
CC-BY-4.0 license <https://creativecommons.org/licenses/by/4.0/legalcode>`_.
You are free:

- to **share** - copy and redistribute the material in any medium or format
- to **adapt** - remix, transform, and build upon the material for any purpose,
  even commercially.

The licensor cannot revoke these freedoms as long as you follow these license terms:

- **Attribution** - You must give appropriate credit (mentioning that your work
  is derived from work that is Copyright (c) ENCCS and, where practical, linking
  to `<https://enccs.se>`_), provide a `link to the license
  <https://creativecommons.org/licenses/by/4.0/>`_, and indicate if changes were
  made. You may do so in any reasonable manner, but not in any way that suggests
  the licensor endorses you or your use.
- **No additional restrictions** - You may not apply legal terms or
  technological measures that legally restrict others from doing anything the
  license permits. With the understanding that:

  - You do not have to comply with the license for elements of the material in
    the public domain or where your use is permitted by an applicable exception
    or limitation.
  - No warranties are given. The license may not give you all of the permissions
    necessary for your intended use. For example, other rights such as
    publicity, privacy, or moral rights may limit how you use the material.


Software
^^^^^^^^

Except where otherwise noted, the example programs and other software provided
with this repository are made available under the `OSI <http://opensource.org/>`_-approved
`MIT license <http://opensource.org/licenses/mit-license.html>`_.
