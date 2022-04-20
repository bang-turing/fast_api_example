# fast_api_example

Learning FastAPI

## Run command

'''
    gunicorn public_enpoint.main:app --bind 0.0.0.0:4003 --worker-class uvicorn.workers.UvicornWorker --workers 4 --threads 2 --timeout 300 --graceful-timeout 300
'''

'''
    DOCKER_BUILDKIT=1 docker build .
'''