from enum import Enum
from typing import Literal, Optional
from urllib.parse import urljoin

from bpkio_api.models.MediaFormat import MediaFormat
from pydantic import AnyHttpUrl, BaseModel, IPvAnyAddress

from .common import BaseResource, NamedModel, PropertyMixin, WithDescription

ADSERVER_SYSTEM_VALUES = [
    ("$MMVAR_CACHE_BUSTER", "Cachebuster value"),
    ("$MAP_REMOTE_ADDR", "Client IP address (from header 'X-Forwarded-For')"),
    (
        "$_MMVAR_LIVEAR_SIGNALID",
        "Signal ID (from the SCTE35 marker)",
    ),
    (
        "$_MMVAR_LIVEAR_UPID",
        "UPID (from the SCTE35 marker)",
    ),
    ("$_MMVAR_LIVEAR_SLOTDURATION", "Slot duration (in seconds)"),
    (
        "${_MMVAR_LIVEAR_SLOTDURATION}000",
        "Slot duration (in microseconds)",
    ),
]


class SourceType(Enum):
    AD_SERVER = "ad-server"
    ASSET = "asset"
    ASSET_CATALOG = "asset-catalog"
    LIVE = "live"
    SLATE = "slate"

    def __str__(self):
        return str(self.value)


# === SOURCES Models ===


class SourceIn(NamedModel, PropertyMixin):
    url: Optional[AnyHttpUrl | str] = None

    @property
    def full_url(self):
        return self.make_full_url()

    def make_full_url(self, *args, **kwargs):
        return self.url


class SourceSparse(SourceIn, BaseResource):
    type: SourceType
    format: Optional[MediaFormat] = None


# === ASSET SOURCE Models ===


class AssetSourceIn(SourceIn, WithDescription):
    backupIp: Optional[IPvAnyAddress] = None

    def is_live(self):
        return False


class AssetSource(AssetSourceIn, BaseResource):
    format: Optional[MediaFormat]
    type: Literal["asset"]

    # @property
    # def type(self):
    #     return SourceType.ASSET


# === LIVE SOURCE Models ===


class LiveSourceIn(SourceIn, WithDescription):
    backupIp: Optional[IPvAnyAddress] = None

    def is_live(self):
        return True


class LiveSource(LiveSourceIn, BaseResource):
    format: Optional[MediaFormat]

    @property
    def type(self):
        return SourceType.LIVE


# === ASSET CATALOG SOURCE Models ===


class AssetCatalogSourceIn(SourceIn, WithDescription):
    backupIp: Optional[IPvAnyAddress] = None
    # TODO - add type and/or validator for path
    assetSample: str

    @property
    def full_url(self):
        return self.make_full_url()

    def make_full_url(self, extra=None, *args, **kwargs):
        u = self.url
        if extra:
            u = urljoin(u, extra)
        else:
            u = urljoin(u, self.assetSample)
        return u

    def is_live(self):
        return False


class AssetCatalogSource(AssetCatalogSourceIn, BaseResource):
    @property
    def type(self):
        return SourceType.ASSET_CATALOG


# === AD SERVER SOURCE Models ===


class AdServerSourceIn(SourceIn, WithDescription):
    # TODO - add type and/or validator for queries
    queries: Optional[str]
    template: Optional[str]

    @property
    def full_url(self):
        return self.make_full_url()

    def make_full_url(self, *args, **kwargs):
        u = self.url
        if self.queries:
            u = u + "?" + self.queries
        return u

    def is_live(self):
        return False


class AdServerSource(AdServerSourceIn, BaseResource):
    @property
    def type(self):
        return SourceType.AD_SERVER


# === SLATE SOURCE Models ===


class SlateSourceIn(SourceIn, WithDescription):
    def is_live(self):
        return False


class SlateSource(SlateSourceIn, BaseResource):
    format: Optional[MediaFormat]
    type: Literal["slate"]

    # @property
    # def type(self):
    #     return SourceType.SLATE


# === CHECK RESULTS Model ===


class SeverityLevel(Enum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"

    def __str__(self):
        return str(self.value)


class SourceCheckResult(BaseModel):
    messageText: str
    severityLevel: SeverityLevel
