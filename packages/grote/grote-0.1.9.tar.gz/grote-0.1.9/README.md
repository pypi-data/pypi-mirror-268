# GroTE: Groningen Translation Environment 🐮

## Accessing the GroTE demo

An online GroTE demo is available at [https://grote-app.hf.space](https://grote-app.hf.space). The demo will log events to the private repository [grote/grote-logs](https://huggingface.co/datasets/grote/grote-logs).

## Running GroTE locally

1. Install requirements: `pip install -r requirements.txt`.
2. Make sure you have a local `npm` installation available to run the front-end.
3. Run `grote` in your command line to start the server.
4. Visit http://127.0.0.1:7860 to access the demo. By default, logs are written to the local `logs` directory, which is synchronized with the repository [grote/grote-logs](https://huggingface.co/datasets/grote/grote-logs).

## TODOs

- [ ] Move loading to [gradio_modal](https://huggingface.co/spaces/aliabid94/gradio_modal)
- [ ] Enable restoring the previous state of edited sentences for a known file if previous edits were logged.
- [ ] Enable local logging if no remote logging is available.
