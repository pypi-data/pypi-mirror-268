from .._abc._model import Model
from ..process._process import Processor

class Segmenter(Model):
    def __init__(self, name: str, preprocessor: Processor = None, postprocessor: Processor = None):
        super().__init__(name, preprocessor, postprocessor)