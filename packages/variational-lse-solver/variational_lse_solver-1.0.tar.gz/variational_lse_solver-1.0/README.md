# Variational-LSE-Solver

This repo contains the code for the PennyLane-based `variational-lse-solver` library introduced in 
"Comprehensive Library of Variational LSE Solvers", N. Meyer et al. (2024).

## Setup and Installation

The library requires an installation of `python 3.12`, and following libraries:
- `pennylane~=0.34`
- `torch~=2.1.2`
- `tqdm~=4.66.2`

We recommend setting up a conda environment:

```
conda create --name ENV_NAME python=3.12
conda activate ENV_NAME
```

The package `variational-lse-solver` can be installed locally via:
```
pip install variational-lse-solver
```

## Usage and Further Information

For further usage details and examples please refer to the repository https://github.com/nicomeyer96/variational-lse-solver

## Acknowledgements

The `variational-lse-solver` library is mostly based on the techniques introduced in
["Variational Quantum Linear Solver", C. Bravo-Prieto et al., Quantum 7, 1188 (2023)](https://quantum-journal.org/papers/q-2023-11-22-1188/).

The concept of using dynamically growing circuits is inspired by
["Variational quantum linear solver with a dynamic ansatz", H. Patil et al., Phys. Rev. A 105, 012423 (2022)](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.105.012423)

There are some alternative implementations of subroutines provided by `variational-lse-solver` in the PennyLane Demos:
- https://pennylane.ai/qml/demos/tutorial_vqls/
- https://pennylane.ai/qml/demos/tutorial_coherent_vqls/

However, those realisations contain several hard-coded parts and can not be used for arbitrary problems out of the box.
Furthermore, we identified some small inaccuracies, which might lead to converging to a wrong solution 
-- this is explained in more detail in the documentation of `variational-lse-solver`.

## Citation

If you use the `variational-lse-solver` or results from the paper, please cite
"Comprehensive Library of Variational LSE Solvers", N. Meyer et al. (2024).

## Version History

Initial release (v1.0): April 2024

## License

Apache 2.0 License
  