# API-documentation

## <code>/home</code>
- Description <br>
    Returns users dashboard and fetching his todays classes, requires a logged in user. 
- Method: <br>
    'GET'
- URL Params: <br>
    None
- Responses:
    - Success respone (200): <br>
        <code>"GET /home HTTP/1.1" 200</code>
    - Redirection (302): <br>
        <code>
            "GET /home HTTP/1.1" 302
            "GET /sign-in HTTP/1.1" 200
        </code>

## <code>/courses</code>

## <code>/classes</code>

## <code>/...</code>

## <code>/...</code>