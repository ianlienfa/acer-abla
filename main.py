import brain
import agent
from torch import multiprocessing as mp
from core import *
import sys



def run_agent(shared_brain, render=False, verbose=False):
    """
    Run the agent.

    Parameters
    ----------
    shared_brain : brain.Brain
        The shared brain the agents will use and update.
    render : boolean, optional
        Should the agent render its actions in the on-policy phase?
    verbose : boolean, optional
        Should the agent print progress to the console?
    """
    if CONTROL is 'discrete':
        local_agent = agent.DiscreteAgent(shared_brain, render, verbose)
    else:
        local_agent = agent.ContinuousAgent(shared_brain, render, verbose)
    local_agent.run()

def create_history_files(filename="reward"):
    # filename = "rewards" + filename
    filename += ".txt"
    f = open(filename, 'w')
    f.close()

if __name__ == "__main__":
    if(len(sys.argv) >= 4):
        if(sys.argv[2] == "-f"):
            create_history_files(sys.argv[3])
    else:
        create_history_files()

    if NUMBER_OF_AGENTS == 1:
        # Don't bother with multiprocessing if only one agent
        run_agent(brain.brain, render=False, verbose = True)
    else:
        processes = [mp.Process(target=run_agent, args=(brain.brain, False, True))
                     for _ in range(NUMBER_OF_AGENTS)]
        for process in processes:
            process.start()

        for process in processes:
            process.join()


def test():
    run_agent(brain.brain, render=True)
