webtest_added_data = {}
if "http_x_edwh" in request.env:
    # support functional_test/test.py's test_pyjwt function
    import jwt

    with open(f"{request.folder}/private/jwt.key", "r") as f:
        key = f.read()
        decoded = jwt.decode(request.env.http_x_edwh, key, algorithms=["HS256"])
    webtest_added_data |= decoded
