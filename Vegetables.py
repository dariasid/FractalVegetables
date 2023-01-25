import fractal
import random
import numpy as np
import matplotlib.pyplot as plt

def generate_fractal_vegetable():
    # Create a fractal object with random parameters
    f = fractal.Fractal(random.randint(3, 6), random.uniform(0.1, 0.9), random.uniform(0.1, 0.9))
    # Generate the fractal shape
    vegetable = f.generate()
    # Add noise to the fractal shape to make it look more like a vegetable
    noise = np.random.normal(0, 0.05, vegetable.shape)
    vegetable = vegetable + noise
    vegetable = np.clip(vegetable, 0, 1)
    # Apply a vegetable-like color map to the fractal shape
    vegetable = plt.cm.YlOrBr(vegetable)
    # Return the fractal vegetable
    return vegetable

# Generate 10 fractal vegetable images
for i in range(10):
    vegetable = generate_fractal_vegetable()
    plt.imsave("fractal_vegetable_{}.png".format(i), vegetable)
