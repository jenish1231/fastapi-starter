import uvicorn

if __name__ == '__main__':
    uvicorn.run(
        "app.web.application:create_app",
        workers=3,
        port=8001,
        host="0.0.0.0",
        reload=True,
        factory=True,
        lifespan="on"
    )
