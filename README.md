# mahesh_praveen_coaching Python and Interview problem solutions

## PART 1 - Coaching on Typical Software Architecture:

### Cloud/Networking 
    - Azure
    - AWS
    - GCP

### Frontend:
    Angular,ReactJS, Html, CSS, Bootstrap

### ServiceLayer:
       programming Language => Java, DotNet,Node, Python,scalable
       Frameworks
            java - spring Boot
            Node - ExpressJs, Sails
            Python - Flask, FastAPI, Django

### Backend:
        SQL - MS SQL, MySQL, Postgres,
        No-SQL - MongoDB, DynamoDB, Cassandra

## Scenario

- Flask API will read the file from S3 using Botocore
and will feed data to MS SQL DB.
- This data will be later fetched from Frontend/ReactUI

- Writing a Servicelayer on Flask API (python) on top of Microsoft SQL DB

### Packages Used
 - Pymssql or SQLAlchemy
 - Botocore (AWS package)

           conn = pymssql.connect(server, user, password, database_name)
          cursor = conn.cursor(as_dict=True)
          cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
          for row in cursor:
              print("ID=%d, Name=%s" % (row['id'], row['name']))
          conn.close()

- We will convert result to JSON response and will share the template with ReactDevelopers

        {"name":suriya,"age":30,""}


## Challenges:
    - connecting to Server:
                    Servers may go down sometime, so we have implemented
                    - "/isHealthy" custom endpoint and
                    - we have configured alert emails for teams (AWS - Cloudwatch)
    - Memory Leaks and Time Taken by api calls increasing:
                - Load tested with 6X load and we found one python
                - function has nested for loops and we refractored the code.
## Deployment:
          - AWS CodeDeploy
          - Devops team takes care of Implementing CI/CD

## Flow
- Data directly dropped into S3 and then moved to MongoDB,
- from where API will take care of processing.

### botocore to fetch files s3
            s3 = boto3.resource('s3')
            bucket = s3.Bucket('test-bucket')
            #Iterates through all the objects, doing the pagination for you. Each obj
            #is an ObjectSummary, so it doesn't contain the body. You'll need to call
            #get to get the whole body.
            for obj in bucket.objects.all():
                key = obj.key
                body = obj.get()['Body'].read()


## Tasks to Explore:
      What is Botocore
      how read file from s3
      how to jsonify ms sql responsse from Pymssql
      how will you form json response to return to Frontend
      make_response in flask
      App_context and Request_context in flask
