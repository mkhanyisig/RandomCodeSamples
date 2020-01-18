# ckb_beakerx
Repo for beakerx jupyter notebooks

The beakerx repo has been included as a subtree, to expose the example notebooks when running from conda

# Options to Run

## Easiest Option is Docker

Run this file in the repo.
``` bash
./docker_command.sh
```
This will start a spin up a docker container with a mount to this directory.

## Another Option is to run via Conda


- [conda info](https://www.anaconda.com/distribution/)
- [beakerx install docs](http://beakerx.com/documentation#tutorials-and-examples)

```bash
conda create -y -n beakerx 'python>=3'
#beakerx docs have 'source activate beakerx' but seems like using conda instead of source is now preferred
conda activate beakerx 
```

When running 'conda activate beakerx' you may see:
```bash
$ conda activate beakerx

CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
To initialize your shell, run

    $ conda init <SHELL_NAME>

Currently supported shells are:
  - bash
  - fish
  - tcsh
  - xonsh
  - zsh
  - powershell

See 'conda init --help' for more information and options.

IMPORTANT: You may need to close and restart your shell after running 'conda init'.
``` 

As you can see, it recommending to run 'conda init bash'.
This adds a block of code at the bottom of ~/.bash_profile.

Given that we don't always use conda, I recommend moving this to a separate file like ~/.conda_init.

Then when wanting to use conda

```bash
source ~/.conda_init
conda activate beakerx 
```

Then you can continue with the install form the beakerx site:
```bash
conda config --env --add pinned_packages 'openjdk>8.0.121'
conda install -y -c conda-forge ipywidgets beakerx
```

### Running beakerx via conda after initial install

cd to the dir where you have this repo cloned.

```bash
conda activate beakerx
beakerx
```

A browser should open for the beackerx flavor of the jupyter notebook with this directory visible.

# Issues activating conda for the bash shell

For at least one member of the team, the 'conda init bash' wasn't working, and still resulted in the 
'CommandNotFound' message.  There were various posts on the web also indicating some issues with this
but no clear resolution.  However, switching to zsh and then activating conda was successful at least
for this team member.

```bash
zsh
conda create -y -n beakerx 'python>=3'
conda activate beakerx
conda config --env --add pinned_packages 'openjdk>8.0.121'
conda install -y -c conda-forge ipywidgets beakerx
beakerx
```

# Plotly.js Useage for Graphing

The built in charts in the notebook are great, however, we can't incorporate them in the existing applications.

[Plotly.js](https://plot.ly/javascript/) is a full featured open source library released under the 
[MIT](https://github.com/plotly/plotly.js/blob/master/LICENSE) license.

Plotly is a library that would be easy to integrate with the existing applications.

The GeneJsonBasedExample notebook has an example of formatting some data in groovy and ploting
the data with Plotly.js.


