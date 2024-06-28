from fastapi.testclient import TestClient
from src.excel_api.main import app
from pandas import DataFrame
import itertools

client = TestClient(app)


def test_upload_excel():
    df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    file_content = df.to_csv(index=False).encode()
    files = {"file": ("test.csv", file_content, "text/csv")}
    response = client.post("/v1/uploading/uploading/upload_excel", files=files)
    assert response.status_code == 200


def test_upload_invalid_file():
    file_content = b"invalid content"
    files = {"file": ("test.txt", file_content, "text/plain")}

    response = client.post("/v1/uploading/uploading/upload_excel", files=files)
    assert response.status_code == 400


def test_upload_excel_invalid_data_type():
    df = DataFrame({"a": [1.0, 2.5, 3.1], "b": [4, 5, 6]})
    file_content = df.to_csv(index=False).encode()
    files = {"file": ("test.csv", file_content, "text/csv")}

    response = client.post("/v1/uploading/upload_excel", files=files)
    assert response.status_code == 400
    assert "Invalid data type" in response.text




def test_upload_excel_subset_combinations():
    features = ["A", "B", "C"]
    all_combinations = []

    # Generate all combinations of subsets
    for r in range(1, len(features) + 1):
        combinations = itertools.combinations(features, r)
        all_combinations.extend(list(combinations))

    # Test each combination
    for combo in all_combinations:
        df = DataFrame({feature: [1] for feature in combo})
        file_content = df.to_csv(index=False).encode()
        files = {"file": ("test.csv", file_content, "text/csv")}

        response = client.post("/v1/uploading/upload_excel", files=files)
        assert response.status_code == 200

