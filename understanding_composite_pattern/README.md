This is a new pattern called CompositePattern. It is just a term which is used to throw people off.
We will refer to this pattern as TreePattern, because essentially this is a f**king tree.

So, there are three major portions of these pattern
1. Component
2. Leaf
3. Composite

Now, read these lines carefully.
1. LEAF IS-A COMPONENT
2. COMPOSITE IS-A COMPONENT
3. COMPONENT IS-A COMPONENT
4. COMPOSITE HAS-A COMPONENT
5. LEAF DOES NOT HAVE A COMPONENT
6. CLIENT ALWAYS TALKS TO COMPONENT

Whenever you feel a TREE like structure is emerging, try and use this composite pattern.
{Generally you wont be able to notice this pattern easily as it is one of the difficult patterns
to notice. But it is a very strong pattern, because if implemented carefully this can lead good
results}