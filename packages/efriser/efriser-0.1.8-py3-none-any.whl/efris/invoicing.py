import json
from services import process_response, encode
from utils import *
from output_cleaner import *

class EFRISInvoicing:
    def __init__(self, ip, device_number, tin, seller_name):
        """
        Initialize the EFRISInvoicing class.

        Args:
            ip (str): The IP address of the EFRIS Enabler server.
            device_number (str): The device number.
            tin (str): The Tax Identification Number.
            seller_name (str): The name of the seller.
        """
        self.ip = f'http://{ip}/efristcs/ws/tcsapp/getInformation'
        self.device_number = device_number
        self.tin = tin
        self.seller_name = seller_name

    def efris_post(self, ic, message):
        """
        Perform a POST request to the EFRIS server.

        Args:
            ic (str): The IC code.
            message (dict): The message payload.

        Returns:
            dict: The response from the EFRIS server.
        """
        transformed_data = encode(str(json.dumps(message))).decode()
        data_section = construct_data_section(transformed_data)
        global_info_section = construct_global_info_section(self.device_number, self.tin, ic)
        return_state_info_section = construct_return_state_info_section()

        payload = {
            "data": data_section,
            "globalInfo": global_info_section,
            "returnStateInfo": return_state_info_section
        }
        return process_response(self.ip, payload)
    

    def query_tax_payer_by_tin(self, tin):
        """
        Query the tax payer by TIN.

        Args:
            TIN (str): The Tax Identification Number.

        Returns:
            dict: The formatted tax payer output.
        """
        ic = 'T119'
        message = {"tin": tin, "ninBrn": ""}
        return format_taxpayer_output(self.efris_post(ic, message))
    
    def query_document(self, fdn, type):
        """
        Query a document by FDN and type.

        Args:
            fdn (str): The FDN (Fiscal Document Number) of the document.
            type (int): The type of the document (1 for Invoice, 2 for Receipt).

        Returns:
            dict: The formatted invoice query output.
        """
        ic = 'T106'
        message = query_invoice_json(fdn, str(type))
        return format_invoice_query_output(self.efris_post(ic, message))

    def query_invoice_details(self, fdn):
        """
        Query the details of an invoice.

        Args:
            fdn (str): The FDN (Fiscal Document Number) of the invoice.

        Returns:
            dict: The cleaned invoice data.
        """
        ic = 'T108'
        message = invoice_details_json(fdn)
        return clean_invoice_data_json(self.efris_post(ic, message))
    
    def system_dictionary(self):
        """
        Query the system dictionary.

        Returns:
            dict: The response from the EFRIS server.
        """
        ic = 'T115'
        message = []
        return self.efris_post(ic, message)


    def credit_notes_query(self):
        """
        Query credit notes.

        Returns:
            dict: The processed credit note output.
        """
        ic = 'T111'
        message = credit_note_json()
        return process_creditnote_output(self.efris_post(ic, message))
    
    def credit_note_details(self, id):
        """
        Query the details of a credit note.

        Args:
            id (str): The ID of the credit note.

        Returns:
            dict: The response from the EFRIS server.
        """
        ic = 'T112'
        message = {'id': id}
        return self.efris_post(ic, message)

    def approve_credit_note(self, reference_no, status, id, remarks):
        """
        Approve a credit note.

        Args:
            reference_no (str): The reference number of the credit note.
            status (int): The status of the credit note.
            id (str): The ID of the credit note.
            remarks (str): The remarks for the credit note.

        Returns:
            dict: The response from the EFRIS server.
        
        Raises:
            ValueError: If the status parameter is invalid.
        """
        ic = 'T113'
        # Input validation for kind
        valid_status = {101: 'Approved', 103: 'Rejected'}
        if status not in valid_status:
            raise ValueError(f"The 'status' parameter must be one of the following: {', '.join(f'{k}: {v}' for k, v in valid_status.items())}")

        message = approve_credit_note(reference_no, status, id, remarks)
        return self.efris_post(ic, message)

    def cancel_credit_note(self, inv_fdn, cn_fdn, reason):
        """
        Cancel a credit note.

        Args:
            inv_fdn (str): The FDN of the original invoice.
            cn_fdn (str): The FDN of the credit note.
            reason (str): The reason for canceling the credit note.

        Returns:
            dict: The response from the EFRIS server.
        """
        ic = 'T112'
        message = cancel_credit_note(inv_fdn, cn_fdn, reason)
        return self.efris_post(ic, message)
    
    # not implemented
    def z_report(self):
        """
        Generate a Z report.

        Returns:
            dict: The response from the EFRIS server.
        """
        ic = 'T116' 
        message = {}
        return self.efris_post(ic, message)
    
    def cancel_credit_note_application(self, business_key, refrence_no):
        """
        Cancel a credit note application.

        Args:
            business_key (str): The business key.
            refrence_no (str): The reference number.

        Returns:
            dict: The response from the EFRIS server.
        """
        ic = 'T120' 
        message = {"businessKey": business_key, "referenceNo": refrence_no}
        # response will be null if true
        return self.efris_post(ic, message)
    
    def acquiring_exchange_rate(self, currency):
        """
        Acquire the exchange rate for a currency.

        Args:
            currency (str): The currency code.

        Returns:
            dict: The cleaned currency output.
        """
        ic = 'T121'
        message = {"currency": currency, "issueDate":str(dt_string)}
        return currency_output_cleaner(self.efris_post(ic, message))

    def query_tax_payer_by_tin(self, tin):
        """
        Query the tax payer by TIN.

        Args:
            tin (str): The Tax Identification Number.

        Returns:
            dict: The formatted tax payer output.
        """
        ic = 'T119'
        message = {"tin": tin, "ninBrn": ""}
        return format_taxpayer_output(self.efris_post(ic, message))

    def upload_products(self, invoice_data):
        """
        Create EFRIS invoices using the provided invoice data.
        
        Args:
            invoice_data (list): A list of dictionaries, where each dictionary
            represents an invoice with the following keys:
                - "havePieceUnit"
                - "goodsName"
                - "goodsCode"
                - "measureUnit"
                - "unitPrice"
                - "currency"
                - "commodityCategoryId"
                - "haveExciseTax"
                - "description"
                - "stockPrewarning"
        
        Returns:
            dict: The response from the EFRIS server.
        """
        for invoice in invoice_data:
            # Validate and process each invoice
            
            # Check if all required keys are present
            required_keys = ["havePieceUnit", "goodsName", "goodsCode", "measureUnit",
                            "unitPrice", "currency", "commodityCategoryId", "haveExciseTax",
                            "description", "stockPrewarning"]
            if not all(key in invoice for key in required_keys):
                print(f"Invalid invoice data: {invoice}")
            continue

        ic = 'T130'
        x = self.efris_post(ic, invoice_data)
        print(x)
        return self.efris_post(ic, invoice_data)
    


    def upload_invoice(self, invoice_data, goods_data, tax_data, payment_data):
        """
        Upload an invoice to the EFRIS server.

        Args:
            invoice_data (dict): The invoice data.
            goods_data (dict): The goods data.
            tax_data (dict): The tax data.
            payment_data (dict): The payment data.

        Returns:
            dict: The response from the EFRIS server.
        
        Raises:
            ValueError: If the type, kind, buyer_type, or industry parameter is invalid.
        """
        ic = 'T109'

        reference_no = invoice_data.get('reference_no')
        operator = invoice_data.get('operator')
        currency = invoice_data.get('currency')
        type = invoice_data.get('type')
        kind = invoice_data.get('kind')
        industry = invoice_data.get('industry')
        tin = invoice_data.get('tin')
        buyer_type = invoice_data.get('buyer_type')

        valid_types = {1: 'Invoice/Receipt', 4: 'Debit Note', 5: 'Credit Memo/rebate'}
        if type not in valid_types:
            raise ValueError(f"The 'type' parameter must be one of the following: {', '.join(f'{k}: {v}' for k, v in valid_types.items())}")
        
        # Input validation for kind
        valid_kinds = {1: 'Invoice', 2: 'Receipt'}
        if kind not in valid_kinds:
            raise ValueError(f"The 'kind' parameter must be one of the following: {', '.join(f'{k}: {v}' for k, v in valid_kinds.items())}")

        # Input validation for buyer_type
        valid_buyer_types = {
            0: 'B2B',
            1: 'B2C',
            2: 'Foreigner',
            3: 'B2G'
        }
        if buyer_type not in valid_buyer_types:
            raise ValueError(f"The 'buyer_type' parameter must be one of the following: {', '.join(f'{k}: {v}' for k, v in valid_buyer_types.items())}")

        # Input validation for kind
        valid_industry = {
            101: 'General Industry',
            102: 'Export',
            104: 'Imported Service',
            105: 'Telecom',
            106: 'Stamp Duty',
            107: 'Hotel Service',
            108: 'Other taxes',
            109: 'Airline Business',
            110: 'EDC'
        }
        if industry not in valid_industry:
            raise ValueError(f"The 'kind' parameter must be one of the following: {', '.join(f'{k}: {v}' for k, v in valid_industry.items())}")

        payload = {
            "sellerDetails":sellers_details(self.tin, self.seller_name, reference_no),
            "basicInformation": basic_info(operator,str(currency), str(type), str(kind)),
            "buyerDetails": buyer_details(str(tin), str(buyer_type)),
            "buyerExtend": buyer_extend(),
            "goodsDetails": goods_data,
            "taxDetails": tax_data,
            "summary": summary_details(),
            "payWay": payment_data,
            "extend":extend_details(),
            "importSericesSeller":import_services_seller(),
            "airlineGoodsDetails": airline_goods_details(),
        }
    
        message = "000f"

        return self.efris_post(ic, message)


invoicing = EFRISInvoicing('198.74.52.28:9880', 'TCS1613912751699535','1000032574', 'WideSpectrum')
tax_payer = invoicing.query_invoice_details('323128406449')
tax_payer = invoicing.acquiring_exchange_rate("USD")


print('**********************************')
print(tax_payer)

invoice_data = [
    {
        "havePieceUnit": "101",
        "goodsName": "Product A",
        "goodsCode": "ABC123",
        "measureUnit": "U22",
        "unitPrice": "10.00",
        "currency": "UGX",
        "commodityCategoryId": "14111511",
        "haveExciseTax": "102",
        "description": "This is Product A",
        "stockPrewarning": "50"
    }
]

#tax_payer = invoicing.upload_products(invoice_data)
