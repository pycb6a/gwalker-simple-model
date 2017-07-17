Graph Walker Simple Model
=========================

:Source code: https://bitbucket.org/pycb6a/gwalker-simple-model

Install
-------

::

    hg clone https://pycb6a@bitbucket.org/pycb6a/gwalker-simple-model

    cd gwalker-simple-model

    pip install --editable .


Usage
-----

::

    java -jar graphwalker-cli-3.4.2.jar -d all online -s RESTFUL -m small_model.graphml "random(edge_coverage(100))"

    gwalker-simple-model

