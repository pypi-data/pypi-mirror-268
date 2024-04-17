import pathlib
import shutil
from unittest import mock

import ckan.tests.factories as factories
import ckanext.dc_log_view.plugin as plugin  # noqa: F401
import ckanext.dcor_schemas.plugin

import dclab
from dcor_shared.testing import (
    make_dataset, synchronous_enqueue_job)

import pytest

data_path = pathlib.Path(__file__).parent / "data"


def test_plugin_info():
    p = plugin.DCLogViewPlugin()
    info = p.info()
    assert info["name"] == "dc_log_view"


@pytest.mark.ckan_config('ckan.plugins', 'dcor_depot dcor_schemas')
@pytest.mark.usefixtures('clean_db', 'with_request_context')
@mock.patch('ckan.plugins.toolkit.enqueue_job',
            side_effect=synchronous_enqueue_job)
def test_plugin_can_view(enqueue_job_mock, create_with_upload, monkeypatch):
    # prerequisites
    monkeypatch.setattr(
        ckanext.dcor_schemas.plugin,
        'DISABLE_AFTER_DATASET_CREATE_FOR_CONCURRENT_JOB_TESTS',
        True)
    user = factories.User()
    owner_org = factories.Organization(users=[{
        'name': user['id'],
        'capacity': 'admin'
    }])
    create_context = {'ignore_auth': False,
                      'user': user['name'],
                      'api_version': 3}
    # create dataset with .rtdc file
    ds_dict, res_dict_dc = make_dataset(
        create_context, owner_org,
        create_with_upload=create_with_upload,
        resource_path=data_path / "calibration_beads_47.rtdc",
        activate=False)
    # Add a text file
    res_dict_text = create_with_upload(
        b"just some text", 'test.txt',
        url="upload",
        package_id=ds_dict["id"],
        context=create_context,
    )

    # test can_view for .rtdc data
    p = plugin.DCLogViewPlugin()
    assert p.can_view({"resource": res_dict_dc})
    assert not p.can_view({"resource": res_dict_text})


@pytest.mark.ckan_config('ckan.plugins', 'dcor_depot dcor_schemas')
@pytest.mark.usefixtures('clean_db', 'with_request_context')
@mock.patch('ckan.plugins.toolkit.enqueue_job',
            side_effect=synchronous_enqueue_job)
def test_plugin_setup_template_variables(
        enqueue_job_mock, create_with_upload, monkeypatch, tmp_path):
    path_in = tmp_path / "test.rtdc"
    shutil.copy2(data_path / "calibration_beads_47.rtdc", path_in)

    with dclab.RTDCWriter(path_in, mode="append") as hw:
        hw.store_log("peter", ["pferde im gurkensalat",
                               "haben keinen hunger"])

    # sanity check
    with dclab.new_dataset(path_in) as ds:
        assert ds.logs["peter"][0] == "pferde im gurkensalat"

    # prerequisites
    monkeypatch.setattr(
        ckanext.dcor_schemas.plugin,
        'DISABLE_AFTER_DATASET_CREATE_FOR_CONCURRENT_JOB_TESTS',
        True)
    user = factories.User()
    owner_org = factories.Organization(users=[{
        'name': user['id'],
        'capacity': 'admin'
    }])
    create_context = {'ignore_auth': False,
                      'user': user['name'],
                      'api_version': 3}
    # create dataset with .rtdc file
    ds_dict, res_dict = make_dataset(
        create_context, owner_org,
        create_with_upload=create_with_upload,
        resource_path=path_in,
        activate=True)

    # test setup_template_variables for .rtdc data
    p = plugin.DCLogViewPlugin()
    data = p.setup_template_variables(
        context=create_context,
        data_dict={"resource": res_dict})
    logs = data["logs"]
    assert len(logs) == 1
    assert logs["peter"][0] == "pferde im gurkensalat"
