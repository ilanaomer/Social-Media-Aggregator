<!DOCTYPE html>
<html lang="en">
<head>
    <title>Ilana & Menachem: Social Aggregrator</title>
    <link href="bootstrap/css/bootstrap.css" rel="stylesheet"/>
</head>
<body>
    <div class="container-fluid">
        <h1> Social Aggregrator!! </h1>
        <ul class ="list-group" >
%for page in pages:
            <li class ="list-group-item" >
                <span class ="badge" > {{page['fan_count']}} </span>
                {{page['name']}}
            </li >
%end
        </ul>
    </div>
</body>
</html>