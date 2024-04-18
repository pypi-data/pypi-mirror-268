# Installation
=== "Using Pip" 
    === "Stable"
        1: Install the PyPi package.

        `pip install proton`.
    === "Unstable"
        1. Install git, from [git-scm.org](https://git-scm.org)
        2. Install from source.

        `pip install git+https://github.com/Xanderplayz16/proton.git`.
=== "Manually"
    1. Install git, from [git-scm.org](https://git-scm.org)

    2: Clone the repo from `https://github.com/Xanderplayz16/proton.git`.

    `git clone https://github.com/Xanderplayz16/proton.git && cd proton`

    3: Install the hatch PyPi package.

    `pip install hatch`

    4: Build the project using Hatch.

    `hatch build`

    5: Files should have been created in the `/dist` directory. Install the .whl file via Pip.

    `pip install filename.whl`