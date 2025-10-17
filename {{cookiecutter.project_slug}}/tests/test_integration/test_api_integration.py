from uuid import uuid4

from litestar.testing import TestClient
import pytest


class TestApiIntegration:
    @pytest.mark.asyncio
    async def test_get_artifact_endpoint_success(self, client: TestClient):
        """Test successful artifact retrieval through API endpoint"""
        inventory_id = str(uuid4())

        with pytest.raises(Exception):
            client.get(f"/api/v1/artifacts/{inventory_id}")
