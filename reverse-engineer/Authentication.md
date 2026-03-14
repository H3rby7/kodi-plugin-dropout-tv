# Authentication

## Login

### Login-Page

Headers:

`set-cookie`
	_session=the-session-cookie

Cookie to send along the login POST.

```html
<meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="the-token" />
```

### Login-Request

trackerJSON
```json
{"country":"en","platform":"linux","uid":1234567,"site_id":SITE_ID}
```

```sh
curl 'https://watch.dropout.tv/login' \
  -X POST \
  -H 'User-Agent: Mozilla/5.0 ...' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Accept-Encoding: gzip, deflate, br, zstd' \
  -H 'Referer: https://watch.dropout.tv/login' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Origin: https://watch.dropout.tv' \
  -H 'Sec-GPC: 1' \
  -H 'Connection: keep-alive' \
  -H 'Cookie: locale_det=en; _session=the-session-cookie; __cf_bm=my-cf_bm-cookie; tracker=url-encoded-trackerJSON; _swb=ccda83d1-98dd-4d12-9be7-b18317be9e26; _swb_consent_=my-swb_bearer_token; gpcsignal=true; gpcsignal=true; gpcsignal=true; _ketch_consent_v1_=my-ketch_consent_v1_token; usprivacy=1---; us_privacy=1---; referrer_url=https%3A%2F%2Fwatch.dropout.tv%2Fbrowse' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'Sec-Fetch-Dest: document' \
  -H 'Sec-Fetch-Mode: navigate' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-Fetch-User: ?1' \
  -H 'Priority: u=0, i' \
  -H 'TE: trailers' \
  --data-raw 'email=url-encoded-email%40domain.com&authenticity_token=url-encoded-token&utf8=%E2%9C%93&password=url-encoded-password-plaintext'
```

### Login-Response

302 to https://watch.dropout.tv/browse

Header: `set-cookie`

```
_session=my-session-cookie; domain=.dropout.tv; path=/; expires=Sun, 14 Mar 2027 14:06:25 GMT; secure; HttpOnly; SameSite=Lax
```

Within the returned htmls there is this snippet:

```html
  <script>
    window.TOKEN = "a-jwt-token";
  </script>
```

That token can be used for the API requests - it is only valid for 5 minutes.
Maybe the session is valid for a longer period of time.

jwt token breakdown

```json
{
  "app_id": 45854,
  "exp": 123456789,
  "nonce": "a-nonce",
  "scopes": [
    "public"
  ],
  "session_id": "a-session-id",
  "site_id": SITE_ID,
  "user_id": CUSTOMER_ID
}
```