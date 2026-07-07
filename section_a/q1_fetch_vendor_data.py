import time
import logging

mock_db = {
    "V001": {"name": "Alpha Corp", "rating": 4.5},
    "V002": {"name": "Beta Ltd", "rating": 3.8},
    "V004": {"name": "Delta Inc", "rating": 4.9},
}


def fetch_vendor_data(vendor_ids):

    fetched_vendors = {}

    for vendor_id in vendor_ids:
        
        time.sleep(0.5)
        
        if vendor_id in mock_db:
            fetched_vendors[vendor_id] = mock_db[vendor_id]
        else:
            logging.warning(f"Vendor ID '{vendor_id}' Not Found!")

    return fetched_vendors


if __name__ == '__main__':
    vendor_ids = ["V001", "V002", "V003", "V004", "V005"]

    result = fetch_vendor_data(vendor_ids)

    print("Fetched Vendor Data: ")
    
    for vendor_id, details in result.items():
        print(f"{vendor_id} : {details}")