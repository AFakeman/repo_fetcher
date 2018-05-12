# repo_fetcher

This project is a tool which retrieves all homeworks done by students and checks them for similarities.

## Getting Started

First, you need to clone this repository. Then there are some things you need to have.

### Prerequisites

* Python3 - everything is written in Python, so you need it installed
* python-gitlab - library which helps to retrieve homeworks from Gitlab
* moss - script which collects files and returns you a link to the report

### Gitlab

First you need to get Gitlab API key. Create your own [here](https://gitlab.com/profile/personal_access_tokens)
or ask you mentor to give you the default one. Also don't forget to configure your SSH keys
(can be done [here](https://gitlab.com/profile/keys)).

Now you need to complete [config](config.py). `GROUP_NAME` is a placeholder for your group, and
`PRIVATE_TOKEN` is a Gitlab API key which you got on the previous step.

Now it's time to install python-gitlab - a library to work with Gitlab API using Python.
Run the following command in terminal:
```Bash
sudo pip install --upgrade python-gitlab
```
Additional information can be found [here](http://python-gitlab.readthedocs.io/en/stable/index.html).

### Moss

Moss (for a Measure Of Software Similarity) is an automatic system for determining the similarity of programs.
First you need to register. In order to do that you need to send a mail message to moss@moss.stanford.edu.
The body of the message should appear exactly as follows:
```Plain text
registeruser 
mail username@domain
```
where the last bit in italics is your email address.

After that you will get a letter with a moss script. Save it under the name `moss` and place in the directory with
the repo_fetcher project. Then you need to change its permissions. Do the following in the directory where the
script is now:
```Bash
chmod +x moss
```
Additional information can be found [here](http://theory.stanford.edu/~aiken/moss/).

Now everything is ready!

## Usage

General usage can be described as
```Bash
./main.py [-h] [-c] branch
```

There are two options:
* Download all homeworks
* Download all homeworks and check them for similarities

For the first option do the following:
```Bash
./main.py branch_name
```

This command simply download all homeworks.

For the second option do the following:
```Bash
./main.py branch_name -c
```

This command download all homeworks and perform steps necessary to find similarities.
It will generate some output - the progress of the work.
In the end (if everything was ok) you will see a link to the report.

## Contributing

Feel free to create issue / make a pull request. There is no strict policy about that.

## Authors

* Suslov Anton - author of the original script, which collected all the homeworks.  
* Rubanenko Evgeny - tuned script and made it possible to check for similarities.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

Thanks to Stanford and all the developers of Moss.
