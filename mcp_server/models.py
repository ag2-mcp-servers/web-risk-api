# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T03:08:12+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, RootModel


class ResponseType(Enum):
    RESPONSE_TYPE_UNSPECIFIED = 'RESPONSE_TYPE_UNSPECIFIED'
    DIFF = 'DIFF'
    RESET = 'RESET'


class GoogleCloudWebriskV1ComputeThreatListDiffResponseChecksum(BaseModel):
    sha256: Optional[str] = Field(
        None,
        description='The SHA256 hash of the client state; that is, of the sorted list of all hashes present in the database.',
    )


class GoogleCloudWebriskV1RawHashes(BaseModel):
    prefixSize: Optional[int] = Field(
        None,
        description='The number of bytes for each prefix encoded below. This field can be anywhere from 4 (shortest prefix) to 32 (full SHA256 hash). In practice this is almost always 4, except in exceptional circumstances.',
    )
    rawHashes: Optional[str] = Field(
        None,
        description='The hashes, in binary format, concatenated into one long string. Hashes are sorted in lexicographic order. For JSON API users, hashes are base64-encoded.',
    )


class GoogleCloudWebriskV1RawIndices(BaseModel):
    indices: Optional[List[int]] = Field(
        None,
        description='The indices to remove from a lexicographically-sorted local list.',
    )


class GoogleCloudWebriskV1RiceDeltaEncoding(BaseModel):
    encodedData: Optional[str] = Field(
        None,
        description='The encoded deltas that are encoded using the Golomb-Rice coder.',
    )
    entryCount: Optional[int] = Field(
        None,
        description='The number of entries that are delta encoded in the encoded data. If only a single integer was encoded, this will be zero and the single value will be stored in `first_value`.',
    )
    firstValue: Optional[str] = Field(
        None,
        description="The offset of the first entry in the encoded data, or, if only a single integer was encoded, that single integer's value. If the field is empty or missing, assume zero.",
    )
    riceParameter: Optional[int] = Field(
        None,
        description='The Golomb-Rice parameter, which is a number between 2 and 28. This field is missing (that is, zero) if `num_entries` is zero.',
    )


class ThreatType(Enum):
    THREAT_TYPE_UNSPECIFIED = 'THREAT_TYPE_UNSPECIFIED'
    MALWARE = 'MALWARE'
    SOCIAL_ENGINEERING = 'SOCIAL_ENGINEERING'
    UNWANTED_SOFTWARE = 'UNWANTED_SOFTWARE'
    SOCIAL_ENGINEERING_EXTENDED_COVERAGE = 'SOCIAL_ENGINEERING_EXTENDED_COVERAGE'


class GoogleCloudWebriskV1SearchHashesResponseThreatHash(BaseModel):
    expireTime: Optional[str] = Field(
        None,
        description='The cache lifetime for the returned match. Clients must not cache this response past this timestamp to avoid false positives.',
    )
    hash: Optional[str] = Field(
        None,
        description='A 32 byte SHA256 hash. This field is in binary format. For JSON requests, hashes are base64-encoded.',
    )
    threatTypes: Optional[List[ThreatType]] = Field(
        None,
        description='The ThreatList this threat belongs to. This must contain at least one entry.',
    )


class GoogleCloudWebriskV1SearchUrisResponseThreatUri(BaseModel):
    expireTime: Optional[str] = Field(
        None,
        description='The cache lifetime for the returned match. Clients must not cache this response past this timestamp to avoid false positives.',
    )
    threatTypes: Optional[List[ThreatType]] = Field(
        None, description='The ThreatList this threat belongs to.'
    )


class GoogleCloudWebriskV1Submission(BaseModel):
    uri: Optional[str] = Field(
        None,
        description='Required. The URI that is being reported for malicious content to be analyzed.',
    )


class GoogleCloudWebriskV1ThreatEntryAdditions(BaseModel):
    rawHashes: Optional[List[GoogleCloudWebriskV1RawHashes]] = Field(
        None,
        description='The raw SHA256-formatted entries. Repeated to allow returning sets of hashes with different prefix sizes.',
    )
    riceHashes: Optional[GoogleCloudWebriskV1RiceDeltaEncoding] = Field(
        None,
        description='The encoded 4-byte prefixes of SHA256-formatted entries, using a Golomb-Rice encoding. The hashes are converted to uint32, sorted in ascending order, then delta encoded and stored as encoded_data.',
    )


class GoogleCloudWebriskV1ThreatEntryRemovals(BaseModel):
    rawIndices: Optional[GoogleCloudWebriskV1RawIndices] = Field(
        None, description='The raw removal indices for a local list.'
    )
    riceIndices: Optional[GoogleCloudWebriskV1RiceDeltaEncoding] = Field(
        None,
        description='The encoded local, lexicographically-sorted list indices, using a Golomb-Rice encoding. Used for sending compressed removal indices. The removal indices (uint32) are sorted in ascending order, then delta encoded and stored as encoded_data.',
    )


