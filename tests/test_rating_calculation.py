import pytest

from tasks import DataCalculationTask

testdata = [
    (25.7, 5, 7),
    (-25.7, 0, 0),
    (19.8, 3, 5),
]


@pytest.mark.parametrize('awt, awp, expected', testdata)
def test_data_calculation(awt: float, awp: float, expected: int):
    rating: int = DataCalculationTask.calculate_rating(
        average_week_temp=awt,
        average_without_precipitation=awp,
    )
    assert rating == expected
