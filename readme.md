# My AWS Beanstalk Flask

As I'm studying for my AWC Cloud practitioner exam I came I like do some hands on projects. I've converted my Open Weather project to Python and deploying it to AWS Beanstalk. 

## My take aways
1. Learned about Python.
2. The [EB CLI](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3.html) makes it really easy to spin up and destroy.
3. AWS doesn't have the best of GitHub Actions but there is enough marketplace actions to get it to work.
4. The AWS CLI makes it really easy to deploy new AWS Beanstalk application versions.

## Setup AWS Beanstalk

Lets setup out AWS Beanstalk environment via CLI. 

```bash
# initalize your EB CLI repo
eb init -p python-3.7 my-flask --region us-east-2

# Lets initialize  to configure default keypar
eb init

# Lets create the environment and deploy
eb create my-flask-env

# Once complete lets open our new website
eb open
```

## Now lets terminate our AWS beanstalk environment

```bash
# Lets terminate our environment
eb terminate my-flask-env
```

## What I've added to this project
- I've added this to GitHub.
- I've added GitHub actions to help with continus deployment, so every time you make a change it creates a new version of your application. 
