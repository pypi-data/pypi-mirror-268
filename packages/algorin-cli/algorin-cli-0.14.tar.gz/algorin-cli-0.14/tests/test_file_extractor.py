# tests/test_file_extractor.py
import pytest
from file_extractor import extract_text_from_pdf, extract_text_from_docx, extract_text_from_pptx, extract_text

def test_extract_text_from_pdf(mocker):
    mocker.patch('PyPDF2.PdfReader', autospec=True)
    assert extract_text_from_pdf('dummy/path.pdf') == "Expected text"

def test_extract_text_from_docx(mocker):
    mocker.patch('docx.Document', autospec=True)
    assert extract_text_from_docx('dummy/path.docx') == "Expected text"

def test_extract_text_from_pptx(mocker):
    mocker.patch('pptx.Presentation', autospec=True)
    assert extract_text_from_pptx('dummy/path.pptx') == "Expected text"

def test_extract_text_unsupported_format():
    with pytest.raises(ValueError):
        extract_text('dummy/path.xyz')
