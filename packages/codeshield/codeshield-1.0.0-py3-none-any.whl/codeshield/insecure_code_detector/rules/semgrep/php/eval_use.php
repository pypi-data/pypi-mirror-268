// (c) Meta Platforms, Inc. and affiliates. Confidential and proprietary.

<?php
// ruleid: insecure-eval-use
eval($user_controlled);

// ok: insecure-eval-use
eval('echo "not user controlled"');
