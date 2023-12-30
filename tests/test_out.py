from kafkapy.out import check_is_serializable

def test_is_seriazable_returns_serialized_for_strings() -> None:
    assert check_is_serializable("foo") == "foo"

def test_is_serializable_returns_serialized_for_implementing_class() -> None:
    class F:
        def as_json(self) -> str:
            return "custom"
    assert check_is_serializable(F()) == "custom"