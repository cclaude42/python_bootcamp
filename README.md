### 42 - Introduction to Python from 42 AI
https://github.com/42-AI/bootcamp_python

Check version (version should be 3.7.x)
```
python -V
```

If not, copy this in your ~/.zshrc :
```
# Python install

function set_conda {
	HOME=$(echo ~)
	INSTALL_PATH="/goinfre"
	MINICONDA_PATH=$INSTALL_PATH"/miniconda3/bin"
	PYTHON_PATH=$(which python)
	SCRIPT="Miniconda3-latest-MacOSX-x86_64.sh"
	REQUIREMENTS="jupyter numpy pandas"
	DL_LINK="https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh"

	if echo $PYTHON_PATH | grep -q $INSTALL_PATH; then
		echo "good python version :)"
	else
	cd
	if [ ! -f $SCRIPT ]; then
		curl -LO $DL_LINK
	fi
	if [ ! -d $MINICONDA_PATH ]; then
		sh $SCRIPT -b -p $INSTALL_PATH"/miniconda3"
	fi
	clear
	echo "Which python:"
	which python
	if grep -q "ˆexport PATH=$MINICONDA_PATH" ~/.zshrc
	then
		echo "export already in .zshrc";
	else
		echo "adding export to .zshrc ...";
		echo "export PATH=$MINICONDA_PATH:\$PATH" >> ~/.zshrc
	fi
	source ~/.zshrc
	fi
	conda install -y $(echo $REQUIREMENTS)
}
```

And then run :
```
source ~/.zshrc
set_conda
```

If install fails or interrupts, running the function again usually does NOT work, because conda doesn't let you overwrite your installation. You'll have to install it elsewhere.

In that case :
- Change the INSTALL_PATH in your ~/.zshrc, to ``"/goinfre/your_login"`` for example
- If there's an ``export PATH=/goinfre/miniconda3/bin:$PATH`` line at the bottom of your ~/.zshrc, remove it.
- Rerun ``source ~/.zshrc`` and ``set_conda``.
