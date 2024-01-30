<div align="center">
  <img src="https://ai4eosc.eu/wp-content/uploads/sites/10/2022/09/horizontal-transparent.png" alt="logo" width="500"/>
</div>

# Automated mail


This project has been developed based on the need to notify users when their [Nomad jobs](https://github.com/AI4EOSC/ai4-papi/tree/master/etc) are assigned after a delay time (currently set to 7 days). For this and due to specific needs of the mail service used it's necessary to take a client-server approach.

Both Docker images ([Client](https://hub.docker.com/repository/docker/sftobias/mail-client) and [Server](https://hub.docker.com/repository/docker/sftobias/mail-server/general)) are available on Dockerhub.


The idea is that the client part will be deployed as a side task (`mailtask`) in a Nomad job, taking care of all the temporal logic. If the premise is met then it will make a request to the server, which will be in charge of sending the email.

## Usage

As mentioned, the idea is to send an email notification if the Nomad Job has been scheduled after the specified deadline.

This means that if the Job is executed within the first 7 days (default) of its creation, no email will be sent. Otherwise, this task will notify the job author when its execution begins.

For this purpose, the client-side script reads a set of environment variables from the container, which must be specified in the Nomad Job.

- **`NUM_DAYS`**: Number of days from which the notification will be sent by email (It has a default value of 7 days).

- **`DATE`**: Date the nomad job was created.

- **`DEST`**: Email address to notify the start of the Job execution.

- **`BODY`**: Body of the mail.

- **`SUBJECT`**: Subject of the mail.

- **`MAILING_TOKEN`**: Must be the same on the client and server side.

The server side only needs the **`MAILING_TOKEN`** environment variable to work.

## API

The server implements an API developed in python through [FastApi](https://fastapi.tiangolo.com/). **This API listens on port 8082**. Once the service is up, the API specification can be accessed in `/docs`.

The status of the service can be checked through a `GET` request to the root route `/`. If the service is active, it should respond with the following message:

```bash
{"message": "Server is UP"}
```

Emails can be sent through a `GET` request to `/notify` with the following query params:

- **`email`**: Email recipient.

- **`body`**: Body of the mail.

- **`subject`**: Subject of the mail.

- **`token`**: Security token. Must be the same on the client and server side.

If the request is received correctly and the token is correct, the following message is returned

```bash
{"status": "ok", "message": "Notification sent successfully"}
```

Otherwise, if an incorrect token is sent, the following message is returned

```bash
{"status": "error", "message": "Invalid token, notification not sent"}
```

## Demo


Both the client and the server can be easily deployed locally using the scripts in the [scripts](https://github.com/ai4os/docker-mail/tree/main/scripts) folder.

To allow connectivity between containers, it is necessary to previously execute the following command:

```bash
docker network create --subnet=192.168.1.0/24 mailing_net
```

Containers can then be deployed by running `launch_client.sh` and `launch_server.sh`. Environment variables for each instance are specified through the `vars.env` file in the server and client folders. For example:

- For the client container
```bash
  NUM_DAYS=7
  DATE="2024-01-07T11:19:29.914177+01:00"
  DEST=test@email.com
  BODY="Body of the test mail"
  SUBJECT="Test mail"
  MAILING_TOKEN=1234
```

- For the server container
```bash
  MAILING_TOKEN=1234
```

Depending on the Date variable, the email will be sent or not.


