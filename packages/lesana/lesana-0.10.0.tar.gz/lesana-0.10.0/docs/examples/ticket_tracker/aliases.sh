#!/bin/sh

LTT_STS_OPEN='\(status:planned OR status:ready OR status:"in progress" OR status:comments\)'
LTT_STS_ACTIVE='\(status:"in progress" OR status:comments\)'
LTT_STS_CLOSED='\(status:done OR status:invalid\)'

alias ltt-s-open="lesana search $LTT_STS_OPEN"
alias ltt-s-active="lesana search $LTT_STS_ACTIVE"
alias ltt-s-closed="lesana search $LTT_STS_CLOSED"
