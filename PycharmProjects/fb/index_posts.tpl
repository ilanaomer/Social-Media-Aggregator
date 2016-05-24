<!DOCTYPE html>
<html lang="en">
<head>
    <title>Ilana & Menachem: Social Aggregrator</title>
    <link href="bootstrap/css/bootstrap.css" rel="stylesheet"/>
</head>
<body>
    <div class="container-fluid">
        <h1> Social Aggregrator - Posts </h1>
        <ul class ="list-group" >
%for post in posts:
            <li class ="list-group-item" >
                <span class ="badge" > {{post['num_likes']}} </span>
                {{post['message']}}
            </li >
%end
        </ul>
    </div>
</body>
</html>