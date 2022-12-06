# DigitalDivide
Digital Divide is a continuous software developed by mutliple classes in Valencia College's CTSD program. Focused on branching the divide between the people of Orlando and technology, the software is designed to pull geojson census data (that must be added personally into the assets) and then filter it to create workable data to display on a map. 

## Project Goals

- [ ] Add issues to put in project goals :tada:

## Installation Guide

1. Ensure that Python is installed on your PC and set as a path variable.

2. Run the InstallDashPlotly.bat file to pip install Dash, Plotly, and Plotly Express. 
    - **RUN .BAT AS ADMINISTRATOR**  You can also install them individually using the developers documents if you do not want to use a .bat file.

3. Run main.py from the terminal

4. Follow the instructions on the new terminal window that appears and navigate to the opened port in your web browser.
    - i.e. 127.0.0.1:8050 in Google Chrome

### Requirement Notes
Using PyTest for application testing. Refer to the developer documentationg for detailed instructions.

https://docs.pytest.org/en/7.2.x/

As of the current version of this software, you must be using Windows, Linux, or a Windows VM within Mac to run this cross platform.

# Conversion to .exe

1. You can use Pyinstaller to convert this app to an executable file. 

https://pyinstaller.org/en/stable/

2. Towards the end of AppMainFolder/main.py, you will see the following lines:

if __name__ == '__main__':
    app.run_server(debug=False)
    
Debug must be set to False, otherwise an exception will be thrown.

4. In AppMainFolder, open the command prompt and use the following command:

pyinstaller --onefile --add-data "assets/;assets" main.py

3. The .exe will show up in 'dist/', where the 'backend_resources' folder will need to be included for the executable to run.
Note: this will generate some build files in the directory. See the Pyinstaller documentation for more information.

Below is a link to an example of a generated .exe.
https://drive.google.com/file/d/1IjPDVcuupHaSgnT8uvv6i2utvl_faqTn/view?usp=share_link
