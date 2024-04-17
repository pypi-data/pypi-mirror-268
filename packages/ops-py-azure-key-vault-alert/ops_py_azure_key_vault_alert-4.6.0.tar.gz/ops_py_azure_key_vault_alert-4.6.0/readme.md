# azure-key-vault-alert

## Description
Generates a **Key Vault** report table and summary table for one more **Key Vaults** using 
[ops-py-azure-key-vault-report](https://pypi.org/project/ops-py-azure-key-vault-report)

The result is posted to a webhook url (`WEBHOOK_REPORT`).
An additional empty notify may also be post secondary webhook url (`WEBHOOK_NOTIFY`)

The result may be posted to a Slack webhook (Slack App or Slack Workflow) or to MS Teams webhook.  
The post requests are handled by [ops-py-message-handler](https://pypi.org/project/ops-py-message-handler).  

**Slack**  
If the url of the webhook contains `slack.com` the report will be posted to **Slack**.
- **Slack App**   
  If the webhook contains `slack.com/services` a payload for a Slack App will be generated in the following format:
    ```
    {"text": "*title*\n```result```"}
    ```
- **Slack Workflow**   
  If the webhook contains `slack.com`, but not the `slack.com/services` part, a payload for a Slack Workflow will
  be generated. The Workflow will have to be set up to accept a `Title` variable and a `Text` variable.

**MS Teams**
- If the url of the webhook **does not** contain `slack.com` a payload for MS Teams will be generated. The payload will
  also contain a html table of the report (if any). If nothing to report, only a summary will be posted as `facts`.


## Installation
`pip install ops-py-azure-key-vault-alert`

## Usage
Export the webhook url(s) as environment variables:
- `WEBHOOK_REPORT`   
  The result is posted to the value of this webhook. E.g.:  
  `export WEBHOOK_REPORT="https://hooks.slack.com/workflows/T02XYZ..."`


- `WEBHOOK_NOTIFY`  
  When the result has been posted, an additional POST is performed to the value of this webhook. E.g.:  
  `export WEBHOOK_NOTIFY="https://hooks.slack.com/workflows/T02ZYX..."`


Provide the list of Key Vaults after the `-v` / `--vaults`' command line argument (space separated), e.g.:      
`python3 azure_key_vault_alert -v kv-prod kv-dev kv-qa`


**Other valid arguments:**   
`--expire_threshold`     
If this argument is provided and followed by an int value,
the record will only be reported if days to the record's Expiration Date is below the threshold.

`--include_no_expiration`   
If this argument is provided, the report will also include the records which has no `Expiration Date` set.  
The default behavior is simply to ignore the record which does not have a `Expiration Date` set.   

`--include_all`  
If this argument is provided, the report will include all the records (verbose).

`--title`  
The title of the message posted in Slack or MS Teams (Default: Azure Key Vault report)   

`--record_types`  
List of record types to check for. E.g. certificate secret  
Valid types are: certificate secret key (Default is all: certificate secret key)  

`--slack_split_chars` 
If the Slack message is above this value it will be split into multiple posts (default: 3500).  
Each post will then include a maximum of 3500 characters.

`--teams_max_chars`  
The max characters the report can have due to the MS Teams payload size limits (default: 17367).  
If the message is above this threshold then only the facts (summary) will be posted to MS Teams.   
The HTML table will in this case not be included.  

`--stdout_only`  
Only print report to stdout. No POST to the Message Handler