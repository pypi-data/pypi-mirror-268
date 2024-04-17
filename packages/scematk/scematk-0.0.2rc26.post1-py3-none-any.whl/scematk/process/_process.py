from ..image._image import Image
from abc import ABC, abstractmethod

class Process(ABC):
    def __init__(self, name: str) -> None:
        assert isinstance(name, str), 'name must be a string'
        self.name = name

    @abstractmethod
    def run(self, image: Image) -> Image:
        pass

class Processor():
    def __init__(self) -> None:
        self.processes = []

    def add_process(self, process: Process) -> None:
        assert isinstance(process, Process), 'process must be a Process'
        self.processes.append(process)

    def run(self, image: Image) -> Image:
        assert isinstance(image, Image), 'image must be an Image'
        image = image
        for process in self.processes:
            image = process.run(image)
        return image

    def __repr__(self) -> str:
        if len(self.processes) == 0:
            ret_str = "Empty processor object"
        else:
            ret_str = "Processor object with processes:"
            for i, proc in enumerate(self.processes):
                ret_str += f"\n\t({i+1}) {proc.name}"
        return ret_str

    def _repr_html_(self) -> str:
        total_width = 400
        html = f' <div style="width: {total_width}px; background-color: #202020; padding: 20px; border-radius: 5px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);">'
        html += f'<h1>SCEMATK Processor Object</h1>'
        if len(self.processes) == 0:
            html += f'<p>Empty processor object</p>'
        else:
            html += f'<p>Processor object with processes:</p>'
            for i, proc in enumerate(self.processes):
                html += f'<p>({i+1}) {proc.name}</p>'
        html += '</div>'
        return html
