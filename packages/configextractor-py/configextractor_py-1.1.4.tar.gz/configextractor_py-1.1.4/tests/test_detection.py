import pytest

from configextractor.main import ConfigExtractor


@pytest.fixture
def cx():
    yield ConfigExtractor(["tests/parsers"])


def test_general_detection(cx):
    # Check to see if we actually detected any of the test parsers
    assert cx.parsers


def test_cape_detection(cx):
    # Ensure the CAPE parser was detected and NOT the class wrapping a similar CAPE function signature
    # A confusion in detection can throw off automated systems like Assemblyline
    assert "parsers.cape_extractor" in cx.parsers
    assert "parsers.cape_extractor.CAPEWrapper" not in cx.parsers


def test_maco_detection(cx):
    # Ensure the subclass was detected
    assert "parsers.maco_extractor.TestMACO" in cx.parsers
    assert "parsers.maco_extractor.Extractor" not in cx.parsers


def test_mwcp_detection(cx):
    # Ensure the subclass was detected
    assert "parsers.mwcp_extractor.TestMWCP" in cx.parsers
    assert "parsers.mwcp_extractor.Parser" not in cx.parsers
