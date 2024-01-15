<div align="center">
  <img src="https://ai4eosc.eu/wp-content/uploads/sites/10/2022/09/horizontal-transparent.png" alt="logo" width="500"/>
</div>

# Automated mail

This is the container that will be deployed as a side task (`mailtask`) in a [Nomad job](https://github.com/AI4EOSC/ai4-papi/tree/master/etc).

 The image is available in [Dockerhub](https://hub.docker.com/repository/docker/sftobias/mail-sender).
 <!-- TODO: move to ai4os Dockerhub account -->

## Usage

All the process logic has been implemented in the `mail.py` file. Specifically, this file sends an email notification if the Nomad Job has been scheduled after the specified deadline.


This means that if the Job is executed within the first 7 days (default) of its creation, no email will be sent. Otherwise, this task will notify the job author when its execution begins.

For this purpose, the script reads a set of environment variables from the container, which must be specified in the Nomad Job.

- **`PSWD`**: Support account password. We are currently working on handling this parameter safely.

- **`NUM_DAYS`**: Number of days from which the notification will be sent by email (It has a default value of 7 days).

- **`DATE`**: Date the nomad job was created.

- **`DEST`**: Email address to notify the start of the Job execution.

To facilitate testing, the container can be run locally with the following command, where the `test.env` file contains the container's environment variables:

  ```bash
  docker run --env-file test.env sftobias/mail-sender:latest
  ```


An example of the Nomad Job definition is found in the `email.nomad.hcl` file.