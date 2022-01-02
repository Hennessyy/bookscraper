#!/bin/bash
docker-compose up -d --build --remove-orphans --scale app=3
