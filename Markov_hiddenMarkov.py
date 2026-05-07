import wave
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


# -------------------------
# MARKOV MODEL
# -------------------------
states = ["Sunny", "Cloudy", "Rainy"]

tp = {
    "Sunny": {"Sunny": 0.6, "Cloudy": 0.3, "Rainy": 0.1},
    "Cloudy": {"Sunny": 0.2, "Cloudy": 0.5, "Rainy": 0.3},
    "Rainy": {"Sunny": 0.1, "Cloudy": 0.4, "Rainy": 0.5},
}


def draw_markov():
    G = nx.DiGraph()

    for s in states:
        G.add_node(s)

    for s1 in states:
        for s2 in states:
            G.add_edge(s1, s2, weight=tp[s1][s2])

    pos = nx.circular_layout(G)

    plt.figure()
    plt.title("Markov Model (State Transitions)")

    nx.draw(G, pos, with_labels=True, node_size=3000)

    labels = {(u, v): f"{d['weight']}" for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.show()


# -------------------------
# HMM MODEL
# -------------------------
observations = ["Normal", "Umbrella", "Raincoat"]

ep = {
    "Sunny": {"Normal": 0.6, "Umbrella": 0.3, "Raincoat": 0.1},
    "Cloudy": {"Normal": 0.4, "Umbrella": 0.4, "Raincoat": 0.2},
    "Rainy": {"Normal": 0.1, "Umbrella": 0.4, "Raincoat": 0.5},
}


def draw_hmm():
    G = nx.DiGraph()

    for s in states:
        G.add_node(s)
    for o in observations:
        G.add_node(o)

    for s1 in states:
        for s2 in states:
            G.add_edge(s1, s2, weight=tp[s1][s2])

    for s in states:
        for o in observations:
            G.add_edge(s, o, weight=ep[s][o])

    pos = {}
    for i, s in enumerate(states):
        pos[s] = (0, i)
    for i, o in enumerate(observations):
        pos[o] = (2, i)

    plt.figure()
    plt.title("HMM (States → Observations)")

    nx.draw_networkx_nodes(G, pos, nodelist=states, node_size=3000)
    nx.draw_networkx_nodes(G, pos, nodelist=observations, node_size=3000)

    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos)

    labels = {(u, v): f"{d['weight']}" for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)

    plt.axis("off")
    plt.show()


# -------------------------
# KALMAN FILTER (UPDATED)
# -------------------------
def read_audio(path):
    with wave.open(path, "rb") as wf:
        sr = wf.getframerate()
        frames = wf.readframes(wf.getnframes())
        data = np.frombuffer(frames, dtype=np.int16).astype(np.float32)

        if wf.getnchannels() > 1:
            data = data.reshape(-1, wf.getnchannels()).mean(axis=1)

    return data / 32768.0, sr


def kalman(x, q=1e-5, r=1e-3):
    y = np.zeros_like(x)
    p = 1.0
    y[0] = x[0]

    for i in range(1, len(x)):
        p += q
        k = p / (p + r)
        y[i] = y[i - 1] + k * (x[i] - y[i - 1])
        p *= (1 - k)

    return y


def plot_audio(x, y, sr):
    n = int(min(3.0, len(x) / sr) * sr)
    t = np.arange(n) / sr

    fig, ax = plt.subplots(3, 1, figsize=(10, 8), sharex=True)
    fig.suptitle("Kalman Filter – Audio Denoising")

    ax[0].plot(t, x[:n], lw=0.8)
    ax[0].set_title("Before (Noisy)")
    ax[0].grid(True, alpha=0.3)

    ax[1].plot(t, y[:n], lw=0.8)
    ax[1].set_title("After (Filtered)")
    ax[1].grid(True, alpha=0.3)

    ax[2].plot(t, x[:n], alpha=0.5, lw=0.8, label="Noisy")
    ax[2].plot(t, y[:n], lw=0.9, label="Filtered")
    ax[2].set_title("Comparison")
    ax[2].legend()
    ax[2].grid(True, alpha=0.3)

    plt.xlabel("Time (s)")
    plt.tight_layout()
    plt.show()


# -------------------------
# MAIN
# -------------------------
draw_markov()
draw_hmm()

audio, sr = read_audio("audio.wav")
filtered = kalman(audio)

plot_audio(audio, filtered, sr)