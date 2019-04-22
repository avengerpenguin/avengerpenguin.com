server: mkdir -p output && cd output && python3 -m pelican.server $PORT & sleep 1 && chromium http://localhost:$PORT & wait
regenerate: pelican --debug --autoreload -r content -o output -s pelicanconf.py
notebook: jupyter-notebook content
