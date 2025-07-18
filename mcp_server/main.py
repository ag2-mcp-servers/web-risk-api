# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T03:08:12+00:00



import argparse
import json
import os
from typing import *
from typing import Optional

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import BaseSecurity, UnsuportedSecurityStub
from fastapi import Query

from models import (
    Alt,
    ConstraintsSupportedCompressions,
    FieldXgafv,
    GoogleCloudWebriskV1ComputeThreatListDiffResponse,
    GoogleCloudWebriskV1SearchHashesResponse,
    GoogleCloudWebriskV1SearchUrisResponse,
    GoogleCloudWebriskV1Submission,
    GoogleLongrunningCancelOperationRequest,
    GoogleLongrunningListOperationsResponse,
    GoogleLongrunningOperation,
    GoogleProtobufEmpty,
    ThreatType,
    ThreatTypes,
    ThreatTypes1,
)

app = MCPProxy(
    contact={'name': 'Google', 'url': 'https://google.com', 'x-twitter': 'youtube'},
    description='',
    license={
        'name': 'Creative Commons Attribution 3.0',
        'url': 'http://creativecommons.org/licenses/by/3.0/',
    },
    termsOfService='https://developers.google.com/terms/',
    title='Web Risk API',
    version='v1',
    servers=[{'url': 'https://webrisk.googleapis.com/'}],
)


@app.get(
    '/v1/hashes:search',
    description=""" Gets the full hashes that match the requested hash prefix. This is used after a hash prefix is looked up in a threatList and there is a match. The client side threatList only holds partial hashes so the client must query this method to determine if there is a full hash match of a threat. """,
    tags=['webrisk_threat_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def webrisk_hashes_search(
    hash_prefix: Optional[str] = Query(None, alias='hashPrefix'),
    threat_types: Optional[ThreatTypes] = Query(None, alias='threatTypes'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/threatLists:computeDiff',
    description=""" Gets the most recent threat list diffs. These diffs should be applied to a local database of hashes to keep it up-to-date. If the local database is empty or excessively out-of-date, a complete snapshot of the database will be returned. This Method only updates a single ThreatList at a time. To update multiple ThreatList databases, this method needs to be called once for each list. """,
    tags=['webrisk_threat_management', 'webrisk_project_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def webrisk_threat_lists_compute_diff(
    constraints_max_database_entries: Optional[int] = Query(
        None, alias='constraints.maxDatabaseEntries'
    ),
    constraints_max_diff_entries: Optional[int] = Query(
        None, alias='constraints.maxDiffEntries'
    ),
    constraints_supported_compressions: Optional[
        ConstraintsSupportedCompressions
    ] = Query(None, alias='constraints.supportedCompressions'),
    threat_type: Optional[ThreatType] = Query(None, alias='threatType'),
    version_token: Optional[str] = Query(None, alias='versionToken'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/uris:search',
    description=""" This method is used to check whether a URI is on a given threatList. Multiple threatLists may be searched in a single query. The response will list all requested threatLists the URI was found to match. If the URI is not found on any of the requested ThreatList an empty response will be returned. """,
    tags=['webrisk_threat_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def webrisk_uris_search(
    threat_types: Optional[ThreatTypes1] = Query(None, alias='threatTypes'),
    uri: Optional[str] = None,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/v1/{name}',
    description=""" Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. """,
    tags=['webrisk_project_management'],
)
def webrisk_projects_operations_delete(
    name: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/{name}',
    description=""" Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. """,
    tags=['webrisk_project_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def webrisk_projects_operations_get(
    name: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/{name}/operations',
    description=""" Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. """,
    tags=['webrisk_threat_management', 'webrisk_project_management'],
)
def webrisk_projects_operations_list(
    name: str,
    filter: Optional[str] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    page_token: Optional[str] = Query(None, alias='pageToken'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/{name}:cancel',
    description=""" Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`. """,
    tags=['webrisk_project_management'],
)
def webrisk_projects_operations_cancel(
    name: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: GoogleLongrunningCancelOperationRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/{parent}/submissions',
    description=""" Creates a Submission of a URI suspected of containing phishing content to be reviewed. If the result verifies the existence of malicious phishing content, the site will be added to the [Google's Social Engineering lists](https://support.google.com/webmasters/answer/6350487/) in order to protect users that could get exposed to this threat in the future. Only allowlisted projects can use this method during Early Access. Please reach out to Sales or your customer engineer to obtain access. """,
    tags=['webrisk_project_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def webrisk_projects_submissions_create(
    parent: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: GoogleCloudWebriskV1Submission = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
