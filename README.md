# Review Rating Summary

Aggregate whole-star review ratings into per-business counts, averages, and histograms.

Uses Python 3.10+ and its standard library only. No package installation, virtual
environment, external server, Redis, Celery, or network access is required.

## Run

```console
python -m reviews_lab --help
python -m reviews_lab examples/sample.json
python -m reviews_lab --check-fixtures fixtures/cases.jsonl
python generate_fixtures.py --count 20
python -m unittest discover -s tests -v
```

Run from this directory. The optional path defaults to `-`, which reads JSON from
stdin. Output is JSON or a fixture-check summary. Exit codes are 0 success,
1 file failure, and 2 invalid input. Examples and fixtures contain generated data.

Input is a list of records with positive integer business_id and whole-star integer rating from 1 through 5. Results sort by business ID and include a count, average rounded to two decimals, and a five-bin histogram. Empty input yields an empty list. This does not implement MapReduce or collect real reviews.

## Learning focus

The roadmap's synthetic review-data aggregation and early backend data-processing exercises. This is an independent concept exercise based on the modeled
roadmap. It makes no claim to be employer-owned or period-authentic production code.

## Structure

- `reviews_lab/core.py`: validated parsing, storage, or state transitions.
- `reviews_lab/cli.py`: JSON command interface.
- `reviews_lab/generate_fixtures.py`: original deterministic validation cases.
- `reviews_lab/fixture_check.py`: expected-output/error checks.
- `fixtures/cases.jsonl`: 367 generated cases, with explicit descriptions.
- `tests/`: independently selected boundaries and the complete corpus check.

Branches `feature/core`, `feature/cli`, `data/fixtures`, and `docs/usage` retain
snapshots; `main` contains the complete tool. Dates and provenance are also recorded
in TIMELINE.json. Many data cases share a scenario; they are not separate features.

Keep changes focused, use actual dates for new work, and add a regression test
for changed behavior. Licensed under [MIT](LICENSE).

[History and provenance](HISTORY.md).
