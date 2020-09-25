# Reinforcement Learning

The problem in reinforcement learning is to find rules about _what_ to do in _which_ situation.
Now, how do we find such a rulebook?
We test.

## How is this accomplished?

This algorithm starts out without any knowledge about what could be a smart move in any given scenario.
We start by testing out various actions and with time and more practice the algorithm refines it's understanding of the world around him.
The astonishing thing about the Q Updates strategy is, that throughout all of this the algorithm, _in fact_, doesn't know anything about it's surroundings. Well, it knows suprisingly little, while still performing beautifully.
Throughout testing it (a so called `agent`) memorized how much benefit any given move had (given the situation the agent finds himself in) and that's already it. Without any idea about what happens after the agent performs an action, it can still infer the "right thing to do".

## Why have I coded this?
I felt a deep appreciation for the simplistic nature of this reinforcement learning algorithm which sparked a desire to formulate it as code and share my attempt. Only needing so little Information makes this strategy breathtakingly efficient and it's even feasable to be used in computers or microcontrollers without much power. (Though having a lot computational power tends to be much fun)

## How can we improve this algorithm further?
Learning smarter:
I already told you that the agent learns by doing. Now, this implementation of an Reinforcement Learning agent just does anything random. It literally doesn't care about what it is doing throughout all of testing.
This is a very simple strategy, but not the best one. One might say, that performing yet untested actions holds more information or one could keep track of the relations between actions and their outcomes while training to infer which actions would yield the most interesting results.

Learning addaptive:
Right now there is no concept of "novelty" in the learning process.
Ideally the agent would put much greater emphasis on the first few bits of information it learns, than on the 1000000th one. Right now, this has to be dealt with manually (by controlling the `falloff` value in q udaptes). The reason for this is, that it's a rather complicated side problem, when to lower the emphasis on new information (in relation to an existing hypothesis/model of the world).
