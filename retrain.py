import torch
import os
import json
from torchvision import models, transforms, datasets
from torch.utils.data import DataLoader
import torch.nn as nn
import torch.optim as optim

data_dir = "labelled"
model_path = "models/latest.pth"
label_path = "models/labels.json"

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

dataset = datasets.ImageFolder(data_dir, transform=transform)
loader = DataLoader(dataset, batch_size=16, shuffle=True)

model = models.mobilenet_v2(pretrained=True)
model.classifier[1] = nn.Linear(model.last_channel, len(dataset.classes))

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

print("🔁 Retraining model...")
for epoch in range(5):
    for imgs, labels in loader:
        optimizer.zero_grad()
        outputs = model(imgs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
print("✅ Training complete.")

os.makedirs("models", exist_ok=True)
torch.save(model.state_dict(), model_path)
with open(label_path, "w") as f:
    json.dump({i: name for i, name in enumerate(dataset.classes)}, f)
