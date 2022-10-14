"""pytest covrage module이 테스트할 파일이 없을 때 에러가 나는 것을 방지하기 위한 예제 파일.

다른 모듈이 구현되면 삭제 예정

Author:
    Kibum Park
E-mail:
    castedice1@gmail.com
"""
from app.example import add


def test_add() -> None:
    """Test add function."""
    a: int = 10
    b: int = 20
    assert add(a, b) == 30
