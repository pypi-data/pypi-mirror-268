import datetime
from typing import Iterable, Any, List
from abc import abstractmethod

import django_filters
import xlwt

from .fields import FieldFileAbsoluteURL

META_REPORT_KEY = "use_for_report"
REPORT_FIELDS_KEY = "flex_report_search_fields"
REPORT_EXCULDE_KEY = "flex_report_search_exclude"
REPORT_COLUMNS_EXCULDE_KEY = "flex_report_columns_exclude"
REPORT_CUSTOM_FIELDS_KEY = "flex_report_custom_fields"

REPORT_CELL_STYLE_MAP = (
    (datetime.datetime, xlwt.easyxf(num_format_str="YYYY/MM/DD HH:MM")),
    (datetime.date, xlwt.easyxf(num_format_str="DD/MM/YYYY")),
    (datetime.time, xlwt.easyxf(num_format_str="HH:MM")),
    (bool, xlwt.easyxf(num_format_str="BOOLEAN")),
    (
        FieldFileAbsoluteURL,
        lambda v: xlwt.Formula(f'HYPERLINK("{v}","{v}")') if v else "",
    ),
)

FILTERSET_DATE_FILTERS = [
    django_filters.DateFilter,
    django_filters.TimeFilter,
    django_filters.DateTimeFilter,
]


class ReportModel:
    models = []

    @classmethod
    def register(cls, *models):
        cls.models.extend(models)
        return models[0]
    

class BaseQuerysetExporter:
    exporters = {}
    exporter_slug = None
    exporter_columns = []
    exporter_headers = {}
    exporter_kwargs = {}
    
    @classmethod
    def register(cls, exporter):
        assert issubclass(exporter, cls)
        cls.exporters.update({exporter.exporter_slug: exporter})
        return exporter
    
    @abstractmethod
    def export(self):
        raise NotImplementedError
    
    def __init__(self, export_qs=[], export_columns=[], export_headers={}, export_kwargs={}):
        self.export_qs = export_qs
        self.export_columns = export_columns
        self.export_headers = export_headers
        self.export_kwargs = export_kwargs


class DynamicSubField:
    slug = None
    verbose_name = None
    
    def __init__(self, verbose_name=None):
        if verbose_name:
            self.verbose_name = verbose_name
    
    def get_verbose_name(self):
        return self.verbose_name
    
    @abstractmethod
    def get_value(cls, *args, **kwargs):
        pass    
        

class BaseDynamicField:
    field_slug = None
    verbose_name = None
    model = None
    fields = {}
    
    @classmethod
    def get_by_slug(cls, slug):
        try:
            return cls.fields[slug]
        except KeyError as e:
            raise NotImplementedError(f"Field with slug {slug} not found") from e
    
    @classmethod
    def register(cls, field):
        assert issubclass(field, cls)
        cls.fields.update({field.field_slug: field})
        return field
    
    @abstractmethod
    def unpack_field(self, obj, *args, **kwargs) -> List[DynamicSubField]:
        pass
    

class BaseExportFormat:
    formats = {}
    queryset_exporter = None
    format_slug = None
    format_name = None
    format_ext = None
    
    @classmethod
    def check_auth(cls, request):
        return True
    
    @classmethod
    def construct_qs_exporter(cls, *args, **kwargs):
        qs_exporter = BaseQuerysetExporter.exporters[cls.queryset_exporter]
        return qs_exporter(*args, **kwargs)

    @classmethod
    def __str__(cls):
        return cls.format_name

    @classmethod
    @property
    @abstractmethod
    def format_slug(cls):
        raise NotImplementedError

    @classmethod
    @property
    @abstractmethod
    def format_name(cls):
        raise NotImplementedError

    @classmethod
    def register(cls, format_):
        assert issubclass(format_, BaseExportFormat)
        return cls.formats.update({format_.format_slug: format_})

    @classmethod
    def register_formats(cls, formats: dict):
        cls.formats.update(formats)

    @classmethod
    @abstractmethod
    def handle(cls, *args, **kwargs):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def handle_response(cls, *args, **kwargs):
        raise NotImplementedError


class FieldTypes:
    field = "field"
    property = "property"
    custom = "custom"
    dynamic = "dynamic"


class BaseDynamicColumn:
    columns = {}
