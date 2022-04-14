#!/bin/bash

if [ ! -f "config.live.yaml" ];
then
  ln -s ../../config.live.yaml config.live.yaml
fi

if [ ! -d "papahana" ];
then
  ln -s ../../papahana papahana
fi

python3 -m unittest -v test_instrument_controller.py 
python3 -m unittest -v test_containers_controller.py 
python3 -m unittest -v test_observation_block_controller.py 
python3 -m unittest -v test_semester_id_controller.py 

