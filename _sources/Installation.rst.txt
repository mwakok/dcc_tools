Installation
''''''''''''

Create environment
------------------

I recommend installing ``ghproject`` inside a conda environment:

.. code-block:: console

    # Create a conda environment
    git clone https://github.com/mwakok/ghprojects.git
    conda env create -f environment.yml
    conda activate env_ghproject

To then install the ``ghproject``:

.. code-block:: console

    # Install ghproject package
    cd ghproject
    pip install .


Uninstalling
''''''''''''

If you want to remove your ``ghproject`` installation together with the conda environment, please follwo these steps:

.. code-block:: console

   # Removing ghproject.
   pip uninstall ghproject

   # Step out the environments.
   conda deactivate

   # List all the active environments. ghproject should be listed.
   conda env list

   # Remove the findpeaks environment
   conda env remove --name ghproject

   # List all the active environments. ghproject should be absent.
   conda env list