# Running

```sh
# Provide proper login data:
cp login_example.env login.env
# Adjust values in login.env, then

docker-compose up --build
```

NOTE: your USER_ID is returned after successful login inside the html response

`window._current_user = {"id":1123123, ... }`
