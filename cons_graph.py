# Create a directed or undirected graph based on the dataset structure
G = nx.from_pandas_edgelist(edges, source='source', target='target', create_using=nx.DiGraph())

# Adding node attributes if available (e.g., demographic info)
for index, row in nodes.iterrows():
    G.nodes[row['node_id']]['attribute'] = row['attribute']

print("Graph Information:", nx.info(G))
