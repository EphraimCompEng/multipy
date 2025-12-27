# Data Structure
___
The representation of a combinational multiplier.


# AND Matrix
___
The AND matrix is a 2D array of bits that represents the AND operation between two input values. Each element in the matrix is the result of the AND operation between the corresponding bits of the two input values.

## Structure

[ Stage 0 ]

```
       overflow|valid
       --------+-----------
        -------|00000000
        ------0|0000000-
        -----00|000000--
        ----000|00000---
        ---0000|0000----
        --00000|000-----
        -000000|00------
        0000000|0-------
```

# Partial Product Reduction
___
The partial product reduction stage reduces the number of partial products across multiple stages, eventually all products are reduced to one output.


## Structure

### Stages

Each stage of a multiplier must reduce the number of partial products. 


A naive approach could look like this:

[ Stage 0 ]
The AND matrix produces initial set of partial products, and the each template isolates 2 rows at a time:
```
        -------|00000000
        ------0|0000000-
```
```
        -----00|000000--
        ----000|00000---
```
```
        ---0000|0000----
        --00000|000-----
```
```
        -000000|00------
        0000000|0-------
```

[ Stage 1 ]
Each group of partial products are reduced, via additions, and are grouped for the next stage:
```
        -----00|00000000
        ---0000|00000---
```
```
        -000000|0000----
       00000000|00------
```

[ Stage n ]
The final reduction results in a single complete value:

```
       00000000|00000000
```


In the [original](first/init/) program data was stored in json and could easily be prettified. However, working the stored structures seemed impossible and the project ended there. This time round there will be a big focus on data structures, allowing for robust analytics, as well as human readable data using matplotlib.

- [ ] Find optimal data structure for combinational multiply stages

### Templates

As mentioned above, each stage recieves a template to dictate how partial products are grouped and operated on. 

Templates need to be simple enough to configure, possibly in a CLI but the main focus is on a configuration file. 

- [ ] Standardise templates


<!--

```

    Here are scenarios I want to like to test:

    Type I
    a) Input values < 255
    b) Input pairs which do not cross overflow threshold during
       AND-matrix

       overflow|valid
       --------+-----------
        -------|00000000
        ------0|0000000-
        -----00|000000--
        ----000|00000---
        ---0000|0000----
        --00000|000-----
        -000000|00------
        0000000|0-------

    c) Input pairs which overflow in partial product reduction


```-->
