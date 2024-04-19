from __future__ import annotations  # Maybe needed

__all__ = ["VietOCR"]

from pathlib import Path
from typing import List, Literal, Union

import cv2
import pytesseract
from cv2.typing import MatLike
from joblib import Parallel, delayed
from PIL import Image
from tqdm import tqdm

VALID_IMG_SUFFIX = [".jpg", ".jpeg", ".png"]


class VietOCR_File:
    """
    Vietnamese image OCR - File
    """

    def __init__(self, image: Union[str, Path], *, lang: str = "vie") -> None:
        self.image_path: Path = Path(image)
        self.lang = lang

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.image_path.name})"

    def ocr_only(
        self,
        preprocess: Literal["thresh", "blur"] = "thresh",
    ) -> str:
        """OCR only (no output file)"""

        # Load
        img: MatLike = cv2.imread(self.image_path.__str__())  # Read img file
        gray_img: MatLike = cv2.cvtColor(
            img, cv2.COLOR_BGR2GRAY
        )  # Convert to grayscale

        # Preprocess
        if preprocess == "thresh":  # Black white only
            gray_img = cv2.threshold(
                gray_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU
            )[1]
        else:  # Blur
            gray_img = cv2.medianBlur(gray_img, 3)

        # Extract text
        text = pytesseract.image_to_string(Image.fromarray(gray_img), lang=self.lang)

        # Return
        return text  # type: ignore

    def ocr(
        self,
        save_destination: Union[str, Path, None] = None,
        preprocess: Literal["thresh", "blur"] = "thresh",
    ) -> None:
        """OCR"""
        if save_destination is None:
            output_path = self.image_path.with_suffix(".txt")
        else:
            output_path = Path(save_destination)
        with open(output_path, "w", encoding="utf-8") as f:
            ocr_res = self.ocr_only(preprocess=preprocess)
            f.write(ocr_res)


class VietOCR_Directory:
    """
    Vietnamese image OCR - Directory
    """

    def __init__(self, image_dir: Union[str, Path], *, lang: str = "vie") -> None:
        self.image_path: Path = Path(image_dir)
        self.lang = lang

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.image_path.name})"

    def list_of_img(self) -> List[Path]:
        list_of_img = [
            img
            for img in self.image_path.iterdir()
            if img.suffix.lower() in VALID_IMG_SUFFIX
        ]
        return list_of_img

    def make_save_destination(
        self,
        save_destination: Union[str, Path, None] = None,
    ) -> Path:
        if save_destination is not None:
            save_folder = Path(save_destination)
        else:
            save_folder = self.image_path.with_name(f"{self.image_path.name}_extracted")
        save_folder.mkdir(exist_ok=True, parents=True)
        return save_folder

    def ocr(
        self,
        save_destination: Union[str, Path, None] = None,
        preprocess: Literal["thresh", "blur"] = "thresh",
    ) -> None:
        """Performs OCR on img dir

        :param save_destination: Folder location, defaults to None
        :type save_destination: str | Path | None, optional
        :param preprocess: Preprocess, defaults to "thresh"
        :type preprocess: Literal[&quot;thresh&quot;, &quot;blur&quot;], optional
        """
        save_folder = self.make_save_destination(save_destination)
        for img in tqdm(
            self.list_of_img(), desc="Extracting text", unit_scale=True, ncols=88
        ):
            ocr_engine = VietOCR_File(img, lang=self.lang)
            save_path = save_folder.joinpath(img.with_suffix(".txt").name)
            ocr_engine.ocr(save_destination=save_path, preprocess=preprocess)

    def ocr_multithread(
        self,
        n_jobs: int = -1,
        save_destination: Union[str, Path, None] = None,
        preprocess: Literal["thresh", "blur"] = "thresh",
    ) -> None:
        save_folder = self.make_save_destination(save_destination)

        def _ocr(img: Path):
            ocr_engine = VietOCR_File(img, lang=self.lang)
            save_path = save_folder.joinpath(img.with_suffix(".txt").name)
            ocr_engine.ocr(save_destination=save_path, preprocess=preprocess)

        # Multithread
        Parallel(n_jobs=n_jobs)(
            delayed(_ocr)(img)
            for img in tqdm(
                self.list_of_img(), desc="Extracting text", unit_scale=True, ncols=88
            )
        )


class VietOCR:
    """
    Vietnamese image OCR
    """

    def __init__(self, path: Union[str, Path], *, lang: str = "vie") -> None:
        self.path: Path = Path(path)
        if not self.path.exists():
            raise ValueError("Path does not exist")
        self.lang = lang

        if self.path.is_dir():
            self.engine = VietOCR_Directory(self.path, lang=self.lang)
        else:
            self.engine = VietOCR_File(self.path, lang=self.lang)  # type: ignore

    def ocr(
        self,
        save_destination: Union[str, Path, None] = None,
        preprocess: Literal["thresh", "blur"] = "thresh",
    ) -> None:
        try:
            self.engine.ocr_multithread(
                save_destination=save_destination, preprocess=preprocess
            )
        except Exception:
            self.engine.ocr(save_destination=save_destination, preprocess=preprocess)
