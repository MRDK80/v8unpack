import unittest
from v8unpack.metadata_types import MetaDataTypes
from v8unpack.MetaDataObject.Form import Form
from v8unpack.MetaDataObject.DataProcessorForm import DataProcessorForm
from v8unpack.MetaObject import _CANONICAL_TYPE_NAME


class TestDataProcessorFormCanonicalName(unittest.TestCase):

    def test_alias_lookup_by_name(self):
        """MetaDataTypes['DataProcessorForm'] не должен бросать KeyError."""
        entry = MetaDataTypes['DataProcessorForm']
        self.assertEqual(entry.value, 'd5b0e5ed-256d-401c-9c36-f630cafd8a62')

    def test_alias_same_uuid_as_form(self):
        """DataProcessorForm и Form указывают на один UUID."""
        self.assertEqual(
            MetaDataTypes['DataProcessorForm'].value,
            MetaDataTypes['Form'].value,
        )

    def test_handler_is_form_subclass(self):
        """DataProcessorForm должен быть подклассом Form."""
        self.assertTrue(issubclass(DataProcessorForm, Form))

    def test_handler_class_name(self):
        """__name__ хендлера должен совпадать с именем каталога."""
        self.assertEqual(DataProcessorForm.__name__, 'DataProcessorForm')

    def test_canonical_name_table_dataprocessor(self):
        """DataProcessor + Form -> DataProcessorForm в таблице."""
        self.assertEqual(
            _CANONICAL_TYPE_NAME.get(('DataProcessor', 'Form')),
            'DataProcessorForm',
        )

    def test_form_not_renamed_for_external(self):
        """ExternalDataProcessor + Form остаётся Form (не трогаем .epf)."""
        result = _CANONICAL_TYPE_NAME.get(('ExternalDataProcessor', 'Form'), 'Form')
        self.assertEqual(result, 'Form')

    def test_form_not_renamed_for_report(self):
        """Report + Form остаётся Form (у отчётов своё каноническое имя ReportForm)."""
        result = _CANONICAL_TYPE_NAME.get(('Report', 'Form'), 'Form')
        self.assertEqual(result, 'Form')


if __name__ == '__main__':
    unittest.main()
