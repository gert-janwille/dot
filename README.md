## Installation

To install the latest development version type the following commands:

```bash
git clone https://github.com/gert-janwille/dot.git # Download the latest revision
cd dot # Switch to tool's directory
sudo python setup.py install # Install any dependencies (Currently pexpect, future, youtube_dl, pubnub, tor)
```

## Usage

Run the tool by typing `dot` or `python bin/dot` (from inside the tool's directory).


## Things you can do
```
command       Description                           options
---------------------------------------------------------------
..        ->  goes back to mainframe                none

exit      ->  exits the dot program                 none

clear     ->  Clears the screen                     none

help      ->  Lists all available options           none

connect   ->  connect to server using ssh,          -u <username>
              if no options it connects to          -p <password>
              default settings                      -h <server_ip>

secure    ->  Relay all internet traffic over       none
              secure tor connection.
              check: https://check.torproject.org/

flush     ->  Close secure connection and set to    none
              default settings

yt        ->  Download a youtube link               -l <link>

isdark    ->  Say in ascii if it is dark outside    none

hangman   ->  Play Hangman, just type a letter      none

```
