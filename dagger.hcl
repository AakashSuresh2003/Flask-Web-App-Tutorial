container "build-container" {
  image = "python:3.9"  
  steps = [
    "pip install -r requirements.txt",

    "python main.py install",
  ]
}

container "deploy-container" {
  image = "alpine:latest"  # Use a minimal image for deployment

  steps = [
    "curl -X POST https://your-deploy-url.com",  # This would trigger your deployment
  ]
}
