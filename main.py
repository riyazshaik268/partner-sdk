import google.generativeai as genai
import json


# installation
# pip install -q -U google-generativeai
# API_KEY taken from Jules' account

# Press <no shortcut> to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
GOOGLE_API_KEY = 'AIzaSyBykeoHrov-BXesnFR0Bvo67r_8nqgq4U0'

genai.configure(api_key=GOOGLE_API_KEY)

sixsense_acccount_schema = """
{
    "Id": {
      "type": "string",
      "description": "Account ID"
    },
    "Name": {
      "type": "string",
      "description": "Account Name"
    },
    "Type": {
      "type": "string",
      "description": "Account Type (e.g., Prospect, Customer)"
    },
    "Industry": {
      "type": "string",
      "description": "Industry the account belongs to"
    },
    "Phone": {
      "type": "string",
      "description": "Account Phone Number"
    },
    "Website": {
      "type": "string",
      "description": "Account Website"
    },
    "AnnualRevenue": {
      "type": "number",
      "format": "float",
      "description": "Annual Revenue of the Account"
    },
    "NumberOfEmployees": {
      "type": "integer",
      "description": "Number of Employees at the Account"
    },
    "BillingStreet": {
      "type": "string",
      "description": "Billing Street Address"
    },
    "BillingCity": {
      "type": "string",
      "description": "Billing City"
    },
    "BillingState": {
      "type": "string",
      "description": "Billing State/Province"
    },
    "BillingPostalCode": {
      "type": "string",
      "description": "Billing Postal Code"
    },
    "BillingCountry": {
      "type": "string",
      "description": "Billing Country"
    },
    "ShippingStreet": {
      "type": "string",
      "description": "Shipping Street Address"
    },
    "ShippingCity": {
      "type": "string",
      "description": "Shipping City"
    },
    "ShippingState": {
      "type": "string",
      "description": "Shipping State/Province"
    },
    "ShippingPostalCode": {
      "type": "string",
      "description": "Shipping Postal Code"
    },
    "ShippingCountry": {
      "type": "string",
      "description": "Shipping Country"
    },
    "Description": {
      "type": "string",
      "description": "Account Description"
    },
    "CreatedDate": {
      "type": "string",
      "format": "date-time",
      "description": "Date and Time the Account was created"
    },
    "LastModifiedDate": {
      "type": "string",
      "format": "date-time",
      "description": "Date and Time the Account was last modified"
    }
}
"""

SAMPLE_ACCOUNT_DATA_ONLY_1 = """
[
     {
        "Id": "0011x0000123Bcd",
        "Name": "Globex Corporation",
        "Account_Type": "Prospect",
        "Rating": "Warm",
        "Industry": "Finance",
        "Phone": "1-555-987-6543",
        "Website": "www.globexcorp.com",
        "Total_AnnualRevenue": 50000000,
        "NumberOfEmployees": 250,
        "Street": "456 Elm St",
        "City": "Somecity",
        "State": "NY",
        "PostalCode": "10001",
        "Country": "USA",
        "Street2": "456 Another St",
        "City2": "Anothercity",
        "State2": "CA",
        "PostalCode2": "10011",
        "ShippingCountry": "USA",
        "Description": "Globex Corporation is a leading financial services provider.",
        "OwnerId": "0051x000004EfgH",
        "CreatedDate": "2023-05-10T14:00:00.000Z",
        "LastModifiedDate": "2024-11-05T16:00:00.000Z",
        "CustomField1__c": "Medium",
        "CustomField2__c": false,
        "CustomField3__c": 8,
        "CustomField4__c": "2024-09-15",
        "CustomField5__c": 560.75,
        "CustomField6__c": "Gold",
        "CustomField7__c": true,
        "CustomField8__c": "2024-01-10T09:15:00.000Z",
        "CustomField9__c": "In Progress",
        "CustomField10__c": 55,
        "CustomField11__c": "www.example.com/account/0011x0000123Bcd",
        "CustomField12__c": "Low",
        "CustomField13__c": 10000,
        "CustomField14__c": "2024-12-20",
        "CustomField15__c": "Inactive"
    }
]
"""

