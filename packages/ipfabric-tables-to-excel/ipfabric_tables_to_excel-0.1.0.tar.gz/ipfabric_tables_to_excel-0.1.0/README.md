# IP Fabric Tables to Excel

This Command Line Tool is used to convert IP Fabric tables to a single Microsoft Excel file.

# Requirements:

- Python 3.8+
- IP Fabric Python SDK
- IP Fabric API Token or Username/Password

## Set up .env file:
```markdown
cat .env
IPF_TOKEN='mylongtokenstring123456789'
IPF_URL='https://ipfabric.is.awesome'
```

# Installation:

### Pip/PyPI 
    
```shell
pip install ipfabric-tables-to-excel
```

### Local Installation
1. Clone the repository:
```shell
git clone
```
2. Change directory to the repository:
```shell
cd ipfabric-tables-to-excel
```
3. Install the package:
```shell
pip install -r requirements.txt
```

# Usage:

### Poetry

#### Ensure you have Poetry installed:

```shell
pip install -U poetry
```
#### Install the dependencies:

```shell
poetry install
```

#### Run the tool:

```shell
poetry run ipfabric-tables-to-excel --help
```

### Pip/PyPI

#### Run the tool:

```shell
ipfabric-tables-to-excel --help
```

# Examples:
### Poetry

```shell
poetry run ipfabric-tables-to-excel --ipf-tables tables/networks/routes --device_hostname L1EXOS1 --ipf-tables inventory/hosts --device_hostname L21PE192
```
```markdown
🚀 IP Fabric Tables to Excel Exporter! 🚀
Retrieving only running, loading, loaded snapshots. To load all snapshots set `unloaded` to True.
🔄Fetching data for tables/networks/routes...for device L1EXOS1...
🔄Fetching data for tables/networks/routes...for device L21PE192...
🔄Fetching data for inventory/hosts...for device L1EXOS1...
🔄Fetching data for inventory/hosts...for device L21PE192...
Exporting data to excel...
Export complete. Check output.xlsx
👋 Bye!
```

### Pip/PyPI

```shell
ipfabric-tables-to-excel --ipf-tables tables/management/dns/settings --device_hostname L1EXOS1 --ipf-tables inventory/hosts --device_hostname L21PE192
```
```markdown
🚀 IP Fabric Tables to Excel Exporter! 🚀
Retrieving only running, loading, loaded snapshots. To load all snapshots set `unloaded` to True.
🔄Fetching data for tables/management/dns/settings...for device L1EXOS1...
🔄Fetching data for tables/management/dns/settings...for device L21PE192...
🔄Fetching data for inventory/hosts...for device L1EXOS1...
🔄Fetching data for inventory/hosts...for device L21PE192...
Exporting data to excel...
Sheet name L21PE192_management_dns_settings is too long. Truncating to 31 characters.
Export complete. Check output.xlsx
👋 Bye!
```

## Known Limitations
- Not all tables are supported. Only tables with a 'sn' and the 'inventory/hosts' table are supported.
  - Example, `technology/interfaces/connectivity-matrix/connectivity-matrix` is not supported. There is no 'sn' column.
    - This table has both a `local_sn` and `remote_sn` column. This tool only supports tables with a single 'sn' column.
    - This table is curated from `technology/interfaces/connectivity-matrix/unmanaged-neighbors-detail` table which has a 'sn' column.
```shell
ipfabric-tables-to-excel --ipf-tables technology/interfaces/connectivity-matrix/connectivity-matrix --device_hostname L1EXOS1 --ipf-tables technology/interfaces/connectivity-matrix/unmanaged-neighbors-detail --device_hostname L21PE192
```
```markdown
🚀 IP Fabric Tables to Excel Exporter! 🚀
Retrieving only running, loading, loaded snapshots. To load all snapshots set `unloaded` to True.
🔄Fetching data for technology/interfaces/connectivity-matrix/connectivity-matrix...for device L1EXOS1...
Cant fetch data for technology/interfaces/connectivity-matrix/connectivity-matrix.
Error: Client error '422 Unprocessable Entity' for url
'https://sa-eu-demo-main01a.hel1-cloud.ipf.cx/api/v6.7/tables/interfaces/connectivity-matrix?format=%7B%22dataType%22:%22json%22%7D&filters=%7B%22and%22:[%7B%22sn%22:[%22eq%22,%22SIM0
067-0000%22]%7D]%7D&columns=[%22localMedia%22,%22siteName%22,%22id%22,%22remoteInt%22,%22localInt%22,%22remoteHost%22,%22localHost%22,%22protocol%22,%22remoteSn%22,%22remoteMedia%22,%
22localSn%22]&snapshot=4253eade-b1af-4061-ac07-caf84bf0626c'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/422
Does Table technology/interfaces/connectivity-matrix/connectivity-matrix support the filter {'and': [{'sn': ['eq', 'SIM0067-0000']}]}?
🔄Fetching data for technology/interfaces/connectivity-matrix/connectivity-matrix...for device L21PE192...
Cant fetch data for technology/interfaces/connectivity-matrix/connectivity-matrix.
Error: Client error '422 Unprocessable Entity' for url
'https://sa-eu-demo-main01a.hel1-cloud.ipf.cx/api/v6.7/tables/interfaces/connectivity-matrix?format=%7B%22dataType%22:%22json%22%7D&filters=%7B%22and%22:[%7B%22sn%22:[%22eq%22,%227798
8032%22]%7D]%7D&columns=[%22localMedia%22,%22siteName%22,%22id%22,%22remoteInt%22,%22localInt%22,%22remoteHost%22,%22localHost%22,%22protocol%22,%22remoteSn%22,%22remoteMedia%22,%22lo
calSn%22]&snapshot=4253eade-b1af-4061-ac07-caf84bf0626c'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/422
Does Table technology/interfaces/connectivity-matrix/connectivity-matrix support the filter {'and': [{'sn': ['eq', '77988032']}]}?
🔄Fetching data for technology/interfaces/connectivity-matrix/unmanaged-neighbors-detail...for device L1EXOS1...
🔄Fetching data for technology/interfaces/connectivity-matrix/unmanaged-neighbors-detail...for device L21PE192...
Exporting data to excel...
Sheet name L1EXOS1_technology_interfaces_connectivity-matrix_unmanaged-neighbors-detail is too long. Truncating to 31 characters.
Sheet name L21PE192_technology_interfaces_connectivity-matrix_unmanaged-neighbors-detail is too long. Truncating to 31 characters.
Export complete. Check output.xlsx
👋 Bye!
```