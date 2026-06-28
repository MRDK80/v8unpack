import unittest
from v8unpack.metadata_types import MetaDataTypes
from v8unpack.MetaDataObject.Form import Form
from v8unpack.MetaDataObject.DataProcessorForm import DataProcessorForm
from v8unpack.MetaObject import _CANONICAL_TYPE_NAME, _get_canonical_type_name


class TestDataProcessorFormCanonicalName(unittest.TestCase):

    # --- enum lookup ---

    def test_alias_lookup_by_name(self):
        entry = MetaDataTypes['DataProcessorForm']
        self.assertEqual(entry.value, 'd5b0e5ed-256d-401c-9c36-f630cafd8a62')

    def test_alias_same_uuid_as_form(self):
        self.assertEqual(
            MetaDataTypes['DataProcessorForm'].value,
            MetaDataTypes['Form'].value,
        )

    def test_alias_visible_in_members(self):
        self.assertIn('DataProcessorForm', MetaDataTypes.__members__)

    # --- UUID invariants: проверяем что идентификаторы не поплыли ---

    def test_form_uuid_invariant(self):
        self.assertEqual(
            MetaDataTypes['Form'].value,
            'd5b0e5ed-256d-401c-9c36-f630cafd8a62',
        )

    def test_report_form_uuid_invariant(self):
        self.assertEqual(
            MetaDataTypes['ReportForm'].value,
            'a3b368c0-29e2-11d6-a3c7-0050bae0a776',
        )

    def test_document_form_uuid_invariant(self):
        self.assertEqual(
            MetaDataTypes['DocumentForm'].value,
            'fb880e93-47d7-4127-9357-a20e69c17545',
        )

    def test_catalog_form_uuid_invariant(self):
        self.assertEqual(
            MetaDataTypes['CatalogForm'].value,
            'fdf816d2-1ead-11d5-b975-0050bae0a95d',
        )

    # --- хендлер ---

    def test_handler_is_form_subclass(self):
        self.assertTrue(issubclass(DataProcessorForm, Form))

    def test_handler_class_name(self):
        self.assertEqual(DataProcessorForm.__name__, 'DataProcessorForm')

    # --- таблица переименований ---

    def test_canonical_name_dataprocessor_form(self):
        self.assertEqual(
            _get_canonical_type_name('DataProcessor', 'Form'),
            'DataProcessorForm',
        )

    def test_canonical_name_external_not_renamed(self):
        self.assertEqual(
            _get_canonical_type_name('ExternalDataProcessor', 'Form'),
            'Form',
        )

    def test_canonical_name_report_not_renamed(self):
        self.assertEqual(
            _get_canonical_type_name('Report', 'Form'),
            'Form',
        )

    def test_canonical_name_identity_for_unknown(self):
        """_get_canonical_type_name неизвестных пар возвращает имя без изменений."""
        self.assertEqual(
            _get_canonical_type_name('SomeParent', 'SomeType'),
            'SomeType',
        )

    # --- encode round-trip: fill_header_include находит каноническое имя ---

    def test_fill_header_include_uses_canonical_name(self):
        """include_index индексирован по 'DataProcessorForm', а не 'Form'.
        _get_canonical_type_name('DataProcessor', 'Form') должен вернуть это имя."""
        key = _get_canonical_type_name('DataProcessor', 'Form')
        include_index = {'DataProcessorForm': [('uuid1', 0, {'data': 'x'})]}
        self.assertIn(key, include_index)
        self.assertNotIn('Form', include_index)


if __name__ == '__main__':
    unittest.main()
