from python.challenges.hashtable.hashtable import *

def test_add():
    table = Hashtable()
    table.add('mahmoud','Engineer')
    assert table.map[table.hash('mahmoud')].head.data == ['mahmoud','Engineer']

def test_update():
    table = Hashtable()
    table.add('mahmoud','Engineer')
    table.add('mahmoudHasan','GOAT')
    assert table.map[table.hash('mahmoud')].head.data[1] == 'Engineer'


def test_get():
    table = Hashtable()
    table.add('mahmoud','Engineer')
    assert table.get('mahmoud') == 'Engineer'

def test_get_Null():
    table = Hashtable()
    assert table.get('mahmoud') == 'Not found'

def test_handle_collisons():
    expected = "['mahmoud', 'Engineer']-->['mahmoudHasan', 'GOAT']-->None"
    table = Hashtable()
    table.add('mahmoud','Engineer')
    table.add('mahmoudHasan','GOAT')
    actual = table.__str__()
    assert actual == expected

    


def test_retrieve():
    table = Hashtable()
    table.add('mahmoud','Engineer')
    table.add('mahmoudhasan','GOAT')
    assert table.get('mahmoud') == 'Engineer'
    assert table.get('mahmoudhasan') == 'GOAT'