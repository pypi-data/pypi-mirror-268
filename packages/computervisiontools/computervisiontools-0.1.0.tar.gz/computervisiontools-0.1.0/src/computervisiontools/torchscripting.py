"""contain function to torchscript a model"""

from typing import Tuple
import torch
from torch.jit import trace


def script_model(
    model: torch.nn.Module, input_image_shape: Tuple[int], device: str
) -> torch.jit._trace.TopLevelTracedModule:
    """Script and return a torch script version of a model.

    Args:
        model (torch.nn.Module): Basic model
        input_image_shape (Tuple[int]): shape of image entering in model
        device (str): either 'cpu' or 'cuda' depending on your processor

    Returns:
        torch.jit._trace.TopLevelTracedModule: Model writted in Torch script
    """
    # set model to eval before scrippting for production
    model = model.eval()
    # create an fake input to go through the model layers
    input_example = torch.rand(input_image_shape, dtype=torch.float32, device=device)
    # script the modele in torchscript by encoding each layer
    model_script = trace(model, input_example)

    return model_script
