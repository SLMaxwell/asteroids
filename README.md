# `Asteroids`

![Asteroids In Action](./asteroids.gif)

## The Cult Classic
Re-imagined as a Python project using pygame, from the [boot.dev](https://www.boot.dev) site.

## Virtual Environment for Python
To work with this application please follow the flow for Python Vitrual Environments for [venv](https://docs.python.org/3/library/venv.html#venv-def).

### `0.` - Auto switching to Virtual Environment
The MAC is set-up to autoswitch to the listed virtual environment if on is present. This should be indicated by the presence of a Virtual Environment indicator at the leading characters of the prompt:
```
(venv:venv) SLMaxwell68%:asteroids[main] >
```

Should the terminal Prompt NOT show that a virtual environment is present:
```
SLMaxwell68%:asteroids[main] >
```

Follow the needed actions below to activate or create a Virtual Environment.

### `1.` - Creating New (Only needed for New Projects)
To create a new Virtual Environment, navigate to the root of the new application directory. Then run:
  - `py -m venv venv` or
  - `py -m venv .venv`

There is a **_.zshrc alias_** set-up to stub in a new Virtual Environment. It performs the creation, activtion, resetting of the prompt, generation of the requirements.txt file and generation of the .gitignore file and entries to ignore the environment. For this run:
  - `venv-create`
    - Which will default the created directory to "venv".

Or you can specify your venv directory with:
  - `venv-create venv` or
  - `venv-create .venv` or
    
### `2.` - Activating Environment
Do this each time you enter the directory.

To activate the environment so that it is controlling the python version and installed packages, run:
  - `source venv/bin/activate` or 
  - `source .venv/bin/activate` or

Or if the .zshrc is properly set-up simply run:
  - `venv-activate`
    - Which will also re-set the prompt to display correctly.

### `3.` - De-Activating Environment
Do this each time you want to leave the directory.

To Deactivate the environment so that it is controlling the python version and installed packages, run:
  - `deactivate`

Or if the .zshrc is properly set-up simply run:
  - `venv-deactivate`
    - Which will also re-set the prompt to display correctly.

### `4.` - Setting the prompt
Do this each time you want to update the prompt to the current venv activation setting.
  - `set-prompt`

### `4.` - Installing needed python venv dependencies
The purpose of maintaining a virtual environment is to allow the needed dependencies to be easily installed, added or recreated for the project and python version being used.

This is accomplished using the standard of setting the desired requirements within a text file and installing them from that file:
  - **_Ex_**: To make sure that the dependency `pygame version 2.6.1` is installed and active.
    1. Make sure there is a text file created for `pip` installation:
        - `requirements.txt`
    2. Place the follong text into the text file:
        - `pygame==2.6.1`
    3. Run the followng installation command:
        - `pip install -r requirements.txt`

Or use the aliased command:
  - `venv-install`