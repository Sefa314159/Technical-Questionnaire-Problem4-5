SELECT username, emailaddress FROM
(SELECT username, emailaddress, MAX(logins)
 FROM (SELECT i_users.userld, i_users.username, i_users.emailaddress,
 COUNT(i_user_login_logs.userld) as logins FROM i_users LEFT JOIN i_user_login_logs ON i_users.userld = i_user_login_logs.userld
 WHERE NOT username = 'Administrator' 
 GROUP BY i_user_login_logs.userld ORDER BY logins DESC)
)
