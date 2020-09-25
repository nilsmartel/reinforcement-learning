import math

def randomElement(l):
    s = len(l)

    return l[s*math.random()]


def maxValue(d):
    n = -math.inf
    for (k, v) in d:
        n = max(n, v)

    return n

def maxKey(d):
    n = -math.inf
    key = None
    for (k,v) in d:
        if v > n:
            n = v
            key = k

    return key


def emptyHeuristic(states, actions):
    policy = dict()

    for s in states:
        d = dict()
        for a in actions:
            d[a] = 0.0

        policy[s] = d

    return policy

# Solves a Problem using Reinforcement Learning
# by performing Q-Updates
class RLProblem:
    # states: [States]
    # actions: [Action]
    # performAction: (State, Action) -> (Action, reward = Number)
    def __init__(self, states, actions,  performAction):
        self.states = states
        self.actions = actions
        self.performAction = performAction

        # TODO figure reward with random policy for
        # choosing actions
        # use Q updates

        self.heuristic = emptyHeuristic(states, actions)
        self.policy = dict()
        for s in states:
            self.policy[s] = randomElement(actions)

    # The actual learning process.
    # Using q Updates the policy of the agent get's further an further refined
    def qUpdate(self, steps, initialState, cutoff):
        state = initialState
        while steps > 0:
            steps -= 1
            action = randomElement(self.actions)
            (nextState, reward) = self.performAction(state, action)

            if nextState == None:
                return

            self.heuristic[state][action] = cutoff*reward + (1-cutoff)*maxValue(self.heuristic[nextState])
            state = nextState

    # returns the policy aquired via reinforcement learning.
    # One needs to perform various Q-Updates before receiving a policy that's
    # any good. How many episodes are needed depends on the problem.
    def getPolicy(self):
        policy = dict()
        for s in self.states:
            policy[s] = maxKey(self.heuristic[s])
