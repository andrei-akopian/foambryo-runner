# Run using sh, bash, or zsh
git clone https://github.com/andrei-akopian/foambryo-runner
cd foambryo-runner
pip3 install --upgrade pip3
python3 -m venv .venv-foambryo-runner
source .venv-foambryo-runner/bin/activate
pip3 install git+https://github.com/andrei-akopian/foambryo@dev
pip3 install -r requirements.txt
echo "The foambryo_runner_v001.py is ready to go."
python3 foambryo_runner_v001.py --help

# Done!
echo "A python virtual environment is active. Type 'deactivate' (or exit the Terminal app/tab) to turn off the python virtual environent."
