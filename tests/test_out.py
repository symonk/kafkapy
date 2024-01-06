from kafkapy.out import check_is_serializable
from pydantic import BaseModel

def test_is_seriazable_returns_serialized_for_strings() -> None:
    assert check_is_serializable("foo") == "foo"

def test_is_serializable_returns_serialized_for_implementing_class() -> None:
    class F(BaseModel):
        foo: str
    assert check_is_serializable(F(foo="foo")) == '{"foo":"foo"}'