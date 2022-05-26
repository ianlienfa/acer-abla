import brain
import agent
from torch import multiprocessing as mp
import torch
import numpy as np
from core import *
import core
import sys
import os




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

def setup_history_files(filename="reward"):
    if(os.path.isdir("./"+filename) == False):
        print(f"Writing log into: {filename}/")    
        os.mkdir("./"+filename)
    core.tracker_file_prefix = filename + "/" + filename + "_"

def create_history_files(tracker_file_prefix, pid=""):  
    f = open(tracker_file_prefix + str(pid) + ".txt" , 'w')
    f.close()

if __name__ == "__main__":    
    if(len(sys.argv) >= 3):
        option = sys.argv[1]
        variable = sys.argv[2]
        if(option == "-f"):
            file_option_on = True
            setup_history_files(variable)
    else:
        setup_history_files()

    # fix random seed
    torch.random.manual_seed(SEED)
    np.random.seed(SEED)

    if NUMBER_OF_AGENTS == 1:
        # Don't bother with multiprocessing if only one agent
        create_history_files(core.tracker_file_prefix, os.getpid())
        run_agent(brain.brain, render=False, verbose = True)
    else:
        processes = [mp.Process(target=run_agent, args=(brain.brain, False, True))
                     for _ in range(NUMBER_OF_AGENTS)]
        for process in processes:
            process.start()
            create_history_files(core.tracker_file_prefix, process.pid)

        for process in processes:
            process.join()


def test():
    run_agent(brain.brain, render=True)
