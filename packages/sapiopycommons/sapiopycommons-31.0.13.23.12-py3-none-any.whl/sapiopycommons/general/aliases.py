from collections.abc import Iterable
from typing import Any

from sapiopylib.rest.pojo.DataRecord import DataRecord
from sapiopylib.rest.utils.recordmodel.PyRecordModel import PyRecordModel
from sapiopylib.rest.utils.recordmodel.RecordModelWrapper import WrappedRecordModel, WrappedType

# Different forms that a record model could take.
RecordModel = PyRecordModel | WrappedRecordModel | WrappedType
# A record could be provided as either a DataRecord, PyRecordModel, or WrappedRecordModel (WrappedType).
SapioRecord = DataRecord | RecordModel


# FR-46064 - Initial port of PyWebhookUtils to sapiopycommons.
class AliasUtil:
    @staticmethod
    def to_data_record(record: SapioRecord) -> DataRecord:
        """
        Convert a single DataRecord, PyRecordModel, or WrappedRecordModel to just a DataRecord
        :return: The DataRecord of the input SapioRecord.
        """
        return record if isinstance(record, DataRecord) else record.get_data_record()

    @staticmethod
    def to_data_records(records: Iterable[SapioRecord]) -> list[DataRecord]:
        """
        Convert a list of variables that could either be DataRecords, PyRecordModels,
        or WrappedRecordModels to just DataRecords.
        :return: A list of DataRecords for the input records.
        """
        return [(x if isinstance(x, DataRecord) else x.get_data_record()) for x in records]

    @staticmethod
    def to_record_ids(records: Iterable[int | SapioRecord]) -> list[int]:
        """
        Convert a list of variables that could either be integers, DataRecords, PyRecordModels,
        or WrappedRecordModels to just integers (taking the record ID from the records).
        :return: A list of record IDs for the input records.
        """
        return [(x if isinstance(x, int) else x.record_id) for x in records]

    @staticmethod
    def to_field_map_lists(records: Iterable[SapioRecord]) -> list[dict[str, Any]]:
        """
        Convert a list of variables that could either be DataRecords, PyRecordModels,
        or WrappedRecordModels to a list of their field maps.
        :return: A list of field maps for the input records.
        """
        field_map_list: list[dict[str, Any]] = []
        for record in records:
            if isinstance(record, DataRecord):
                field_map_list.append(record.get_fields())
            else:
                field_map_list.append(record.fields.copy_to_dict())
        return field_map_list
