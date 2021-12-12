import itertools

def getGroups(lst: list):
    N = len(lst)
    choice_indices = itertools.product(*[
        range(k) for k in reversed(range(1, N, 2))])

    for choice in choice_indices:
        tmp = lst[:]
        result = []

        for index in choice:
            result.append((tmp.pop(0), tmp.pop(index)))
        yield result

def checkForSame(lst: list) -> bool:
  for pair in lst:
    if pair[0][:2] == pair[1][:2] and pair[0][0] != "F":
      return False
  
  return True

def getUniqueContributions(n_power: int, k_term: int, ni: int, nf: int):
  integralTerms = [f"a_{i +1}" for i in range(ni)]
  integralTerms += [f"F_{j +1}" for j in range(k_term) for i in range(n_power)]
  integralTerms += [f"b_{i +ni +1}" for i in range(nf)]

  diagram_terms = list(getGroups(integralTerms))

  # Filtering
  diagram_terms = list(filter(checkForSame, diagram_terms))
  for i in diagram_terms:
    i.sort(key = lambda a: a[1])

  final_terms = []
  [final_terms.append(x) for x in diagram_terms if x not in final_terms]
  
  return final_terms

def calculateFeynmanNodes(n_power: int, k_term: int, ni: int, nf: int):
  if (n_power * k_term +ni +nf) % 2 != 0:
    return []
  
  a = getUniqueContributions(n_power, k_term, ni, nf)
  
  return a

# def createFeynmanDiagrams(n_power: int, k_term: int, ni: int, nf: int):
#   if (n_power * k_term +ni +nf) % 2 != 0:
#     return []
  
#   a = getUniqueContributions(n_power, k_term, ni, nf)
  
#   return a