"""(Incomplete) Tests for Place class."""
from place import Place


def run_tests():
    """Test Place class."""

    # Test empty place (defaults)
    print("Test empty place:")
    default_place = Place()
    print(default_place)
    assert default_place.name == ""
    assert default_place.country == ""
    assert default_place.priority == 0
    assert not default_place.is_visited

    # Test initial-value place
    print("Test initial-value place:")
    new_place = Place("Malagar", "Spain", 1, False)
    # TODO: Write tests to show this initialisation works
    assert new_place.__str__() == "Malagar in Spain, priority 1"
    new_place.mark_visited()
    assert new_place.__str__() == "Malagar in Spain, priority 1 (visited)"
    assert new_place.isImp() == True
    # TODO: Add more tests, as appropriate, for each method

    place3 = Place("abc", "US", 12, True)
    # TODO: Write tests to show this initialisation works
    assert place3.__str__() == "abc in US, priority 12 (visited)"
    place3.mark_unvisited()
    assert place3.__str__() == "abc in US, priority 12"
    assert place3.isImp() == False

    place4 = Place("cde", "", 2, True)
    assert place4.__str__() == "cde in , priority 2 (visited)"
    place4.mark_unvisited()
    assert place4.__str__() == "cde in , priority 2"
    assert place4.isImp() == True

run_tests()
