import  numpy as np

def run_markov_chain(transition_matrix, n=10, print_transitions=False):
    step = transition_matrix
    
    for time_step in range(1, n):
        if print_transitions:
            print('Transition Matrix at step:', +str(time_step))
            print(step)
            print('--------------------------')
            
        