from pathlib import Path

from napari_imodmodel import napari_get_reader

TEST_DATA_DIRECTORY = Path(__file__).parent / "test_data"


# tmp_path is a pytest fixture
def test_reader():
    file = str(TEST_DATA_DIRECTORY / "rec_TS_01.mod")
    reader = napari_get_reader(file)
    layers = reader(file)
    assert len(layers) == 3
