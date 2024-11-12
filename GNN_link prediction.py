import torch
from torch_geometric.data import Data
from torch_geometric.nn import GCNConv

# Prepare data for PyTorch Geometric
edge_index = torch.tensor(list(G.edges()), dtype=torch.long).t().contiguous()
x = torch.tensor([[1] for _ in range(G.number_of_nodes())], dtype=torch.float)

data = Data(x=x, edge_index=edge_index)

# Define a simple GNN model
class GCN(torch.nn.Module):
    def __init__(self):
        super(GCN, self).__init__()
        self.conv1 = GCNConv(1, 16)
        self.conv2 = GCNConv(16, 1)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index
        x = self.conv1(x, edge_index)
        x = torch.relu(x)
        x = self.conv2(x, edge_index)
        return x

# Initialize and run the model
model = GCN()
out = model(data)
print("GNN output for advanced link prediction:\n", out)
