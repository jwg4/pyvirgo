import re


MULTILINE_COMMENT_REGEX = re.compile(r"[/][*][^*]*([*][^/][^*]*)*[*][/]")
CONTINUATION_REGEX = re.compile(r"[|]\n")
COMMENT_REGEX = re.compile(r"[/]{2}.*$")

def _gen_preprocess(data):
    data = MULTILINE_COMMENT_REGEX.sub("", data)
    data = CONTINUATION_REGEX.sub("", data)
    for line in data.split("\n"):
        yield COMMENT_REGEX.sub("", line)        
    yield ""


def preprocess(data):
    return "\n".join(_gen_preprocess(data))
