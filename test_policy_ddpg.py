from spinup.utils.test_policy import load_policy_and_env, run_policy
from spinup.utils.plot import plot_data

# Indicate path to saved data
path = '/tmp/experiments/exp11_can'

# Load data from save
loaded_env , get_action = load_policy_and_env(path)

# Run policy with env.render() method
run_policy(loaded_env,get_action)

# Idée de plot pour les données ??
# plot_data(path)



