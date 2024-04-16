import unittest
from unittest.mock import MagicMock
from efris.utils import credit_note_json
from invoicing import InvoicingClass

class TestInvoicingClass(unittest.TestCase):
    def setUp(self):
        self.invoicing = InvoicingClass()

    def test_credit_notes_query(self):
        # Mock the efris_post method
        self.invoicing.efris_post = MagicMock(return_value={'status': 'success', 'data': 'credit_note_data'})

        # Call the credit_notes_query method
        result = self.invoicing.credit_notes_query()

        # Assert that the efris_post method was called with the correct arguments
        self.invoicing.efris_post.assert_called_once_with('T111', credit_note_json())

        # Assert that the result is as expected
        self.assertEqual(result, {'status': 'success', 'data': 'credit_note_data'})

if __name__ == '__main__':
    unittest.main()