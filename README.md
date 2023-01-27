# run_delft_python
Script to run Deltares D-Flow Flexible Mesh in python, in different time scale. 
Here the outputs are at daily and monthly scale, using restart files.  


########################### RUN MODEL ###########################

Run model using python

You will required:

	- script 'run_delft.py'
	- FlowFM_temp.mdu
	- run.bat

The model will not run without those three files. They need to be at the simulation folder.
In case you are using the Delft-Flexible Mesh version (https://www.deltares.nl/en/software/delft3d-flexible-mesh-suite/), 
you need to put the files at a path like this:

example: 'D:\YourPath\Project1.dsproj_data\FlowFM\'

The run.bat file also require some modifications. 
You need to add your exe software folder path to the run.bat, 
example: 

	"C:\Program Files (x86)\Deltares\Delft3D FM Suite 2019.01 HMWQ (1.5.1.41875)\plugins\DeltaShell.Dimr\kernels\x64\dflowfm\bin\dflowfm-cli.exe" --autostart FlowFM.mdu

In the 'FlowFM_temp.mdu', you can change your model parameters, as NetFile, map, his and rst interval. 
This is up to you to change according to your model necessities, however, it is required to keep:

	RefDate           = RefDate_replace
	TStop             = TStop_replace
	RestartFile       = RestartFile_replace
	HisFile           = His_File_replace
	MapFile           = MapFile_replace

In the script 'run_delft.py', you can change the definition of these keywords, so don't forget to change this file. 

After these alterations, using Anaconda Prompt, use command lines  to start the simulation:

	C: 				(choose your working disk)

	cd C:\Your\Simulation\Path	(this will leave you in your simulation folder)

	python run_delft.py		(this will run your simulation)
