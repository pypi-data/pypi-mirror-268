import typing as T
import json
import uuid

import typer
from rich.console import Console
from rich.table import Table
from rich.progress import track
import httpx
from pydantic import BaseModel

err_console = Console(stderr=True)
console = Console()


app = typer.Typer(no_args_is_help=True)


def valid_input(schema: dict, input: dict) -> bool:
    # TODO
    if False:
        console.print("[bold red]Error: invalid schema!")
        return False
    return True


class StepResult(BaseModel):
    time_took_ms: int

    result: dict | None = None

    exception_str: str | None = None
    result_text: str | None = None


@app.command()
def run(
    *,
    json_file: T.Annotated[
        T.Optional[str], typer.Option(help="Path to the JSON file to run.")
    ] = None,
    json_string: T.Annotated[
        T.Optional[str], typer.Option(help="JSON string to run.")
    ] = None,
    output_length: T.Annotated[
        T.Optional[int],
        typer.Option(
            help("Number of characters to print for the output of each step.")
        ),
    ] = 200,
):
    """
    Provide either a --json_file or a --json_string to run.
    """
    if not json_file and not json_string:
        err_console.print(
            "[bold red]Error:[/bold red] Please provide either [green]--json_file[/green] or [green]--json_string[/green]."
        )
        return
    if json_file and json_string:
        err_console.print(
            "[bold red]Error:[/bold red] Please provide either [green]--json_file[/green] or [green]--json_string[/green], not both."
        )
        return
    if json_file:
        with open(json_file, "r") as f:
            steps_j = json.loads(f.read())
    else:
        steps_j = json.loads(json_string)
    result_by_step: dict[str, StepResult] = {}
    for step in track(steps_j["steps"], description="Running steps..."):
        console.log(f"running step {step['id']}")
        # confirm the input types conform to the plugins inputSchema
        input = step["input"]
        plugin = steps_j["plugins"][step["pluginId"]]
        input_schema = plugin["inputSchema"]
        valid_input(schema=input_schema, input=input)
        r = httpx.post(
            url=plugin["execute"],
            json=input,
            headers={
                "x-whitecloak-run-id": str(uuid.uuid4()),
                "x-whitecloak-step-id": step["id"],
            },
            timeout=60,
        )
        time_took_ms = int(r.elapsed.total_seconds() * 1_000)
        try:
            step_j = r.json()
            step_result = StepResult(time_took_ms=time_took_ms, result=step_j)
        except Exception as e:
            step_result = StepResult(
                time_took_ms=time_took_ms, result_text=r.text, exception_str=str(e)
            )
        result_by_step[step["id"]] = step_result
    table = Table("Step Id", "Latency (ms)", "Result")
    for step_id, step_result in result_by_step.items():
        table.add_row(
            step_id,
            str(step_result.time_took_ms),
            json.dumps(step_result.result)[0:output_length],
        )
    console.print(table)


@app.command()
def hi():
    console.print("hi")


if __name__ == "__main__":
    app()