SAMPLE_ACCOUNT_DATA = """
[
    {
        "Id": "0011x0000123Abc",
        "Name": "Acme Corporation",
        "Type": "Customer",
        "Rating": "Hot",
        "Industry": "Technology",
        "Phone": "1-555-123-4567",
        "Website": "www.acmecorp.com",
        "AnnualRevenue": 100000000,
        "NumberOfEmployees": 500,
        "BillingStreet": "123 Main St",
        "BillingCity": "Anytown",
        "BillingState": "CA",
        "BillingPostalCode": "91234",
        "BillingCountry": "USA",
        "ShippingStreet": "123 Main St",
        "ShippingCity": "Anytown",
        "ShippingState": "CA",
        "ShippingPostalCode": "91234",
        "ShippingCountry": "USA",
        "Description": "Acme Corporation provides cutting-edge technology solutions.",
        "OwnerId": "0051x000004DefG",
        "CreatedDate": "2023-08-15T10:00:00.000Z",
        "LastModifiedDate": "2024-11-06T12:00:00.000Z",
        "CustomField1__c": "High",
        "CustomField2__c": true,
        "CustomField3__c": 15,
        "CustomField4__c": "2024-10-20",
        "CustomField5__c": 1200.50,
        "CustomField6__c": "Platinum",
        "CustomField7__c": false,
        "CustomField8__c": "2023-12-25T14:30:00.000Z",
        "CustomField9__c": "Completed",
        "CustomField10__c": 88,
        "CustomField11__c": "www.example.com/account/0011x0000123Abc",
        "CustomField12__c": "Medium",
        "CustomField13__c": 25000,
        "CustomField14__c": "2025-03-10",
        "CustomField15__c": "Active"
    },
    {
        "Id": "0011x0000123Bcd",
        "Name": "Globex Corporation",
        "Type": "Prospect",
        "Rating": "Warm",
        "Industry": "Finance",
        "Phone": "1-555-987-6543",
        "Website": "www.globexcorp.com",
        "AnnualRevenue": 50000000,
        "NumberOfEmployees": 250,
        "BillingStreet": "456 Elm St",
        "BillingCity": "Somecity",
        "BillingState": "NY",
        "BillingPostalCode": "10001",
        "BillingCountry": "USA",
        "ShippingStreet": "456 Elm St",
        "ShippingCity": "Somecity",
        "ShippingState": "NY",
        "ShippingPostalCode": "10001",
        "ShippingCountry": "USA",
        "Description": "Globex Corporation is a leading financial services provider.",
        "OwnerId": "0051x000004EfgH",
        "CreatedDate": "2023-05-10T14:00:00.000Z",
        "LastModifiedDate": "2024-11-05T16:00:00.000Z",
        "CustomField1__c": "Medium",
        "CustomField2__c": false,
        "CustomField3__c": 8,
        "CustomField4__c": "2024-09-15",
        "CustomField5__c": 560.75,
        "CustomField6__c": "Gold",
        "CustomField7__c": true,
        "CustomField8__c": "2024-01-10T09:15:00.000Z",
        "CustomField9__c": "In Progress",
        "CustomField10__c": 55,
        "CustomField11__c": "www.example.com/account/0011x0000123Bcd",
        "CustomField12__c": "Low",
        "CustomField13__c": 10000,
        "CustomField14__c": "2024-12-20",
        "CustomField15__c": "Inactive"
    },
    {
        "Id": "0011x0000123Cde",
        "Name": "Stark Industries",
        "Type": "Customer",
        "Rating": "Hot",
        "Industry": "Defense",
        "Phone": "1-555-852-9637",
        "Website": "www.starkindustries.com",
        "AnnualRevenue": 2000000000,
        "NumberOfEmployees": 10000,
        "BillingStreet": "789 Oak St",
        "BillingCity": "Bigcity",
        "BillingState": "CA",
        "BillingPostalCode": "90210",
        "BillingCountry": "USA",
        "ShippingStreet": "789 Oak St",
        "ShippingCity": "Bigcity",
        "ShippingState": "CA",
        "ShippingPostalCode": "90210",
        "ShippingCountry": "USA",
        "Description": "Stark Industries is a global leader in defense technology.",
        "OwnerId": "0051x000004FghI",
        "CreatedDate": "2022-01-20T16:00:00.000Z",
        "LastModifiedDate": "2024-11-04T18:00:00.000Z",
        "CustomField1__c": "Low",
        "CustomField2__c": true,
        "CustomField3__c": 50,
        "CustomField4__c": "2024-11-05",
        "CustomField5__c": 5000.25,
        "CustomField6__c": "Silver",
        "CustomField7__c": false,
        "CustomField8__c": "2024-05-15T11:45:00.000Z",
        "CustomField9__c": "Cancelled",
        "CustomField10__c": 120,
        "CustomField11__c": "www.example.com/account/0011x0000123Cde",
        "CustomField12__c": "High",
        "CustomField13__c": 500000,
        "CustomField14__c": "2025-06-15",
        "CustomField15__c": "Pending"
    },
    {
        "Id": "0011x0000123Abc",
        "Name": "Acme Corporation",
        "Type": "Customer",
        "Rating": "Hot",
        "Industry": "Technology",
        "Phone": "1-555-123-4567",
        "Website": "www.acmecorp.com",
        "AnnualRevenue": 100000000,
        "NumberOfEmployees": 500,
        "BillingStreet": "123 Main St",
        "BillingCity": "Anytown",
        "BillingState": "CA",
        "BillingPostalCode": "91234",
        "BillingCountry": "USA",
        "ShippingStreet": "123 Main St",
        "ShippingCity": "Anytown",
        "ShippingState": "CA",
        "ShippingPostalCode": "91234",
        "ShippingCountry": "USA",
        "Description": "Acme Corporation provides cutting-edge technology solutions.",
        "OwnerId": "0051x000004DefG",
        "CreatedDate": "2023-08-15T10:00:00.000Z",
        "LastModifiedDate": "2024-11-06T12:00:00.000Z",
        "CustomField1__c": "High",
        "CustomField2__c": true,
        "CustomField3__c": 15,
        "CustomField4__c": "2024-10-20",
        "CustomField5__c": 1200.50,
        "CustomField6__c": "Platinum",
        "CustomField7__c": false,
        "CustomField8__c": "2023-12-25T14:30:00.000Z",
        "CustomField9__c": "Completed",
        "CustomField10__c": 88,
        "CustomField11__c": "www.example.com/account/0011x0000123Abc",
        "CustomField12__c": "Medium",
        "CustomField13__c": 25000,
        "CustomField14__c": "2025-03-10",
        "CustomField15__c": "Active"
    },
    {
        "Id": "0011x0000123Bcd",
        "Name": "Globex Corporation",
        "Type": "Prospect",
        "Rating": "Warm",
        "Industry": "Finance",
        "Phone": "1-555-987-6543",
        "Website": "www.globexcorp.com",
        "AnnualRevenue": 50000000,
        "NumberOfEmployees": 250,
        "BillingStreet": "456 Elm St",
        "BillingCity": "Somecity",
        "BillingState": "NY",
        "BillingPostalCode": "10001",
        "BillingCountry": "USA",
        "ShippingStreet": "456 Elm St",
        "ShippingCity": "Somecity",
        "ShippingState": "NY",
        "ShippingPostalCode": "10001",
        "ShippingCountry": "USA",
        "Description": "Globex Corporation is a leading financial services provider.",
        "OwnerId": "0051x000004EfgH",
        "CreatedDate": "2023-05-10T14:00:00.000Z",
        "LastModifiedDate": "2024-11-05T16:00:00.000Z",
        "CustomField1__c": "Medium",
        "CustomField2__c": false,
        "CustomField3__c": 8,
        "CustomField4__c": "2024-09-15",
        "CustomField5__c": 560.75,
        "CustomField6__c": "Gold",
        "CustomField7__c": true,
        "CustomField8__c": "2024-01-10T09:15:00.000Z",
        "CustomField9__c": "In Progress",
        "CustomField10__c": 55,
        "CustomField11__c": "www.example.com/account/0011x0000123Bcd",
        "CustomField12__c": "Low",
        "CustomField13__c": 10000,
        "CustomField14__c": "2024-12-20",
        "CustomField15__c": "Inactive"
    },
    {
        "Id": "0011x0000123Cde",
        "Name": "Stark Industries",
        "Type": "Customer",
        "Rating": "Hot",
        "Industry": "Defense",
        "Phone": "1-555-852-9637",
        "Website": "www.starkindustries.com",
        "AnnualRevenue": 2000000000,
        "NumberOfEmployees": 10000,
        "BillingStreet": "789 Oak St",
        "BillingCity": "Bigcity",
        "BillingState": "CA",
        "BillingPostalCode": "90210",
        "BillingCountry": "USA",
        "ShippingStreet": "789 Oak St",
        "ShippingCity": "Bigcity",
        "ShippingState": "CA",
        "ShippingPostalCode": "90210",
        "ShippingCountry": "USA",
        "Description": "Stark Industries is a global leader in defense technology.",
        "OwnerId": "0051x000004FghI",
        "CreatedDate": "2022-01-20T16:00:00.000Z",
        "LastModifiedDate": "2024-11-04T18:00:00.000Z",
        "CustomField1__c": "Low",
        "CustomField2__c": true,
        "CustomField3__c": 50,
        "CustomField4__c": "2024-11-05",
        "CustomField5__c": 5000.25,
        "CustomField6__c": "Silver",
        "CustomField7__c": false,
        "CustomField8__c": "2024-05-15T11:45:00.000Z",
        "CustomField9__c": "Cancelled",
        "CustomField10__c": 120,
        "CustomField11__c": "www.example.com/account/0011x0000123Cde",
        "CustomField12__c": "High",
        "CustomField13__c": 500000,
        "CustomField14__c": "2025-06-15",
        "CustomField15__c": "Pending"
    },
    {
        "Id": "0011x0000123Def",
        "Name": "Wayne Enterprises",
        "Type": "Customer",
        "Rating": "Warm",
        "Industry": "Technology",
        "Phone": "1-555-529-6378",
        "Website": "www.wayneenterprises.com",
        "AnnualRevenue": 500000000,
        "NumberOfEmployees": 2000,
        "BillingStreet": "1011 Pine St",
        "BillingCity": "Gotham City",
        "BillingState": "NY",
        "BillingPostalCode": "10004",
        "BillingCountry": "USA",
        "ShippingStreet": "1011 Pine St",
        "ShippingCity": "Gotham City",
        "ShippingState": "NY",
        "ShippingPostalCode": "10004",
        "ShippingCountry": "USA",
        "Description": "Wayne Enterprises is a diversified technology conglomerate.",
        "OwnerId": "0051x000004GhiJ"
    },
    {
        "Id": "0012x0000345Abc",
        "Name": "Cyberdyne Systems",
        "Type": "Prospect",
        "Rating": "Cold",
        "Industry": "Technology",
        "Phone": "1-555-234-5678",
        "Website": "www.cyberdyne.com",
        "AnnualRevenue": 500000000,
        "NumberOfEmployees": 1000,
        "BillingStreet": "456 Elm St",
        "BillingCity": "New York",
        "BillingState": "NY",
        "BillingPostalCode": "10001",
        "BillingCountry": "USA",
        "ShippingStreet": "456 Elm St",
        "ShippingCity": "New York",
        "ShippingState": "NY",
        "ShippingPostalCode": "10001",
        "ShippingCountry": "USA",
        "Description": "Cyberdyne Systems develops advanced artificial intelligence systems.",
        "OwnerId": "0052x000005DefG",
        "CreatedDate": "2023-01-15T10:00:00.000Z",
        "LastModifiedDate": "2024-10-06T12:00:00.000Z",
        "CustomField1__c": "Low",
        "CustomField2__c": false,
        "CustomField3__c": 5,
        "CustomField4__c": "2024-05-20",
        "CustomField5__c": 600.50,
        "CustomField6__c": "Bronze",
        "CustomField7__c": true,
        "CustomField8__c": "2023-06-25T14:30:00.000Z",
        "CustomField9__c": "Pending",
        "CustomField10__c": 44,
        "CustomField11__c": "www.example.com/account/0012x0000345Abc",
        "CustomField12__c": "High",
        "CustomField13__c": 15000,
        "CustomField14__c": "2024-08-10",
        "CustomField15__c": "Inactive"
    },
    {
        "Id": "0012x0000345Bcd",
        "Name": "Umbrella Corporation",
        "Type": "Customer",
        "Rating": "Hot",
        "Industry": "Pharmaceuticals",
        "Phone": "1-555-345-6789",
        "Website": "www.umbrellacorp.com",
        "AnnualRevenue": 1000000000,
        "NumberOfEmployees": 5000,
        "BillingStreet": "789 Oak St",
        "BillingCity": "Raccoon City",
        "BillingState": "PA",
        "BillingPostalCode": "19101",
        "BillingCountry": "USA",
        "ShippingStreet": "789 Oak St",
        "ShippingCity": "Raccoon City",
        "ShippingState": "PA",
        "ShippingPostalCode": "19101",
        "ShippingCountry": "USA",
        "Description": "Umbrella Corporation is a pharmaceutical giant with a dark secret.",
        "OwnerId": "0052x000005EfgH",
        "CreatedDate": "2022-05-10T14:00:00.000Z",
        "LastModifiedDate": "2024-10-05T16:00:00.000Z",
        "CustomField1__c": "Medium",
        "CustomField2__c": true,
        "CustomField3__c": 18,
        "CustomField4__c": "2024-09-15",
        "CustomField5__c": 1560.75,
        "CustomField6__c": "Gold",
        "CustomField7__c": false,
        "CustomField8__c": "2024-01-10T09:15:00.000Z",
        "CustomField9__c": "In Progress",
        "CustomField10__c": 155,
        "CustomField11__c": "www.example.com/account/0012x0000345Bcd",
        "CustomField12__c": "Low",
        "CustomField13__c": 100000,
        "CustomField14__c": "2024-12-20",
        "CustomField15__c": "Active"
    },
    {
        "Id": "0012x0000345Cde",
        "Name": "Tyrell Corporation",
        "Type": "Customer",
        "Rating": "Warm",
        "Industry": "Biotechnology",
        "Phone": "1-555-456-7890",
        "Website": "www.tyrellcorp.com",
        "AnnualRevenue": 200000000,
        "NumberOfEmployees": 2000,
        "BillingStreet": "1011 Pine St",
        "BillingCity": "Los Angeles",
        "BillingState": "CA",
        "BillingPostalCode": "90001",
        "BillingCountry": "USA",
        "ShippingStreet": "1011 Pine St",
        "ShippingCity": "Los Angeles",
        "ShippingState": "CA",
        "ShippingPostalCode": "90001",
        "ShippingCountry": "USA",
        "Description": "Tyrell Corporation manufactures bioengineered replicants.",
        "OwnerId": "0052x000005FghI",
        "CreatedDate": "2021-01-20T16:00:00.000Z",
        "LastModifiedDate": "2024-10-04T18:00:00.000Z",
        "CustomField1__c": "High",
        "CustomField2__c": false,
        "CustomField3__c": 50,
        "CustomField4__c": "2024-11-05",
        "CustomField5__c": 500.25,
        "CustomField6__c": "Silver",
        "CustomField7__c": true,
        "CustomField8__c": "2024-05-15T11:45:00.000Z",
        "CustomField9__c": "Cancelled",
        "CustomField10__c": 220,
        "CustomField11__c": "www.example.com/account/0012x0000345Cde",
        "CustomField12__c": "Medium",
        "CustomField13__c": 50000,
        "CustomField14__c": "2025-06-15",
        "CustomField15__c": "Pending"
    }
]
"""

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config={"response_mime_type": "application/json"}
    )

    prompt = """
    Extract values from the following object using the following object metadata and produce
    in a json format. Only output the json object.
    object_to_extract:{object_to_extract}
    object_metadata:{object_metadata}
    """

    sample_account_data_json_list = json.loads(SAMPLE_ACCOUNT_DATA_ONLY_1)
    for sample_account_data_json in sample_account_data_json_list:
        print(f'Extracting result for sample data:{sample_account_data_json}')
        extract_result = model.generate_content(prompt.format(
            object_to_extract=sample_account_data_json,
            object_metadata=sixsense_acccount_schema
        ))
        json_response = extract_result.candidates[0].content.parts[0].text
        print(json_response)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


