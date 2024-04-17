from typing import Any, Callable, Tuple, Union

import torch

from .pytorch_exported_program_adater_impl import \
    PytorchExportedProgramAdapterImpl
from .types import ModelExplorerGraphs
from .server import start


def import_pytorch(model: Callable, inputs: Tuple[Any, ...]) -> ModelExplorerGraphs:
  """Converts the given pytorch model with inputs into model explorer format."""
  exported = torch.export.export(model, inputs)
  adapter = PytorchExportedProgramAdapterImpl(exported)
  return adapter.convert()


def import_pytorch_and_start(
        model: Callable,
        inputs: Tuple[Any, ...],
        host='localhost',
        port=8080,
        no_open_in_browser: bool = False,
        colab: bool = False,
        colab_height: int = 850,
        cors_host: Union[str, None] = None):
  """Converts the given pytorch model and starts the ME server."""
  graphs = import_pytorch(model, inputs)
  start(host=host,
        port=port,
        graphs=graphs,
        no_open_in_browser=no_open_in_browser,
        colab=colab,
        colab_height=colab_height,
        cors_host=cors_host)
