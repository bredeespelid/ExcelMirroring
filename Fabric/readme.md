# Setting up Microsoft Fabric Mirroring for Azure Blob Storage

This guide describes how to configure Microsoft Fabric to automatically mirror Parquet files from Azure Blob Storage into a Lakehouse for analytics.

By completing this setup:
- Any new Parquet files written by the Azure Function will automatically appear in Fabric
- Data will be available for Power BI and SQL-based analytics without manual ETL steps

---

## Prerequisites

Before you start, ensure you have:
- An Azure Blob Storage account containing Parquet files (output from the Azure Function)
- Access to Microsoft Fabric with permissions to create Lakehouses and connections
- A Fabric workspace set up for data engineering
- Your Azure Storage Account Name and Container Name
- Either an Access Key or SAS Token for your Azure Storage account

---

## Process Overview




---

## Step-by-step setup

### 1. Create a Lakehouse in Fabric

1. Log into [Microsoft Fabric](https://app.fabric.microsoft.com).
2. Go to the workspace where you want the Lakehouse.
3. Click "New" and select "Lakehouse".
4. Enter a name for your Lakehouse (for example, `RegnskapLakehouse`).
5. Click "Create".

This Lakehouse will act as the destination where all mirrored data will appear.

---

### 2. Connect Azure Blob Storage to Fabric

1. Open the Lakehouse you just created.
2. Click "Get Data" in the Lakehouse interface.
3. Search for and select "Azure Data Lake Storage Gen2" or "Azure Blob Storage".
4. Click "Connect".

---

### 3. Configure the connection

Provide the required details for your Azure Storage:

- **Storage account name**: The name of your Azure Storage account.
- **Container name**: The name of the container where the Parquet files are stored (for example, `regnskap-parquet`).
- **Folder path**: The folder within the container to monitor. Use `/` for the root or specify a subfolder if needed.
- **Authentication method**: Choose either "Account key" or "SAS token".
  - If using Account key, retrieve it from Azure Portal → Storage Account → Access keys.
  - If using SAS token, create one in Azure Portal → Storage Account → Shared access signature.

After entering these details, click "Next".

---

### 4. Enable mirroring

1. Select "Mirror data" when prompted.
2. Choose the container or folder where your Parquet files are located.
3. Click "Next" to proceed.

This step configures Fabric to continuously watch for new or updated files in the specified folder.

---

### 5. Map the mirrored data to a Lakehouse table

1. Choose the table mapping strategy:
   - Single table: Use this if all Parquet files have the same schema.
   - Multiple tables: Use this if each folder represents a different table with different schemas.
2. Specify the table name (for example, `regnskap_data`).
3. Click "Finish" to complete the setup.

Fabric will now create tables in your Lakehouse and populate them as files arrive.

---

### 6. Test the mirroring

1. Upload a new Parquet file into the Azure Blob Storage container (or let the Azure Function drop one).
2. Wait a few minutes for Fabric to detect the change.
3. Open your Lakehouse and verify that the data appears under the "Tables" section.

---

### 7. Query the data

1. Open SQL analytics within Microsoft Fabric.
2. Run a query to explore the data:
```sql
SELECT TOP 100 * FROM RegnskapLakehouse.regnskap_data;

