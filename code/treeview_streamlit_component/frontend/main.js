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
        let treeData = event.detail.args['params']
        console.log(treeData)
        const myTree = new Tree('#treeview', {
            data: [treeData],
        });
    }
}

Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
Streamlit.setComponentReady()
Streamlit.setFrameHeight(600)
