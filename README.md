1. Setup virtual environment

```
python3 -m venv env
```

2. Add requirements.txt file in root dir and add dependencies

```
fastapi
uvicorn[standard]
```

3. Activate env file

```
source env/bin/activate
```

4. Install dependencies

```
pip3 install wheel
pip3 install -r requirements.txt
```

5. Install Playwright for end-to-end testing

Install the Pytest plugin:

```
pip3 install pytest-playwright
```

Install the required browsers:

```
playwright install
```

Run the app:

```
uvicorn main:app
```

Choose specific port (optional), e.g:

```
uvicorn main:app --port=300
```

Use the `--reload` flag to automatically re-run the server after any change:

```
uvicorn main: app --reload
```