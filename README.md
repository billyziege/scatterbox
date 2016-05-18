# scatterbox
This is code to be run in vpython.  Two versions of the code exist.  An all included code in scatterbox/scatterbox.py and a modular code in main.py with modules in scatterbox/physics.py, scatterbox/interupt.py, and scatterbox/particle.py.

To run main.py, you will probably  need to install the modules into python (Need to check this).  Do so with

python setup.py develop

This will create links to the modules in the scatterbox directory to your python site-packages allowing any edits to automatically appear when running Vpython.

Then open main.py in VIDLE and run the module.

To output the energy and momentum of the system while the simulation is running, hit the "s" key.  To toggle the smaller balls from visible to and from invisible, hit the "v" key.  To exit the simulation, hit the "x" key.
