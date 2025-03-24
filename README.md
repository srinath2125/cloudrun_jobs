# cloudrun_jobs
create a python script for taking mongodb backup for (mongodump) -- [ backup.py ]
create a docker file for this python script [ Dockerfile ]
check python script in local using comand  [ pyton3 backup.py ]
build the docker image in local  using [ docker build -t mongo-backup1 . ]
run the docker for the image in local  using [ docker run --env-file .env mongo-backup1 ]
check the logs for docker using  [ docker logs < container_id or container_name > ]
push the docker image to gcr.io in Artifact registory [ docker tag mongo-backup1 gcr.io/PROJECT ID/mongo-backup1:latest ] && [ docker push gcr.io/vpc-peering-453205/mongo-backup1:latest ]
Run the cloud run jobs --> cloud run Jobs ---> select on Delpoy container ---> select the docker image from gcr.io in Artifact registory. ---->fill the required detials and click on create.
Execute the cloud run jobs 
check the logs---------working fine  
Once everything is working fine and cloud run job is success then schedule it as per needed uing the triggers option in cloudrun.
