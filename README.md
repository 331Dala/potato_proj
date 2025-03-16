# potato_proj🥔  
A ML project detect the 💉potato early blight and late blight disease.  
🤖

Dataset：  
https://www.kaggle.com/datasets/arjuntejaswi/plant-village?resource=download  

if you used python version higher than python3.9, can't find tensorflow2.5(some of tensorflow didn't have tensorflow.keras.layers.experimental)

when install pakages, notice the depency impactibility
cuda 11.3
windows10


I encounter a cuda problem, when I want to training my model. 
I get hint from notebook:"Kernel Restarting The kernel for training/training.ipynb appears to have died. It will restart automatically." 
and nothing else I jupyter notebook Browser interface.
check the runnig logs in CLI I find a massage said :"ould not locate zlibwapi.dll. Please make sure it is in your library path"
I try to find It from NVIDIA official website, from here 
https://forums.developer.nvidia.com/t/zlib-dll-for-latest-cudnn-in-official-install-guide-is-missing/197630/6
I get some clues.
I can't find file zlibwapi.dll from what they find zlibwapi.dll file.
I search all the C desk ,find lot of zlibwapi.dll file.
pick one of them paste it to your directory may like C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.3\bin
then, restart your kernel try to train again. nice, probelm fixed!

