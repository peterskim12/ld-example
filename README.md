# ld-example

## Overview

This is a small project to show how to add feature flags to a Python script. 

One way feature flags can be utilized is to make a website or application behave differently based on how we decide to segment users. This could be by geography, demographics, or any other information we have about the user or request. We may segment users based on whether they're a `standard` user or a user who's opted in to a `beta` program to get bleeding edge features. Or we may choose to deliver different features to different geographic markets for various business reasons.

In this case, this Python script uses [musicalbeeps](https://pypi.org/project/musicalbeeps/) to play the C note at various octaves depending on the user which we identify using a username from a command-line argument that's passed to the LaunchDarkly `variation()` method. 

There are four named users for whom there are rules to target specific octaves:

- peter: 5
- rafael: 3
- sung: 7
- mateo: 8

My 11yo son Rafael's voice has been deepening so I gave him the lowest octave.

## Setup

### Pre-req

Python3 and pip3 are installed.

### Get code

Clone git repo with code:

`git clone https://github.com/peterskim12/ld-example.git`

### Install required modules:

`pip3 install musicalbeeps`

`pip3 install launchdarkly-server-sdk`

### Set environment variable with LaunchDarkly API key

`export ld_api=<api-key>`

## Execution

Command syntax is:
`python3 beep.py --user <username>`

If you run
`python3 beep.py --user peter`
it will play the note C5 since that is the rule defined in the feature flag.

If you run
`python3 beep.py --user rafael`
it will play the note C3 since that is the rule defined in the feature flag.

If you run
`python3 beep.py --user jim`
it will play the note C4 since 'jim' does not have an explicit rule and we've configure C4 as the default.

