[![DOI](https://zenodo.org/badge/727786061.svg)](https://zenodo.org/badge/latestdoi/727786061)

Schema definition for run section in NOMAD.

## Publishing a release

Publishing a GitHub release triggers the **Upload Python Package** workflow.
If publishing fails and the workflow needs fixing, merge the fix into `develop`
and run **Upload Python Package** manually from that branch, supplying the existing
release tag (for example `v1.0.6`) in the `tag` input. The workflow builds the tagged
source with the corrected publishing steps and uploads it to PyPI.

Rerunning the original failed job uses its original workflow revision, so it does
not pick up a workflow fix merged afterward. The manual run avoids moving the
release tag or changing the package version.

## How to cite this work
Ladines, A.N., Daelman, N., Ghiringhelli, L.M., Pizarro, J.M. Rudzinski, J.F., & Scheidgen, M. NOMAD Schema Plugin Run [Computer software]. https://doi.org/10.5281/zenodo.13850738
