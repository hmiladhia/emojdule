def test_import() -> None:
    import package

    assert package.A == "a"

    from package import module

    assert module.B == "b"

    from package.subpackage import C

    assert C == "c"

    from package.subpackage.submodule import D

    assert D == "d"

    from package.subpackage.submodule2 import E

    assert E == "e"
