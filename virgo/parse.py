import re


COMMENT_REGEX = re.compile(r"[/]{2}.*$")

def _gen_preprocess(data):
    for line in data.split("\n"):
        yield COMMENT_REGEX.sub(line, "")        


def preprocess(data):
    return "\n".join(_gen_preprocess(data))


def parse(data):
    clean_data = preprocess(data)
    return None
