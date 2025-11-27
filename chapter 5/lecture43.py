"""Virtual Environment """
import pandas as pd
#create a virtual environment in windows command prompt :
print("python -m venv myenv")
#to activate V-Env:
print("myenv\\Scripts\\Activate")
#to activate V-Env:
print("deactivate")
# Requirements.txt
print("pip freeze > requirements.txt")
#to install requirements
print("pip install -r requirements.txt")
print(pd.__version__)
