def heuristic(state, goal):
    h = 0

    for i in range(9):

        if state[i] != 0:

            current_row = i // 3
            current_col = i % 3

            goal_pos = goal.index(state[i])

            goal_row = goal_pos // 3
            goal_col = goal_pos % 3

            h = h + abs(current_row - goal_row)
            h = h + abs(current_col - goal_col)

    return h


def display(state):
    print(state[0], state[1], state[2])
    print(state[3], state[4], state[5])
    print(state[6], state[7], state[8])
    print()


def astar(start, goal):

    open = []
    closed = []

    h = heuristic(start, goal)

    open.append([start, 0, h, h, ""])

    while open:

        # Find node with smallest f
        min_index = 0

        for i in range(1, len(open)):
            if open[i][3] < open[min_index][3]:
                min_index = i

        node = open.pop(min_index)

        state = node[0]
        g = node[1]
        h = node[2]
        f = node[3]
        path = node[4]

        print("State:")
        display(state)

        print("g =", g)
        print("h =", h)
        print("f =", f)
        print()

        if state == goal:
            print("Goal Reached")
            print("Solution:", path)
            print("Cost:", g)
            return

        closed.append(state)

        blank = state.index(0)

        row = blank // 3
        col = blank % 3

        moves = [
            (-1, 0, "U"),
            (1, 0, "D"),
            (0, -1, "L"),
            (0, 1, "R")
        ]

        for dr, dc, move in moves:

            new_row = row + dr
            new_col = col + dc

            if new_row >= 0 and new_row < 3 and new_col >= 0 and new_col < 3:

                new_state = state.copy()

                new_blank = new_row * 3 + new_col

                new_state[blank] = new_state[new_blank]
                new_state[new_blank] = 0

                if new_state not in closed:

                    new_g = g + 1
                    new_h = heuristic(new_state, goal)
                    new_f = new_g + new_h

                    open.append([
                        new_state,
                        new_g,
                        new_h,
                        new_f,
                        path + move
                    ])

    print("No solution")


start = [
    2, 8, 3,
    1, 6, 4,
    7, 0, 5
]

goal = [
    1, 2, 3,
    8, 0, 4,
    7, 6, 5
]

astar(start, goal)