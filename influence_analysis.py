# Calculate PageRank for each node to determine influential nodes
pagerank = nx.pagerank(G)

# Sort nodes by PageRank score to get top influencers
top_influencers = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)[:10]
print("Top 10 influential nodes by PageRank:", top_influencers)
