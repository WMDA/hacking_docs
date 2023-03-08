# Flaws.cloud walk through

## Task one

s3 buckets can host static websites (similar to github pages)

When hosting on an s3 bucket the s3 bucket name must match the domain name and must be unique.

Can determine the site is hosted in an s3 bucket by running

```dig +nocmd <domain name> any +multiline +noall +answer```

This will return an ip address and by going to the ip address it will take to aws s3 

```nslookup <ip>```

All S3 buckets, when configured for web hosting, are given an AWS domain you can use to browse to it without setting up your own DNS. 

i.e flaws.cloud is at http://flaws.cloud.s3-website-us-west-2.amazonaws.com/

From the nslookup we can get the location of the bucket and then browse the bucket

```aws s3 ls  s3://flaws.cloud/ --no-sign-request --region us-west-2```

This command will list all the pages in the bucket.

If don't know the region then can use https://cyberduck.io/?l=en to automatically work out the region.

Also can go to the AWS domain (i.e http://flaws.cloud.s3-website-us-west-2.amazonaws.com/) to list the files and permissions


## Task two

Buckets can be set up with a different permissions (should'nt be allowed to just list the directory). By default, S3 buckets are private and secure when they are created. To allow it to be accessed as a web page, turn on "Static Website Hosting" and change the bucket policy to allow everyone "s3:GetObject" privileges, to publicly host the bucket as a web page. 
