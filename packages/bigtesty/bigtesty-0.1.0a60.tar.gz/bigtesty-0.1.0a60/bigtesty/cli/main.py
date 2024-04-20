import typer
from typing_extensions import Annotated

from bigtesty.infra.launch_tests_ephemeral_infra import launch_tests_ephemeral_infra

app = typer.Typer()


@app.command("test")
def run_tests(root_test_folder: Annotated[str, typer.Option("--root-test-folder")],
              root_tables_folder: Annotated[str, typer.Option("--root-tables-folder")],
              tables_config_file_path: Annotated[str, typer.Option("--tables-config-file")],
              destroy_ephemeral_infra: Annotated[bool, typer.Option("--tables-config-file")] = True):
    print(f"####################### The CLI is invoked with params : ")

    print(f"root_test_folder : {root_test_folder}")
    print(f"root_tables_folder : {root_tables_folder}")
    print(f"tables_config_file_path : {tables_config_file_path}")
    print(f"destroy_ephemeral_infra : {destroy_ephemeral_infra}")

    launch_tests_ephemeral_infra(
        root_test_folder=root_test_folder,
        root_tables_folder=root_tables_folder,
        tables_config_file_path=tables_config_file_path,
        destroy_ephemeral_infra=destroy_ephemeral_infra
    )


@app.command("info")
def display_bigtesty_info():
    print("BigTesty is an integration testing framework for BigQuery")


def run():
    app()
