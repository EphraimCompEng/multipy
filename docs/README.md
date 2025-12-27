# Multiplier Saturation
A project to aid research in the saturation of multipliers.

# Why?

This project was initially focused on how [saturation](https://en.wikipedia.org/wiki/Saturation_arithmetic) allows for the optimisation of a combinational [multiplier](https://en.wikipedia.org/wiki/Binary_multiplier). Once saturation is introduced, calculating the ceiling, or overflow, becomes extremely fast for one range of inputs. Another range always produces values within the extremes. The remaining range of inputs may or may not fall outside the extremes. Finding ways to predict if a given input results in an overflow, as early as possible, will result in faster calculations.

Generating and analysing designs by hand is labour intensive even for small datasets. For entire [truth tables](https://en.wikipedia.org/wiki/Truth_table), this becomes close to impossible after 8-bits.

## Combinational Multipliers

A combinational multiplier starts by creating all possible partial products. Then, reduces the number of partial products across multiple stages, eventually all products are reduced to one output.

For example, using a [Wallice tree](https://en.wikipedia.org/wiki/Wallice_tree)  to multiply 11 * 12: 

```
11 * 12 -> 0b1011 * 0b1100
```

Can be represented like so:
```
        1011
   [____0000] 0
   [___0000_] 0
   [__1011__] 1
   [_1011___] 1
   ----------
0b [10000100] -> 132
```

This is oversimplified and only 4-bit, but you get the idea.

Note that for any multiplication the output can be upto **2x** the input width.


## Saturation

Using the 11 * 12 example above, if the output was saturated to 4-bits, the result would be 15 since the maximum value is 0b1111 -> 15.
Typically, saturation restricts the output bit width to the input bit width. 

This project will work towards:
  - 8-bit with and without saturation 
  - 16-bit with saturation
