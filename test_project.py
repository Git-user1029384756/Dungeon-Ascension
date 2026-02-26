from project import should_descend_floor, calculate_new_floor_on_defeat, create_enemy_for_floor
from config import VICTORIES_REQUIRED, MAX_FLOOR


def test_create_enemy_for_floor_boss():
    enemy = create_enemy_for_floor(5)
    assert enemy.is_boss is True

def test_create_enemy_for_floor_non_boss():
    enemy = create_enemy_for_floor(1)
    assert enemy.is_boss is False

def test_should_descend_floor():
    assert should_descend_floor(VICTORIES_REQUIRED, 2) is True
    assert should_descend_floor(VICTORIES_REQUIRED - 1, MAX_FLOOR) is False

def test_calculate_new_floor_on_defeat():
    assert calculate_new_floor_on_defeat(3) == 2

def test_calculate_new_floor_on_defeat_floor1():
    assert calculate_new_floor_on_defeat(1) == 1
