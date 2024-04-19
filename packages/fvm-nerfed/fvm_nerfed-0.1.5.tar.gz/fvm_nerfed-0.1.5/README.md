# FVM bitcode evaluator

Feather Virtual Machine (FVM) is a bitcode-based VM in development by
[@wryl](https://gitlab.com/wryl).

This is a simplified version of FVM that interprets ascii representations
of a future bitcode.

## The bitcode

This version of FVM runs ASCII representations of the bitcode.

> The bytecode (or rather bitcode) is an 8-instruction virtual machine that manipulates a circular tape of bits. The tape is dynamically resizable, and > internally is ideally modeled as a deque.
> Instructions:
> * `0`: Insert a `0` bit to the left of the tape head.
> * `1`: Insert a `1` bit to the left of the tape head.
> * `<`: Move the tape head left.
> * `>`: Move the tape head right.
> * `[`: Consume the bit under the tape head. If it's a `1`, proceed forward by one instruction. If it's a `0`, proceed to the next matching `]`.
> * `]`: Proceed to the previous matching `[`.
> * `^`: Consume and send a bit to the outside world.
> * `v`: Receive a bit from the outside world.
>
> I/O is blocking. Something needs to acknowledge the send, and execution pauses on receive until something is sent.

## Docker Hub

https://hub.docker.com/r/booniepepper/fvm

## PyPI

Coming

## As a discord bot

This docker image is the FVM runtime used for a discord
bot running on the concatenative programming discord server.

As of 2024-04-18 details on the discord bot can be found here:
* https://github.com/booniepepper/dt-discord-bot/tree/fvm
