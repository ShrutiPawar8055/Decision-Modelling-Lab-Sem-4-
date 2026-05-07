#sprinker and rain are the parents of the wetgrass and we have to find the probability 
#when we know grass is wet and it rained(P(W|R))
Pr = 0.2
Pnr = 1-Pr

Ps = 0.4
Pns = 1-Ps

Pw = {
    (1, 1): 0.99,
    (1, 0): 0.90,
    (0, 1): 0.80,
    (0, 0): 0.00
}

Pw_total = (
    Pw[(1,1)] * Pr * Ps +
    Pw[(1,0)] * Pr * Pns +
    Pw[(0,1)] * Pnr * Ps +
    Pw[(0,0)] * Pnr * Pns
)

Pr_and_w = (
    Pw[(1,1)] * Pr * Ps +
    Pw[(1,0)] * Pr * Pns
)

Pr_given_w = Pr_and_w / Pw_total

print("The Probability of rain given that grass is wet is :",round(Pr_given_w,4)*100,"%")



import networkx as nx
import matplotlib.pyplot as plt

# Create directed graph
G = nx.DiGraph()

# Add edges (parents -> child)
G.add_edge("Sprinkler", "WetGrass")
G.add_edge("Rain", "WetGrass")

# Draw graph
pos = nx.spring_layout(G)  # automatic layout
nx.draw(G, pos, with_labels=True, node_size=3000,
        node_color="lightblue", font_size=12, font_weight="bold")

plt.title("Bayesian Network Structure")
plt.show()