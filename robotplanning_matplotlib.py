import numpy as np
import matplotlib.pyplot as plt

# -------------------- TASK 1: 1D ROBOT --------------------
def robot_1d():
    n = 1000
    particles = np.random.uniform(0, 10, n)
    weights = np.ones(n)/n
    true_pos = 5

    true_vals, meas_vals, est_vals = [], [], []

    for t in range(25):
        true_pos += np.random.normal(0.5, 0.5)
        measurement = true_pos + np.random.normal(0, 1)

        particles += np.random.normal(0.5, 0.5, n)

        weights *= np.exp(-(particles - measurement)**2 / 2)
        weights += 1e-300
        weights /= np.sum(weights)

        idx = np.random.choice(n, n, p=weights)
        particles = particles[idx]
        weights = np.ones(n)/n

        estimate = np.mean(particles)

        true_vals.append(true_pos)
        meas_vals.append(measurement)
        est_vals.append(estimate)

    t = np.arange(len(true_vals))

    plt.figure()
    plt.plot(t, true_vals, label="True Position")
    plt.plot(t, est_vals, label="Estimated Position")
    plt.plot(t, meas_vals, linestyle="--", label="Noisy Sensor")
    plt.title("1D Robot Tracking")
    plt.legend()
    plt.grid()
    plt.show()


# -------------------- TASK 2: 2D PERSON --------------------
def person_2d():
    n = 1000
    particles = np.random.uniform(0, 10, (n,2))
    weights = np.ones(n)/n
    true_pos = np.array([5.0,5.0])

    true_x, true_y = [], []
    est_x, est_y = [], []

    for t in range(25):
        true_pos += np.random.normal(0.5, 0.5, 2)
        measurement = true_pos + np.random.normal(0, 1, 2)

        particles += np.random.normal(0.5, 0.5, (n,2))

        dist = np.linalg.norm(particles - measurement, axis=1)
        weights *= np.exp(-(dist**2)/2)

        weights += 1e-300
        weights /= np.sum(weights)

        idx = np.random.choice(n, n, p=weights)
        particles = particles[idx]
        weights = np.ones(n)/n

        estimate = np.mean(particles, axis=0)

        true_x.append(true_pos[0])
        true_y.append(true_pos[1])
        est_x.append(estimate[0])
        est_y.append(estimate[1])

    plt.figure()
    plt.plot(true_x, true_y, label="True Path")
    plt.plot(est_x, est_y, label="Estimated Path")
    plt.scatter(true_x[-1], true_y[-1])
    plt.title("2D Person Tracking")
    plt.legend()
    plt.grid()
    plt.show()


# -------------------- TASK 3: DRONE ALTITUDE --------------------
def drone_altitude():
    n = 1000
    particles = np.random.uniform(50, 55, n)
    weights = np.ones(n)/n
    true_alt = 50

    true_vals, meas_vals, est_vals = [], [], []

    for t in range(25):
        true_alt += np.random.normal(1, 0.5)
        measurement = true_alt + np.random.normal(0, 2)

        particles += np.random.normal(1, 1, n)

        weights *= np.exp(-(particles - measurement)**2 / 4)
        weights += 1e-300
        weights /= np.sum(weights)

        idx = np.random.choice(n, n, p=weights)
        particles = particles[idx]
        weights = np.ones(n)/n

        estimate = np.mean(particles)

        true_vals.append(true_alt)
        meas_vals.append(measurement)
        est_vals.append(estimate)

    t = np.arange(len(true_vals))

    plt.figure()
    plt.plot(t, true_vals, label="True Altitude")
    plt.plot(t, est_vals, label="Estimated Altitude")
    plt.plot(t, meas_vals, linestyle="--", label="Noisy Barometer")
    plt.title("Drone Altitude Estimation")
    plt.legend()
    plt.grid()
    plt.show()


# -------------------- MAIN --------------------
robot_1d()
person_2d()
drone_altitude()