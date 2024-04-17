# azure-key-vault-report

## Description
Generates **Markup tables**, in plain text format, of secrets in the specified Key Vaults.   

### Summary table
Includes stats about the records in the specified Key Vaults.   

### Report table
A table with more info about each record.   

This table is sorted (from top to bottom) by:
  - the oldest `Expiration` date, then by
  - the oldest `Last Updated` date

This table also contains a `Comment` columns, which may include info about:
  - Days to when the secret will expire
  - Days since the secret expired
  - Info if the secret has no expiration date set
  - Days since the Secret was last updated

### MS Teams json payload
A json payload (MS Teams) with the report(s) included as a html table may also be generated.   
The MS Team payload will use the following base template:   
```
{
  "@type": "MessageCard",
  "@context": "http://schema.org/extensions",
  "themeColor": "0076D7",
  "summary": "-",
  "sections": [
    {
      "activityTitle": "<TITLE>",
      "activitySubtitle": "",
      "activityImage": "",
      "facts": [],
      "markdown": true
    },
    {
      "startGroup": true,
      "text": "<TEXT>"
    }
  ]
}
```
- `activityTitle` will contain the value of the provided `title`  
- `facts` will contain the rows from the summary table   
- `text` may contain additional data. Defaults to a html table

## Installation
`pip install ops-py-azure-key-vault-report`

## Usage
The `azure_key_vault_report` object must be initialized with the json output of one more `az keyvault` list commands.  
Please refer to the code documentation provided in the `az_cmd.py` file.    

Example code:
```
#!/usr/bin/env python

import os
from azure_key_vault_report import az_cmd
from azure_key_vault_report import azure_key_vault_report

vaults = ["kv-qa"]
record_types = "secret"        
#record_types = "secret key"  # valid record types are: "secret key certficate"

results = []
for vault in vaults:
  results += az_cmd.az_cmd(vault, record_types)

# The azure_key_vault_report object is initialized with the json output of the `az keyvault` list commands.
kv_report = azure_key_vault_report.AzureKeyVaultReport(results)

# Parse the result
kv_report.parse_results()

# Create the summary markdown table and print it to standard output
kv_report.add_summary()
summary = kv_report.get_markdown_summary()
print(summary)

# Create the report markdown table and print it to standard output
# This table is customized by provided arguments
kv_report.add_report()
report = kv_report.get_markdown_report_only()
print(report)

# The get_markdown_report method will return both the summary table and report table
full_report = kv_report.get_markdown_report()
print(full_report)

# Create a report table including all records
kv_report.add_report(include_all=True)
full_report = kv_report.get_markdown_report()
print(full_report)

## Create a MS Teams payload output including html table
kv_report.add_report(teams_json=True)
ms_payload = kv_report.get_teams_payload("Title of the message")
print(ms_payload)
```

