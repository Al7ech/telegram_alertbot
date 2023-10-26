# Telegram Alertbot

Send telegram alert messages when endpoint is called.

## Architecture
```
┌──────┐  POST request  ┌───────────────────┐        ┌──────────────┐ Alert! ┌────────────────────┐
│ curl │ ─────────────> │ Telegram Alertbot │ ─────> │ Telegram Bot │ ─────> │ Telegram Messenger │
└──────┘                └───────────────────┘        └──────────────┘        └────────────────────┘
```

## Install
1. Setup
    Rename `template_config.env` to `config.env`.
    
    In `config.env` file, fill the vaules written below.
    ```
    BOT_TOKEN: your Telegram Bot token to access the Telegram HTTP API.
    RECEIVER_ID: list of user id's seperated by whitespace.
    AUTH_USERNAME: username for HTTP Basic Auth.
    AUTH_PASSWORD: password for HTTP Basic Auth.
    ENDPOINT(Optional): endpoint name to call (default: /alert)
    ```
2. Run
   
    `docker compose up -d`

## Testing
```
curl -X POST http://localhost:8000/alert --basic \
-u username:password \
-H "Content-Type: application/json" \
-d '{"title":"Example Title", "content":"Example Content"}'
```
would give you

`{"status":"OK"}`
