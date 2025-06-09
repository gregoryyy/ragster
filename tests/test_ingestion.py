def test_chunk():
    from ingest.utils import chunk_text
    assert len(chunk_text('a'*1000)) > 1