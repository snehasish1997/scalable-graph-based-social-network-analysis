# Predict potential new links based on common neighbors
potential_links = []
for u, v in combinations(G.nodes(), 2):
    if not G.has_edge(u, v) and not G.has_edge(v, u):
        common_neighbors = len(list(nx.common_neighbors(G, u, v)))
        if common_neighbors > 2:  # Threshold for link prediction
            potential_links.append((u, v, common_neighbors))

# Sort predicted links by common neighbors count
predicted_links = sorted(potential_links, key=lambda x: x[2], reverse=True)[:10]
print("Top 10 predicted links:", predicted_links)
