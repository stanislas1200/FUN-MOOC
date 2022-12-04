
import sys  
from unittest import mock
import random
from pytest import MonkeyPatch
import demineur as demineur

"""
Lancez les tests avec la commande "pytest -v demineur_test.py"
La librairie Pytest de Python doit pour cela être installée.
Pour que les test fonctionnet, il faut également que votre fonction "main()" renvoie 1 en cas de victoire, 0 en cas de défaite.
En cas d'échec, regardez bien les coups joués ainsi que les conditions de réussite du test.
"""

def test_place_mines():
    random.seed(27)
    ref = demineur.create_board(12, 12)
    n_mines = 20
    positions = [[10, 7], [11, 4], [4, 3], [4, 8], [5, 4], [5, 6], [3, 7], 
                 [1, 11], [10, 9], [10, 1], [9, 6], [6, 11], [0, 10], [7, 5], 
                [7, 4], [2, 9], [5, 9], [10, 3], [11, 8], [6, 4]]


    computed_positions = demineur.place_mines(ref, n_mines, 2, 2)
    assert(positions == computed_positions)

def test_init_game(monkeypatch):
    random.seed(35)
    # Série de coups joués par le test
    inputs = (inp for inp in ['c 2 2']) 
    monkeypatch.setattr('builtins.input', lambda x: next(inputs))
    _, _, mines_list = demineur.init_game(12, 12, 20)
    expected_mines_list = [[8, 5], [2, 11], [5, 2], [4, 6], [4, 9], [0, 11], 
                           [8, 4], [10, 5], [11, 9], [1, 5], [0, 8], [0, 1], 
                           [11, 7], [5, 11], [0, 5], [10, 7], [0, 0], [3, 5], 
                           [9, 1], [7, 5]]


    assert(expected_mines_list == mines_list)

def test_main_win_1(monkeypatch):
    """
    Victoire en découvrant toutes les cases safe
    """
    random.seed(35)
    args = ['', '12', '12', '5']
    with mock.patch.object(sys, 'argv', args):
        # Série de coups joués par le test
        inputs = (inp for inp in ['c 2 2', 'c 4 7', 'c 4 8']) 
        monkeypatch.setattr('builtins.input', lambda x: next(inputs))
        game = demineur.main()
        assert (game == 1)

def test_main_win_2(monkeypatch):
    """
    Victoire en flaggant toutes les mines
    """
    random.seed(74)
    args = ['', '8', '12', '4']
    with mock.patch.object(sys, 'argv', args):
        # Série de coups joués par le test
        inputs = (inp for inp in ['c 2 2', 'f 5 1', 'F 1 4', 'f 1 5', 'F 7 7']) 
        monkeypatch.setattr('builtins.input', lambda x: next(inputs))
        game = demineur.main()
        assert (game == 1)

def test_main_win_3(monkeypatch):
    """
    Victoire en flaggant toutes les mines
        - Avec retrait de drapeau mal placé
    """
    random.seed(74)
    args = ['', '8', '12', '4']
    with mock.patch.object(sys, 'argv', args):
        # Série de coups joués par le test
        inputs = (inp for inp in ['c 2 2', 'f 5 1', 'F 1 4', 'F 0 4', 'F 0 4',
                                  'f 1 5', 'F 7 7']) 
        monkeypatch.setattr('builtins.input', lambda x: next(inputs))
        game = demineur.main()
        assert (game == 1)

def test_main_win_4(monkeypatch):
    """
    Découverte de toutes les cases, multiples propagations de clicks
    """
    random.seed(74)
    args = ['', '10', '10', '20']
    with mock.patch.object(sys, 'argv', args):
        # Série de coups joués par le test
        inputs = (inp for inp in ['c 2 2', 'c 5 7', 'c 9 0', 'c 9 6',
                  'c 0 1', 'c 0 4', 'c 0 5', 'c 0 6', 'c 0 7', 'c 0 9',
                  'c 1 6', 'c 1 7', 'c 1 8', 'c 1 9', 'c 1 7', 'c 1 9',
                  'c 2 4', 'c 2 5', 'c 2 6', 'c 2 7', 'c 2 8',
                  'c 3 4', 'c 3 5',  'c 3 6',
                  'c 5 2', 'c 5 3',
                  'c 6 1', 'c 6 2', 'c 6 4',
                  'c 7 3', 'c 7 4', 'c 7 5', 'c 7 6',
                  'c 8 8',
                  'c 9 3', 'c 9 4', 'c 9 9'])
        monkeypatch.setattr('builtins.input', lambda x: next(inputs))
        game = demineur.main()
        assert (game == 1)

def test_main_lose_1(monkeypatch):
    """
    Click sur mine
    """
    random.seed(35)
    args = ['', '12', '12', '5']
    with mock.patch.object(sys, 'argv', args):
        # Série de coups joués par le test
        inputs = (inp for inp in ['c 2 2', 'c 5 2']) 
        monkeypatch.setattr('builtins.input', lambda x: next(inputs))
        game = demineur.main()
        assert (game == 0)

def test_echec_input(monkeypatch):
    """
    Séries d'inputs incorrects suivi 
    """
    random.seed(74)
    args = ['', '12', '12', '5']
    with mock.patch.object(sys, 'argv', args):
        # Série de coups joués par le test
        inputs = (inp for inp in ['c 20 20', 'c -1 2', '2 2', 'v 2 2', 'c 2 2', 'c 5 1']) 
        monkeypatch.setattr('builtins.input', lambda x: next(inputs))
        game = demineur.main()
        assert (game == 0)
