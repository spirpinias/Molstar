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
        let viewerInstance = new PDBeMolstarPlugin();
        let customData = event.detail.args['params']
        let options = {
            customData: customData,
            bgColor: {r: 255, g: 255, b: 255},
            expanded: true,
            hideControls: true,
            hideCanvasControls: ['expand']
        }

        let viewerContainer = document.querySelector('#molstar');
        viewerInstance.render(viewerContainer, options);
        window.rendered = true
    }
}

Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
Streamlit.setComponentReady()
Streamlit.setFrameHeight(600)
