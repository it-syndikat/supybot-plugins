# -*- coding: utf-8 -*-
###
# Copyright (c) 2013, detlef prskavec
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import re
import random

class Translators(callbacks.Privmsg):
    """Add the help for "@plugin help Translators" here
    This should describe *how* to use this plugin."""
   
    def ibk(self, irc, msg, args, text):
        """text

        translates text to the dialect of innsbruck
        """
        text = re.sub(r'k', 'kch', text)
        text = re.sub(r'st', 'scht', text)
        irc.reply(text.rstrip(".,?!") + ", kchhhh!", prefixNick=True)
    ibk = wrap(ibk, ['text'])
    

    def xi(self, irc, msg, args, text):
        """text

        translates text to the dialect of vorarlberg
        """
        irc.reply(text.rstrip(".,?!") + ", odr?", prefixNick=True)
    xi = wrap(xi, ['text'])

    
    def wean(self, irc, msg, args, text):
        """text

        translates text to the dialect of vienna
        """
        text = text.encode('utf-8')
        suffixes = [u'heast!', u'oida!', u'heast oida!', u'ka schmäh oida!']
        text = re.sub(r'ill', u'üü', text)
        text = re.sub(r'was', 'wos', text)
        text = re.sub(r'das', 'des', text)
        text = re.sub(r'alt', 'oid', text)
        #add more subs
        suffix = suffixes[random.randint(0,len(suffixes)-1)]
        response = text.rstrip(u'.,?!') + ', ' + suffix
        irc.reply(response.encode("utf-8"), prefixNick=True)
    wean = wrap(wean, ['text'])

Class = Translators


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
# vim:set fileencoding=UTF-8:
