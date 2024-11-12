

from pyspark.sql import SparkSession
from graphframes import GraphFrame

# Initialize Spark session
spark = SparkSession.builder.appName("GraphAnalysis").getOrCreate()

# Load data into Spark DataFrames
nodes_df = spark.createDataFrame(nodes)
edges_df = spark.createDataFrame(edges)

# Construct the graph
graph = GraphFrame(nodes_df, edges_df)

# Run PageRank, community detection, etc., using GraphFrames APIs
pagerank_df = graph.pageRank(resetProbability=0.15, maxIter=10)
communities = graph.labelPropagation(maxIter=5)

# Export results to pandas for visualization
pagerank_df = pagerank_df.toPandas()
