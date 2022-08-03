-- SQLite
SELECT fname, lname, role
FROM User u
INNER JOIN UCourse uc ON u.id=uc.user_id
WHERE u.id=1 AND uc.course_id=1;