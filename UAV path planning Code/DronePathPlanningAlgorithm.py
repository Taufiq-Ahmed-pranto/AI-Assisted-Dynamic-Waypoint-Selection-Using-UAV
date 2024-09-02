import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.spatial.distance import cdist

# Initialize search area. I have choosen it 10 and number of waypoint where is probabilty to have fire is 5
grid_size = 10
num_targets = 5
search_area = np.zeros((grid_size, grid_size))

# Randomly place targets in the search area
targets = set()
while len(targets) < num_targets:
    target_position = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
    if target_position not in targets:
        targets.add(target_position)
        search_area[target_position] = 1

# Randomly select rescue zones from targets (for checking upon visiting)
all_rescue_zones = set(random.sample(list(targets), num_targets // 2))  # Convert targets to list before sampling

# Initialize probabilities
probabilities = np.full((grid_size, grid_size), 1 / (grid_size * grid_size))


def update_probabilities(probabilities, observation, cell):
    """
    Update probabilities based on observation.
    """
    likelihood = 0.8 if observation else 0.2  # Assume 80% detection accuracy
    probabilities[cell] *= likelihood
    probabilities /= probabilities.sum()  # Normalize


def get_next_cell(probabilities, current_position, targets):
    """
    Get the next cell to ve highest probabilisit based on thity and proximity to targets.
    """
    if targets:
        target_positions = np.array(list(targets))
        current_pos_array = np.array([current_position])
        distances = cdist(current_pos_array, target_positions, metric='euclidean')
        closest_target_index = np.argmin(distances)
        closest_target = tuple(target_positions[closest_target_index])
        return closest_target
    return np.unravel_index(np.argmax(probabilities), probabilities.shape)


# Simulate drone path planning and visualization
fig, ax = plt.subplots()


def visualize(probabilities, path, targets, checked_zones):
    ax.clear()
    cax = ax.matshow(probabilities, cmap='viridis')

    # Plot grid
    ax.set_xticks(np.arange(-0.5, grid_size, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, grid_size, 1), minor=True)
    ax.grid(which='minor', color='w', linestyle='-', linewidth=2)

    # Plot path
    ax.plot([p[1] for p in path], [p[0] for p in path], marker='o', color='r', linestyle='-', linewidth=2, markersize=8,
            markerfacecolor='yellow')

    # Plot targets and checked zones
    for target in targets:
        ax.plot(target[1], target[0], marker='x', color='white', markersize=12, markeredgewidth=3)

    for checked in checked_zones:
        color = 'green' if checked in all_rescue_zones else 'red'
        ax.plot(checked[1], checked[0], marker='o', color=color, markersize=12, markeredgewidth=2)

    # Adding labels
    ax.set_title('Drone Path Planning with Bayesian Inference')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')

    plt.pause(0.5)


# Starting point
start_point = (0, 0)
path = [start_point]
current_cell = start_point
checked_zones = set()

for _ in range(grid_size ** 2):
    observation = current_cell in targets
    if observation:
        checked_zones.add(current_cell)
        targets.remove(current_cell)

    update_probabilities(probabilities, observation, current_cell)
    visualize(probabilities, path, targets, checked_zones)

    if not targets:
        print(f"All targets checked! Path: {path}")
        break

    current_cell = get_next_cell(probabilities, current_cell, targets)
    path.append(current_cell)

# Return to start point
path.append(start_point)
visualize(probabilities, path, targets, checked_zones)
print(f"Returning to start point. Final Path: {path}")

plt.show()
