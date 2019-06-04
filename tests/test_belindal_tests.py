from hypothesis import strategies as st, given, reproduce_failure
from ds_bootcamp.flask_app import MIN_VALUE, MAX_VALUE


def test_get_meta(client):
    res = client.get("/belinda")
    assert res.status_code == 200


def test_bye(client):
    res = client.get("/belinda_bye")
    assert res.status_code == 200


def test_belinda_model(client):
    res = client.get("/belinda_model/submodel_1/10")
    assert res.status_code == 200
    assert res.json['score'] == 25


@given(
    x=st.integers(min_value=MIN_VALUE, max_value=MAX_VALUE)
)
def test_belinda_model_hypothesis(client, x):
    res = client.get(f"/belinda_model/submodel_1/{x}")
    assert res.status_code == 200
    assert res.json['score'] > x


@given(
    x=st.integers(max_value=MIN_VALUE-1)
)
def test_belinda_model_hypothesis_bad_value(client, x):
    res = client.get(f"/belinda_model/submodel_1/{x}")
    assert res.status_code == 400


def test_belinda_model_404(client):
    res = client.get("/belinda_model/submodel_3/10")
    assert res.status_code == 404
