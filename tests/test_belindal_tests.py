

def test_get_meta(client):
    res = client.get("/belinda")
    assert res.status_code == 200


def test_bye(client):
    res = client.get("/belinda_bye")
    assert res.status_code == 200


def test_belinda_model(client):
    res = client.get("/belinda_model/submodel_1/10")
    assert res.status_code == 200
    assert res.json['score'] == 10


def test_belinda_model_404(client):
    res = client.get("/belinda_model/submodel_3/10")
    assert res.status_code == 404
