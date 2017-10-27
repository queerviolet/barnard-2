def subsets(s):
  if not s:
    return set([ frozenset() ])
  first = s.__iter__().next()
  without_first = set(s)
  without_first.remove(first)
  output = set()
  for subset in subsets(without_first):
    output.add(frozenset(subset))
    with_first = set(subset)
    with_first.add(first)
    output.add(frozenset(with_first))
  return output

def subsets2(s):
  for i in xrange(2 ** len(s)):
    yield subsetWithIndex(s, i)

def subsetWithIndex(input, i):
  return frozenset(x for (b, x) in enumerate(input) if (i >> b) & 1)

s = set([1,2,3])
print subsets(s)
print set(subsets2(s))
assert len(subsets(s)) == len(set(subsets2(s)))
  
  