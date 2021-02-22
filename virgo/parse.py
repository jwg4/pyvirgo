import re

import ply.lex as lex
import ply.yacc as yacc


COMMENT_REGEX = re.compile(r"[/]{2}.*$")

def _gen_preprocess(data):
    for line in data.split("\n"):
        yield COMMENT_REGEX.sub("", line)        
    yield ""


def preprocess(data):
    return "\n".join(_gen_preprocess(data))


tokens = (
    'NODENAME',
    'LEFT_CONNECT',
    'RIGHT_CONNECT',
    'BOTH_CONNECT',
    'COMMA',
    'NEWLINE',
)

t_NODENAME = r'[a-zA-Z_:][a-zA-Z_:0-9]*'
t_LEFT_CONNECT = r'->'
t_RIGHT_CONNECT = r'<-'
t_BOTH_CONNECT = r'--'
t_COMMA = r','
t_NEWLINE = r'\n'

t_ignore = " \t"

lexer = lex.lex()


def tokenize(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        yield tok


def p_connectionlist_lines(p):
    'connection_list : connection_list connection_list'
    p[0] = p[1] + p[2]


def p_nodelist_node(p):
    'nodelist : NODENAME'
    p[0] = [p[1]]


def p_nodelist_comma(p):
    'nodelist : nodelist COMMA NODENAME'
    p[0] = p[1] + [p[3]]


def p_right_connect(p):
    'connect : RIGHT_CONNECT'
    p[0] = p[1]


def p_left_connect(p):
    'connect : LEFT_CONNECT'
    p[0] = p[1]


def p_both_connect(p):
    'connect : BOTH_CONNECT'
    p[0] = p[1]


def p_nodelist_connection(p):
    'connections : nodelist connect nodelist'
    p[0] = [Connection(p[1], p[3], p[2])]


def p_nodelist_further_connections(p):
    'connections : connections connect nodelist'
    p[0] = p[1] + [Connection(p[1][-1].second, p[3], p[2])]


def p_connectionlist_empty_line(p):
    'connection_list : NEWLINE'
    p[0] = []


def p_connectionlist_line(p):
    'connection_list : connections NEWLINE'
    p[0] = [p[1]]


def p_error(p):
    print("Syntax error in input: %s" % (p, ))


class Connection(object):
    def __init__(self, first, second, op):
        self.first = first
        self.second = second
        self.op = op


parser = yacc.yacc()


def parse(data):
    clean_data = preprocess(data)
    #tokens = list(tokenize(clean_data))
    print(clean_data)
    result = parser.parse(clean_data, debug=True)
    return result
