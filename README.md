# potato_proj🥔  
A ML project detect the 💉potato early blight and late blight disease.  
🤖

Dataset：  
https://www.kaggle.com/datasets/arjuntejaswi/plant-village?resource=download  

system: windows10 (with **cuda11.3**)

## problems & solutions

- python version higher than **python3.9**, can't find **tensorflow2.5**.  
(some version of tensorflow didn't have tensorflow.keras.layers.experimental.)

- when install pakages, notice the **compatibility** of dependencies and packages.  
Use commands like `pip check`.   

- Encounter cuda problem, when training model.   
Get hint from notebook Browser userInterface:
`Kernel Restarting The kernel for training/training.ipynb appears to have died.It will restart automatically.`
if without any hints else,
try to check the notebook running logs, in CLI, find massage like:
`Could not locate zlibwapi.dll. Please make sure it is in your library path`
so we try to find zlibwapi.dll. From NVIDIA official website below, I get some clues.  
https://forums.developer.nvidia.com/t/zlib-dll-for-latest-cudnn-in-official-install-guide-is-missing/197630/6  
If you can't find file zlibwapi.dll from where they find zlibwapi.dll file directories.
Try to search all the C desk ,u will find a lot of zlibwapi.dll file.
copy any one of them paste it to your directory like `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.3\bin`.
then, restart your kernel try to train again.  

- Working on **FastAPI** error below occur.  
ImportError: cannot import name 'ParamSpec' from 'typing_extensions'.  
Try ```pip uninstall fastapi```and```
pip install --no-cache fastapi```.  

- Docker problems maybe due to the ports num, typos like me   
  **8501:8501\-\->8501:8051**  
  😫😫😫
