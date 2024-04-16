from __future__ import annotations

import pytest

from toolforge_weld.kubernetes import K8sClient, parse_quantity
from toolforge_weld.kubernetes_config import fake_kube_config


@pytest.fixture
def fake_kubernetes_client() -> K8sClient:
    return K8sClient(
        kubeconfig=fake_kube_config(),
        user_agent="fake",
        timeout=5,
    )


@pytest.mark.parametrize(
    "value,expected",
    [
        ["0.5", 0.5],
        ["500m", 0.5],
        ["1", 1],
        ["0.5k", 500],
        ["1k", 1000],
        ["1G", 1000000000],
        ["1Gi", 1073741824],
    ],
)
def test_parse_quantity(value: str, expected: int | float):
    assert parse_quantity(value) == expected


@pytest.mark.parametrize(
    "kind,name,expected",
    [
        ["namespaces", None, "/api/v1/namespaces"],
        ["namespaces", "tool-test", "/api/v1/namespaces/tool-test"],
        ["pods", None, "/api/v1/namespaces/tool-test/pods"],
        ["pods", "some-pod", "/api/v1/namespaces/tool-test/pods/some-pod"],
        [
            "ingresses",
            None,
            "/apis/networking.k8s.io/v1/namespaces/tool-test/ingresses",
        ],
        [
            "ingresses",
            "some-pod",
            "/apis/networking.k8s.io/v1/namespaces/tool-test/ingresses/some-pod",
        ],
    ],
)
def test_create_url(
    fake_kubernetes_client: K8sClient, kind: str, name: str | None, expected: str
):
    kwargs = fake_kubernetes_client.make_kwargs(
        kind,
        name=name,
        version=K8sClient.VERSIONS[kind],
        namespace="tool-test",
    )

    assert kwargs["url"] == f"{fake_kubernetes_client.server}{expected}"
