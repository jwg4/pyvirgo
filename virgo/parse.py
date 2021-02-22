import re

import ply.lex as lex
import ply.yacc as yacc

from .graph import make_graph
from .internal import Connection
from .preprocess import preprocess


tokens = (
    'NODENAME',
    'QUOTED',
    'LEFT_CONNECT',
    'RIGHT_CONNECT',
    'BOTH_CONNECT',
    'COMMA',
    'NEWLINE',
    'EQUALS',
    'BACKTICK',
    'TEXT',
)

t_NODENAME = r'[a-zA-Z_:][a-zA-Z_:0-9]*'
t_QUOTED = r'"[a-zA-Z_:][a-zA-Z_:0-9 \t]*"'
t_LEFT_CONNECT = r'->'
t_RIGHT_CONNECT = r'<-'
t_BOTH_CONNECT = r'--'
t_COMMA = r','
t_NEWLINE = r'\n'
t_EQUALS = r'='
t_TEXT = r'`[^`]*`'

t_ignore = " \t"

def t_error(t):
    print("Illegal character '%s'" % (t.value[0], ))
    t.lexer.skip(1)

lexer = lex.lex()


def tokenize(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        yield tok


def p_edges_and_nodes_base(p):
    'edges_and_nodes : '
    p[0] = ([], [])


def p_edges_and_nodes_edges(p):
    'edges_and_nodes : edges_and_nodes connection_list'
    p[0] = (p[1][0] + p[2], p[1][1])


def p_edges_and_nodes_nodes(p):
    'edges_and_nodes : edges_and_nodes node_spec'
    p[0] = (p[1][0], p[1][1] + [p[2]])


def p_node_name_nodename(p):
    'node_name : NODENAME'
    p[0] = p[1]


def p_node_name_quoted(p):
    'node_name : QUOTED'
    text = p[1][1:-1]
    p[0] = text


def p_node_spec(p):
    'node_spec : node_name EQUALS TEXT NEWLINE'
    text = p[3][1:-1]
    p[0] = (p[1], text)


def p_nodelist_node(p):
    'nodelist : node_name'
    p[0] = [p[1]]


def p_nodelist_comma(p):
    'nodelist : nodelist COMMA node_name'
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


parser = yacc.yacc()


def parse(data):
    clean_data = preprocess(data)
    result = parser.parse(clean_data)
    return make_graph(result)
