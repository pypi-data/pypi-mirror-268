from ..image._image import Image
from ..process._process import Processor
from abc import ABC, abstractmethod

class Model(ABC):
    def __init__(self, name: str, preprocessor: Processor = None, postprocessor: Processor = None) -> None:
        preprocessor = preprocessor if preprocessor is not None else self._default_preprocessor()
        postprocessor = postprocessor if postprocessor is not None else self._default_postprocessor()
        assert isinstance(name, str), "name must be a string"
        assert isinstance(preprocessor, Processor), "preprocessor must be a Processor instance"
        assert isinstance(postprocessor, Processor), "postprocessor must be a Processor instance"
        self.name = name
        self.preprocessor = preprocessor
        self.postprocessor = postprocessor
        self.fitted = False

    @abstractmethod
    def fit(self, image: Image) -> None:
        pass

    @abstractmethod
    def run(self, image: Image) -> Image:
        pass

    @abstractmethod
    def fit_and_run(self, image: Image) -> Image:
        pass

    @abstractmethod
    def _default_preprocessor(self) -> Processor:
        pass

    @abstractmethod
    def _default_postprocessor(self) -> Processor:
        pass