Note that the specified `kv-qa` Key Vault in the code example above is just a made up fictive Key Vault, as are the record names.   
If the `kv-qa` existed and the records, the output might have looked like the following output:  
```
| Summary                                  | Comment |
|------------------------------------------|---------|
| Total number of vaults                   |       1 |
| Total number of records                  |      15 |
| Records missing Expiration Date          |      14 |
| Records updated in the last year         |       6 |
| Records NOT updated in the last year     |       5 |
| Records NOT updated for the last 2 years |       2 |
| Records NOT updated for the last 3 years |       2 |

| Record Name | Record Type | Vault Name | Last Updated | Expiration | Comment                                       |
|-------------|-------------|------------|--------------|------------|-----------------------------------------------|
| LicenseKey  | secret      | kv-qa      | 2023-12-11   | 2024-12-26 | Will expire in 314 days. Updated 67 days ago. |

| Summary                                  | Comment |
|------------------------------------------|---------|
| Total number of vaults                   |       1 |
| Total number of records                  |      15 |
| Records missing Expiration Date          |      14 |
| Records updated in the last year         |       6 |
| Records NOT updated in the last year     |       5 |
| Records NOT updated for the last 2 years |       2 |
| Records NOT updated for the last 3 years |       2 |


| Record Name | Record Type | Vault Name | Last Updated | Expiration | Comment                                       |
|-------------|-------------|------------|--------------|------------|-----------------------------------------------|
| LicenseKey  | secret      | kv-qa      | 2023-12-11   | 2024-12-26 | Will expire in 314 days. Updated 67 days ago. |

| Summary                                  | Comment |
|------------------------------------------|---------|
| Total number of vaults                   |       1 |
| Total number of records                  |      15 |
| Records missing Expiration Date          |      14 |
| Records updated in the last year         |       6 |
| Records NOT updated in the last year     |       5 |
| Records NOT updated for the last 2 years |       2 |
| Records NOT updated for the last 3 years |       2 |


| Record Name      | Record Type | Vault Name | Last Updated | Expiration | Comment                                        |
|------------------|-------------|------------|--------------|------------|------------------------------------------------|
| LicenseKey       | secret      | kv-qa      | 2023-12-11   | 2024-12-26 | Will expire in 314 days. Updated 67 days ago.  |
| ConnectionString | secret      | kv-qa      | 2020-10-12   |            | Has no expiration date. Updated 1222 days ago. |
| ApplicationKey   | secret      | kv-qa      | 2020-10-22   |            | Has no expiration date. Updated 1212 days ago. |
| MaintenanceKey   | secret      | kv-qa      | 2021-10-15   |            | Has no expiration date. Updated 854 days ago.  |
| ApimKey          | secret      | kv-qa      | 2021-10-27   |            | Has no expiration date. Updated 842 days ago.  |
| TestBearerToken  | secret      | kv-qa      | 2022-05-02   |            | Has no expiration date. Updated 655 days ago.  |
| ClientId         | secret      | kv-qa      | 2022-06-09   |            | Has no expiration date. Updated 617 days ago.  |
| EmailPassword    | secret      | kv-qa      | 2022-06-17   |            | Has no expiration date. Updated 609 days ago.  |
| AzureString      | secret      | kv-qa      | 2022-06-24   |            | Has no expiration date. Updated 602 days ago.  |
| SubscriptionKey  | secret      | kv-qa      | 2022-12-02   |            | Has no expiration date. Updated 441 days ago.  |
| ApiToken         | secret      | kv-qa      | 2023-04-11   |            | Has no expiration date. Updated 311 days ago.  |
| Secret           | secret      | kv-qa      | 2023-06-01   |            | Has no expiration date. Updated 260 days ago.  |
| MyClientSecret   | secret      | kv-qa      | 2023-06-08   |            | Has no expiration date. Updated 253 days ago.  |
| SubscriptionKey  | secret      | kv-qa      | 2023-08-24   |            | Has no expiration date. Updated 176 days ago.  |
| ApiSnKey         | secret      | kv-qa      | 2023-09-08   |            | Has no expiration date. Updated 161 days ago.  |

{"@type": "MessageCard", "@context": "http://schema.org/extensions", "themeColor": "0076D7", "summary": "-", "sections": [{"activityTitle": "Title of the message", "activitySubtitle": "", "activityImage": "", "facts": [{"name": "Total number of Key Vaults:", "value": 1}, {"name": "Total number of records:", "value": 15}, {"name": "Records missing Expiration Date:", "value": 14}, {"name": "Records updated in the last year:", "value": 6}, {"name": "Records NOT updated in the last year:", "value": 5}, {"name": "Records NOT updated for the last 2 years:", "value": 2}, {"name": "Records NOT updated for the last 3 years:", "value": 2}], "markdown": true}, {"startGroup": true, "text": "<table bordercolor='black' border='2'>    <thead>    <tr style='background-color : Teal; color: White'>        <th>Record Name</th>        <th>Record Type</th>        <th>Vault Name</th>        <th>Last Updated</th>        <th>Expiration</th>        <th>Comment</th>    </tr>    </thead>    <tbody>    <tr><td>LicenseKey</td><td>secret</td><td>kv-qa</td><td>2023-12-11</td><td>2024-12-26</td><td>Will expire in 314 days<br>Updated 67 days ago<br></td></tr></tbody></table>"}]}
```

## Arguments

### add_report()
This method accepts the following arguments:

- `expire_threshold` : `int`  
  Ignore to report the record if days till the secret will expire are more than specified value.  
  **NOTE:** Secrets expiring **today** or has **already expired** will always be reported.  
  Default: `None`


- `ignore_no_expiration` : `bool`  
  Report all records if set to `False`. If set to `True` only secrets with a `Expiration Date` set will be reported.  
  Default: `True`

 
- `include_all` : `bool`  
  If set to `True` all records are included in the output.  
  Default: `False`   

 
- `teams_json` : `bool`  
  If set to `True` a html table will also be generated which might be used in the MS Teams payload.    
  Default: `False`   


### get_teams_payload()
This method accepts the following arguments:

- `title` : txt   
  The `activityTitle` of the payload.


- `text` : txt  
  Additional text. Default to the generated html table.  
