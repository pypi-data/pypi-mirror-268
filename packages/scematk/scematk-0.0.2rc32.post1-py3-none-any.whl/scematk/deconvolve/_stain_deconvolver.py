from .._abc._model import Model
from ..process._process import Processor
from typing import List

class StainDeconvolver(Model):
    def __init__(self, name: str, preprocessor: Processor = None, postprocessor: Processor = None, out_stains = List[str]) -> None:
        super().__init__(name, preprocessor, postprocessor)
        if isinstance(out_stains, str):
            out_stains = [out_stains]
        assert isinstance(out_stains, list)
        self.out_stains = out_stains