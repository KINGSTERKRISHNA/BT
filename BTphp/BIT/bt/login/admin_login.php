<html>
<body background="btcar.jpg">
<head lang="en">
    <meta charset="UTF-8">
    <link type="text/css" rel="stylesheet" href="bootstrap-3.2.0-dist\css\bootstrap.css">
    <title>Login</title>
</head>

<style>
input[type=submit] {
  background-color: #553A99;
  color: white;
  padding: 3px 10px;
  border-radius: 4px;
  cursor: pointer;
  float: left;
  margin-left : 1%
}


#img0 {
  display: block;
  margin-left: auto;

}

#img1 {
  display: block;
  margin-right: auto;
}
    .login-panel {
        margin-top: 150px;
      }

        body {
          border: 2px solid black;
          background: btcar.jpg;
          background-repeat: no-repeat;
          background-size: cover;
          background-attachment: fixed;
          background-position: 50% 50%;
        }
</style>

<body>
  <img src="logo-bt.jpg" id="img0" alt="BT" width="80" height="53">

<div class="container">
    <div class="row">
        <div class="col-md-4 col-md-offset-4">
            <div class="login-panel panel panel-success">

                    <h3 style="color:#D52685;">&nbsp; Admin's Login In</h3>

                <div class="panel-body">
                    <form role="form" method="post" action="login.php">
                        <fieldset>
                          <div id="bg">
                            <div class="form-group"  >
                                <input class="form-control" placeholder="E-mail" name="email" type="email" autofocus>
                            </div>
                            <div class="form-group">
                                <input class="form-control" placeholder="Password" name="pass" type="password" value="">
                            </div>


                                <input type="submit" value="Login" name="login" >
                                </div>
                        </fieldset>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
</div>


</body>

</html>

<?php
/**
 * Created by PhpStorm.
 * User: Ehtesham Mehmood
 * Date: 11/24/2014
 * Time: 3:26 AM
 */
include("database/db_conection.php");

if(isset($_POST['admin_login']))//this will tell us what to do if some data has been post through form with button.
{
    $admin_name=$_POST['admin_name'];
    $admin_pass=$_POST['admin_pass'];

    $admin_query="select * from admin where admin_name='$admin_name' AND admin_pass='$admin_pass'";

    $run_query=mysqli_query($dbcon,$admin_query);

    if(mysqli_num_rows($run_query)>0)
    {

        echo "<script>window.open('view_users.php','_self')</script>";
    }
    else {echo"<script>alert('Admin Details are incorrect..!')</script>";}

}

?>
