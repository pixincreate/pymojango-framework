"""
This file is important. Deleting this file will stop you from connecting to the MongoDB_Atlas unless you replace the
complete uri which is fed to the MongoClient().
Give the user AtlasAdmin permission to avoid *Errors* by following the below given steps:
- Head to https://cloud.mongodb.com (your Database Deployment page)
- Security > Database Access
- Click on *Edit* button under the *Actions* for the user.
- Scroll down to Database *User Privileges* > Built-in Role.
- Select Atlas Admin > Update user (green box below)
- Now, you should see atlasAdmin@admin under MongoDB Roles
"""

username = ""
password = ""
atlas_cluster_name = ""
