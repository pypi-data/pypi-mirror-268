
import requests
import base64
import gzip
import json

def encode(text):
    to_bytes = text.encode('utf-8')
    # 'utf-8' ascii
    return (base64.b64encode(to_bytes))

def decode(text):
    return (base64.b64decode(text))

def decode_content(content):
    decoded_content = base64.b64decode(content.encode('utf-8'))
    decoded_dict = json.loads(decoded_content)
    return decoded_dict

def process_response(ip, data_dump):
    response = requests.post(ip, json=data_dump)
    response.raise_for_status()
    json_data = response.json()
    print('-------------------------')
    print(json_data)

    if json_data['returnStateInfo']['returnMessage'] == 'SUCCESS':
        if json_data['data']['dataDescription']['zipCode'] != '1':
            content = json_data['data']['content']
            decoded_data = decode_content(content)
            return decoded_data
        else:
            content = json_data['data']['content']
            gz = base64.b64decode(content)
            decompressed_data = gzip.decompress(gz).decode('utf-8')
            if isinstance(decompressed_data, str):
                return decompressed_data
            else:
                return json.loads(decompressed_data)
    else:
        # print(f"Error: {json_data['returnStateInfo']['returnMessage']}")
        return json_data['returnStateInfo']['returnMessage']