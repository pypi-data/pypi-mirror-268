import json
from utils import *
from services import process_response, encode
from output_cleaner import *

class Efriser:
    def __init__(self, ip, device_number, tin, seller_name):
        self.ip = f'http://{ip}/efristcs/ws/tcsapp/getInformation'
        self.device_number = device_number
        self.tin = tin
        self.seller_name = seller_name

    def efris_post(self, ic, message):
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
        ic = 'T119'
        message = {"tin": tin, "ninBrn": ""}
        
        return format_taxpayer_output(self.efris_post(ic, message))
    
    def query_document(self, fdn, type):
        # type 1 for Invoice and 2 for Receipt
        ic = 'T106'
        message = query_invoice_json(fdn, str(type))
        return format_invoice_query_output(self.efris_post(ic, message))

    def query_invoice_details(self, fdn):
        ic = 'T108'
        message = invoice_details_json(fdn)
        return clean_invoice_data_json(self.efris_post(ic, message))
    
    def system_dictionary(self):
        ic = 'T115'
        message = []
        return self.efris_post(ic, message)


    def credit_notes_query(self):
        ic = 'T111'
        message = credit_note_json()
        return process_creditnote_output(self.efris_post(ic, message))
    
    def credit_note_details(self, id):
        ic = 'T112'
        message = {'id': id}
        return self.efris_post(ic, message)

    def approve_credit_note(self, reference_no, status, id, remarks):
        ic = 'T113'
        # Input validation for kind
        valid_status = {101: 'Approved', 103: 'Rejected'}
        if status not in valid_status:
            raise ValueError(f"The 'status' parameter must be one of the following: {', '.join(f'{k}: {v}' for k, v in valid_status.items())}")

        message = approve_credit_note(reference_no, status, id, remarks)
        return self.efris_post(ic, message)

    def cancel_credit_note(self, inv_fdn, cn_fdn, reason):
        # fdn of the original invoice
        ic = 'T112'
        message = cancel_credit_note(inv_fdn, cn_fdn, reason)
        return self.efris_post(ic, message)
    
    # not implemented
    def z_report(self):
        # fdn of the original invoice
        ic = 'T116' 
        message = {}
        return self.efris_post(ic, message)
    
    def cancel_credit_note_application(self, business_key, refrence_no):
        ic = 'T120' 
        message = {"businessKey": business_key, "referenceNo": refrence_no}
        # response will be null if true
        return self.efris_post(ic, message)
    
    def acquiring_exchange_rate(self, currency):
        ic = 'T121'
        message = {"currency": currency, "issueDate":str(dt_string)}
        return currency_output_cleaner(self.efris_post(ic, message))
    
    def upload_invoice(self, invoice_data, goods_data, tax_data, payment_data):
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


invoicing = Efriser('198.74.52.28:9880', 'TCS1613912751699535','1000032574', 'WideSpectrum')
tax_payer = invoicing.query_invoice_details('323128406449')
#tax_payer = invoicing.acquiring_exchange_rate("USD")


print('**********************************')
print(tax_payer)