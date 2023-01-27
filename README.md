# run_delft_python
Script to run Deltares D-Flow Flexible Mesh in python, in different time scale (daily and monthly)

########################### RUN MODEL ###########################
Run model using python

You will required:

	- script 'run_delft.py'
	- FlowFM_temp.mdu
	- run.bat

The model will not run without those three files. They need to be at the simulation folder.
In case you are using the Delft-FM version (owned by LAPMAR), 
you need to put the files at a path like this:

example: 'D:\YourPath\Project1.dsproj_data\FlowFM\'

The run.bat file also require some modifications. 
You need to add your exe software folder path to the run.bat, 
example: 

"C:\Program Files (x86)\Deltares\Delft3D FM Suite 2019.01 HMWQ (1.5.1.41875)\plugins\DeltaShell.Dimr\kernels\x64\dflowfm\bin\dflowfm-cli.exe" --autostart FlowFM.mdu

After these alterations, using Anaconda Prompt, 
use command lines  to start the simulation:

C: (choose your working disk)

cd C:\Your\Simulation\Path    (this will leave you in your simulation folder)

python run_delft.py		(this will run your simulation)
