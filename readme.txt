# The SIF(n) Project

SIF(n) or Self Interacting Feynmans of n-th order is a Python program that calculates any possible
Feynman Diagrams for a n1 -> n2 particle scattering for any n-theory self interacting field at any
order of approximation.

## Usage

To get a list of encoded information on Feynman Diagrams use the CreateFeynmanDiagrams() function.

For example:
The Feynman Diagrams of a 4-theory 2 -> 2 scattering up to a k_term order

```python
CreateFeynmanDiagrams(n_power = 4, k_term = 2, ni = 2, nf = 2)
```