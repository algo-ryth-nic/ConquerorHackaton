# DERMA360 Server Code
This is the API interface that our frontend will talk too.  
It's nothing but a simple flask application that will host the trained models. 
It's deployed as a docker container due to compatiblity issues with tensorflow in the cloud. The frontend will hit the endpoint to get back the results. 