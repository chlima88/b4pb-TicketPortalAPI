import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:api", port=3000, reload=True)
