
import json


def format_taxpayer_output(input_data):
    if isinstance(input_data, dict):
        # If input is a dictionary (structured data)
        taxpayer_info = input_data.get('taxpayer')
        if taxpayer_info:
            formatted_info = {
                "status": "success",
                "data": {
                    "Taxpayer Name": taxpayer_info.get('legalName', 'N/A'),
                    "Business Name": taxpayer_info.get('businessName', 'N/A'),
                    "Address": taxpayer_info.get('address', 'N/A'),
                    "Contact Email": taxpayer_info.get('contactEmail', 'N/A'),
                    "Contact Number": taxpayer_info.get('contactNumber', 'N/A'),
                    "TIN": taxpayer_info.get('tin', 'N/A'),
                    "Government TIN": taxpayer_info.get('governmentTIN', 'N/A'),
                    "Taxpayer Type": taxpayer_info.get('taxpayerType', 'N/A')
                }
            }
        else:
            formatted_info = {
                "status": "error",
                "message": "The taxpayer does not exist or the state is abnormal!"
            }
    else:
        # If input is a plain text (e.g., "This is wrong")
        formatted_info = {
            "status": "error",
            "message": input_data
        }
    
    return formatted_info


def format_invoice_query_output(input_data):
    if isinstance(input_data, dict):
        # If input is a dictionary (structured data)
        records = input_data.get('records', [])
        if records:
            formatted_records = []
            for record in records:
                formatted_record = {
                    "branchId": record.get('branchId', ''),
                    "branchName": record.get('branchName', ''),
                    "businessName": record.get('businessName', ''),
                    "buyerBusinessName": record.get('buyerBusinessName', ''),
                    "buyerLegalName": record.get('buyerLegalName', ''),
                    "buyerTin": record.get('buyerTin', ''),
                    "currency": record.get('currency', ''),
                    "dataSource": record.get('dataSource', ''),
                    "dateFormat": record.get('dateFormat', 'N/A'),
                    "deviceNo": record.get('deviceNo', ''),
                    "grossAmount": record.get('grossAmount', ''),
                    "id": record.get('id', ''),
                    "invoiceIndustryCode": record.get('invoiceIndustryCode', ''),
                    "invoiceKind": record.get('invoiceKind', ''),
                    "invoiceNo": record.get('invoiceNo', ''),
                    "invoiceType": record.get('invoiceType', ''),
                    "isInvalid": record.get('isInvalid', ''),
                    "isRefund": record.get('isRefund', ''),
                    "issuedDate": record.get('issuedDate', ''),
                    "issuedDateStr": record.get('issuedDateStr', ''),
                    "legalName": record.get('legalName', ''),
                    "nowTime": input_data.get('nowTime', ''),
                    "operator": record.get('operator', ''),
                    "pageIndex": record.get('pageIndex', 0),
                    "pageNo": record.get('pageNo', 0),
                    "pageSize": record.get('pageSize', 0),
                    "referenceNo": record.get('referenceNo', ''),
                    "taxAmount": record.get('taxAmount', ''),
                    "uploadingTime": record.get('uploadingTime', ''),
                    "userName": record.get('userName', '')
                }
                formatted_records.append(formatted_record)
            
            formatted_info = {
                "status": "success",
                "data": {
                    "dateFormat": input_data.get('dateFormat', 'N/A'),
                    "nowTime": input_data.get('nowTime', ''),
                    "page": {
                        "pageCount": input_data.get('page', {}).get('pageCount', 0),
                        "pageNo": input_data.get('page', {}).get('pageNo', 0),
                        "pageSize": input_data.get('page', {}).get('pageSize', 0),
                        "totalSize": input_data.get('page', {}).get('totalSize', 0)
                    },
                    "records": formatted_records,
                    "timeFormat": input_data.get('timeFormat', 'N/A')
                }
            }
        else:
            formatted_info = {
                "status": "error",
                "message": "No invoice records found!"
            }
    else:
        # If input is a plain text (e.g., "This is wrong")
        formatted_info = {
            "status": "error",
            "message": input_data
        }
    
    return formatted_info

