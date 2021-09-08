import environment_2d
import numpy as np
import random
def init_nodes(env, random):
    q = env.random_query()
    x_start, y_start, x_goal, y_goal = q
    points = []
    points.append([x_start, y_start])

    if random == False:
        for i in range(11):
            for j in range(7):
                if not env.check_collision(i,j):
                    points.append((i,j))
                    env.plot_query(i,j,x_goal,y_goal)
    elif random == True:
        i = np.random.uniform(0, 10, 100)
        j = np.random.uniform(0, 6, 100)
        for ii,jj in zip(i,j):
            points.append((ii, jj))
            env.plot_query(ii, jj, x_goal, y_goal)

    points.append([x_goal, y_goal])
    return points, x_start, y_start, x_goal, y_goal, q