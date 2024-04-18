# Changelog

## 1.0.1 (2024-04-18)
Minor fixes and suggestions from CPC reviewers.

### CLI
- Add `check` command to verify the installation of AutoEFT (!3)
- Add `--no_hc` option to `construct` command to prevent the explicit construction of conjugate operator types (!3)
- Add `--no_hc` option to `count` command to prevent the implicit counting of conjugate operator types (!3)
- Add `--name` option to `construct` command to set a custom EFT name (!3)

### Model file
- If a field has at least one complex representation or an odd number of pseudo-real representations it is assumed to be *complex* by default. This can be overwritten by setting the `conjugate` property in the model file. (!3)

### Bug fixes
- Temporary files are created with `.tmp` suffix (!2)

## 1.0.0 (2023-09-28)
Initial release.
