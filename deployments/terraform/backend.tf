terraform {
  backend "gcs" {
    bucket  = "tolganayatb"
    prefix  = "qa/hello-world"
    project = "velvety-folder-315513"
  }
}
