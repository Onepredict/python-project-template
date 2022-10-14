"""pytest covrage module이 테스트할 파일이 없을 때 에러가 나는 것을 방지하기 위한 예제 파일.

다른 모듈이 구현되면 삭제 예정

Author:
    Kibum Park
E-mail:
    castedice1@gmail.com
"""


def add(int_a: int, int_b: int) -> int:
    """Add two integer.

    Args:
        int_a (int): any integer.
        int_b (int): any integer.

    Returns:
        int: sum of two integers

    """
    return int_a + int_b
