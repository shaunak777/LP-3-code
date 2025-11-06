# Gradient Descent to find local minima of y = (x + 3)^2

# Function derivative: dy/dx = 2*(x + 3)
def derivative(x):
    return 2 * (x + 3)

# Gradient Descent function
def gradient_descent(starting_point, learning_rate, iterations):
    x = starting_point
    for i in range(iterations):
        grad = derivative(x)
        x = x - learning_rate * grad
        print(f"Iteration {i+1}: x = {x:.5f}")
    return x

# Parameters
initial_x = 2          # Starting point
learning_rate = 0.1    # Step size
iterations = 25        # Number of updates

# Run gradient descent
minima = gradient_descent(initial_x, learning_rate, iterations)
print("\nLocal minima occurs at x =", round(minima, 5))
