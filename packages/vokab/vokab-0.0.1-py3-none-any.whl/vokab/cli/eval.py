import csv
import os
from pathlib import Path

import click
from tqdm import tqdm

from vokab import Collection
from vokab.cli import app


@app.command(name="eval")
@click.argument("file_path", type=click.Path(exists=True))
@click.pass_context
def do_eval(ctx, file_path: str):
    """Run fuzzing on a given annotated type."""

    collection: Collection = ctx.obj["collection"]
    file_path = Path(os.path.expanduser(file_path))
    output_path = Path(file_path.with_name(f"{file_path.stem}-output.csv"))
    fieldnames = ["input_text", "output_name", "label", "codes"]

    with file_path.open() as file:
        total_lines = sum(1 for _ in file)

    with open(file_path) as f, open(output_path, "w", newline="") as w:
        f = filter(None, map(str.strip, f))
        reader = csv.DictReader(f)

        writer = csv.DictWriter(w, fieldnames=fieldnames)
        writer.writeheader()

        record: dict
        with tqdm(reader, total=total_lines, unit="rows") as progress:
            for record in progress:
                input_text = record.get("input_text")
                response = collection(input_text)

                if response.match:
                    record["output_name"] = response.match.name
                    record["label"] = response.match.label

                    if response.match.codes:
                        codes = response.match.codes.split(",")
                        record["codes"] = "\n".join(codes)

                writer.writerow(record)

    click.echo(f"Results saved to {output_path}")
