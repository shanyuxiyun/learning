#!/bin/bash

# remove blink line
cat -s text.sh
cat text.sh | tr -s '\n'
