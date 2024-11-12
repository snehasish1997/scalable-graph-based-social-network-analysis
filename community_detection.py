# Detect communities using Louvain Modularity 
partition = community_louvain.best_partition(G.to_undirected())

# Assign community labels as node attributes
nx.set_node_attributes(G, partition, 'community')

# Display sample communities for validation
print("Sample community partition:", {k: partition[k] for k in list(partition)[:10]})
