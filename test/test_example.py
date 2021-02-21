import virgo


def test_parse_basic_example():
    with open("test/files/config.vgo") as f:
        data = f.read()
    g = virgo.parse(data)
    assert g is not None 
