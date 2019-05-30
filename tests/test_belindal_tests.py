

def test_get_meta(client):
    res = client.get("/")
    assert res.status_code == 200


def test_bye(client):
    res = client.get("/bye")
    assert res.status_code == 200
