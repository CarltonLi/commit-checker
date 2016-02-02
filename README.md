Commit check tools
==================

Commit check are tools to check code style before commit to repository,
using regular expressions.


Installation
------------

Commit check requires GitPython and commitcheck packages.

- https://github.com/gitpython-developers/GitPython.git

```
sudo pip install gitpython
```

Add packages to python path or link it.

    $ cd /path/to/commit-check
    $ ln -s /path/to/commitcheck/commitcheck .
    $ ln -s /path/to/GitPython/git .

Usage
-----

Run checker:

    $ cd /path/to/working-directory
    $ /path/to/commit-check/android-check.py -v -t staged
    $ /path/to/commit-check/ios-check.py -h # Print full help message.

Commit check:

```
    $ cd /path/to/working-directory
    $ cat > .git/hooks/pre-commit
#!/bin/sh
if git rev-parse --verify HEAD >/dev/null 2>&1
then
	against=HEAD
else
	# Initial commit: diff against an empty tree object
	against=4b825dc642cb6eb9a060e54bf8d69288fbee4904
fi

exec ~/src/work/opensource/commit-checker/android-check.py -t staged
^D
    $ chmod a+x .git/hooks/pre-commit
```

You can also customize extra patterns in settings_local.py. Please refer to
settings.py for more details.
