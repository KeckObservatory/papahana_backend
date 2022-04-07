#!/bin/bash

python3 -m unittest -v test_instrument_controller.py 
python3 -m unittest -v test_containers_controller.py 
python3 -m unittest -v test_observation_block_controller.py 
python3 -m unittest -v test_semester_id_controller.py 

