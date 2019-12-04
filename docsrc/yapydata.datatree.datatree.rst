
.. _DATATREE_DATATREE:

.. raw:: html

   <div class="shortcuttab">


yapydata.datatree.datatree
==========================
The module 'datatree.datatree' implements the actual access to structured in-memory data.
The data is implemented by a subset of Python data types as a canonical in-memory
structure comaptible to the standard package *json*.
The specific modules for the supported syntaxes extend the required methods.

Module
------

.. automodule:: yapydata.datatree.datatree

Sources: `yapydata/datatree/datatree.py <_modules/yapydata/datatree/datatree.html#>`_


Functions
---------

grow_branch
^^^^^^^^^^^
.. automethod:: yapydata.datatree.datatree.grow_branch


readout_data
^^^^^^^^^^^^
.. autofunction::  yapydata.datatree.datatree.readout_data


DataTree
--------

.. autoclass:: yapydata.datatree.datatree.DataTree 

__init__
^^^^^^^^
.. automethod:: yapydata.datatree.datatree.DataTree.__init__

__call__
^^^^^^^^
.. automethod:: yapydata.datatree.datatree.DataTree.__call__ 

create
^^^^^^
.. automethod:: yapydata.datatree.datatree.DataTree.create

get
^^^
.. automethod:: yapydata.datatree.datatree.DataTree.get

isvalid_top
^^^^^^^^^^^
.. automethod:: yapydata.datatree.datatree.DataTree.isvalid_top

join
^^^^
.. automethod:: yapydata.datatree.datatree.DataTree.join

import_data
^^^^^^^^^^^
.. automethod:: yapydata.datatree.datatree.DataTree.import_data


Exceptions
----------

.. autoexception:: yapydata.datatree.datatree.YapyDataDataTreeError

s.. autoexception:: yapydata.datatree.datatree.YapyDataDataTreeOidError

.. raw:: html

   </div>


