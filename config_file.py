"""
config_file.py
"""

#NEAT

fitness_criterion = max
fitness_threshold = 10000
    pop_size = 0
reset_on_extinction = True

#DEFAULT GENOME

##activation options
    activation_default = sigmoid
activation_mutate_rate = .05
    activation_options = sigmoid gauss

##node aggregation options
    aggregation_default = random
aggregation_mutate_rate = .05
    aggregation_options = sum product min max median maxabs

##node bias options
bias_init_mean = .05
bias_init_stdev = 1
bias_max_value = 30
bias_min_value = -30
bias_mutate_power = .5
bias_mutate_rate = .7
bias_replace_rate = .1

##genome compatibility options
compatibility_disjoint_coefficients = 1
compatibility_weight_coefficients = .5

##connection add/remove rates
conn_add_prob = .5
conn_delete_prob = .5

##connection enable options
enable_default = False
enable_mutation_rate = .5
    feed_forward = False
    initial_connection = unconnected
    #initial_connection = partial_nodirect .5

##node add/remove rates
node_add_prob = .5
node_delete_prob = .2

##network parameters
    num_hidden =
    num_inputs =
    num_outputs =

##node response options
response_init_mean = 1
response_init_stdev = .05
response_max_value = 30
response_min_value = -30
response_mutate_power = .1
response_mutate_rate = .75
response_replace_rate= .1

##connection weight options
weight_init_mean = .1
weight_init_stdev = 1
weight_max_value = 30
weight_min_value = -30
weight_mutate_power = .5
weight_mutate_rate = .8
weight_replace_rate = .1

#DEFAULT SPECIES SET

compatibility_threshold = 2.5

#DEFAULT STAGNATION

    species_fitness_func = max
    max_stagnation = 50
    species_elitism = 1

#DEFAULT REPRODUCTION
    elitism = 3
    survival_threshold = .3
