import pytest
from favorite_things_functions import add_favorite, update_favorite, delete_favorite, display_favorites, validate_input

def test_add_favorite():
    data = {}
    # 模拟添加
    def fake_input(prompt):
        if "category" in prompt:
            return "color"
        return "blue"
    orig_input = __builtins__.input
    __builtins__.input = fake_input
    try:
        add_favorite(data)
    finally:
        __builtins__.input = orig_input
    assert data == {"color": "blue"}

def test_update_favorite():
    data = {"food": "pizza"}
    def fake_input(prompt):
        if "category" in prompt:
            return "food"
        return "sushi"
    orig_input = __builtins__.input
    __builtins__.input = fake_input
    try:
        update_favorite(data)
    finally:
        __builtins__.input = orig_input
    assert data["food"] == "sushi"

def test_delete_favorite():
    data = {"movie": "Interstellar"}
    def fake_input(prompt):
        if "Are you sure" in prompt:
            return "y"
        return "movie"
    orig_input = __builtins__.input
    __builtins__.input = fake_input
    try:
        delete_favorite(data)
    finally:
        __builtins__.input = orig_input
    assert "movie" not in data

def test_validate_input():
    # 测试有效输入
    assert validate_input("test")[0] == True
    
    # 测试空输入
    assert validate_input("")[0] == False
    assert validate_input("   ")[0] == False
    
    # 测试特殊字符
    assert validate_input("test<test")[0] == False
    assert validate_input("test>test")[0] == False
    assert validate_input("test:test")[0] == False
    
    # 测试长度限制
    long_input = "a" * 51
    assert validate_input(long_input)[0] == False

def test_display_favorites(capfd):
    # Test with data
    favorites = {"color": "blue", "food": "pizza"}
    display_favorites(favorites)
    out, err = capfd.readouterr()
    assert "color: blue" in out
    assert "food: pizza" in out
    
    # Test with empty data
    display_favorites({})
    out, err = capfd.readouterr()
    assert "You don't have any favorites yet" in out 