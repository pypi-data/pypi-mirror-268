import pytest
from src.twwt import TextCleaner


@pytest.mark.parametrize(
    "parentheses,punctuation,gap,qmark,symbols,math,custom,text,result",
    [
        (True, False, False, False, False, False, None, """(){}[],.!?:;'"«»&^%$#@~-+=*/><\t\n""", """,.!?:;'"«»&^%$#@~-+=*/><\t\n"""),
        (False, True, False, False, False, False, None, """(){}[],.!?:;'"«»&^%$#@~-+=*/><\t\n""", """(){}[]'"«»&^%$#@~-+=*/><\t\n"""),
        (False, False, True, False, False, False, None, """(){}[],.!?:;'"«»&^%$#@~-+=*/><\t\n""", """(){}[],.!?:;'"«»&^%$#@~-+=*/><"""),
        (False, False, False, True, False, False, None, """(){}[],.!?:;'"«»&^%$#@~-+=*/><\t\n""", """(){}[],.!?:;&^%$#@~-+=*/><\t\n"""),
        (False, False, False, False, True, False, None, """(){}[],.!?:;'"«»&^%$#@~-+=*/><\t\n""", """(){}[],.!?:;'"«»-+=*/><\t\n"""),
        (False, False, False, False, False, True, None, """(){}[],.!?:;'"«»&^%$#@~-+=*/><\t\n""", """(){}[],.!?:;'"«»&^%$#@~\t\n"""),
        (False, False, False, False, False, False, ["(", ",", "«", "+", "\t"], """(){}[],.!?:;'"«»&^%$#@~-+=*/><\t\n""", """){}[].!?:;'"»&^%$#@~-=*/><\n"""),
        (True, True, False, False, False, False, None, """(){}[],.!?:;'"«»&^%$#@~-+=*/><\t\n""", """'"«»&^%$#@~-+=*/><\t\n"""),
        (False, True, True, False, False, False, None, """(){}[],.!?:;'"«»&^%$#@~-+=*/><\t\n""", """(){}[]'"«»&^%$#@~-+=*/><"""),
        (False, False, True, True, False, False, None, """(){}[],.!?:;'"«»&^%$#@~-+=*/><\t\n""", """(){}[],.!?:;&^%$#@~-+=*/><"""),
        (False, False, False, True, True, False, None, """(){}[],.!?:;'"«»&^%$#@~-+=*/><\t\n""", """(){}[],.!?:;-+=*/><\t\n"""),
        (False, False, False, False, True, True, None, """(){}[],.!?:;'"«»&^%$#@~-+=*/><\t\n""", """(){}[],.!?:;'"«»\t\n"""),
        (False, False, False, False, False, False, None, """(){}[],.!?:;'"«»&^%$#@~-+=*/><\t\n""", """(){}[],.!?:;'"«»&^%$#@~-+=*/><\t\n"""),
        (True, False, False, False, False, False, None, """ ( ) { } [ ] !""", """       !"""),
    ]
)
def test_clean(
        parentheses,
        punctuation,
        gap,
        qmark,
        symbols,
        math,
        custom,
        text,
        result
):
    """Тестирование функции clean()"""
    assert TextCleaner(
        parentheses,
        punctuation,
        gap,
        qmark,
        symbols,
        math,
        custom
    ).clean(text) == result
