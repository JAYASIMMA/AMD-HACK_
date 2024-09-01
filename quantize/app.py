# Install the required packages first
# !pip install streamlit scikit-learn torch torchvision matplotlib

import streamlit as st
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from torch.utils.data import DataLoader, TensorDataset
import matplotlib.pyplot as plt

# Define a simple neural network
class SimpleNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

def quantize_model(model, data_loader):
    model.eval()
    quantized_model = torch.quantization.quantize_dynamic(model, {nn.Linear}, dtype=torch.qint8)
    return quantized_model

# Streamlit app
st.title('Model Optimization and Quantization')

# Get user input for model parameters
input_size = st.number_input('Input Size', min_value=1, value=20)
hidden_size = st.number_input('Hidden Size', min_value=1, value=10)
output_size = st.number_input('Output Size', min_value=1, value=2)
num_epochs = st.number_input('Number of Epochs', min_value=1, value=20)
batch_size = st.number_input('Batch Size', min_value=1, value=32)
learning_rate = st.number_input('Learning Rate', min_value=0.0001, value=0.001)

# Generate synthetic data
X, y = make_classification(n_samples=1000, n_features=input_size, n_classes=output_size)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Convert to PyTorch tensors
X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train, dtype=torch.long)
X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
y_test_tensor = torch.tensor(y_test, dtype=torch.long)

# Create data loaders
train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
test_dataset = TensorDataset(X_test_tensor, y_test_tensor)
train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=False)

# Initialize model, loss function, and optimizer
model = SimpleNN(input_size, hidden_size, output_size)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# Training loop
losses = []
for epoch in range(num_epochs):
    for i, (inputs, labels) in enumerate(train_loader):
        outputs = model(inputs)
        loss = criterion(outputs, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    losses.append(loss.item())

# Quantize the model
quantized_model = quantize_model(model, train_loader)

# Display training loss graph
fig, ax = plt.subplots()
ax.plot(range(num_epochs), losses, label='Training Loss')
ax.set_xlabel('Epoch')
ax.set_ylabel('Loss')
ax.set_title('Training Loss over Epochs')
ax.legend()
st.pyplot(fig)

# Display model size comparison
original_size = sum(p.numel() for p in model.parameters())
quantized_size = sum(p.numel() for p in quantized_model.parameters())
st.write(f"Original Model Size: {original_size} parameters")
st.write(f"Quantized Model Size: {quantized_size} parameters")
