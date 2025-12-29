import pytest
from hypothesis import given, strategies as st
from app.utils import id_generator


@given(start=st.integers(min_value=-10**6, max_value=10**6), n=st.integers(min_value=1, max_value=50))
def test_id_generator_monotonic(start, n):
    gen = id_generator(start)
    vals = [next(gen) for _ in range(n)]
    assert vals == list(range(start, start + n))


@given(start=st.integers(min_value=0, max_value=1000), n=st.integers(min_value=1, max_value=100))
def test_id_generator_unique(start, n):
    gen = id_generator(start)
    vals = [next(gen) for _ in range(n)]
    assert len(set(vals)) == n


@given(bad=st.one_of(st.text(), st.none(), st.lists(st.integers())))
def test_id_generator_invalid_types_raise(bad):
    gen = id_generator(bad)
    # the generator yields the initial value but should fail when attempting to increment
    _ = next(gen)
    with pytest.raises(TypeError):
        next(gen)


@given(start=st.integers(min_value=10**18, max_value=10**20), n=st.integers(min_value=1, max_value=5))
def test_id_generator_large_values(start, n):
    gen = id_generator(start)
    vals = [next(gen) for _ in range(n)]
    assert vals == list(range(start, start + n))


@given(start=st.floats(allow_nan=False, allow_infinity=False), n=st.integers(min_value=2, max_value=5))
def test_id_generator_with_float(start, n):
    # floats are supported by current implementation; verify sequence increments by 1.0
    gen = id_generator(start)
    vals = [next(gen) for _ in range(n)]
    assert vals[0] == start
    assert pytest.approx(vals[1]) == start + 1.0
