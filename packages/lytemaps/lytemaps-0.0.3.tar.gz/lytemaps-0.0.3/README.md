# `lytemaps`

This repository contains an implementation of a minimal fork of `neuromaps` functionality. If you're an end user, this is likely not for you -- this implementation exists mostly for `hypercoil` developer purposes. As developers, we'd like to use certain `neuromaps` operations without burdening our software with the bulky dependencies (`nilearn`, `sklearn` and Connectome Workbench) that the full install of `neuromaps` requires. This implementation is intended to support the subset of functionality that requires only core Scientific Python packages together with the essential `nibabel` and `pooch` for handling data fetch operations. (But we're not there yet -- in particular, many transforms still require Workbench at this time.) Obviously, functionality here is limited -- inter alia, this means that null models aren't included for now. As development progresses, we'll index the `neuromaps` functions that are implemented below.

If for some reason you still decide to use this repository, please follow the citation prescriptions from [Neuromaps](https://github.com/netneurolab/neuromaps) and [pooch](https://github.com/fatiando/pooch). In particular, specify that you used `lytemaps` in your methods section, specify that `lytemaps` comprises code from `neuromaps` with a `pooch`-based downloader backend, and cite the `neuromaps` and `pooch` papers.

### License

Most code in this repository is taken directly from the `neuromaps` repository, and is therefore licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International Public License. The exception to this is several small utility functions in `src/lytemaps/utils.py` and `src/lytemaps/datasets/utils.py`, which are taken from the `nilearn` and `sklearn` repositories and are therefore licensed under the 3-clause BSD license. As we redevelop code into our own implementations, we will relicense. See the `LICENSE` file for more details.

### Roadmap

- [x] Implement `pooch`-based data fetchers for `neuromaps` datasets
- [ ] Add support for token-based authentication for OSF datasets
- [ ] Add support for querying the `templateflow` API
- [ ] Use `nitransforms` wherever possible for surface-to-surface, volume-to-surface, and surface-to-volume transforms
- [ ] Use neuroimaging tensor library backend for operations originally implemented with `nilearn` and `sklearn`
