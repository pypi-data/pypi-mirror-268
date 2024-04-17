# Vizibridge

This module is a [maturin](https://www.maturin.rs/) bridge between the rust crate [vizicomp](https://gitlab.inria.fr/cpaperma/vizicomp)
containing compiled code for efficient genomic data manipulation in the Python module [Vizitig](https://gitlab.inria.fr/pydisk/examples/vizitig/)

## How to install vizibrdige

The simplest way is to use `pip` as `vizibridge` is deploy in Pypi:

```bash
pip install vizibridge
```

Alternative, download the wheel from the [latest release obtained from gitlab](https://gitlab.inria.fr/cpaperma/vizibridge/-/releases/permalink/latest)

In the case where your architecture/systems is not presents, it is possible to compile it locally as well as follows.

First install the [rust tool chain](https://www.rust-lang.org) and then run 

```bash
cargo install maturin
maturin build --release
```

To install the module in your python then run

```bash
pip install target/wheels/vizibridge**.whl
``` 
replacing `**` by the appropriate name generated in the folder.


## How-to modifiate this  https://gitlab.inria.fr/cpaperma/vizibridge/-/releases/permalink/latestmodule

The CI/CD takes care to compiling everything so you can simply push the content to create a new compiled module.
To publish to Pypi, simply push a release tag:

```bash
git tag -d vx -m "Some description of the release to broadcast
git push origin vx 
``` 

Here `vx` is the version number that should be sync with the version declared in the `Cargo.toml`.

## What should be here

The actual computing content should never been performed within this repo but
always either in `vizicomp` repo or through another repo that we would like to
have exposed in the Python ecosystem.  This repo is **solely** dedicated to
performing the bridge without polluting efficient standalone Rust tooling.

## TODO

- Add in the CI/CD windows and MacOS compilations
- Integrate ggcat binding
- Other tools?
