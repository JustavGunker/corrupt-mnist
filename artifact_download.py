import torch

import wandb

import os

_TEST_ROOT = os.path.dirname(__file__)  # root of test folder
_PROJECT_ROOT = os.path.dirname(_TEST_ROOT)  # root of project

from src.package.model import MyAwesomeModel

api = wandb.Api()
artifact_name = (
    f"justav-danmarks-tekniske-universitet-dtu/corrupt_mnist/corrupt_mnist_model:v0"
)
artifact = api.artifact(name=artifact_name)
artifact_dir = artifact.download("artifacts")
model = MyAwesomeModel()
model.load_state_dict(torch.load("artifacts/model.pth"))

print("Model loaded from artifact successfully.")
print(model)
