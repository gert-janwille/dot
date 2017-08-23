<div align="center">
  <a href="https://github.com/gert-janwille/dot">
    <img width="250" heigth="250" src="https://raw.github.com/gert-janwille/dot/master/docs/Dot.png">
  </a>
  <br/>
  <p>
    DOT is a multi use tool for developers, hackers, testers and everyone who want to be secure and playing simple terminal games.
  <p>
</div>


![Python Version](https://img.shields.io/badge/python-2.7-blue.svg)
![License](https://img.shields.io/badge/license-GPL-blue.svg)



## Getting Started

Following instructions will get you to install DOT on your mac. See usage for notes on how to call it.

### Requirements

Following are the requirements for getting the most out of DOT:

 - OS X Although people have made DOT work on other Systems, Mac OS X is the officially supported distribution, all new features are primarily tested on this platform.

- [Homebrew](https://brew.sh) to download tor. (only needed when you don't have tor installed).

**Install Homebrew:**
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### Installation

To install the latest development version type the following commands:

```bash
git clone https://github.com/gert-janwille/dot.git # Download the latest revision
cd dot # Switch to tool's directory
sudo python setup.py install # Install any dependencies (Currently pexpect, future, youtube_dl, pubnub, tor)
```
Alternatively, you can download the latest stable version from the [Releases page](https://github.com/gert-janwille/dot/releases).

If you want to make a default ssh connection, add in the Dot/dot folder a new file called `settings.py` and set the values:

```python
KALI_SERVER = <HOSTNAME>
SSH_USER = <USERNAME>
SSH_PASS = <PASSWORD>
```

## Usage

Run the tool by typing `dot` or `python bin/dot` (from inside the tool's directory).

By running DOT without any options, it will start the DOT mainframe.
Use `dot -t <TASK>` to start a task immediately


<br/>

### Main Functions
These are all functions who can be use immediately or using the dot mainframe.

***

```shell
DOT > connect
```
or `dot -t connect`


Use the connect function to connect over ssh to a server like Kali Linux. By running connect without any options you'll connect to a default server that you setup in the `settings.py` on the dot folder file.

OPTIONAL: `-u <username> -p <password> -h <hostname>`

***
```shell
DOT > secure
```
or `dot -t secure`


Use the secure function to push all your network through a secure tor relay. If you use the secure function you'll browse anonymously and secure.
Check if you're on the tor network by surfing to: [https://check.torproject.org/](https://check.torproject.org/)

***
```shell
DOT > flush
```
or `dot -t flush`


Use the flush function to stop the anonymously browsing and reset to previous settings. Check if you're not on the tor network by surfing to: [https://check.torproject.org/](https://check.torproject.org/)

***
```shell
DOT > yt -l <link>
```
or `dot -t yt -l <link>`


Use the yt function to download your favorite music from youtube. The song will be downloaded and moved to your downloads folder in a couple of seconds.



<br/>

### Games
Dot has a couple of build-in mini-games. They are listed below and makes waiting for code to compile less boring.

***
```shell
DOT > hangman
```
or `dot -t hangman`


Use the hangman function to play the original and old-fashion game. Guess the word before you hang.



<br/>

### Mainframe Functions
The mainframe functions are little function that only need to be used when you're on DOT's mainframe.

***
```shell
DOT > ..
```


Use the .. function to go back to the mainframe.

***
```shell
DOT > exit
```


Use the exit function to close the DOT application.

***
```shell
DOT > clear
```


Use the clear function to clear the screen.

***
```shell
DOT > help
```


Use the help function to see all the available options.



<br/>

## Built With

* [Python 2.7](https://www.python.org/) - The program language used
* [Tor](https://www.torproject.org) - Dependency Management
* [PubNub](https://www.pubnub.com) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/gert-janwille/dot/tags).

## Authors

* **Gert-Jan Wille** - *Initial work* - [gert-janwille](https://github.com/gert-janwille)

See also the list of [contributors](https://github.com/gert-janwille/dot/contributors) who participated in this project.

## License

This project is licensed under the GPL License - see the [LICENSE.txt](LICENSE.txt) file for details

## Acknowledgments

* Love for [PubNub](https://www.pubnub.com)
* Inspirated by [WifiPhisher](https://github.com/wifiphisher/wifiphisher)
