// (c) Meta Platforms, Inc. and affiliates. Confidential and proprietary.

<?php

function dangerousBackticks(){
    $user_input = $_GET['command'];
    // ruleid: backticks-use
    output = `adasd {$user_input}`;
}

function notDangerousUsage(){
    // ok: backticks-use
    output = `ls -l`;
}
