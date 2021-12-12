# Self Interacting Feynman Diagrams of n-th order

SIF(n) or Self Interacting Feynmans of n-th order is a Python program that calculates any possible
Feynman Diagrams for a $n_1 \rightarrow n_2$ particle scattering for any n-theory self interacting field at any
order of approximation.

## Usage

To get a list of encoded information on Feynman Diagrams use the CreateFeynmanDiagrams() function.

For example:

The Feynman Diagrams of a 4-theory $2 \rightarrow 2$ scattering up to a k_term order.

```python
CreateFeynmanDiagrams(n_power = 4, k_term = 2, ni = 2, nf = 2)
```

## Todo

The code currently only calculates the connection between the nodes of the Feynman diagrams in symbolic notation
and does not draw the diagrams. This requires further suport.