def clean_invoice_data_json(input_data):
    cleaned_data = {}
    
    # Extract and clean 'basicInformation' details
    basic_info = input_data.get('basicInformation', {})
    cleaned_basic_info = {
        'antifakeCode': basic_info.get('antifakeCode', ''),
        'currency': basic_info.get('currency', ''),
        'currencyRate': basic_info.get('currencyRate', ''),
        'dataSource': basic_info.get('dataSource', ''),
        'deviceNo': basic_info.get('deviceNo', ''),
        'invoiceId': basic_info.get('invoiceId', ''),
        'invoiceIndustryCode': basic_info.get('invoiceIndustryCode', ''),
        'invoiceKind': basic_info.get('invoiceKind', ''),
        'invoiceNo': basic_info.get('invoiceNo', ''),
        'invoiceType': basic_info.get('invoiceType', ''),
        'isBatch': basic_info.get('isBatch', ''),
        'isInvalid': basic_info.get('isInvalid', ''),
        'isPreview': basic_info.get('isPreview', ''),
        'isRefund': basic_info.get('isRefund', ''),
        'issuedDate': basic_info.get('issuedDate', ''),
        'issuedDatePdf': basic_info.get('issuedDatePdf', ''),
        'operator': basic_info.get('operator', '')
    }
    
    cleaned_data['basicInformation'] = cleaned_basic_info
    
    # Extract and clean 'buyerDetails' details
    buyer_details = input_data.get('buyerDetails', {})
    cleaned_buyer_details = {
        'buyerBusinessName': buyer_details.get('buyerBusinessName', ''),
        'buyerEmail': buyer_details.get('buyerEmail', ''),
        'buyerLegalName': buyer_details.get('buyerLegalName', ''),
        'buyerTin': buyer_details.get('buyerTin', ''),
        'buyerType': buyer_details.get('buyerType', ''),
        'dateFormat': buyer_details.get('dateFormat', ''),
        'nowTime': buyer_details.get('nowTime', ''),
        'pageIndex': buyer_details.get('pageIndex', ''),
        'pageNo': buyer_details.get('pageNo', ''),
        'pageSize': buyer_details.get('pageSize', ''),
        'timeFormat': buyer_details.get('timeFormat', '')
    }
    
    cleaned_data['buyerDetails'] = cleaned_buyer_details
    
    # Extract and clean 'goodsDetails'
    goods_details = input_data.get('goodsDetails', [])
    cleaned_goods_details = []
    for goods_item in goods_details:
        cleaned_goods_item = {
            'deemedFlag': goods_item.get('deemedFlag', ''),
            'discountFlag': goods_item.get('discountFlag', ''),
            'exciseFlag': goods_item.get('exciseFlag', ''),
            'exciseTax': goods_item.get('exciseTax', ''),
            'goodsCategoryId': goods_item.get('goodsCategoryId', ''),
            'goodsCategoryName': goods_item.get('goodsCategoryName', ''),
            'item': goods_item.get('item', ''),
            'itemCode': goods_item.get('itemCode', ''),
            'orderNumber': goods_item.get('orderNumber', ''),
            'qty': goods_item.get('qty', ''),
            'tax': goods_item.get('tax', ''),
            'taxRate': goods_item.get('taxRate', ''),
            'total': goods_item.get('total', ''),
            'unitOfMeasure': goods_item.get('unitOfMeasure', ''),
            'unitPrice': goods_item.get('unitPrice', ''),
            'vatApplicableFlag': goods_item.get('vatApplicableFlag', '')
        }
        cleaned_goods_details.append(cleaned_goods_item)
    
    cleaned_data['goodsDetails'] = cleaned_goods_details
    
    # Extract and clean 'sellerDetails'
    seller_details = input_data.get('sellerDetails', {})
    cleaned_seller_details = {
        'address': seller_details.get('address', ''),
        'branchCode': seller_details.get('branchCode', ''),
        'branchId': seller_details.get('branchId', ''),
        'branchName': seller_details.get('branchName', ''),
        'businessName': seller_details.get('businessName', ''),
        'emailAddress': seller_details.get('emailAddress', ''),
        'legalName': seller_details.get('legalName', ''),
        'referenceNo': seller_details.get('referenceNo', ''),
        'tin': seller_details.get('tin', '')
    }
    
    cleaned_data['sellerDetails'] = cleaned_seller_details
    
    # Extract and clean 'summary'
    summary_info = input_data.get('summary', {})
    cleaned_summary_info = {
        'grossAmount': summary_info.get('grossAmount', ''),
        'itemCount': summary_info.get('itemCount', ''),
        'modeCode': summary_info.get('modeCode', ''),
        'netAmount': summary_info.get('netAmount', ''),
        'qrCode': summary_info.get('qrCode', ''),
        'remarks': summary_info.get('remarks', ''),
        'taxAmount': summary_info.get('taxAmount', '')
    }
    
    cleaned_data['summary'] = cleaned_summary_info
    
    return cleaned_data


