# Import necessary libraries
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from community import community_louvain
from itertools import combinations
import numpy as np

# Load the dataset
edges = pd.read_csv('social_network_edges.csv')  # Adjust the path for edge list file
nodes = pd.read_csv('social_network_nodes.csv')  # Adjust the path for node list file

# Display basic information about the dataset
print("Edges:\n", edges.head())
print("Nodes:\n", nodes.head())

# Data cleaning (remove duplicates and handle missing data if any)
edges = edges.drop_duplicates()
nodes = nodes.drop_duplicates()
