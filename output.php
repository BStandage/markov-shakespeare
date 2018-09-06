<?php
    // This will only execute if a POST request is
    // sent to this page with the parameter "output"
    // set to some value (doesn't matter what value).
    // See the $.ajax() call in index.html line 25
    if (isset($_POST['output'])) {

        // Execute output.cgi on the webserver
        // and return output
        echo shell_exec("./output.cgi");

    }
?>