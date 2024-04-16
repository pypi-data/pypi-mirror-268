# EFRIS Package

This Python package provides a simple interface to interact with the EFRIS (Electronic Fiscal Receipt Information System) API provided by the Uganda Revenue Authority (URA) for invoicing.

## Features

- Create EFRIS invoices
- Retrieve the status of credit notes
- Easily integrate with your existing application
- Query taxpayer by TIN
- Query document details
- Query invoice details by FDN (Fiscal Document Number)
- Get the system dictionary for API-related details
- Approve credit notes
- Cancel credit notes
- Get the Z daily report from the fiscal device
- Cancel credit note applications
- Acquire exchange rates for transactional purposes


## Why I Created This Package

While working with the Uganda Revenue Authority (URA) API, I encountered numerous obstacles. My experiences led me to a deep understanding of the API's intricacies. This package is the result of my efforts to alleviate the "pain" for others—ensuring that you don't have to face the same challenges. Designed to be user-friendly, this guide will assist you, irrespective of your programming language, through the entire process from setting up the offline enabler to generating your first e-invoice. So grab a cup of chai and let's get started.

### Setting Up the Offline Enabler

1. **Download the Enabler**:
   Navigate to the [URA eFris test site](https://efristest.ura.go.ug/efrissite) and download the offline enabler. Follow the installation instructions provided on the website.

2. **Installation and Configuration**:
   After installation, you will receive an IP address from the enabler, for example, `199.82.32.128`. Append a port, such as `9880`, resulting in `http://199.82.32.128:9880` — this will serve as your base URL. To access the GUI of your enabler, visit `http://199.82.32.128:9880/efristcs`.

   Ensure you follow the detailed installation procedures in the guide to initialize your enabler and configure both a public and private key.

### Consuming the API

Once everything is set up, you're ready to dive into using the API to produce your e-invoices and more. The detailed steps provided in this guide will ensure a smooth experience as you integrate with the URA's systems.

## `__init__(self, ip, device_number, tin, seller_name)`

Initialize the EFRISInvoicing class.

### Args:
- `ip` (str): The IP address of the EFRIS Enabler server.
- `device_number` (str): The device number.
- `tin` (str): The Tax Identification Number.
- `seller_name` (str): The name of the seller.

# Function: `query_tax_payer_by_tin(self, tin)`

This function is part of a class (not shown in the snippet) and is used to query a tax payer by their Tax Identification Number (TIN).

## Parameters:

- `tin` (str): The Tax Identification Number of the tax payer. This is the unique identifier for the tax payer.

## Returns:

- `dict`: A dictionary containing the formatted tax payer output.

## Code Explanation:

The function takes a TIN as input and creates a message dictionary with the TIN and an empty 'ninBrn' field. The 'ic' variable is set to 'T119', which might be a code indicating the type of query being performed.

The function then calls `self.efris_post(ic, message)`, which is likely a method in the same class that sends a POST request to a server (presumably the EFRIS server) with the 'ic' and 'message' as arguments.

The response from this POST request is then passed to the `format_taxpayer_output()` function (not shown in the snippet), which presumably formats the response into a more usable form. The result of this formatting function is what gets returned by `query_tax_payer_by_tin()`.

---

## Function: query_document(self, fdn, type)

This method queries a document by its Fiscal Document Number (FDN) and type.

### Parameters:
- `fdn` (str): The Fiscal Document Number of the document being queried.
- `type` (int): The type of the document (1 for Invoice, 2 for Receipt).

### Returns:
- `dict`: A dictionary containing the formatted output of the invoice query.

### Code Explanation:

The `query_document` method initializes the `ic` variable with the value `'T106'`, which likely denotes the type of query being performed.

Next, it prepares the `message` by calling `query_invoice_json(fdn, str(type))`. This function likely formats the `fdn` and `type` into a JSON message suitable for querying the invoice.

The method then sends a POST request to an external server (possibly the EFRIS server) using `self.efris_post(ic, message)`. This method handles the POST request and retrieves the response.

The response from the POST request is then passed to the `format_invoice_query_output` function (not shown in this snippet), which likely processes the response and formats it into a more usable dictionary.

Finally, the formatted output of the invoice query is returned as a dictionary by the `query_document` method.


---

## Function: query_invoice_details(self, fdn)

This method queries the details of an invoice using its Fiscal Document Number (FDN).

### Parameters:
- `fdn` (str): The Fiscal Document Number (FDN) of the invoice.

### Returns:
- `dict`: A dictionary containing the cleaned invoice data.

### Code Explanation:

The `query_invoice_details` method initializes the `ic` variable with the value `'T108'`, which likely indicates the type of query being performed for invoice details.

Next, it prepares the `message` by calling `invoice_details_json(fdn)`. This function likely formats the `fdn` into a JSON message suitable for querying the invoice details.

The method then sends a POST request to an external server (possibly the EFRIS server) using `self.efris_post(ic, message)`. This method handles the POST request and retrieves the response.

The response from the POST request is then passed to the `clean_invoice_data_json` function (not shown in this snippet), which likely processes the response and cleans the invoice data, preparing it for use.

Finally, the cleaned invoice data is returned as a dictionary by the `query_invoice_details` method.

---

## Function: system_dictionary(self)

This method queries the system dictionary from the EFRIS server.

### Returns:
- `dict`: The response from the EFRIS server, representing the system dictionary.

### Code Explanation:

The `system_dictionary` method initializes the `ic` variable with the value `'T115'`, which likely indicates the type of query being performed to retrieve the system dictionary.

It prepares an empty `message` list, as the system dictionary query may not require additional parameters.

The method then sends a POST request to an external server (presumably the EFRIS server) using `self.efris_post(ic, message)`. This method handles the POST request and retrieves the response.

The response from the POST request, which is expected to contain the system dictionary information, is returned directly as a dictionary by the `system_dictionary` method.


---

## Function: credit_notes_query(self)

This method queries credit notes from the EFRIS server.

### Returns:
- `dict`: The processed credit note output.

### Code Explanation:

The `credit_notes_query` method initializes the `ic` variable with the value `'T111'`, which likely indicates the type of query being performed to retrieve credit notes.

It prepares the `message` by calling `credit_note_json()`. This function likely prepares a JSON message suitable for querying credit notes.

The method then sends a POST request to an external server (presumably the EFRIS server) using `self.efris_post(ic, message)`. This method handles the POST request and retrieves the response.

The response from the POST request is then passed to the `process_creditnote_output` function (not shown in this snippet), which likely processes the response and formats the credit note data for further use.

Finally, the processed credit note output is returned as a dictionary by the `credit_notes_query` method.

---

## Function: credit_note_details(self, id)

This method queries the details of a specific credit note from the EFRIS server.

### Parameters:
- `id` (str): The ID of the credit note to query.

### Returns:
- `dict`: The response from the EFRIS server containing the details of the credit note.

### Code Explanation:

The `credit_note_details` method initializes the `ic` variable with the value `'T112'`, which likely indicates the type of query being performed to retrieve credit note details.

It prepares the `message` as a dictionary containing the `id` parameter provided as an argument to the method.

The method then sends a POST request to an external server (presumably the EFRIS server) using `self.efris_post(ic, message)`. This method handles the POST request and includes the `ic` and `message` as arguments.

The response from the POST request, which contains the details of the queried credit note, is returned as a dictionary by the `credit_note_details` method.

---

## Function: approve_credit_note(self, reference_no, status, id, remarks)

This method is used to approve or reject a credit note by sending a request to the EFRIS server.

### Parameters:
- `reference_no` (str): The reference number of the credit note.
- `status` (int): The status of the credit note, where:
  - `101`: Indicates approval ("Approved")
  - `103`: Indicates rejection ("Rejected")
- `id` (str): The ID of the credit note.
- `remarks` (str): Remarks or comments for the credit note.

### Returns:
- `dict`: The response from the EFRIS server confirming the action.

### Raises:
- `ValueError`: If the `status` parameter is invalid and does not match the allowed values.

### Code Explanation:

The `approve_credit_note` method initializes the `ic` variable with the value `'T113'`, which likely indicates the type of action being performed to approve or reject a credit note.

Input validation is performed for the `status` parameter using a dictionary `valid_status` that maps valid status codes (`101` for approval and `103` for rejection) to their corresponding descriptions ("Approved" and "Rejected").

If the provided `status` value does not match any of the valid codes in `valid_status`, a `ValueError` is raised with a descriptive error message indicating the valid options.

The `message` is prepared by calling the `approve_credit_note` function with the provided parameters (`reference_no`, `status`, `id`, `remarks`). This function likely constructs a JSON message representing the request to approve or reject the credit note.

Finally, a POST request is sent to the EFRIS server using `self.efris_post(ic, message)`, where `ic` is the action code and `message` is the request data. The response from the server, confirming the approval or rejection action, is returned as a dictionary by the `approve_credit_note` method.

---
## Function: cancel_credit_note(self, inv_fdn, cn_fdn, reason)

This method is used to cancel a credit note by sending a request to the EFRIS server.

### Parameters:
- `inv_fdn` (str): The FDN (Fiscal Document Number) of the original invoice associated with the credit note.
- `cn_fdn` (str): The FDN of the credit note to be canceled.
- `reason` (str): The reason for canceling the credit note.

### Returns:
- `dict`: The response from the EFRIS server confirming the cancellation.

### Code Explanation:

The `cancel_credit_note` method initializes the `ic` variable with the value `'T112'`, which likely indicates the type of action being performed to cancel a credit note.

The `message` is prepared by calling the `cancel_credit_note` function with the provided parameters (`inv_fdn`, `cn_fdn`, `reason`). This function likely constructs a JSON message representing the request to cancel the credit note, including the necessary document numbers (`inv_fdn`, `cn_fdn`) and cancellation reason.

Finally, a POST request is sent to the EFRIS server using `self.efris_post(ic, message)`, where `ic` is the action code and `message` is the request data. The response from the server, confirming the cancellation of the credit note, is returned as a dictionary by the `cancel_credit_note` method.

---

## Function: z_report(self)

This method is used to generate a Z report by sending a request to the EFRIS server.

### Returns:
- `dict`: The response from the EFRIS server containing the Z report data.

### Code Explanation:

The `z_report` method initializes the `ic` variable with the value `'T116'`, which likely represents the action code for generating a Z report.

The `message` variable is initialized as an empty dictionary (`{}`), indicating that no specific parameters or data are required to generate the Z report.

A POST request is then sent to the EFRIS server using `self.efris_post(ic, message)`, where `ic` is the action code and `message` is the request data (in this case, empty). The response from the server containing the Z report data is returned as a dictionary by the `z_report` method.

---

## Function: cancel_credit_note_application(self, business_key, reference_no)

This method is used to cancel a credit note application by sending a request to the EFRIS server.

### Args:
- `business_key (str)`: The business key associated with the credit note application.
- `reference_no (str)`: The reference number of the credit note application.

### Returns:
- `dict`: The response from the EFRIS server confirming the cancellation.

### Code Explanation:

The `cancel_credit_note_application` method initializes the `ic` variable with the value `'T120'`, representing the action code for canceling a credit note application.

The `message` variable is initialized as a dictionary containing the `businessKey` and `referenceNo` fields, which are provided as arguments to the method.

A POST request is then sent to the EFRIS server using `self.efris_post(ic, message)`, where `ic` is the action code and `message` contains the business key and reference number of the credit note application to be canceled.

The response from the server confirming the cancellation of the credit note application is returned as a dictionary by the `cancel_credit_note_application` method.

---

## Function: acquiring_exchange_rate(self, currency)

This method is used to acquire the exchange rate for a specific currency from the EFRIS server.

### Args:
- `currency (str)`: The currency code for which the exchange rate is requested.

### Returns:
- `dict`: A dictionary containing the cleaned currency output, including the exchange rate.

### Code Explanation:

The `acquiring_exchange_rate` method begins by initializing the `ic` variable with the value `'T121'`, which is the action code used to request the exchange rate for a currency.

The `message` variable is then created as a dictionary containing the `currency` code provided as an argument and the `issueDate`, presumably representing the date of the exchange rate request.

The method sends a POST request to the EFRIS server using `self.efris_post(ic, message)`, passing the action code (`ic`) and message (`message`) as parameters.

The response from the server is then passed to the `currency_output_cleaner` function, which processes and cleans the currency output data.

Finally, the cleaned currency output, including the exchange rate, is returned as a dictionary by the `acquiring_exchange_rate` method.

---
## Function: query_tax_payer_by_tin(self, tin)

This method is used to query a tax payer by their Tax Identification Number (TIN) from the EFRIS server.

### Args:
- `tin (str)`: The Tax Identification Number of the tax payer. This is the unique identifier for the tax payer.

### Returns:
- `dict`: A dictionary containing the formatted tax payer output.

### Code Explanation:

The `query_tax_payer_by_tin` method initializes the `ic` variable with the value `'T119'`, which represents the action code for querying a tax payer by TIN.

The `message` variable is created as a dictionary with keys `"tin"` set to the provided `tin` argument and `"ninBrn
---

## Function: query_tax_payer_by_tin(self, tin)

This method is used to query a tax payer by their Tax Identification Number (TIN) from the EFRIS server.

### Args:
- `tin (str)`: The Tax Identification Number of the tax payer. This is the unique identifier for the tax payer.

### Returns:
- `dict`: A dictionary containing the formatted tax payer output.

### Code Explanation:

The `query_tax_payer_by_tin` method initializes the `ic` variable with the value `'T119'`, which represents the action code for querying a tax payer by TIN.

The `message` variable is created as a dictionary with keys `"tin"` set to the provided `tin` argument and `"ninBrn"` set to an empty string (`""`), which might represent another identifier or parameter.

The method then sends a POST request to the EFRIS server using `self.efris_post(ic, message)`, passing the action code (`ic`) and message (`message`) as parameters.

The response from the server is passed to the `format_taxpayer_output` function, which formats and processes the tax payer data received from the server.

Finally, the formatted tax payer output is returned as a dictionary by the `query_tax_payer_by_tin` method.

---

If you found this package helpful, consider buying me a coffee! 😊

Mobile money number: +256705860416

Or get in touch with me on [douglasekuwanda@gmail.com](mailto:douglasekuwanda@gmail.com)

