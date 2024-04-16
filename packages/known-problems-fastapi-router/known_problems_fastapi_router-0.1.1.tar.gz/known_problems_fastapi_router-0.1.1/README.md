### FastAPI Known Problems API router

Override the FastAPI APIRouter to handle endpoints' known problems at router level.
For known problems a response following the [RFC 7807](https://datatracker.ietf.org/doc/html/rfc7807) 
is be returned.


### Examples

To run the examples execute the uvicorn command from the `examples` directory of the project.
e.g. `known-problems-fastapi-router/examples$`

```bash
 uvicorn basic_usage.web:app --host 0.0.0.0 --port 8000
```

After running the example code through the CLI three example documentations
will be available at the following URLs:

- Swagger: [http://0.0.0.0:8000/docs](http://0.0.0.0:8000/docs)

- Redoc: [http://0.0.0.0:8000/redoc](http://0.0.0.0:8000/redoc)

- RapiDoc: [http://0.0.0.0:8000/rapidoc](http://0.0.0.0:8000/rapidoc)


### FastAPI validation error

FastAPI Validation Error has to be handled by the FastAPI exception handler middleware.

```python
@app.exception_handler(RequestValidationError)
    async def custom_exception_handler(
            request: Request, exc: RequestValidationError
    ):
        return standard_validation_exception_handler(request, exc)
```