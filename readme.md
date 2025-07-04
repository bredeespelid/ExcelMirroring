# Excel Mirroring

Excel Mirroring is a proof-of-concept project for automatically monitoring a folder for Excel files, converting them to Parquet format, and uploading them to Microsoft Fabric OneLake using AZCopy.

This repository is intended as a personal project and should not be considered production-ready.

## Overview

The application monitors a configured folder for new or modified Excel files. Once a file is detected, it:

1. Converts the Excel file into a DataTable using EPPlus.
2. Exports the DataTable as a Parquet file using ParquetSharp.
3. Uploads the Parquet file to OneLake via AZCopy.

## Prerequisites

- .NET 8 SDK
- AZCopy installed and available in PATH
- Service Principal credentials for OneLake access
- Visual Studio 2022 or later (optional)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ExcelMirroring.git
   cd ExcelMirroring