def process_creditnote_output(data):
    data_dict = json.loads(data)

    date_format = data_dict.get('dateFormat')
    now_time = data_dict.get('nowTime')
    records = data_dict.get('records', [])

    best_data = []
    for record in records:
        record_data = {
            'applicationTime': record.get('applicationTime'),
            'approveStatus': record.get('approveStatus'),
            'businessName': record.get('businessName'),
            'buyerBusinessName': record.get('buyerBusinessName'),
            'buyerLegalName': record.get('buyerLegalName'),
            'buyerTin': record.get('buyerTin'),
            'currency': record.get('currency'),
            'dataSource': record.get('dataSource'),
            'grossAmount': record.get('grossAmount'),
            'id': record.get('id'),
            'invoiceApplyCategoryCode': record.get('invoiceApplyCategoryCode'),
            'invoiceNo': record.get('invoiceNo'),
            'legalName': record.get('legalName'),
            'nowTime': record.get('nowTime'),
            'oriGrossAmount': record.get('oriGrossAmount'),
            'oriInvoiceNo': record.get('oriInvoiceNo'),
            'pageIndex': record.get('pageIndex'),
            'pageNo': record.get('pageNo'),
            'pageSize': record.get('pageSize'),
            'referenceNo': record.get('referenceNo'),
            'source': record.get('source'),
            'tin': record.get('tin'),
            'totalAmount': record.get('totalAmount'),
            'waitingDate': record.get('waitingDate')
        }
        best_data.append(record_data)

    formatted_output = {
        'dateFormat': date_format,
        'nowTime': now_time,
        'bestData': best_data
    }

    return formatted_output


def currency_output_cleaner(data):
    try:
        if isinstance(data, str):
            # Try to parse input data as JSON
            data = json.loads(data)

        # Ensure `data` is a dictionary after JSON parsing
        if not isinstance(data, dict):
            raise ValueError("Input data is not in the expected dictionary format.")

        formatted_data = {
            'Export Levy': data.get('exportLevy', 'N/A'),
            'Rate': data.get('rate', 'N/A'),
            'Import Duty Levy': data.get('importDutyLevy', 'N/A'),
            'Currency': data.get('currency', 'N/A'),
            'Income Tax': data.get('inComeTax', 'N/A')
        }
    except json.JSONDecodeError as e:
        # Handle JSON parsing errors
        formatted_data = {
            'status': 'error',
            'message': f'Failed to parse input data as JSON: {str(e)}'
        }
    except ValueError as e:
        # Handle unexpected input data format
        formatted_data = {
            'status': 'error',
            'message': str(e)
        }
    
    return formatted_data
