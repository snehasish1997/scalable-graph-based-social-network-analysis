# Draw the graph with node colors based on community assignment
pos = nx.spring_layout(G)  # Layout for better visual clarity
plt.figure(figsize=(14, 10))

# Color nodes by community
community_colors = [partition[node] for node in G.nodes()]
nx.draw_networkx(G, pos, node_color=community_colors, with_labels=False, node_size=50, cmap=plt.cm.rainbow)

plt.title("Social Network Graph with Community Detection")
plt.show()
