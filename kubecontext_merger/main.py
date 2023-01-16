import typing as t

import typer

from kubecontext_merger.utils import load_kubecontext, build_kubecontext, save_kubecontext

app = typer.Typer(help="CLI for merging kubectl configs.")


@app.command(name="merge")
def merge_command(
        contexts: t.List[str] = typer.Argument(..., help="Config to be merged"),
        output: str = typer.Option("config", "-o", "--output", show_default=True, help="Output file path"),
):
    contexts_data = []

    for context in contexts:
        contexts_data.append(load_kubecontext(context))

    merged_kubecontext = build_kubecontext(contexts_data)

    save_kubecontext(output, merged_kubecontext)
    print(f'Done. Merged kubecontext file located at "{output}".')
    return
