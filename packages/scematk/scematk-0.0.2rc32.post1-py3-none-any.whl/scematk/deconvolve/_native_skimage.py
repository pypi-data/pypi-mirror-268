from ._stain_deconvolver import StainDeconvolver
from ..process._process import Processor
from ..image._ubyte_image import UByteImage
import dask.array as da
from skimage.color import rgb2hed

class NativeSKImageStainDeconvolver(StainDeconvolver):
    def __init__(self, preprocessor: Processor = None, postprocessor: Processor = None, stain_type: str = "H&E") -> None:
        assert isinstance(stain_type, str), "stain_type must be a string"
        assert stain_type in ['H&E', 'H-DAB'], "stain_type must be either 'H&E' or 'H-DAB'"
        if stain_type == 'H&E':
            out_stains = ['Hematoxylin', 'Eosin']
        elif stain_type == 'H-DAB':
            out_stains = ['Hematoxylin', 'DAB']
        else:
            raise ValueError("stain_type must be either 'H&E' or 'H-DAB'")
        super().__init__("Stain deconvolver using scikit-image defaults", preprocessor, postprocessor, out_stains)
        self.fitted = True

    def fit(self, image: UByteImage) -> None:
        pass

    def run(self, image: UByteImage) -> UByteImage:
        image = self.preprocessor.run(image)
        assert isinstance(image, UByteImage), "image must be a UByteImage"
        assert image.channel_names == ['Red', 'Green', 'Blue'], "image must have channels ['Red', 'Green', 'Blue']"
        if self.out_stains == ['Hematoxylin', 'Eosin']:
            deconv_func = lambda x: rgb2hed(x)[:, :, :2]
        elif self.out_stains == ['Hematoxylin', 'DAB']:
            deconv_func = lambda x: rgb2hed(x)[:, :, [0, 2]]
        else:
            raise ValueError("out_stains must be either ['Hematoxylin', 'Eosin'] or ['Hematoxylin', 'DAB']")
        img = image.image
        chunks = image.image.chunks
        deconv_img = da.map_blocks(deconv_func, img, dtype='float64', chunks=(chunks[0], chunks[1], 2))
        deconv_img = deconv_img * 255
        deconv_img = deconv_img.astype('uint8')
        deconv_img = UByteImage(deconv_img, image.info, self.out_stains)
        deconv_image = self.postprocessor.run(deconv_img)
        return deconv_image


    def fit_and_run(self, image: UByteImage) -> UByteImage:
        return self.run(image)

    def _default_preprocessor(self) -> Processor:
        return Processor()

    def _default_postprocessor(self) -> Processor:
        return Processor()