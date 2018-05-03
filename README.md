# Bespoke Learning

Have you ever felt overwhelmed when trying to break into a new field? Maybe you have a high level understanding of a
subject area, but you aren't familiar with the literature?

The purpose of this code is to spark an exploration of how academic citation networks can be analyzed to produce
reasonable reading and learning goals, whether the Learner (you, your colleagues, and the students of the future) is
just now coming into his or her field of study, or is versed in the basics of a subject but can't quite decipher
the specifics of a specific paper.

## Approaches
There are two approaches here now. Both make some assumptions about citation networks that haven't been thoroughly
explored yet, but seem like intuitive steps.

### Base Building
How should a learner attack a new field once they feel ready to dive into some seminal research papers?

I think it's reasonable to start with the papers with the most citations (which we think of as outgoing edges in a
citation network where papers are vertices). These are the survey papers that will generally give insight into the
state of research in the domain of the topic at the time of writing, and can serve as reference for direction later
on. Here the learner will develop an idea of the structure of the topic's research efforts.

Next, it may be appropriate to begin reading papers that are cited most by others (vertices with the highest in-degree).
These will be more 'popular' papers that a learner breaking into the field would likely be expected to recognize, and
the results of these papers are the most likely to be influential in the field's past and/or current research meta.

### New Papers: Touching Base
How should a learner approach a new paper? This approach targets learners who have a footing in the knowledge base
described above. This learner should be able to work forwards from the base down a directed acyclic citation graph
towards the new paper, but reading every paper along every path from the set of vertices B to the target paper t
is daunting, and frankly unreasonable. The approach I took with this code works backwards from t towards the vertices
in B by adding at most b best neighbors of t (references, in t, to past papers) sorted by Katz centrality (highest first).

In citation networks, I've assumed that following paths of a few most central neighbors will yield a reasonably sized DAG
that a learner can digest in a 'reasonable' amount of time. It could downright ignore important citations in any of the
n-b other neighbors (and probably does). Maybe the top quarter of a node's neighbors should be added to the queue instead!

This code began as a component of my final project in ECE 498 Network Science: Dynamics and Flow at UIUC.
