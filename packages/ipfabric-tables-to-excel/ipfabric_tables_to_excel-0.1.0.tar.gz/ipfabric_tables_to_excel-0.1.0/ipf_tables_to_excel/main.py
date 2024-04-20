import argparse
import ipfabric
import random
from rich import print, markdown
import httpx
import pandas as pd


def collect_endpoints(data, endpoints=[]):
    for key, value in data.items():
        if isinstance(value, dict):
            if "endpoint" in value:
                endpoints.append(value["endpoint"])
            collect_endpoints(value, endpoints)
    return endpoints


def main():
    parser = argparse.ArgumentParser(
        description="fetch tables from IP Fabric and insert into a single excel file with multiple sheets"
    )
    print(":rocket: IP Fabric Tables to Excel Exporter! :rocket:")
    ipf = ipfabric.IPFClient()
    ipf_inv_tables_model = ipf.inventory.model_dump()
    ipf_tech_tables_model = ipf.technology.model_dump()
    ipf_tables = list()

    endpoints = collect_endpoints(ipf_tech_tables_model)
    ipf_tables.extend(collect_endpoints(ipf_inv_tables_model))
    ipf_tables.extend(endpoints)
    parser.add_argument(
        "--ipf-tables",
        help="API or Front end URL for IP Fabric tables to fetch. Can be used multiple times.",
        metavar=f"{ipf_tables[random.randint(0, len(ipf_tables))]}",
        nargs="+",
        action="extend",
    )
    parser.add_argument(
        "--device_hostname",
        help="Device Hostname to fetch data for. Can be used multiple times. If not provided, all devices will be used.",
        metavar="device_name",
        nargs="+",
        action="extend",
    )
    parser.add_argument(
        "--print-tables",
        type=bool,
        help="Print first 3 rows of each table fetched",
        default=False,
    )
    args = parser.parse_args()

    dataframes_for_export = list()
    if args.ipf_tables:
        table_filter = None
        for table in args.ipf_tables:
            for device in args.device_hostname:
                if args.device_hostname:
                    table_filter = {
                        "and": [
                            {"sn": ["eq", f"{ipf.devices.by_hostname[device][0].sn}"]}
                        ]
                    }
                print(
                    f":arrows_counterclockwise:Fetching data for {table}...for device {device}..."
                )
                if table_filter and args.device_hostname:
                    if "inventory/hosts" in table or "addressing/hosts" in table:
                        table_filter = {
                            "edges": ["any", "hostname", "like", f"{device}"]
                        }
                try:
                    data = ipf.fetch_all(table, filters=table_filter, export="df")
                    data.title = f"{device}/{table}"
                    dataframes_for_export.append(data)
                except httpx.HTTPStatusError as e:
                    if e.response.status_code == 422:
                        print(f"Cant fetch data for {table}.")
                        print(
                            f"[red]Error:[/red] {e} ",
                        )
                        print(
                            f"Does Table {table} support the filter [underline]{table_filter}[/underline]?"
                        )
                        continue
                    else:
                        print(
                            f"[red]Error:[/red] {e} ",
                        )
                if args.print_tables:
                    print(
                        markdown.Markdown(data.head(3).to_markdown(tablefmt="github"))
                    )
        print("Exporting data to excel...")
        with pd.ExcelWriter("output.xlsx", engine="xlsxwriter") as writer:
            for index, df in enumerate(dataframes_for_export):
                sheet_name = f"{df.title}"
                sheet_name = sheet_name.replace("tables/", "")
                sheet_name = sheet_name.replace("/", "_")
                if len(sheet_name) > 31:
                    print(
                        f"[yellow]Sheet name {sheet_name} is too long.[/yellow] Truncating to 31 characters."
                    )
                    sheet_name = sheet_name[:31]
                df.to_excel(writer, sheet_name=f"{sheet_name}", index=False)
        print("Export complete. Check output.xlsx")
    if not args.ipf_tables:
        print("No tables provided. Exiting...")
    print(":wave: Bye!")


if __name__ == "__main__":
    main()
