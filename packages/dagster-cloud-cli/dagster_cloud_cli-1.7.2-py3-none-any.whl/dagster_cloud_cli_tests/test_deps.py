import pytest
from dagster_cloud_cli.core.pex_builder.deps import (
    get_and_check_dependency_versions_from_distributions,
)

dagster_dist_name = "dagster-1.0.14-py3-none-any.whl"
cloud_dist_name = "dagster_cloud-1.1.7-py3-none-any.whl"
plus_dist_name = "dagster_plus-1.7.2-py3-none-any.whl"


def test_check_dagster_cloud_dependency_versions():
    distribution_names = [dagster_dist_name, cloud_dist_name]
    assert get_and_check_dependency_versions_from_distributions(distribution_names) == {
        "dagster": "1.0.14",
        "dagster_cloud": "1.1.7",
    }


def test_check_dagster_plus_dependency_versions():
    distribution_names = [dagster_dist_name, plus_dist_name]
    assert get_and_check_dependency_versions_from_distributions(distribution_names) == {
        "dagster": "1.0.14",
        "dagster_plus": "1.7.2",
    }


def test_raise_error_on_missing_cloud_dep():
    distribution_names = [dagster_dist_name]
    with pytest.raises(ValueError, match="dagster_cloud or dagster_plus"):
        assert get_and_check_dependency_versions_from_distributions(distribution_names)
