# tripleten_sprint4

Project Description: 

In this project, we were given a large dataset of both new and used vehicles of all types and brands.  Because the dataset was so large, I decided to subset it, but not before creating a few new important variables of my own.  The original dataset contained a variable named 'model', which actually consisted of both the make and the model.  I decided to rename the 'model' variable to 'make_n_model', and from that, create the variables 'make' and 'model' by splitting it.  From the 'make' variable, I created a dictionary to map the nationality of each car brand into a new column named 'make_country'.  I also used a dictionary to create a numerical variable called 'condition_rank' from the 'condition' variable.  I decided to subset the data into sedans by filtering the 'type' variable.  I then only copied the variables I was interested in looking at into the subset.  Only then did I remove missing values to limit the ammount of data being discarded.  I was able to create visualizations of the average price of sedans by car brand nationality, condition, odometer reading, and model year.  



To view app.py running directly from the GitHub directory, click the following link below:

https://tripleten-sprint4-fjmk.onrender.com/ 



You may also run this app locally on your own machine.  In order to do so, you must first download the contents of this GitHub directory.

Using your Command Prompt / Terminal, you must use the following command line to determine where you default directory is located: 

    cd ./

You then must choose which location you will want to change your directory to.  Let's say you want to place this this tripleten_sprint4 file into your Documents.  You can use the following command line: 

    cd Documents/tripleten_sprint4/

Now that you've change directories, you must now create a vertual emvironment.  Enter the following command line: 

    python<version> -m venv <virtual-environment-name>

To activate the virtual environment, enter the following command line: 

    source <virtual-environment-name>/bin/activate

Now that you have your directory and virtual environment set up, you must now install all the requirements in requirements.txt.  Enter the following command line: 

    pip install -r requirements.txt

Once all the libraries and packages are installerd, you may now pass the following command line into your Command Prompt / Terminal: 

    streamlit run app.py 

You will be given the following link: 

    http://0.0.0.0:10000 

This is an offline link that is running directly from your machine.  

To stop the app from running locally, press ctrl+C into the Terminal.  
