# Initial and goal states
initial_state = ['A', 'B', 'C']
goal_state = ['C', 'A', 'B']

# Count misplaced blocks
def misplaced_blocks(state):
    return sum(state[i] != goal_state[i] for i in range(len(state)))

# Steepest-Ascent Hill Climbing
def hill_climbing(state):
    current_state = state
    moves = 0

    print(f"Step 0: {current_state}")

    while True:
        best_state = current_state
        best_eval = misplaced_blocks(current_state)

        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                new_state = current_state[:]
                new_state[i], new_state[j] = new_state[j], new_state[i]
                new_eval = misplaced_blocks(new_state)

                if new_eval < best_eval:
                    best_state = new_state
                    best_eval = new_eval

        if best_eval == misplaced_blocks(current_state):
            break

        current_state = best_state
        moves += 1
        print(f"Step {moves}: {current_state}")

    return current_state, moves

# Run the algorithm
final_state, total_moves = hill_climbing(initial_state)
print(f"\nFinal state: {final_state}")
print(f"Total moves: {total_moves}")
