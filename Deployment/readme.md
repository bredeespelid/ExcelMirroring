# Deploying Azure Function with Microsoft Graph API Polling

This guide explains how to deploy the Azure Function that polls Microsoft Graph API for Excel files, converts them to Parquet, and uploads them to Azure Blob Storage.

---

## Prerequisites

- An Azure subscription
- Azure Storage Account (with container created)
- Azure Active Directory App Registration (with `Sites.Read.All` and `Files.Read.All` permissions)
- Microsoft Fabric workspace for mirroring (optional but recommended)
- Azure Function Core Tools (for CLI deployment)
- GitHub repository (for CI/CD deployment)

---

## Deployment Options

You can deploy using one of these methods:

1. **Portal Zip Deploy (easiest)** – Ideal for testing or proof of concept
2. **Azure CLI (Function Core Tools)** – Ideal for developer workflows
3. **GitHub Actions CI/CD** – Ideal for production pipelines

---

## 1. Portal Zip Deploy

This is the fastest method to deploy your Azure Function without installing any local tools.

### Steps

1. Go to [Azure Portal](https://portal.azure.com).
2. Navigate to **Function Apps** and click **Create**.
   - **Runtime stack**: Python 3.9
   - **Region**: Select your nearest region
   - **Hosting plan**: Consumption (Serverless)
3. Once created, open the Function App and go to **Deployment Center**.
4. Select **Zip Deploy**.
5. Zip your function app folder:
   - Navigate to `src/GraphPollingFunction`
   - Create a zip file containing all contents of this folder (not the folder itself).
6. Upload the zip file in Deployment Center.
7. Configure Application Settings:
   - Go to **Configuration** → **Application settings**
   - Add the following keys and values from your AppConfig.py:
     - `tenant_id`
     - `client_id`
     - `client_secret`
     - `site_id`
     - `drive_id`
     - `blob_connection_string`
     - `blob_container_name`
8. Save and restart the Function App.

The function is now live and will execute every 5 minutes.

---

## 2. Azure CLI (Function Core Tools)

This method requires local development tools but gives you more control.

### Install tools
```bash
npm install -g azure-functions-core-tools@4 --unsafe-perm true
