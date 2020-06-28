#!/usr/bin/env bash

# assume pipenv installed
export PACKAGE_FILE=fastapi-cdk-example-lambda-package.zip

rm -rf $PACKAGE_FILE
zip $PACKAGE_FILE main.py
zip -r9 $PACKAGE_FILE src
zip -r9 $PACKAGE_FILE data
pipenv lock -r > requirements.txt
pip install -r requirements.txt --no-cache-dir --target package
cd package
zip -r9 ../$PACKAGE_FILE .
cd ..
aws s3 cp $PACKAGE_FILE s3://fastapi-cdk-bucket
rm -rf package
rm -rf requirements.txt