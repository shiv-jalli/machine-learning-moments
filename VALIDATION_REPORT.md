# Validation Report

This scaffold was validated for public repo consistency.

## Checks performed

- Required top-level files exist.
- `notebooks/core-path/` contains exactly the 17 agreed core-path folders.
- `ROADMAP.md` references each core-path folder using the same path.
- `notebooks/core-path/README.md` lists the same 17 folders.
- `CONTENT_INDEX.md` references only existing core-path folders.
- Mac metadata and local Git metadata are excluded from the release zip.
- The generator script and validator script are included under `scripts/`.

## Result

Validation passed.

## Notes

The `CONTENT_INDEX.md` file contains planned notebook filenames. These notebooks are not expected to exist until their status changes from `Planned` to `Notebook ready` or `Published`.
