# Run using sh, bash, or zsh
echo "Starting to clone Repository"
git clone https://github.com/andrei-akopian/foambryo-runner
echo "Finished Cloning Repository"
cd foambryo-runner
echo "Creating Virtual Environment"
python3 -m venv .venv-foambryo-runner
echo "Created virtual environment .venv-foambryo-runner"
source .venv-foambryo-runner/bin/activate
echo "Installing custom foambryo and other requirements"
pip3 install git+https://github.com/andrei-akopian/foambryo@dev
pip3 install -r requirements.txt
deactivate
chmod +x foambryo_runner_v001.py
echo "The foambryo_runner_v001.py is ready to go."
python3 foambryo_runner_v001.py --help

# Done
echo "To run:"
echo "./foambryo_runner_v001.py <filename>"
echo "or"
echo ".venv-foambryo-runner/bin/python3 foambryo_runner_v001.py <filename>"
