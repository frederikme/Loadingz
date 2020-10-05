# Loadingz
Loadingbar that can display a loading process.</br>
**Now available on** ***[PyPi](https://pypi.org/project/loadingz/)***.

## Install Loadingz using pip
```
pip install loadingz
```

## Usage
```
from loadingz import Loadingbar

# let's say you have to iterate through some data
data = [elem_one, elem_two, ...]

loadingbar = Loadingbar(length_of_loop=len(data))

for index in range(len(data)):
    # Handle your data here
    element = data[index]
    
    # update loadingbar 
    loadingbar.update(index)
```
## Demo
<img src="https://user-images.githubusercontent.com/60892381/95025533-acd7a800-068a-11eb-9537-b4ab7cfd536e.gif"></img>
