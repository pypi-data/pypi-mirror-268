from pathlib import Path

import pytest

from vocr.vocr import VietOCR, VietOCR_Directory, VietOCR_File


class TestVOCR:
    @pytest.mark.skip(reason="Somehow doesn't work with Github Action")
    def test_file(self, test_pic: Path, test_output: Path) -> None:
        instance = VietOCR_File(test_pic)
        instance.ocr(test_output.joinpath(test_pic.with_suffix(".txt").name))
        assert True

    @pytest.mark.skip(reason="Somehow doesn't work with Github Action")
    def test_directory(self, test_directory: Path, test_output: Path) -> None:
        instance = VietOCR_Directory(test_directory)
        instance.ocr(test_output.joinpath(test_directory.name))

    @pytest.mark.skip(reason="Somehow doesn't work with Github Action")
    def test_directory_multithread(
        self, test_directory: Path, test_output: Path
    ) -> None:
        instance = VietOCR_Directory(test_directory)
        instance.ocr_multithread(
            save_destination=test_output.joinpath(
                f"{test_directory.name}_multithreaded"
            )
        )

    def test_engine(self, test_pic: Path, test_directory: Path) -> None:
        focr = VietOCR(test_pic)
        assert isinstance(focr.engine, VietOCR_File)
        docr = VietOCR(test_directory)
        assert isinstance(docr.engine, VietOCR_Directory)
