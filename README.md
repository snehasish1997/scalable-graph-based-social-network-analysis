
# Scalable Graph-Based Social Network Analysis

This project performs scalable graph-based analysis on social networks, focusing on community detection, link prediction, influence analysis, and large-scale data processing. The implementation leverages advanced algorithms like Louvain and Leiden for community detection and GNNs (Graph Neural Networks) for link prediction.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Project Overview

This project provides a comprehensive pipeline to analyze large-scale social networks by exploring:
1. **Community Detection**: Using Louvain and Leiden algorithms to uncover community structures.
2. **Link Prediction**: Utilizing traditional and GNN-based methods for predicting missing links.
3. **Influence Analysis**: Identifying influential nodes within the network.
4. **Scalability**: Processing large datasets by leveraging optimization techniques.

## Features

- **Community Detection**: Implements Louvain and Leiden algorithms to reveal hidden communities.
- **Link Prediction**: Uses traditional and GNN-based approaches for predicting new connections.
- **Graph Visualization**: Visualize the network structure and communities using various visualization techniques.
- **Influence Analysis**: Determines key influencers in the network.
- **Scalability**: Designed to handle large datasets efficiently.

## Installation

To install the required dependencies, use:
```bash
pip install -r requirements.txt
```

Ensure you have Python 3.8+ and necessary packages, such as NetworkX, PyTorch, and Matplotlib.

## Usage

Each script serves a different purpose in the project:

1. **community_detection.py**: Run this script for community detection analysis.
   ```bash
   python community_detection.py
   ```

2. **cons_graph.py**: Use this script to construct the network graph from data.
   ```bash
   python cons_graph.py
   ```

3. **data.py**: Preprocesses the data and loads it for analysis.
   ```bash
   python data.py
   ```

4. **GNN_link_prediction.py**: Apply GNN-based methods for link prediction.
   ```bash
   python GNN_link_prediction.py
   ```

5. **graph_visualisation.py**: Visualize the graph structure and communities.
   ```bash
   python graph_visualisation.py
   ```

6. **influence_analysis.py**: Analyze the influence of nodes within the network.
   ```bash
   python influence_analysis.py
   ```

7. **link_prediction.py**: Execute traditional link prediction methods.
   ```bash
   python link_prediction.py
   ```

8. **scaling_large_data.py**: Manage large datasets for scalability.
   ```bash
   python scaling_large_data.py
   ```

## Project Structure

- **community_detection.py**: Contains functions for implementing community detection algorithms.
- **cons_graph.py**: Defines methods for constructing and modifying the graph.
- **data.py**: Manages data ingestion, cleaning, and preparation.
- **GNN_link_prediction.py**: Implements Graph Neural Network-based link prediction.
- **graph_visualisation.py**: Visualizes nodes, edges, communities, and influencers in the graph.
- **influence_analysis.py**: Analyzes node influence based on metrics such as centrality.
- **link_prediction.py**: Runs traditional link prediction methods.
- **scaling_large_data.py**: Includes techniques for processing large-scale graphs.

## License

This project is licensed under the MIT License.
