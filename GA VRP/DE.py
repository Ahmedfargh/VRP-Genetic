import random
def ensure_bounds(vec, bounds):
    vec_new = []
    # cycle through each variable in vector
    for i in range(len(vec)):

        # variable exceedes the minimum boundary
        if vec[i] < bounds[i][0]:
            vec_new.append(bounds[i][0])

        # variable exceedes the maximum boundary
        if vec[i] > bounds[i][1]:
            vec_new.append(bounds[i][1])

        # the variable is fine
        if bounds[i][0] <= vec[i] <= bounds[i][1]:
            vec_new.append(vec[i])

    return vec_new
def main(bounds, popsize, mutate, recombination, maxiter):
    # --- INITIALIZE A POPULATION (step #1) ----------------+

    population = []
    for i in range(0, popsize):
        indv = []
        for j in range(len(bounds)):
            indv.append(random.uniform(bounds[j][0], bounds[j][1]))
        population.append(indv)

    # --- SOLVE --------------------------------------------+

    # cycle through each generation (step #2)
    for i in range(1, maxiter + 1):

        # cycle through each individual in the population (step #3)
        for j in range(0, popsize):

            # --- MUTATION (step #3.A) ---------------------+

            # select three random vector index positions [0, popsize), not including current vector (j)
            canidates = range(0, popsize)
            canidates.remove(j)
            random_index = random.sample(canidates, 3)

            x_1 = population[random_index[0]]
            x_2 = population[random_index[1]]
            x_3 = population[random_index[2]]
            x_t = population[j]  # target individual

            # subtract x3 from x2, and create a new vector (x_diff)
            x_diff = [x_2_i - x_3_i for x_2_i, x_3_i in zip(x_2, x_3)]

            # multiply x_diff by the mutation factor (F) and add to x_1
            v_donor = [x_1_i + mutate * x_diff_i for x_1_i, x_diff_i in zip(x_1, x_diff)]
            v_donor = ensure_bounds(v_donor, bounds)

            # --- RECOMBINATION (step #3.B) ----------------+

            v_trial = []
            # cycle through each variable in our target vector
            for k in range(len(x_t)):
                crossover = random.random()

                # recombination occurs when crossover <= recombination rate
                if crossover <= recombination:
                    v_trial.append(v_donor[k])

                # recombination did not occur
                else:
                    v_trial.append(x_t[k])

    return best_individual