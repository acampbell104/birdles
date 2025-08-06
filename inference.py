import torch
from torchvision import models, transforms
from PIL import Image
import json
import os

model_path = "models/latest.pth"
label_path = "models/labels.json"

def load_model():
    model = models.mobilenet_v2(pretrained=False)
    model.classifier[1] = torch.nn.Linear(model.last_channel, len(load_labels()))
    model.load_state_dict(torch.load(model_path))
    model.eval()
    return model

def load_labels():
    with open(label_path, "r") as f:
        return json.load(f)

def predict(image_path):
    labels = load_labels()
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])
    image = Image.open(image_path).convert("RGB")
    input_tensor = transform(image).unsqueeze(0)
    model = load_model()
    with torch.no_grad():
        output = model(input_tensor)
    _, predicted = torch.max(output, 1)
    return labels[str(predicted.item())]
