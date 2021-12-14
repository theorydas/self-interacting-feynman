import itertools

def getGroups(lst: list) -> list:
    N = len(lst)
    choice_indices = itertools.product(*[range(k) for k in reversed(range(1, N, 2))])

    for choice in choice_indices:
        tmp = lst[:]
        result = []

        for index in choice:
            result.append((tmp.pop(0), tmp.pop(index)))
        yield result

def checkForSame(lst: list) -> bool:
  """ Iterates through pairs of nodes to find if any correspond to the same diagram. """
  for pair in lst:
    if pair[0][:2] == pair[1][:2] and pair[0][0] != "F":
      return False
  
  return True

def getUniqueContributions(n_power: int, k_term: int, ni: int, nf: int) -> list:
  integralTerms = [f"a_{i +1}" for i in range(ni)] # Starting particles.
  integralTerms += [f"F_{j +1}" for j in range(k_term) for i in range(n_power)] # Mediators
  integralTerms += [f"b_{i +ni +1}" for i in range(nf)] # Final particles.

  diagram_terms = list(getGroups(integralTerms))

  # Filtering
  diagram_terms = list(filter(checkForSame, diagram_terms))
  for i in diagram_terms:
    i.sort(key = lambda a: a[1])

  final_terms = []
  [final_terms.append(x) for x in diagram_terms if x not in final_terms]
  
  return final_terms

def calculateFeynmanNodes(n_theory: int, k_term: int, ni: int, nf: int) -> list:
  """ Calculates the unique Feynman nodes of the n-theory interaction and returns a list
  of all possible diagrams in symbolic notation.
  
  ### Parameters
  n_theory : {int}
    The power of the interaction describing the n-theory.
  k_term : {int}
    The amount of mediators inbetween the particles.
  ni : {int}
    The amount of starting particles.
  nf : {int}
    The amount of final particles.
  
  ### Returns
  unique_nodes : {list}
    A list of symbolic notation for the connected nodes of each available Feynman diagram on the theory.
  """
  # Return an empty list when no valid Feynman diagrams can be drawn.
  if (n_theory * k_term +ni +nf) % 2 != 0:
    return []
  
  return getUniqueContributions(n_theory, k_term, ni, nf)