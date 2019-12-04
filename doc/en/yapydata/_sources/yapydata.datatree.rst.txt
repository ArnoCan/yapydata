
.. _DATATREE_INIT:

.. raw:: html

   <div class="shortcuttab">


yapydata.datatree.__init__
==========================
The subpackage 'yapydata.datatree' implements the homogeneous access to abstract data 
based on various syntaxes.
The data is implemented by a canonical subset of *Python* data types organized in layouts of
nested trees of one or more data nodes.

The base set of valid nodes comprising all permitted Python data types is adapted to
additional semantical constraints and structural extension by derived syntax modules.
The provided syntax standard modules are:

* **Python** - The core module supporting the full scope of *Python* data 
  with access to in-memory data only.

* **INI** - The extended ini-file format based on the standard configuration parser.
  The extended support includes the syntax elements of standard *JSON*.
  The data is finally read out as *JSON* compliant data. 
   
* **JSON** - The standard *JSON* syntax and data layout as provided by the standard
  module.

* **XML** - The standard *XML* format adapted to a common shared format in order to
  allow maximum semantic interchangeability. 
  The data is finally read out as *JSON* compliant data. 

* **YAML** - The common *YAML* library - *PyYAML* - is utilized as the parser.  
  The data is finally read out as *JSON* compliant data. 

* **Java-Properties** - The standard format of the common *Java* configuration
  syntax of *.properties*.
  The syntax is extended in order to comply with the data layout of the
  standard *json* package.
  The data is finally read out as *JSON* compliant data. 

The provided syntax modules by default comply to a subset of syntax elements supported
by *JSON*, these could be optionally switched into their specific syntax scopes.
Either by reduction - e.g. *INI* - or by extension, e.g. *YAML*.

The following in-memory access to the data tree elements is provided.
Where these provide either intermediate nodes as branches, or end nodes
as leafs.

.. raw:: html

   <style>
      div.tmptabmodules1 table td:nth-child(2) {
         background: lightgrey;
         border: none;
      }
      
   </style>

   <div class="tmptabmodules1">

   <div class="nonbreakheadtab">
   <div class="autocolumntab">


+---------------+--------+-----+------+-----+-----+-----+-----+-----+
| type          | Python |     | JSON |     | XML |     | INI |     |
+---------------+--------+-----+------+-----+-----+-----+-----+-----+
|               | sub    | end | sub  | end | sub | end | sub | end |
+===============+========+=====+======+=====+=====+=====+=====+=====+
| list          | rw     | rw  | rw   | rw  | rw  | rw  |     |     |
+---------------+--------+-----+------+-----+-----+-----+-----+-----+
| dict          | rw     | rw  | rw   | rw  | rw  | rw  |     |     |
+---------------+--------+-----+------+-----+-----+-----+-----+-----+
| tuple         | r      | rw  | --   | --  | --  | --  | --  | --  |
+---------------+--------+-----+------+-----+-----+-----+-----+-----+
| set           | --     | rw  | --   | --  | --  | --  | --  | --  |
+---------------+--------+-----+------+-----+-----+-----+-----+-----+
| frozenset     | --     | rw  | --   | --  | --  | --  | --  | --  |
+---------------+--------+-----+------+-----+-----+-----+-----+-----+
| bytearray (1) | rw     | rw  | --   | --  | --  | --  | --  | --  |
+---------------+--------+-----+------+-----+-----+-----+-----+-----+
| str       (2) | r      | rw  | r    | rw  | r   | rw  | r   | rw  |
+---------------+--------+-----+------+-----+-----+-----+-----+-----+
| int           | --     | rw  | --   | rw  | --  | rw  | --  | rw  |
+---------------+--------+-----+------+-----+-----+-----+-----+-----+
| float         | --     | rw  | --   | rw  | --  | rw  | --  | rw  |
+---------------+--------+-----+------+-----+-----+-----+-----+-----+
| True          | --     | rw  | --   | rw  | --  | rw  | --  | rw  |
+---------------+--------+-----+------+-----+-----+-----+-----+-----+
| False         | --     | rw  | --   | rw  | --  | rw  | --  | rw  |
+---------------+--------+-----+------+-----+-----+-----+-----+-----+
| None          | --     | rw  | --   | rw  | --  | rw  | --  | rw  |
+---------------+--------+-----+------+-----+-----+-----+-----+-----+

.. raw:: html

   </div>
   </div>
   </div>

**sub**: subpath entry nodes - branches; used as intermediate nodes by subscriptions

**end**: endnodes - leafs; treated as a single data antry

**r**: native read access

**w**: native write acces

**(1)**: *bytearray* supports only one nested level - the byte

**(2)**: *str* supports for subscription read-only access of one nested level

The supported syntaxes either provide the full scope of *JSON*, or could be easily
extended to do so.

.. raw:: html

   <style>
      div.tmptabmodules1 table td:nth-child(2) {
         background: lightgrey;
         border: none;
      }
      
   </style>

   <div class="tmptabmodules1">

   <div class="nonbreakheadtab">
   <div class="autocolumntab">

