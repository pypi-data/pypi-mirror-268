
import pytz
from datetime import datetime

now = datetime.now()
dt_string = datetime.now(pytz.timezone('Africa/Nairobi')).strftime("%Y-%m-%d %H:%M:%S")
date_string = datetime.now(pytz.timezone('Africa/Nairobi')).strftime("%Y-%m-%d")

def construct_data_section(message):
    data_section = {
        "content": message,
        "signature": "",
        "dataDescription": {
            "codeType": "0",
            "encryptCode": "1",
            "zipCode": "0"
        }
    }
    return data_section


def construct_global_info_section(device_number,tin, ic):
    global_info_section = {
        "appId": "AP04",
        "version": "1.1.20191201",
        "dataExchangeId": "9230489223014123",
        "interfaceCode": str(ic),
        "requestCode": "TP",
        "requestTime": str(dt_string),
        "responseCode": "TA",
        "userName": "admin",
        "deviceMAC": "FFFFFFFFFFFF",
        "deviceNo": str(device_number),
        "tin": str(tin),
        "brn": "",
        "taxpayerID": "1",
        "longitude": "116.397128",
        "latitude": "39.916527",
        "extendField": {
            "responseDateFormat": "dd/MM/yyyy",
            "responseTimeFormat": "dd/MM/yyyy HH:mm:ss"
        }
    }
    return global_info_section


def construct_return_state_info_section():
    return_state_info_section = {
        "returnCode": "",
        "returnMessage": ""
    }
    return return_state_info_section


def query_invoice_json(fdn, type):
    request_message = {
    "Request Message": "",  # Descriptive message
    "oriInvoiceNo": "",
    "invoiceNo": str(fdn),
    "deviceNo": "",
    "buyerTin": "",
    "buyerNinBrn": "",
    "buyerLegalName": "",
    "combineKeywords": "",
    "invoiceType": "",
    "invoiceKind": type,
    "isInvalid": "",
    "isRefund": "",
    "startDate": "",
    "endDate": "",
    "pageNo": "1",
    "pageSize": "98",
    "referenceNo": "",
    "branchName": "",
    "queryType": "",
    "dataSource": "",
    "sellerTinOrNin": "",
    "sellerLegalOrBusinessName": ""
    }
    return request_message

def invoice_details_json(fdn):
    request_message = {
    "invoiceNo": str(fdn),
    }
    return request_message


# invoice upload jsons
def sellers_details(tin, name, reference_no):
    data = {
        "tin": tin,
        "ninBrn": "",
        "legalName": name,
        "businessName": "",
        "address": "",
        "mobilePhone": "",
        "linePhone": "",
        "emailAddress": "",
        "placeOfBusiness": "",
        "referenceNo": reference_no,
        "branchId": "",
        "branchName": "Main",
        "isCheckReferenceNo": ""
    }
    return data

def basic_info(operator, currency, type, kind):
    data ={
        "invoiceNo": "",
        "antifakeCode": "",
        "deviceNo": "",
        "issuedDate": str(dt_string),
        "operator": operator,
        "currency": currency,
        "oriInvoiceId": "",
        "invoiceType": type,
        "invoiceKind": kind,
        "dataSource": "106",
        "invoiceIndustryCode": "",
        "isBatch": ""
    }
    return data


def buyer_details(tin, buyer_type):
    data = {
        "buyerTin": tin,
        "buyerNinBrn": "",
        "buyerPassportNum": "",
        "buyerLegalName": "",
        "buyerBusinessName": "",
        "buyerAddress": "",
        "buyerEmail": "",
        "buyerMobilePhone": "",
        "buyerLinePhone": "",
        "buyerPlaceOfBusi": "",
        "buyerType": buyer_type,
        "buyerCitizenship": "",
        "buyerSector": "",
        "buyerReferenceNo": "",
        "nonResidentFlag": ""
    }
    return data

def buyer_extend():
    data = {
        "propertyType": "",
        "district": "",
        "municipalityCounty": "",
        "divisionSubcounty": "",
        "town": "",
        "cellVillage": "",
        "effectiveRegistrationDate": "",
        "meterStatus": ""
    }
    return data

def goods_details():
    data = {
        "item": "",
        "itemCode": "",
        "qty": "",
        "unitOfMeasure": "",
        "unitPrice": "",
        "total": "",
        "taxRate": "",
        "tax": "",
        "discountTotal": "",
        "discountTaxRate": "",
        "orderNumber": "",
        "discountFlag": "",
        "deemedFlag": "",
        "exciseFlag": "",
        "categoryId": "",
        "categoryName": "",
        "goodsCategoryId": "",
        "goodsCategoryName": "",
        "exciseRate": "",
        "exciseRule": "",
        "exciseTax": "",
        "pack": "",
        "stick": "",
        "exciseUnit": "",
        "exciseCurrency": "",
        "exciseRateName": "",
        "vatApplicableFlag": "",
        "deemedExemptCode": "",
        "vatProjectId": "",
        "vatProjectName": ""
    }
    return data

def tax_details():
    data = {
        "taxCategoryCode": "",
        "netAmount": "",
        "taxRate": "",
        "taxAmount": "",
        "grossAmount": "",
        "exciseUnit": "",
        "exciseCurrency": "",
        "taxRateName": ""
    }
    return data

def summary_details():  
    data = {
        "netAmount": "",
        "taxAmount": "",
        "grossAmount": "",
        "itemCount": "",
        "modeCode": "",
        "remarks": "",
        "qrCode": ""
    }
    return data

def payment_details():  
    data = {
        "paymentMode": "",
        "paymentAmount": "",
        "orderNumber": ""
    }
    return data

def extend_details():  
    data = {
        "reason": "",
        "reasonCode": ""
    }
    return data

def import_services_seller():  
    data = {
        "importBusinessName": "",
        "importEmailAddress": "",
        "importContactNumber": "",
        "importAddress": "",
        "importInvoiceDate": "",
        "importAttachmentName": "",
        "importAttachmentContent": ""
    }
    return data

def airline_goods_details():  
    data = {
        "airlineGoodsDetails": ""
    }
    return data


def credit_note_json():
    data = {
    "referenceNo": "",
    "oriInvoiceNo": "",
    "invoiceNo": "",
    "combineKeywords": "",
    "approveStatus": "",
    "queryType": "1",
    "invoiceApplyCategoryCode": "",
    "startDate": "",
    "endDate": "",
    "pageNo": "1",
    "pageSize": "99",
    "creditNoteType": "",
    "branchName": "",
    "sellerTinOrNin": "",
    "sellerLegalOrBusinessName": ""
    }
    return data


def approve_credit_note(ref_no, status, id, remarks):
    data = {
    "referenceNo": ref_no,
    "approveStatus": status,
    "taskId": id,
    "remark": remarks
    }
    return data

def cancel_credit_note(fdn, cn_fdn, reason):
    data = {
    "oriInvoiceId": fdn,
    "invoiceNo": cn_fdn,
    "reason": reason,
    "reasonCode": "103",
    "invoiceApplyCategoryCode": "104",
    "attachmentList": [{
        "fileName": "",
        "fileType": "",
        "fileContent": ""
    }]
}

    return data