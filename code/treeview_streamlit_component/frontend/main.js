function sendValue(value) {
    Streamlit.setComponentValue(value)
}

/**
 * The component's render function. This will be called immediately after
 * the component is initially loaded, and then again every time the
 * component gets new data from Python.
 */
function onRender(event) {
    if (!window.rendered) {
        const paths = event.detail.args['path'];
        const tree = new Tree('#treeview', {
            data: [paths],
            onChange: function () {
                sendValue(this.values);
            }
        });
        window.rendered = true;
    }
}

Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
Streamlit.setComponentReady()
Streamlit.setFrameHeight("auto")
