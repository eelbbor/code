#!/bin/bash

echo "####################################################"
echo "# Installing dependencies #"
echo "####################################################"
echo

echo "##### Install utilities"
brew install git npm yarn bazelisk

echo "##### Install jdk@17"
brew install openjdk@17
sudo ln -sfn $(brew --prefix)/opt/openjdk@17/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-17.jdk