+----------------+--------+------+-----+-----+------+------+
| syntax element | Python | JSON | XML | INI | PROP | YAML |
+================+========+======+=====+=====+======+======+
| list           | y      | y    | y   | c   | c    | y    |
+----------------+--------+------+-----+-----+------+------+
| dict           | y      | y    | y   | c   | c    | y    |
+----------------+--------+------+-----+-----+------+------+
| tuple          | y      | --   | --  | o   | o    | --   |
+----------------+--------+------+-----+-----+------+------+
| set            | y      | --   | --  | o   | o    | --   |
+----------------+--------+------+-----+-----+------+------+
| frozenset      | y      | --   | --  | o   | o    | --   |
+----------------+--------+------+-----+-----+------+------+
| bytearray (1)  | y      | --   | --  | o   | o    | --   |
+----------------+--------+------+-----+-----+------+------+
| str       (2)  | y      | y    | y   | y   | y    | y    |
+----------------+--------+------+-----+-----+------+------+
| int            | y      | y    | y   | c   | c    | y    |
+----------------+--------+------+-----+-----+------+------+
| float          | y      | y    | y   | c   | c    | y    |
+----------------+--------+------+-----+-----+------+------+
| True           | y      | y    | c   | c   | c    | y    |
+----------------+--------+------+-----+-----+------+------+
| False          | y      | y    | c   | c   | c    | y    |
+----------------+--------+------+-----+-----+------+------+
| None           | y      | y    | c   | c   | c    | y    |
+----------------+--------+------+-----+-----+------+------+

.. raw:: html

   </div>
   </div>
   </div>

**y**: Native support.

**c**: Custom default extension - assures cross-compatibility.

**o**: Optional extension - breaking cross-compatibility.

Some minor differences remain in case of the data structure.
This is results from the difference of the production rules 
in particular defined for *XML*.
Beneath the presence of the attributes and content data, which
could be used in most cases interchageably,
the top production of the XML syntax requires an element.
The elemnt consists in case of a non-empty document of a containing
tag-pair and a value, or a short-tag with attributes.
In both cases resulting in a named top node as root-container.
Definitions like e.g. *JSON* do not have a named top node, in
case e.g. of [RFC7159]_ even a pure value such as *int* as
the only document root is permitted. 
This makes for the technical implementation a difference to be
handeled when multiple implementation syntaxes for a given semantic data set
are used.

The following table depicts the structural differences of data-trees.

.. raw:: html

   <style>
      div.tmptabmodules1 table td:nth-child(2) {
         background: lightgrey;
         border: none;
      }
      
   </style>

   <div class="tmptabmodules1">

   <div class="nonbreakheadtab">
   <div class="autocolumntab">

+----------------------------------+--------+------+-----+-----+------+------+
| syntax element                   | Python | JSON | XML | INI | PROP | YAML |
+==================================+========+======+=====+=====+======+======+
| top-as-pure-nameless-object/dict | y      | y    | --  | --  | --   | y    |
+----------------------------------+--------+------+-----+-----+------+------+
| top-as-pure-nameless-list/array  | y      | y    | --  | --  | --   | y    |
+----------------------------------+--------+------+-----+-----+------+------+
| top-as-pure-int                  | --     | y    | --  | --  | --   | y    |
+----------------------------------+--------+------+-----+-----+------+------+
| top-as-pure-float                | --     | y    | --  | --  | --   | y    |
+----------------------------------+--------+------+-----+-----+------+------+
| top-as-pure-str                  | --     | y    | --  | --  | --   | y    |
+----------------------------------+--------+------+-----+-----+------+------+
| top-as-named-node                | y      | --   | y   | y   | y    |      |
+----------------------------------+--------+------+-----+-----+------+------+
| nodes-with-fixed-type            | y      | y    | --  | c   | c    | y    |
+----------------------------------+--------+------+-----+-----+------+------+

.. raw:: html

   </div>
   </div>
   </div>

The modules provide a compatibility mode, where either a named top-node is inserted,
or silently dropped.
The other option is to keep the marginal differences and let it handle by the caller.

Similar differences remain by basically typeless formats, where the actual type is defined
by the application, while the parser by default handles all data as strings - consisting
e.g. of letters and/or digits.
The provided syntax scanners apply here a maximum-plausible assumption in order to
gain syntax independent in-memory data based on common meta-types.
Thus digit-only values are treated as *int*, digits with punctuation as floats.
While the presence of a character forces a pure string as type.
In case of *INI* syntax custom extension is added for *list* and *dict* types
based either on context, or forced by the introduced keywords *list* and *dict*.

Module
------

.. automodule:: yapydata.datatree

Sources: `yapydata/datatree/__init__.py <_modules/yapydata/datatree/__init__.html#>`_



Exceptions
----------

.. autoexception:: yapydata.datatree.YapyDataError

.. raw:: html

   </div>