class GoogleLongrunningCancelOperationRequest(BaseModel):
    pass


class GoogleProtobufEmpty(BaseModel):
    pass


class GoogleRpcStatus(BaseModel):
    code: Optional[int] = Field(
        None,
        description='The status code, which should be an enum value of google.rpc.Code.',
    )
    details: Optional[List[Dict[str, Any]]] = Field(
        None,
        description='A list of messages that carry the error details. There is a common set of message types for APIs to use.',
    )
    message: Optional[str] = Field(
        None,
        description='A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the google.rpc.Status.details field, or localized by the client.',
    )


class FieldXgafv(Enum):
    field_1 = '1'
    field_2 = '2'


class Alt(Enum):
    json = 'json'
    media = 'media'
    proto = 'proto'


class ThreatTypes(RootModel[List[ThreatType]]):
    root: List[ThreatType]


class ConstraintsSupportedCompression(Enum):
    COMPRESSION_TYPE_UNSPECIFIED = 'COMPRESSION_TYPE_UNSPECIFIED'
    RAW = 'RAW'
    RICE = 'RICE'


class ConstraintsSupportedCompressions(
    RootModel[List[ConstraintsSupportedCompression]]
):
    root: List[ConstraintsSupportedCompression]


class ThreatTypes1(RootModel[List[ThreatType]]):
    root: List[ThreatType]


class GoogleCloudWebriskV1ComputeThreatListDiffResponse(BaseModel):
    additions: Optional[GoogleCloudWebriskV1ThreatEntryAdditions] = Field(
        None, description="A set of entries to add to a local threat type's list."
    )
    checksum: Optional[GoogleCloudWebriskV1ComputeThreatListDiffResponseChecksum] = (
        Field(
            None,
            description="The expected SHA256 hash of the client state; that is, of the sorted list of all hashes present in the database after applying the provided diff. If the client state doesn't match the expected state, the client must discard this diff and retry later.",
        )
    )
    newVersionToken: Optional[str] = Field(
        None,
        description="The new opaque client version token. This should be retained by the client and passed into the next call of ComputeThreatListDiff as 'version_token'. A separate version token should be stored and used for each threatList.",
    )
    recommendedNextDiff: Optional[str] = Field(
        None,
        description='The soonest the client should wait before issuing any diff request. Querying sooner is unlikely to produce a meaningful diff. Waiting longer is acceptable considering the use case. If this field is not set clients may update as soon as they want.',
    )
    removals: Optional[GoogleCloudWebriskV1ThreatEntryRemovals] = Field(
        None,
        description="A set of entries to remove from a local threat type's list. This field may be empty.",
    )
    responseType: Optional[ResponseType] = Field(
        None,
        description='The type of response. This may indicate that an action must be taken by the client when the response is received.',
    )


class GoogleCloudWebriskV1SearchHashesResponse(BaseModel):
    negativeExpireTime: Optional[str] = Field(
        None,
        description='For requested entities that did not match the threat list, how long to cache the response until.',
    )
    threats: Optional[List[GoogleCloudWebriskV1SearchHashesResponseThreatHash]] = Field(
        None,
        description='The full hashes that matched the requested prefixes. The hash will be populated in the key.',
    )


class GoogleCloudWebriskV1SearchUrisResponse(BaseModel):
    threat: Optional[GoogleCloudWebriskV1SearchUrisResponseThreatUri] = Field(
        None,
        description='The threat list matches. This might be empty if the URI is on no list.',
    )


class GoogleLongrunningOperation(BaseModel):
    done: Optional[bool] = Field(
        None,
        description='If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available.',
    )
    error: Optional[GoogleRpcStatus] = Field(
        None,
        description='The error result of the operation in case of failure or cancellation.',
    )
    metadata: Optional[Dict[str, Any]] = Field(
        None, description='Contains a `SubmitUriMetadata` object.'
    )
    name: Optional[str] = Field(
        None,
        description='Matches the `/v1/{project-name}/operations/{operation-id}` pattern.',
    )
    response: Optional[Dict[str, Any]] = Field(
        None,
        description='The normal response of the operation in case of success. If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`. If the original method is standard `Get`/`Create`/`Update`, the response should be the resource. For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name. For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.',
    )


class GoogleLongrunningListOperationsResponse(BaseModel):
    nextPageToken: Optional[str] = Field(
        None, description='The standard List next-page token.'
    )
    operations: Optional[List[GoogleLongrunningOperation]] = Field(
        None,
        description='A list of operations that matches the specified filter in the request.',
    )
