# Azure Function – Microsoft Graph API Polling

This project is an **Azure Function** that polls Microsoft Graph API every 5 minutes to:

- Retrieve Excel files from a SharePoint or OneDrive folder
- Convert them to Parquet format
- Upload them to Azure Blob Storage (or OneLake)

It is designed for environments where multiple users (e.g., store managers, accountants) work with Excel files in Microsoft 365.

---

## 🚀 Features

- Polls SharePoint/OneDrive folder for new or updated `.xlsx` files
- Converts Excel files to **Parquet** using Pandas
- Uploads Parquet files to Azure Blob Storage
- Designed for Azure Function Consumption Plan (low-cost, serverless)
- Handles multiple users updating files simultaneously

---

## 📖 Process Overview

**User perspective:**

1. Users add or modify Excel files in a shared SharePoint/OneDrive folder.
2. Azure Function runs every 5 minutes.
3. Function:
   - Fetches new/changed files using Microsoft Graph API
   - Converts Excel to Parquet
   - Uploads them to Azure Blob Storage
4. Accountants and analysts can access consolidated Parquet data for Power BI or analytics.

---

## ✅ Prerequisites

- Azure Subscription
- Azure Storage Account
- Azure Active Directory App Registration with API permissions
- Python 3.9+ (for local development)
- Azure Functions Core Tools (for deployment)

---

## 🛠 Configuration

Edit `src/GraphPollingFunction/Config/AppConfig.py`:

```python
config = {
    "tenant_id": "<your-tenant-id>",
    "client_id": "<your-client-id>",
    "client_secret": "<your-client-secret>",
    "site_id": "<sharepoint-site-id>",
    "drive_id": "<drive-id>",
    "folder_path": "/Regnskap",  # Path to folder to monitor
    "blob_connection_string": "<azure-blob-connection-string>",
    "blob_container_name": "regnskap-parquet"
}


### 🔑 How to get these values

| Key                    | How to get it                                                                                                                                              |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `tenant_id`            | Azure Portal → Azure Active Directory → Overview → Directory (tenant) ID                                                                                   |
| `client_id`            | Azure Portal → Azure AD → App Registrations → Select your app → Application (client) ID                                                                    |
| `client_secret`        | Azure Portal → Azure AD → App Registrations → Certificates & Secrets → New client secret                                                                   |
| `site_id`              | Use Microsoft Graph Explorer: `GET https://graph.microsoft.com/v1.0/sites/<tenant>.sharepoint.com:/sites/<site-name>`Copy the `id` field from the response |
| `drive_id`             | Use Graph Explorer:`GET https://graph.microsoft.com/v1.0/sites/<site-id>/drives`Copy the `id` field for the document library (usually "Documents")         |
| `folder_path`          | The relative path to the folder in SharePoint or OneDrive (e.g., `/Files`)                                                                                 |
| `blob_connection_string`| Azure Portal → Storage Account → Access keys → Connection string                                                                                          |
| `blob_container_name`  | Azure Portal → Storage Account → Containers → Your container name (e.g., `files-parquet`)                                                                  |

```

