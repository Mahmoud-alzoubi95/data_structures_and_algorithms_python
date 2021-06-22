from python.challenges.left_join.left_join import *

def test_regular_way():
    h1 = Hashtable()
    h1.add('fond','enamored')        
    h1.add('fnod', 'anger')          
    h1.add('fodn', 'employed')    
    h1.add('donf', 'garb')           
    h1.add('ofnd', 'usher')

    h2 = Hashtable()
    h2.add('fond', 'averse')
    h2.add('fnod', 'delight')
    h2.add('fodn', 'idle')
    h2.add('guide', 'follow')
    h2.add('flow', 'jam')

    expected = [['ofnd', 'usher', None], ['donf', 'garb', None], ['fodn', 'employed', 'idle'], ['fnod', 'anger', 'delight'], ['fond', 'enamored', 'averse']]
    actual = left_join(h1,h2)
    assert expected == actual

def test_first_hashtable_empty():
    h1 = Hashtable()
    h2 = Hashtable()
    h2.add('fond', 'averse')
    h2.add('wrath', 'delight')
    h2.add('diligent', 'idle')
    h2.add('guide', 'follow')
    h2.add('flow', 'jam')

    expected = []
    actual = left_join(h1,h2)
    assert expected == actual

def test_left_join_no_matches():
    one = Hashtable()
    one.add('pond','enamored')        
    one.add('rath', 'anger')          
    one.add('adiligent', 'employed')    
    one.add('poutfit', 'garb')           
    one.add('hangguide', 'usher')           

    two = Hashtable()
    two.add('fond', 'averse')
    two.add('wrath', 'delight')
    two.add('diligent', 'idle')
    two.add('guide', 'follow')
    two.add('flow', 'jam')

    expected = [['poutfit', 'garb', None], ['hangguide', 'usher', None], ['adiligent', 'employed', None], ['rath', 'anger', None], ['pond', 'enamored', None]]

    actual = left_join(one,two)

    assert expected == actual


