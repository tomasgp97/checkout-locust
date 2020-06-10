# Checkout Load and Stress test
This project is just a load and stress tests for the checkout-backend project, framed in the final project for the ACS subject.

## Prerequisites
In order to run this project you must first install [Anaconda](https://www.anaconda.com/products/individual).

## Installation
In order to install all necesary dependencies just run

```conda env create -f environment.yml```

This will create a conda environment named ```checkout-locust```

### For the terminal
To use the new environment in the terminal just type in 

`conda activate checkout-locust` 

After that you should see `(checkout-locust)` before all of your lines.

### For PyCharm
In order to use the environment in PyCharm go to the bottom-right corner of your IDE and look for `Project Interpreter` tab. It is usually at the left of the branches tab.

Click in `Add Intepreter` and and in the pop up window choose `Conda Environment`. Choose `Existing Environment` and configure in the `Interpreter` the next path:

`anaconda3/envs/checkout-locust/bin/python`

This could change but the essence remains and applies for all OS: you have to find the `python` file in the `checkout-locust` environment.

## Usage 
In order to run locust just type in ```locust``` while standing in the project root folder.

This will fire up a locust web server which should be in ```localhost:8089```. 

This will allow you to start new locust swarm

For all tests cases please use as host ```http://127.0.0.1:8080``` where the Spring application will be listening. 
### Test cases
#### Load
For load testing 
#### Stress
For stress testing
