from ._tissue_segmenter import TissueSegmenter
from ...image._binary_mask import BinaryMask
from ...image._image import Image
from ...image._ubyte_image import UByteImage
from ...process._process import Processor
from ...process.colour._rgb_to_grey import RGBToGrey
import dask.array as da
from skimage.filters import threshold_otsu

class OtsuThresholder(TissueSegmenter):
    def __init__(self, preprocessor: Processor = None, postprocessor: Processor = None, below_thresh: bool = True):
        super().__init__("Otsu Thresholder", preprocessor, postprocessor)
        assert isinstance(below_thresh, bool), "below_thresh must be a boolean"
        self.below_thresh = below_thresh

    def fit(self, image: Image) -> None:
        image = self.preprocessor.run(image)
        if not isinstance(image, UByteImage):
            raise NotImplementedError("OtsuThresholder only supports UByteImage at this time")
        assert image.shape[2] == 1, "Image must be single channel"
        counts, _ = da.histogram(image.image, bins=256, range=[0, 256])
        self.threshold = threshold_otsu(hist=counts.compute(), nbins=256)
        self.fitted = True

    def run(self, image: Image) -> BinaryMask:
        if not self.fitted:
            raise RuntimeError("Model must be fitted before running")
        image = self.preprocessor.run(image)
        if not isinstance(image, UByteImage):
            raise NotImplementedError("OtsuThresholder only supports UByteImage at this time")
        assert image.shape[2] == 1, "Image must be single channel"
        img = image.image
        img = da.squeeze(img, axis=2)
        if self.below_thresh:
            mask = img < self.threshold
        else:
            mask = img > self.threshold
        mask = BinaryMask(mask, image.info, "TissueMask")
        mask = self.postprocessor.run(mask)
        return mask

    def fit_and_run(self, image: Image) -> Image:
        self.fit(image)
        return self.run(image)

    def _default_preprocessor(self) -> Processor:
        proc = Processor()
        proc.add_process(RGBToGrey())
        return proc

    def _default_postprocessor(self) -> Processor:
        return Processor()