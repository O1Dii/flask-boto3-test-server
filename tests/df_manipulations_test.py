from df_manipulations import df_sum
import pandas as pd
import pytest


@pytest.fixture
def df_with_floats():
    return pd.DataFrame({
        '1': [1, 2, 3],
        '2': [3, 2, 1]
    })


# @given(data_frames([
#     column('1', dtype='float'),
#     column('2', dtype='float')
# ]))
def test_sum(monkeypatch, df_with_floats):
    with monkeypatch.context() as context:
        result = df_sum(df_with_floats)

    assert len(result.columns) == 3
    assert result['3'].dtype == 'int'
