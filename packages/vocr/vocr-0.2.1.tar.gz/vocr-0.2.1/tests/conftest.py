from pathlib import Path

import pytest

IMG_TEST_FOLDER = Path(__file__).parent.joinpath("img")
IMG_TEST_OUTPUT = IMG_TEST_FOLDER.with_name("output")
IMG_TEST_OUTPUT.mkdir(exist_ok=True, parents=True)
with open(IMG_TEST_OUTPUT.joinpath(".gitignore"), "w", encoding="utf-8") as f:
    f.write("*")


@pytest.fixture
def test_pic() -> Path:
    return IMG_TEST_FOLDER.joinpath("sample1.jpg")


@pytest.fixture
def test_directory() -> Path:
    return IMG_TEST_FOLDER


@pytest.fixture
def test_output() -> Path:
    return IMG_TEST_OUTPUT
