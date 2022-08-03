# API-documentation

## <code>/sign-in</code>
- Description <br>
    Logs user in and fetches user_info in cookies (session)
- Method: <br>
    'GET' | 'POST'
- URL Params: <br>
    None
- Responses:
    - Success respone (200): <br>

            "GET /sign-in HTTP/1.1" 200

    - Redirection (302): 
        - if user is already logged in, logs user out<br>

                "GET /sign-in HTTP/1.1" 302
                "GET /logout HTTP/1.1" 302x
                "GET /sign-in HTTP/1.1" 200

        - if logged in, redirects to <code>/home</code><br>

                "POST /sign-in HTTP/1.1" 302
                "GET /home HTTP/1.1" 200

## <code>/sign-up</code>
- Description <br>
    Creates an user account
- Method: <br>
    'GET' | 'POST'
- URL Params: <br>
    None
- Responses:
    - Success respone (200): returns sign-up page<br>

            "GET /sign-up HTTP/1.1" 200

    - Redirection (302): creates user account and redirects to login page<br>
        
            "POST /sign-up HTTP/1.1" 302
            "POST /sign-up HTTP/1.1" 302

## <code>/logout</code>
- Description <br>
    Logs user out and deletes the user's cookies (session)
- Method: <br>
    'GET'
- URL Params: <br>
    None
- Responses:
    - Redirection (302): user is not logged in<br>
        
            "GET /logout HTTP/1.1" 302
            "GET /sign-in HTTP/1.1" 200
        

## <code>/home</code>
- Description <br>
    Returns users dashboard and fetching his todays classes, requires a logged in user. 
- Method: <br>
    'GET'
- URL Params: <br>
    None
- Responses:
    - Success respone (200): <br>

            "GET /home HTTP/1.1" 200

    - Redirection (302): user is not logged in<br>
    
            "GET /home HTTP/1.1" 302
            "GET /sign-in HTTP/1.1" 200
            

## <code>/courses</code>
- Description <br>
    Fetches all the user courses.
    Admins can post or delete a course.
- Method: <br>
    'GET' | 'POST'
- URL Params: <br>
    None
- Responses:
    - Success respone (200): <br>

            "GET /courses HTTP/1.1" 200

    - Redirection (302): user is not logged in <br>
    
            "GET /courses HTTP/1.1" 302
            "GET /sign-in HTTP/1.1" 200


## <code>/course/<course_id>/start</code>
- Description <br>
    Fetches course info (start page)
- Method: <br>
    'GET' | 'POST'
- URL Params: <br>
    - course_id: integer for appropriate course
- Responses:
    - Success respone (200): returns course start page<br>

            "GET /course/2/start HTTP/1.1" 200

    - Redirection (302): user is not logged in <br>
    
            "GET /course/2/start HTTP/1.1" 302
            "GET /sign-in HTTP/1.1" 200

## <code>/course/<course_id>/users</code>
- Description <br>
    Fetches course users sorted alphabetically. (users page)
    Admins and teachers can add and delete users.
- Method: <br>
    'GET' | 'POST'
- URL Params: <br>
    - course_id: integer for appropriate course
- Responses:
    - Success respone (200): returns course users page<br>

            "GET /course/3/users HTTP/1.1" 200

    - Redirection (302): user is not logged in <br>
    
            "GET /course/3/users HTTP/1.1" 302
            "GET /sign-in HTTP/1.1" 200


## <code>/course/<course_id>/classes</code>
- Description <br>
    Fetches course classes (classes page) sorted by date and time.
    Admins and teachers can add and delete classes.
- Method: <br>
    'GET' | 'POST'
- URL Params: <br>
    - course_id: integer for appropriate course
- Responses:
    - Success respone (200): returns course classes page<br>

            "GET /course/3/classes HTTP/1.1" 200

    - Redirection (302): user is not logged in <br>
    
            "GET /course/3/classes HTTP/1.1" 302
            "GET /sign-in HTTP/1.1" 200

## <code>/course/<course_id>/class/<class_id>/attendances</code>
- Description <br>
    Fetches course attendances (attendance page) sorted by date and time, requires admin or teacher role.
- Method: <br>
    'GET'
- URL Params: <br>
    - course_id: integer for appropriate course
    - class_id: integer for appropriate class
- Responses:
    - Success respone (200): returns course class attendances page<br>

            "GET /course/6/class/25/attendances HTTP/1.1" 200

    - Redirection (302): 
        - user is not logged in <br>
    
                "GET /course/3/classes HTTP/1.1" 302
                "GET /sign-in HTTP/1.1" 200

        - if user has no rights (requires admin or teacher role)

                "GET /course/6/class/25/attendances HTTP/1.1" 302
                "GET /home HTTP/1.1" 200

## <code>/classes</code>
- Description <br>
    Fetches all the users classes sorted by date and time.
- Method: <br>
    'GET'
- URL Params: <br>
    - None
- Responses:
    - Success respone (200): returns all users classes<br>

            "GET /classes HTTP/1.1" 200

    - Redirection (302): user is not logged in <br>
    
            "GET /classes HTTP/1.1" 302
            "GET /sign-in HTTP/1.1" 200

## <code>/class/<class_id>/attend</code>
- Description <br>
    Post users attendance for the class
- Method: <br>
    'GET'
- URL Params: <br>
    - class_id: integer for appropriate class
- Responses:
    - Redirection (302):      
        - posts the attendance for the class

                "GET /class/28/attend HTTP/1.1" 302
                "GET /home HTTP/1.1" 200
                
        - user has no rights (not enrolled for the course or over data) <br>
    
                "GET /class/28/attend HTTP/1.1" 302
                "GET /home HTTP/1.1" 200

        - user is not logged in <br>
    
                "GET /classes HTTP/1.1" 302
                "GET /sign-in HTTP/1.1" 200
