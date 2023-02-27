""" Tests"""
import pytest
import httpx
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()
client = TestClient(app)


@pytest.mark.asyncio
async def test_get_data():
    response = await client.get("/v1/")
    assert response.status_code == 200
    assert "data" in response.json()
    assert len(response.json()["data"]) > 0


@pytest.mark.asyncio
async def test_get_data_with_invalid_url():
    response = await client.get("/v1/?url=invalid_url")
    assert response.status_code == 500
    assert "detail" in response.json()
    assert "Failed to get data from URL:" in response.json()["detail"]
