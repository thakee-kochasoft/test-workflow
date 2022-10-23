#!/bin/bash

bucket_name=thakee-client-3

ibmcloud cos bucket-head --bucket $bucket_name --region us-east

if [ $? -eq 0 ]; then
    echo OK bucket exists
else
    echo FAIL bucket not exists
fi
