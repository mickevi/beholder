Requirements
============

Write down all requirements here
Prioritize, Mandatory, nice to have, spuerfluous

Requirements should be:
 * simple
 * Testable
 * Organised
 * Numberd ( for tracability)

Introduction
------------

User requirements
-----------------

System requirements
-------------------




Server requirements
___________________

The server that collects messages and relays to irc/rocketchat/rss/web

1. Send messages to
  * irc
  * rocketchat
  * rss
  * web

2. creat channels
3. handle message severity [ info, warning, error ?]
4. handle message types []
5. Delete empty channels
6. Non persistant messages
7.

Client requirements
___________________

The desktop client that recievs messages

1. Configure channels
  Like what messages to recieve from a channel
2. Pop up messages
3. Handle subscription to channels
  both subscribe and unsubscribe
4. Configure popup messages



Message producer requirements
_____________________________
The client that sends messages

1. Tag messages with:
  * Severity [error, warning, info]
  * Type [user defined, ex starting, stopping]
  * timestamp
  * Sender
2. send messages asyncron
3. Non blocking
4.
