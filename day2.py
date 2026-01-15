# %% Open the Codespace in your local VS Code

# Terminal display path : /workspaces/DS3021Day2

# %% Create a virtual environment 

# No, you should not include the environment because the other people working on the project can create their own virtual environment using the requirements.txt file. 

# Terminal display path: /workspaces/DS3021Day2
# The terminal display path is not different. 

# %% Viewing Data

import pandas as pd 
df = pd.read_csv("tip.csv")

# %% Extension Management

# The extension menu lists all the extensions I have installed in my local VS Code and in Codespaces. It allows me to search for specific extensions, install new ones, and manage existing ones.

# The Data Wrangler extension allows me to look at the dataset like a spreadsheet in VS Code, gives a summary of the data, and click buttons to transform the data without having to write the code. 

# %% Package managing

# plotly version 6.5.1

# We use a requirements.txt file to specify the packages and versions that are needed for the project, allowing those who fork or clone the repo to easily download and use them. 
