from python.challenges.graph_business.graph_business import *
import pytest

def test_pass_case():
    graph = Graph()
    node_a = graph.add_node('a')
    node_b = graph.add_node('b')
    node_c = graph.add_node('c')
    graph.add_edge(node_a,node_c, 13)
    graph.add_edge(node_b,node_c, 7)
    lis=[node_a,node_c]
    acctual = graph.business_trip(lis)
    excepted = True ,"13$"
    assert acctual==excepted

def test_three_nodes():
    graph = Graph()
    node_a = graph.add_node('a')
    node_b = graph.add_node('b')
    node_c = graph.add_node('c')
    graph.add_edge(node_a,node_c, 13)
    graph.add_edge(node_b,node_c, 7)
    lis=[node_a,node_c,node_b ]
    acctual = graph.business_trip(lis)
    excepted = True ,"20$"
    assert acctual==excepted
def test_no_edges():
    graph = Graph()
    node_a = graph.add_node('a')
    node_b = graph.add_node('b')
    node_c = graph.add_node('c')
    graph.add_edge(node_a,node_c, 13)
    graph.add_edge(node_b,node_c, 7)
    lis=[node_a,node_b ]
    acctual = graph.business_trip(lis)
    excepted = False ,"0$"
    assert acctual==excepted
def test_three_edges():
    graph = Graph()
    node_a = graph.add_node('a')
    node_b = graph.add_node('b')
    node_c = graph.add_node('c')
    node_d = graph.add_node('d')
    node_e = graph.add_node('e')
    node_f = graph.add_node('f')
    graph.add_edge(node_a,node_c,5)
    graph.add_edge(node_a,node_d,6)
    graph.add_edge(node_b,node_c, 11)
    graph.add_edge(node_b,node_f,7)
    graph.add_edge(node_c,node_e,8)
    graph.add_edge(node_d ,node_e,9)
    graph.add_edge(node_e,node_f,10)
    lis=[node_a, node_c,  node_e,node_f,]
    acctual = graph.business_trip(lis)
    excepted = True, '23$'
    assert acctual==excepted


def test_false_edges():
    graph = Graph()
    node_a = graph.add_node('a')
    node_b = graph.add_node('b')
    node_c = graph.add_node('c')
    node_d = graph.add_node('d')
    node_e = graph.add_node('e')
    node_f = graph.add_node('f')
    graph.add_edge(node_a,node_c,5)
    graph.add_edge(node_a,node_d,6)
    graph.add_edge(node_e,node_f,10)
    lis=[node_a, node_d, node_e]
    acctual = graph.business_trip(lis)
    excepted = False, '0$'
    assert acctual==excepted
def test_edges():
    graph = Graph()
    node_a = graph.add_node('a')
    node_b = graph.add_node('b')
    node_c = graph.add_node('c')
    node_d = graph.add_node('d')
    node_e = graph.add_node('e')
    node_f = graph.add_node('f')
    graph.add_edge(node_a,node_c,5)
    graph.add_edge(node_a,node_d,6)
    graph.add_edge(node_b,node_c, 11)
    graph.add_edge(node_b,node_f,7)
    graph.add_edge(node_c,node_e,8)
    graph.add_edge(node_d ,node_e,9)
    graph.add_edge(node_e,node_f,10)
    lis=[node_a, node_d, node_e]
    acctual = graph.business_trip(lis)
    excepted = True, '15$'
    assert acctual==excepted
def test_tow_edges():
    graph = Graph()
    node_a = graph.add_node('a')
    node_b = graph.add_node('b')
    node_c = graph.add_node('c')
    node_d = graph.add_node('d')
    node_e = graph.add_node('e')
    node_f = graph.add_node('f')
    graph.add_edge(node_a,node_c,5)
    graph.add_edge(node_a,node_d,6)
    graph.add_edge(node_b,node_c, 11)
    graph.add_edge(node_b,node_f,7)
    graph.add_edge(node_c,node_e,8)
    graph.add_edge(node_d ,node_e,9)
    graph.add_edge(node_e,node_f,10)
    lis=[node_a, node_e]
    acctual = graph.business_trip(lis)
    excepted = False, '0$'
    assert acctual==excepted
def test_tow_pass_edges():
    graph = Graph()
    node_a = graph.add_node('a')
    node_b = graph.add_node('b')
    node_c = graph.add_node('c')
    node_d = graph.add_node('d')
    node_e = graph.add_node('e')
    node_f = graph.add_node('f')
    graph.add_edge(node_a,node_c,5)
    graph.add_edge(node_a,node_d,6)
    graph.add_edge(node_b,node_c, 11)
    graph.add_edge(node_b,node_f,7)
    graph.add_edge(node_c,node_e,8)
    graph.add_edge(node_d ,node_e,9)
    graph.add_edge(node_e,node_f,10)
    lis=[node_d, node_e]
    acctual = graph.business_trip(lis)
    excepted = True, '9$'
    assert acctual==excepted