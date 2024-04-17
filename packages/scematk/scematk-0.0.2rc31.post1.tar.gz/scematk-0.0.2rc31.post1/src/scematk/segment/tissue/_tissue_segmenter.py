from scematk.process._process import Processor
from .._segmenter import Segmenter

class TissueSegmenter(Segmenter):
    def __init__(self, name: str, preprocessor: Processor = None, postprocessor: Processor = None):
        super().__init__(name, preprocessor, postprocessor)