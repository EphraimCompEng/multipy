.. _guide:
==========
User Guide
==========



soon™

(below is an incomplete guide which will grow with the project.)


Contents
--------

- :ref:`setup`
- :ref:`remap`
- :ref:`define_algorithm`
- :ref:`use_algorithm`






**Setup**

- import multipy as mp
- create matrix
- create algorithm object

**Reduce & Map**

- create patterns and templates
- create maps
-

**Define Algorithm**

**Use Algorithm**

Algorithm process:
0: Generate logical AND matrix
1: split matrix
2: apply template, update state
3: generate result
4: optionally apply map
5: update matrix
6: GOTO 1:


.. _setup:
Setup
-----
MultiPy focuses on combinational multiplication, fine-grained control over algorithms, and the choice of making algorithms entirely by hand or using build-in building blocks.

Recommended resources before starting:

.. hlist::
    :columns: 3

    * `Binary Multipliers <https://en.wikipedia.org/wiki/Binary_multiplier>`_
    * `Wallace Tree <https://en.wikipedia.org/wiki/Wallace_tree>`_
    * `Teman, A. Fast Multipliers <https://youtu.be/4FwESTOVT-o/>`_


Import
~~~~~~

First, import multipy and decide on a bitwidth for our algorithm, to keep it simple let's pick 4-bits:

.. code-block:: python

    import multipy as mp
    matrix = mp.Matrix(4) # 4-bit logical AND matrix

Here's what it looks like:

.. code-block:: python

    print(matrix.matrix)

.. code-block:: python

    ____0000
    ___0000_
    __0000__
    _0000___


The ``matrix`` is a "structure" used to generate the logical AND matrix, aka partial products, for a given set of inputs. It also tells the algorithm *where* each partial product is located.

.. note::
    To populate an AND matrix without an Algorithm object use:

    .. code-block:: python

        matrix = mp.build_matrix(operand_a=0, operand_b=0, bits=4)



Next, create an algorithm object.

.. code-block:: python

    first_alg = mp.Algorithm(matrix)

The Algorithm object will hold the templates that define a given algorithm. It also holds an internal state to track which template it should use next.

.. _remap:
Reduce & Map
------------

Now let's make some templates. This involves figuring out where you want to place:

- Carry Save Adders -- CSA (Half Adders, HA, are automtically placed when using simple templates) [3 to 2]
- Adders -- [2 to 1]
and in the future:

- Decoders -- [n to n-k]
- Greedy Adders -- Adder which makes use of carry in (cin) [2 to 1]

All of which reduce a set of partial products by 1, each with their characteristics in latency, complexity and size. None of this applies to Multipy.
Decoders are an exception and can potentially reduce a set of partial products by more than 1.

To inform the algorithm on how a given template reduces groups of partial products, an array of characters, or pattern is used:

.. code-block:: python

    pattern = [
        a,      # +-
        a,      # | run of 3 == CSA [3 to 2]
        a,      # +-
        b,      # +- run of 1 == None -- no reduction needed
    ]

.. note::
    It is recommended to write patterns vertically to make it clear how rows are effected.

For this 4-bit multiplier algorithm it will take 3 rounds, minimum, of reductions to reach out final output:

.. code-block:: text

    # Patterns for each stage of first_alg

    1st:    2nd:    3rd:    output:

    a       _       _
    a       c       _
    a       c       d
    b       c       d       x

.. note::
    Multipy will allow you to make any algorithm, even if it's sub-optimal.

Each step needs a pattern or a template, but they also need to regoup their partial products. This is where maps come in.

First, note that bits can only move vertically as moving horizontally changes it's value. Therefore, each map value is a signed hexadecimal number.
For simple maps, the map value represents an entire row rather than a specific bit.

.. code-block:: text

    # Maps for each stage of first_alg

    1st:    2nd:    3rd:

    FF      __      __
    FF      FF      __
    00      FF      00
    00      00      00


Algorithms use a template to produce a result, which is then "mapped" to the next template. Each Adder/CSA/etc. needs to know where it needs to be in relation to the next template.
This means as long as output is mapped to input the final output (x from the pattern example) can be anywhere within the matrix. Here's the breakdown of this example:

1st stage - the first two rows of the result are being move by -1 == FF.

2nd stage - each row of the result will be moved again by -1

3rd stage - No moves required, as long as output is within the matrix.






.. _define_algorithm:
Define Algorithm
----------------


.. _use_algorithm:
Use Algorithm
-------------
