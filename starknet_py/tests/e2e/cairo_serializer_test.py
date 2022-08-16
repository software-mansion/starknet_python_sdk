import pytest


value_types = [
    {"name": "key", "type": "felt"},
    {"name": "prev_value", "type": "felt"},
    {"name": "value", "type": "felt"},
]


@pytest.mark.asyncio
async def test_from_python(cairo_serializer):
    args = [10]
    kwargs = {"prev_value": 0, "value": 20}
    cairo_data = cairo_serializer.from_python(value_types, *args, **kwargs)

    assert cairo_data == ([10, 0, 20], {"key": [10], "prev_value": [0], "value": [20]})


@pytest.mark.asyncio
async def test_from_python_both_positional_and_named(cairo_serializer):
    args = [10, 11]
    kwargs = {"prev_value": 0, "value": 20}
    with pytest.raises(
        TypeError, match="Both positional and named argument provided for prev_value."
    ):
        cairo_serializer.from_python(value_types, *args, **kwargs)


@pytest.mark.asyncio
async def test_from_python_invalid_positional(cairo_serializer):
    args = [10, 11, 12, 13]
    with pytest.raises(
        TypeError,
        match=f"Provided {len(args)} positional arguments, {len(value_types)} possible.",
    ):
        cairo_serializer.from_python(value_types, *args)


@pytest.mark.asyncio
async def test_from_python_unnecessary_named(cairo_serializer):
    args = [10, 11]
    kwargs = {"value": 20, "count": 4}
    with pytest.raises(TypeError, match="Unnecessary named argument count=4 provided."):
        cairo_serializer.from_python(value_types, *args, **kwargs)
