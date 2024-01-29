job "demo-email" {
  namespace = "default"
  type      = "batch"
  region    = "global"
  id        = "demo-email"
  priority  = "50"


  group "email" {

    ephemeral_disk {
      size = 500 //TODO check accurate disc size
    }

    task "usertask" {

      driver = "docker"

      config {
        image    = "sftobias/mail-sender:latest"
        shm_size = 1000000000
      }

      env {
        NUM_DAYS=7 #Number of days from which to notify
        DATE="2024-01-07T11:19:29.914177+01:00"
        DEST="sftobias@ifca.unican.es"
        BODY="Body of the test mail"
        SUBJECT="Test mail"
      }

      //TODO check accurate resources
      resources {
        cores  = 1
        memory = 2000
      }

    }

  }
}