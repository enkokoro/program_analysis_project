# Test cases automatically generated by Pynguin (https://github.com/se2p/pynguin).
# Please check them before you use them.
import pytest
import pet_types as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    none_type_0 = None
    none_type_0.get_age()


def test_case_1():
    str_0 = "_Wmain_j"
    animal_0 = module_0.create_pet(str_0, str_0, str_0)
    assert (
        f"{type(animal_0).__module__}.{type(animal_0).__qualname__}" == "pet_types.Pet"
    )


def test_case_2():
    str_0 = "__main__"
    animal_0 = module_0.Animal(str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "zRJR\x0cP[&_slwIas"
    none_type_0 = None
    var_0 = module_0.create_pet(str_0, none_type_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "pet_types.Pet"
    var_0.__str__()


def test_case_4():
    str_0 = "tA)B[';hP"
    none_type_0 = None
    var_0 = module_0.create_pet(str_0, none_type_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "pet_types.Pet"
    int_0 = var_0.get_age()


def test_case_5():
    none_type_0 = None
    int_0 = -1234
    animal_0 = module_0.Animal(none_type_0, int_0)
    str_0 = "w]QSK+){:*"
    animal_1 = module_0.Animal(str_0)
    var_0 = animal_1.get_complex_object()
    animal_2 = module_0.Animal(animal_1, var_0)
    var_1 = var_0.__str__()


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "pet_types"
    animal_0 = module_0.Animal(str_0)
    var_0 = animal_0.get_complex_object()
    str_1 = animal_0.get_species()
    var_1 = animal_0.__str__()
    str_2 = "3Zce"
    var_2 = module_0.create_pet(var_0, str_2, var_0)
    assert f"{type(var_2).__module__}.{type(var_2).__qualname__}" == "pet_types.Pet"
    int_0 = var_2.get_age()
    assert f"{type(int_0).__module__}.{type(int_0).__qualname__}" == "random.Random"
    assert int_0.gauss_next is None
    var_1.get_species()


def test_case_7():
    none_type_0 = None
    var_0 = module_0.create_pet(none_type_0, none_type_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "pet_types.Pet"