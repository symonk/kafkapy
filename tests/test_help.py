from kafkapy.help import generate_help
from kafkapy.constants import CommandMeta

def test_generate_basic_help() -> None:
    basic = CommandMeta("list", danger=False)
    expected = f"[b][white]list.[/][/] :star2:"
    assert generate_help(command=basic) == expected


def test_generate_danger_help() -> None:
    dangerous = CommandMeta("delete", danger=True)
    expected = f"[b][white][b][red][Danger][/][/] delete.[/][/] :triangular_flag_on_post:"
    assert generate_help(command=dangerous) == expected